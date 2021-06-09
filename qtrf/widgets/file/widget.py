from .ui_file                   import Ui_FileWidget
from pathlib                    import Path
from PySide2.QtCore             import Signal, Slot
from PySide2.QtWidgets          import QFileDialog, QWidget


class FileWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)
        self.caption    = 'Open...'
        self.filter     = ''
        self._filename  = None
        self._last_path = Path('.')
        self.ui.open .clicked.connect(self.choose_file)
        self.ui.clear.clicked.connect(self.clear)

    @property
    def filename(self):
        if self._filename:
            return str(self._filename)
        else:
            return None

    @filename.setter
    def filename(self, filename):
        if not filename and self.filename:
            # clear
            self._filename = None
            self._update_filename()
            self.filename_changed.emit(None)
            return

        if filename and filename != self.filename:
            self._filename  = Path(filename)
            self._last_path = self._filename.parent
            self._update_filename()
            self.filename_changed.emit(self.filename)

    filename_changed = Signal(str)

    @Slot()
    def choose_file(self, dir=None):
        filename = self._dialog(dir)
        if not filename:
            return
        self.filename = filename

    @Slot()
    def clear(self):
        self.filename = None

    # helpers

    def _dialog(self, dir=None):
        return QFileDialog.getOpenFileName(self.window(),
                                           self.caption,
                                           dir or str(self._last_path),
                                           self.filter)[0]
    def _update_filename(self):
        if self._filename:
            self.ui.filename.setText(Path(self._filename).name)
        else:
            self.ui.filename.clear()
