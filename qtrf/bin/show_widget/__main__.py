from   .command_line     import parse_args
import code
from   qtrf.QtWidgets import QApplication
import qtrf.widgets
import sys


def is_qtrf_widget(name):
    return name in dir(qtrf.widgets)


def main():
    # parse CLI input
    args = parse_args()

    # create qt app
    app  = QApplication()

    # is qtrf.widget_class?
    try:
        WidgetClass = getattr(qtrf.widgets, args.widget_class)
    except AttributeError:
        print(f"error: class '{args.widget_class}' not found in qtrf")
        sys.exit(404)

    # create
    widget = WidgetClass()
    widget.show()

    # run
    return_code = app.exec_()

    # interactive mode?
    if args.interactive:
        banner = f'widget: {widget}'
        code.interact(banner, local=locals())

    sys.exit(return_code)


if __name__ == '__main__':
    main()
