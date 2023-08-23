import numpy


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
