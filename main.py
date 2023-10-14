import os
import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

import numpy
import pyqtgraph as pg

from signal_processing import open_csv_file, open_data_frame, tfa
from interface import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()

        # File menu
        self.menu_file_open_action.setShortcut("Ctrl+O")
        self.menu_file_open_action.triggered.connect(self.open_file)

        # Combo boxes
        self.topAxesComboBox.currentIndexChanged.connect(self.change_top_plot)
        self.bottomAxesComboBox.currentIndexChanged.connect(self.change_bottom_plot)

        # Init last opened directory
        self.last_dir = "."
        self.file_name = ""

        # Init plot config variables
        self.top_roi = None
        self.bottom_roi = None
        self._roi_region = None

    @property
    def duration(self):
        if self.time is not None:
            return self.time[-1]
        else:
            return None

    @property
    def start_signal(self):
        if self.time is not None:
            return self.time[0]
        else:
            return None

    @property
    def vlf_range(self):
        return float(self.lineEditVLFLower.text()), float(self.lineEditVLFUpper.text())

    @property
    def lf_range(self):
        return float(self.lineEditLFLower.text()), float(self.lineEditLFUpper.text())

    @property
    def hf_range(self):
        return float(self.lineEditHFLower.text()), float(self.lineEditHFUpper.text())

    @property
    def roi_region(self):
        if self._roi_region is None:
            return [0, self.duration]
        else:
            return self._roi_region

    def _save_last_dir(self, file_name):
        self.last_dir = os.path.dirname(file_name)

    def _set_file_name(self, file_path):
        file_name = os.path.basename(file_path)
        self.lineEditFileName.setText(file_name)

    def _update_edit_time_ranges(self, region):
        self.lineEditStartTimeAxes.setText(f"{region[0]:.2f}")
        self.lineEditEndTimeAxes.setText(f"{region[1]:.2f}")

    def open_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select file",
            self.last_dir,
            "CSV files (*.txt)"
        )
        if self.file_path:
            self._save_last_dir(self.file_path)
            # self.time, self.cbv, self.abp = open_csv_file(self.file_name)
            self.time, self.abp, self.cbfv = open_data_frame(self.file_path)
            self._set_file_name(self.file_path)

            self.plot_cbfv()
            self.plot_abp()
            self._update_edit_time_ranges(region=(0, self.duration))

            # Signal Processing
            # TODO: get config from panel
            fs = 10.0
            self.results = tfa(self.abp, self.cbfv, fs)

    def change_top_plot(self):
        {
            0: self.plot_cbfv,
            1: self.plot_cbfv_psd,
        }.get(self.topAxesComboBox.currentIndex(), lambda: None)()

    def change_bottom_plot(self):
        {
            0: self.plot_abp,
            1: self.plot_abp_psd,
        }.get(self.bottomAxesComboBox.currentIndex(), lambda: None)()

    def update_top_roi(self):
        # Do not let area outside signal
        region = self.top_roi.getRegion()
        self._roi_region = region
        if self.bottom_roi is not None:
            self.bottom_roi.setRegion(region)

        self._update_edit_time_ranges(region)

    def update_bottom_roi(self):
        # Do not let area outside signal
        region = self.bottom_roi.getRegion()
        self._roi_region = region
        if self.top_roi is not None:
            self.top_roi.setRegion(region)

        self._update_edit_time_ranges(region)

    def add_roi(self, axes, action):
        roi = pg.LinearRegionItem(self.roi_region, pen=pg.mkPen(width=3.5))
        roi.setZValue(-10)

        # Callback when area change.
        roi.sigRegionChanged.connect(action)
        axes.addItem(roi)
        return roi

    def plot_cbfv(self):
        self.plot_time_series(
            self.top_plot,
            self.time,
            self.cbfv,
            xlabel="Time (s)",
            ylabel="CBFV (cm/s)",
            xlim=[0, self.duration],
            color="g"
        )
        self.top_roi = self.add_roi(self.top_plot, self.update_top_roi)

    def plot_cbfv_psd(self):
        self.plot_psd(
            self.top_plot,
            self.results["frequency"],
            self.results["pyy"],  # TODO: change pyy to cbfv_psd
            vlf=self.vlf_range,
            lf=self.lf_range,
            hf=self.hf_range,
        )

    def plot_abp(self):
        self.plot_time_series(
            self.bottom_plot,
            self.time,
            self.abp,
            xlabel="Time (s)",
            ylabel="ABP (mmHg)",
            xlim=[0, self.duration],
            color="y"
        )
        self.bottom_roi = self.add_roi(self.bottom_plot, self.update_bottom_roi)

    def plot_abp_psd(self):
        self.plot_psd(
            self.bottom_plot,
            self.results["frequency"],
            self.results["pxx"],  # TODO: change pxx to abp_psd
            vlf=self.vlf_range,
            lf=self.lf_range,
            hf=self.hf_range,
        )

    def plot_time_series(self, axes, time, signal, xlabel, ylabel, xlim, color):
        axes.clear()
        axes.plot(time, signal, pen=pg.mkPen(color,  width=2))
        axes.setLabel("left", ylabel)
        axes.setLabel("bottom", xlabel)
        axes.showGrid(x=True, y=True, alpha=1.0)
        axes.setRange(xRange=xlim)

    def plot_psd(self, axes, frequency, psd, vlf, lf, hf):
        # For aesthetic reasons, the psd plot starts at 0 Hz and goes 1 frequency beyond its boundary
        indexes_vlf = numpy.where(numpy.logical_and(frequency >= 0, frequency < vlf[1]))[0]
        indexes_lf = numpy.where(numpy.logical_and(frequency >= lf[0], frequency < lf[1]))[0]
        indexes_hf = numpy.where(numpy.logical_and(frequency >= hf[0], frequency < hf[1]))[0]

        # Interp areas
        indexes_vlf = numpy.append(indexes_vlf, indexes_vlf[-1] + 1)
        indexes_lf = numpy.append(indexes_lf, indexes_lf[-1] + 1)

        axes.clear()
        # VLF
        axes.plot(frequency[indexes_vlf], psd[indexes_vlf], fillLevel=0.0, brush=(127, 127, 255, 200))
        # LF
        axes.plot(frequency[indexes_lf], psd[indexes_lf], fillLevel=0.0, brush=(178, 127, 255, 200))
        # HF
        axes.plot(frequency[indexes_hf], psd[indexes_hf], fillLevel=0.0, brush=(127, 127, 255, 200))

        axes.setRange(xRange=[0, 0.5])
        axes.setLabel("left", "PSD (ms²/Hz)")
        axes.setLabel("bottom", "Frequency (Hz)")
        axes.showGrid(x=True, y=True, alpha=1.0)
        # axes.removeItem(self.lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
