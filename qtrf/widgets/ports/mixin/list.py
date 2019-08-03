from ..ports import entry_to_list, list_to_entry

class ListMixin(object):
    @property
    def list(self):
        return entry_to_list(self.text())
    @list.setter
    def list(self, ports):
        self.setText(list_to_entry(ports))
