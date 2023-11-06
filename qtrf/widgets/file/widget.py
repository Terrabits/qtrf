from .ui_file                   import Ui_FileWidget
from pathlib                    import Path
from PySide6.QtCore             import Signal, Slot
from PySide6.QtWidgets          import QFileDialog, QWidget


# constants
FILENAME_INDEX = 0


class FileWidget(QWidget):

    # constructor

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)
        self._filename  = None
        self.caption    = None
        self.filter     = ''
        self.save       = False
        self.last_path  = '.'
        self.connect_qt_signals_and_slots()


    # last path (pathlib Path object)

    @property
    def last_path(self):
        return self._last_path

    @last_path.setter
    def last_path(self, last_path):
        self._last_path = Path(last_path)


    # filename

    @property
    def filename(self):
        return self._filename


    @filename.setter
    def filename(self, filename):

        # clear filename?
        if not filename and self.filename:
            self._filename = None
            self.update_filename()
            self.filename_changed.emit(None)
            return

        # change filename?
        if filename and filename != self.filename:
            self._filename  = Path(filename)
            self._last_path = self._filename.parent
            self.update_filename()
            self.filename_changed.emit(self.filename)


    # signal: filename changed
    filename_changed = Signal(str)


    # slot: choose file (dialog)

    @Slot()
    def choose_file(self, dir=None):
        filename = self.dialog(dir)
        if not filename:
            return
        self.filename = filename


    # slot: clear filename

    @Slot()
    def clear(self):
        self.filename = None


    # helpers


    def default_caption(self):
        return 'Save...' if self.save else 'Open...'


    def dialog(self, dir=None):
        dialog   = QFileDialog.getSaveFileName if self.save else QFileDialog.getOpenFileName
        settings = {
            "parent":  self.window(),
            "caption": self.default_caption(),
            "dir":     dir or str(self.last_path),
            "filter":  self.filter
        }
        return dialog(*settings.values())[FILENAME_INDEX]


    def update_filename(self):
        if self._filename:
            self.ui.filename.setText(Path(self._filename).name)
        else:
            self.ui.filename.clear()


    def connect_qt_signals_and_slots(self):
        self.ui.open .clicked.connect(self.choose_file)
        self.ui.clear.clicked.connect(self.clear)
