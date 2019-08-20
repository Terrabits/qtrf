from .ui_filewidget             import Ui_FileWidget
from pathlib                    import Path
from PySide2.QtCore             import Slot
from PySide2.QtWidgets          import QFileDialog, QWidget

class FileWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)
        self.caption    = 'Open...'
        self.filter     = ''
        self._filename  = None
        self._last_path = ''
        self.ui.open .clicked.connect(self.choose_file)
        self.ui.clear.clicked.connect(self.clear)

    @property
    def filename(self):
        return self._filename
    @filename.setter
    def filename(self, value):
        self._filename  = value or ''
        self._last_path = str(Path(value).parent) if value else self._last_path
        self._update_filename()

    @Slot()
    def choose_file(self, dir=None):
        filename,_    = self._dialog(dir)
        self.filename = filename or self.filename
        return filename

    @Slot()
    def clear(self):
        self.filename = None

    def _dialog(self, dir=None):
        return QFileDialog.getOpenFileName(self.window(),
                                           self.caption,
                                           dir or self._last_path,
                                           self.filter)
    def _update_filename(self):
        if self._filename:
            self.ui.filename.setText(Path(self._filename).name)
        else:
            self.ui.filename.clear()
