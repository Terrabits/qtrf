from .ui_file       import Ui_FileWidget
from pathlib        import Path
from qtrf.QtCore    import Signal, Slot
from qtrf.QtWidgets import QFileDialog, QWidget


# constants
FILENAME_INDEX = 0


class FileWidget(QWidget):

    # constructor

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)
        self._file_path = None
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


    # file_path

    @property
    def file_path(self):
        return self._file_path


    @file_path.setter
    def file_path(self, file_path):

        # clear file path?
        if not file_path and self.file_path:
            self._file_path = None
            self.update_view()
            self.file_path_changed.emit(None)
            return

        # change file path?
        if file_path and file_path != self.file_path:
            self._file_path = Path(file_path)
            self._last_path = self.file_path.parent
            self.update_view()
            self.file_path_changed.emit(str(self.file_path))


    # signal: file path changed
    file_path_changed = Signal(str)


    # slot: choose file dialog

    @Slot(str)
    def choose_file(self):
        file_path = self.dialog()
        if not file_path:
            return
        self.file_path = file_path


    # slot: clear file_path

    @Slot()
    def clear(self):
        self.file_path = None


    # helpers


    def default_caption(self):
        return 'Save...' if self.save else 'Open...'


    def dialog(self):
        dialog   = QFileDialog.getSaveFileName if self.save else QFileDialog.getOpenFileName
        settings = {
            "parent":  self.window(),
            "caption": self.default_caption(),
            "dir":     str(self.last_path),
            "filter":  self.filter
        }
        return dialog(*settings.values())[FILENAME_INDEX]


    def update_view(self):
        # clear?
        if not self._file_path:
            self.ui.filename.clear()
            return

        # display file_path
        self.ui.filename.setText(self.file_path.name)


    def connect_qt_signals_and_slots(self):
        self.ui.open .clicked.connect(self.choose_file)
        self.ui.clear.clicked.connect(self.clear)
