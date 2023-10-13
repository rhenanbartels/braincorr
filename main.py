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

        # Init last opened directory
        self.last_dir = "."
        self.file_name = ""

        # Init plot config variables
        self.top_plot_roi_coord = None
        self.bottom_plot_roi_coord = None

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

    def _save_last_dir(self, file_name):
        self.last_dir = os.path.dirname(file_name)

    def _set_file_name(self, file_path):
        file_name = os.path.basename(file_path)
        self.lineEditFileName.setText(file_name)

    def _update_edit_time_ranges(self):
        self.lineEditStartTimeAxes.setText(f"{self.top_plot_roi_coord[0]:.2f}")
        self.lineEditEndTimeAxes.setText(f"{self.top_plot_roi_coord[1]:.2f}")

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

            self.plot(self.time, self.cbfv, self.abp)
            self.top_plot_roi_coord = (0, self.duration)
            self.bottom_plot_roi_coord = (0, self.duration)
            self._update_edit_time_ranges()

            # Signal Processing
            # TODO: get config from panel
            fs = 10.0
            self.results = tfa(self.abp, self.cbfv, fs)

            self.plot_psd(
                self.bottom_plot,
                self.results["frequency"],
                self.results["pxx"],
                vlf=self.vlf_range,
                lf=self.lf_range,
                hf=self.hf_range,
            )

    def _plot(self, time, cbv, abp):
        global p1, p2
        pw = self.top_plot
        pw.setWindowTitle('pyqtgraph example: MultiplePlotAxes')
        p1 = pw.plotItem
        p1.setLabels(left='axis 1')

        p2 = pg.ViewBox()
        p1.showAxis('right')
        p1.scene().addItem(p2)
        p1.getAxis('right').linkToView(p2)
        p2.setXLink(p1)
        p1.getAxis('right').setLabel('axis2', color='#0000ff')

        ## Handle view resizing
        def updateViews():
            ## view has resized; update auxiliary views to match
            global p1, p2
            p2.setGeometry(p1.vb.sceneBoundingRect())
            ## need to re-update linked axes since this was called
            ## incorrectly while views had different shapes.
            ## (probably this should be handled in ViewBox.resizeEvent)
            p2.linkedViewChanged(p1.vb, p2.XAxis)

        updateViews()
        p1.vb.sigResized.connect(updateViews)

        p1.plot(time, cbv)
        p2.addItem(pg.PlotCurveItem(time, abp, pen='b'))

    def update_top_plot(self):
        # Do not let area outside signal
        self.top_plot_roi_coord = self.lb.getRegion()
        self.lr.setRegion(self.top_plot_roi_coord)
        self._update_edit_time_ranges()

    def update_bottom_plot(self):
        # Do not let area outside signal
        self.bottom_plot_roi_coord = self.lr.getRegion()
        self.lb.setRegion(self.bottom_plot_roi_coord)
        self._update_edit_time_ranges()

    def plot(self, time, cbfv, abp):
        self.top_plot.plot(time, cbfv, pen=pg.mkPen("g",  width=2))
        self.top_plot.setLabel("left", "CBFV (cm/s)")
        self.top_plot.setLabel("bottom", "Time (s)")
        self.top_plot.showGrid(x=True, y=True, alpha=1.0)
        #self.top_plot.addItem(pg.LineROI([0,  90], [300, 0], width=1, pen=(1,9)))

        self.lr = pg.LinearRegionItem([0, self.duration], pen=pg.mkPen(width=3.5))
        self.lr.setZValue(-10)

        # Callback when area change.
        self.lr.sigRegionChanged.connect(self.update_bottom_plot)
        self.top_plot.addItem(self.lr)

        #self.top_plot.addLine(x=0, y=90, pen=pg.mkPen("b", width=3))
        #self.top_plot.addLine(x=300, y=90, pen=pg.mkPen("b", width=3))

        self.top_plot.setRange(xRange=[self.start_signal, self.duration])

        self.bottom_plot.plot(time, abp, pen=pg.mkPen("y", width=2))
        self.bottom_plot.setLabel("left", "ABP (mmHg)")
        self.bottom_plot.setLabel("bottom", "Time (s)")
        self.bottom_plot.showGrid(x=True, y=True, alpha=1.0)
        self.lb = pg.LinearRegionItem([0, self.duration], pen=pg.mkPen(width=3.5))
        self.lb.setZValue(-10)

        # Callback when area change.
        self.lb.sigRegionChanged.connect(self.update_top_plot)
        self.bottom_plot.addItem(self.lb)

        # self.side_top_plot.plot(x, y)
        # self.side_bottom_plot.plot(x, y)

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
        # axes.removeItem(self.lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
