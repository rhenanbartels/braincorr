import numpy
import scipy


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


def welch(x, y, window, overlap, fs, nfft):
    window_size = len(window)
    shift = round((1-overlap) * window_size)
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
    coherence = pxy / numpy.sqrt(abs(pxx * pyy))

    return frequency, pxx, pyy, pxy, coherence


def analyze(abp, cbfv, fs, **options):
    avg_abp = abp.mean()
    # std_abp = abp.std()

    avg_cbfv = cbfv.mean()
    # std_cbfv = cbfv.std()

    abp = abp - avg_abp
    cbfv = cbfv - avg_cbfv

    window = scipy.signal.windows.hann(1024)
    overlap = 0.5
    nfft = 1024
    frequency, pxx, pyy, pxy, coherence = welch(abp, cbfv, window, overlap, fs, nfft)
