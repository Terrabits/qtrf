from PySide2.QtCore import QObject, QPropertyAnimation, Slot
from threading      import RLock


# constants
STOPPED = QPropertyAnimation.Stopped


# filter
def is_stopped(animation):
    return animation.state() == STOPPED


class AnimationsList(QObject):
    def __init__(self):
        super().__init__()

        self.lock       = RLock()
        self.animations = []

    def __del__(self):
        with self.lock:
            self.stop_all()
            self.prune_all()

    def add(self, animation):
        with self.lock:
            self.clear()

            # add
            self.animations.append(animation)

            # prune on finished
            animation.finished.connect(self.prune)

    @Slot()
    def prune(self):
        with self.lock:
            for animation in self.animations:
                if not is_stopped(animation):
                    # animation is still active.
                    # leave it alone
                    continue

                # animation is stopped.
                # need to remove it.
                self.prune_animation(animation)


    # helpers

    def stop_all(self):
        with self.lock:
            for animation in self.animations:
                animation.stop()

    def prune_animation(self, animation):
        with self.lock:
            assert animation in self.animations

            # find index
            index = self.animations.index(animation)
            assert index != -1

            # delete python reference
            del(self.animations[index])

            # mark for Qt garbage collection
            animation.deleteLater()

    def prune_all(self):
        with self.lock:
            for animation in self.animations:
                self.prune_animation(animation)

    def clear(self):
        self.stop_all()
        self.prune_all()
