import os
import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

import pyqtgraph as pg

from signal import open_csv_file
from ui_braincorr import Ui_MainWindow


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

    def _save_last_dir(self, file_name):
        self.last_dir = os.path.dirname(file_name)

    def open_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select file",
            self.last_dir,
            "CSV files (*.csv)"
        )
        if self.file_name:
            self._save_last_dir(self.file_name)
            self.time, self.cbv, self.abp = open_csv_file(self.file_name)
            self.plot(self.time, self.cbv, self.abp)

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
        self.lr.setRegion(self.lb.getRegion())

    def update_bottom_plot(self):
        # Do not let area outside signal
        self.lb.setRegion(self.lr.getRegion())

    def plot(self, time, cbv, abp):
        self.top_plot.plot(time, cbv, pen=pg.mkPen("g",  width=2))
        self.top_plot.setLabel("left", "CBV (cm/s)")
        self.top_plot.setLabel("bottom", "Time (s)")
        self.top_plot.showGrid(x=True, y=True, alpha=1.0)
        #self.top_plot.addItem(pg.LineROI([0,  90], [300, 0], width=1, pen=(1,9)))

        self.lr = pg.LinearRegionItem([0, 300], pen=pg.mkPen(width=3.5))
        self.lr.setZValue(-10)

        # Callback when area change.
        self.lr.sigRegionChanged.connect(self.update_bottom_plot)
        self.top_plot.addItem(self.lr)

        #self.top_plot.addLine(x=0, y=90, pen=pg.mkPen("b", width=3))
        #self.top_plot.addLine(x=300, y=90, pen=pg.mkPen("b", width=3))

        # self.top_plot.setRange(xRange=[5, 20], yRange=[55, 65])

        self.bottom_plot.plot(time, abp, pen=pg.mkPen("y", width=2))
        self.bottom_plot.setLabel("left", "ABP (mmHg)")
        self.bottom_plot.setLabel("bottom", "Time (s)")
        self.bottom_plot.showGrid(x=True, y=True, alpha=1.0)
        self.lb = pg.LinearRegionItem([0, 300], pen=pg.mkPen(width=3.5))
        self.lb.setZValue(-10)

        # Callback when area change.
        self.lb.sigRegionChanged.connect(self.update_top_plot)
        self.bottom_plot.addItem(self.lb)

        # self.side_top_plot.plot(x, y)
        # self.side_bottom_plot.plot(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
