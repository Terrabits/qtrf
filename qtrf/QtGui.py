try:

    # dumpy pyside6
    from PySide6.QtGui import *


except ModuleNotFoundError:

    # pyside6 not installed


    try:

        # dump pyside2
        from PySide2.QtGui import *

    except ModuleNotFoundError:

        # pyside2 not installed

        # pyside not found
        raise ModuleNotFoundError('qtrf requires either PySide6 or PySide2')
