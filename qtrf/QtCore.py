try:

    # dumpy pyside6
    from PySide6.QtCore import *


except ModuleNotFoundError:

    # pyside6 not installed


    try:

        # dumpy pyside2
        from PySide2.QtCore import *

    except ModuleNotFoundError:

        # pyside2 not installed

        # pyside not found
        raise ModuleNotFoundError('qtrf requires either PySide6 or PySide2')
