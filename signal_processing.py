import numpy
import pandas
import scipy


def open_data_frame(file_path):
    data = pandas.read_csv(file_path)
    return data["Time"].values, data["abp"].values, data["cbfv_simulated"].values


def open_csv_file(file_path):
    def _format(value):
        return float(value.replace(",", "."))

    with open(file_path) as fid:
        header = fid.readline()
        rows = [r.strip().split(";") for r in fid.readlines()]
        rri, cbv, abp = [], [], []
        for row in rows:
            if [r.strip() for r in row] == ["", "", ""]:
                continue
            rri.append(_format(row[0]))
            cbv.append(_format(row[1]))
            abp.append(_format(row[2]))

        rri = numpy.array(rri)
        cbv = numpy.array(cbv)
        abp = numpy.array(abp)
        time = numpy.cumsum(rri) - rri[0]
        return time, cbv, abp


def band_indexes(frequency, lower, upper):
    return numpy.where(numpy.logical_and(frequency >= lower, frequency < upper))[0]


def band_gain(gain, indexes):
    return numpy.nanmean(abs(gain[indexes]))


def band_phase(phase, indexes):
    return numpy.nanmean(phase[indexes]) / (2 * numpy.pi) * 360


def band_coherence(coherence, indexes):
    return numpy.nanmean(abs(coherence[indexes]) ** 2)


def band_power(psd, indexes, freq_resolution):
    return 2 * sum(psd[indexes]) * freq_resolution


def frequency_bands_results(frequency, pxx, pyy, gain, phase, coherence, options):
    indexes_vlf = band_indexes(frequency, *options["vlf"])
    indexes_lf = band_indexes(frequency, *options["lf"])
    indexes_hf = band_indexes(frequency, *options["hf"])

    return {
        "gain_vlf": band_gain(gain, indexes_vlf),
        "gain_lf": band_gain(gain, indexes_lf),
        "gain_hf": band_gain(gain, indexes_hf),
        "phase_vlf": band_phase(phase, indexes_vlf),
        "phase_lf": band_phase(phase, indexes_lf),
        "phase_hf": band_phase(phase, indexes_hf),
        "coherence_vlf": band_coherence(coherence, indexes_vlf),
        "coherence_lf": band_coherence(coherence, indexes_lf),
        "coherence_hf": band_coherence(coherence, indexes_hf),
        "pxx_vlf": band_power(pxx, indexes_vlf, frequency[1]),
        "pxx_lf": band_power(pxx, indexes_lf, frequency[1]),
        "pxx_hf": band_power(pxx, indexes_hf, frequency[1]),
        "pyy_vlf": band_power(pyy, indexes_vlf, frequency[1]),
        "pyy_lf": band_power(pyy, indexes_lf, frequency[1]),
        "pyy_hf": band_power(pyy, indexes_hf, frequency[1]),
    }


def welch(x, y, segment_size, overlap, window_fun, fs, nfft):
    n_windows = int((len(x) - segment_size) / (segment_size - overlap)) + 1

    frequency = numpy.arange(0, fs, fs / nfft)
    _, pxx = scipy.signal.welch(
        x,
        fs=fs,
        window=window_fun(segment_size),
        nperseg=segment_size,
        noverlap=overlap,
        nfft=None,
        detrend=False,
        return_onesided=False,
    )
    _, pyy = scipy.signal.welch(
        y,
        fs=fs,
        window=window_fun(segment_size),
        nperseg=segment_size,
        noverlap=overlap,
        nfft=None,
        detrend=False,
        return_onesided=False,
    )

    _, pxy = scipy.signal.csd(
        x,
        y,
        fs=fs,
        window=window_fun(segment_size),
        nperseg=segment_size,
        noverlap=overlap,
        nfft=None,
        detrend=False,
        return_onesided=False,
    )

    return frequency, pxx, pyy, pxy, n_windows


def smooth(psd, smooth_factor):
    triang = numpy.ones((int((smooth_factor + 1) / 2), 1))
    triang = (triang / sum(triang)).flatten()
    psd_copy = psd.copy()
    psd_copy[0] = psd[1]
    psd_filt = scipy.signal.filtfilt(triang, 1, psd_copy)
    psd_filt[0] = psd[0]
    return psd_filt


def tfa(abp, cbfv, fs, options: dict = None):
    # TODO: docstring
    if options is None:
        options = dict()

    coherence_thresholds = {
        3: 0.51,
        4: 0.40,
        5: 0.34,
        6: 0.29,
        7: 0.25,
        8: 0.22,
        9: 0.20,
        10: 0.18,
        11: 0.17,
        12: 0.15,
        13: 0.14,
        14: 0.13,
        15: 0.12,

    }
    default_options = {
        "vlf": (0.02, 0.07),
        "lf": (0.07, 0.2),
        "hf": (0.2, 0.5),
        "nfft": 1024,
        "detrend": lambda x: x - numpy.mean(x),
        "smooth_factor": 3,
        "coherence_threshold": None,
        "coherence_thresholds": coherence_thresholds,
        "apply_coherence_threshold": True,
        "remove_negative_phase": True,
        "negative_phase_cutoff": 0.1,
        "normalize": False,
        "window": scipy.signal.windows.hann,
        "segment_size": 1024,
        "overlap": 512,
        "normalize_cbfv": False,
        "normalize_abp": False,
    }
    options = {**default_options, **options}

    avg_abp = abp.mean()
    avg_cbfv = cbfv.mean()
    std_abp = abp.std()
    std_cbfv = cbfv.std()

    abp = options["detrend"](abp - avg_abp)
    cbfv = options["detrend"](cbfv - avg_cbfv)

    if options["normalize_cbfv"]:
        cbfv = (cbfv / avg_cbfv) * 100

    if options["normalize_abp"]:
        abp = (abp / avg_abp) * 100

    frequency, pxx, pyy, pxy, n_windows, = welch(
        x=abp,
        y=cbfv,
        window_fun=options.get("window"),
        segment_size=options.get("segment_size"),
        overlap=options.get("overlap"),
        fs=fs,
        nfft=options.get("nfft"),
    )

    # Smoothing
    pxx = smooth(pxx, options.get("smooth_factor"))
    pyy = smooth(pyy, options.get("smooth_factor"))
    pxy = smooth(pxy, options.get("smooth_factor"))

    gain = pxy / pxx
    coherence = pxy / (numpy.sqrt(pxx * pyy))

    if options.get("coherence_threshold") is not None:
        coherence_threshold = options.get("coherence_threshold")
    else:
        coherence_threshold = coherence_thresholds.get(n_windows, options.get("coherence_threshold"))

    # If manual threshold is disable and there is no simulated coherence value
    # for a given n_widows
    if coherence_threshold is None:
        apply_coherence_threshold = False
    else:
        apply_coherence_threshold = options.get("apply_coherence_threshold")

    if apply_coherence_threshold:
        gain[numpy.where(abs(coherence) ** 2 < coherence_threshold)[0]] = numpy.nan

    phase = numpy.angle(gain)
    if options.get("remove_negative_phase"):
        cutoff = options.get("negative_phase_cutoff")
        indexes = numpy.where(phase[numpy.where(frequency < cutoff)[0]] < 0)
        phase[indexes] = numpy.nan

    results = frequency_bands_results(
        frequency,
        pxx,
        pyy,
        gain,
        phase,
        coherence,
        options
    )
    if options["normalize_cbfv"]:
        results["gain_vlf_norm"] = results["gain_vlf"]
        results["gain_lf_norm"] = results["gain_lf"]
        results["gain_hf_norm"] = results["gain_hf"]
        results["gain_vlf"] = results["gain_vlf"] * avg_cbfv / 100
        results["gain_lf"] = results["gain_lf"] * avg_cbfv / 100
        results["gain_hf"] = results["gain_hf"] * avg_cbfv / 100
    else:
        results["gain_vlf_norm"] = results["gain_vlf"] / avg_cbfv * 100
        results["gain_lf_norm"] = results["gain_lf"] / avg_cbfv * 100
        results["gain_hf_norm"] = results["gain_hf"] / avg_cbfv * 100

    results["coherence_threshold_applied"] = apply_coherence_threshold
    results["n_windows"] = n_windows
    results["avg_abp"] = avg_abp
    results["avg_cbfv"] = avg_cbfv
    results["std_abp"] = std_abp
    results["std_cbfv"] = std_cbfv
    results["pxx"] = abs(pxx)
    results["pyy"] = abs(pyy)
    results["pxy"] = abs(pxy)
    results["gain"] = abs(gain)
    results["coherence"] = abs(coherence) ** 2
    results["phase"] = abs(phase)
    results["coherence_threshold"] = coherence_threshold
    results["frequency"] = frequency
    return results


def linear_interp(time, signal, fs):
    interp_time = _create_interp_time(time, fs)
    return numpy.interp(interp_time, time, signal)


def cubic_spline(time, signal, fs):
    interp_time = _create_interp_time(time, fs)
    cs = scipy.interpolate.CubicSpline(time, signal)
    return cs(interp_time)


def _create_interp_time(time, fs):
    time_resolution = 1 / float(fs)
    return numpy.arange(time[0], time[-1] + time_resolution, time_resolution)
