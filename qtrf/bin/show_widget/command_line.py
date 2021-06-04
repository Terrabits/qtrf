import argparse


description='dtool for live debug of qtrf widgets'


def parse_args():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--interactive', action='store_true', help='show python prompt before exit')
    parser.add_argument('widget_class')
    return parser.parse_args()
