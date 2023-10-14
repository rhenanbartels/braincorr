import numpy
import pandas
import scipy


def open_data_frame(file_path):
    data = pandas.read_csv(file_path, sep="\t")
    return data["Time"].values, data["MABP [mmHg]"].values, data["CBFV-L [cm/s]"].values


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


def welch(x, y, window, overlap, fs, nfft):
    window_size = len(window)
    shift = window_size - overlap
    n_windows = int((len(x) - window_size) / shift) + 1
    start = 0
    end = window_size
    x_fft = numpy.zeros((window_size, n_windows), dtype=complex)
    y_fft = numpy.zeros((window_size, n_windows), dtype=complex)
    for index in range(n_windows):
        x_fft[:, index] = scipy.fft.fft(x[start:end] * window)
        y_fft[:, index] = scipy.fft.fft(y[start:end] * window)
        start += shift
        end += shift

    frequency = numpy.arange(0, fs, fs / nfft)

    window_energy = numpy.sum(window ** 2)
    pxx = numpy.sum(numpy.real(x_fft * numpy.conj(x_fft)), axis=1) / n_windows / window_energy / fs
    pyy = numpy.sum(numpy.real(y_fft * numpy.conj(y_fft)), axis=1) / n_windows / window_energy / fs
    pxy = numpy.sum(numpy.conj(x_fft) * y_fft, axis=1) / n_windows / window_energy / fs

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
        "coherence_threshold": 0.0,
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

    abp = options["detrend"](abp - avg_abp)
    cbfv = options["detrend"](cbfv - avg_cbfv)

    if options["normalize_cbfv"]:
        cbfv = (cbfv / avg_cbfv) * 100

    if options["normalize_abp"]:
        abp = (abp / avg_abp) * 100

    window = options.get("window")(options.get("segment_size"))
    frequency, pxx, pyy, pxy, n_windows, = welch(
        abp,
        cbfv,
        window,
        options.get("overlap"),
        fs,
        options.get("nfft"),
    )

    # Smoothing
    pxx = smooth(pxx, options.get("smooth_factor"))
    pyy = smooth(pyy, options.get("smooth_factor"))
    pxy = smooth(pxy, options.get("smooth_factor"))

    gain = pxy / pxx
    coherence = pxy / (numpy.sqrt(pxx * pyy))

    coherence_threshold = coherence_thresholds.get(n_windows, options.get("coherence_threshold"))
    if options.get("apply_coherence_threshold"):
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

    results["n_windows"] = n_windows
    results["avg_abp"] = avg_abp
    results["avg_cbfv"] = avg_cbfv
    results["pxx"] = pxx
    results["pyy"] = pyy
    results["pxy"] = pxy
    results["gain"] = abs(gain)
    results["coherence"] = abs(coherence) ** 2
    results["phase"] = abs(phase)
    results["coherence_threshold"] = coherence_threshold
    results["frequency"] = frequency
    return results
