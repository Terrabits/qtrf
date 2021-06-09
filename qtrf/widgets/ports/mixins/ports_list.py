from   .ports         import to_list, to_str
import builtins
from   PySide2.QtCore import Signal


class PortsListMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._list = []

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, list):
        if self.list == list:
            # list is unchanged
            return

        # set
        self._list = list
        self.update_text()

        # list has changed:
        # emit signal
        self.list_changed.emit(self.list)

    list_changed = Signal(builtins.list)

    # helpers

    def update_text(self):
        self.setText(to_str(self.list))
