from PySide2.QtCore import QEasingCurve, QPropertyAnimation
from time import sleep


# constants
OFFSET_PX    =  10
AMPLITUDE_PX =   3
PERIOD_S     = 300e-3
DURATION_MS  = 500


def shake(window):
    # window starts shifted to the right
    start_position = window.geometry()
    start_position.moveRight(start_position.right() + OFFSET_PX)

    # window stops in original position
    end_position = window.geometry()

    # define window shake "curve"
    shake_curve = QEasingCurve(QEasingCurve.OutElastic)
    shake_curve.setAmplitude(AMPLITUDE_PX)
    shake_curve.setPeriod(PERIOD_S)

    # define animation properties
    animation = QPropertyAnimation(window, b'geometry')
    animation.setStartValue(start_position)
    animation.setEndValue  (end_position)
    animation.setDuration(DURATION_MS)
    animation.setEasingCurve(shake_curve)

    # start
    animation.start()
    return animation
