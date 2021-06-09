from .helpers import validator


class ValidatorMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_validator()


    # helpers

    def update_validator(self):
        self.setValidator(validator())
