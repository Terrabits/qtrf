from .helpers                         import points_validator
from qtrf.widgets.int_value.line_edit import IntValueLineEdit


class PointsLineEdit(IntValueLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.update_validator()

    def update_validator(self):
        self.setValidator(points_validator())
