""" pprint sys.modules
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
import sys
import pprint

try:
    from . import _add_path
except:
    try:
        import _add_path
    except Exception as e:
        raise e
from python_cli_samples import utils


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    parser.description = __doc__
    parser.formatter_class = RawDescriptionHelpFormatter
    return parser


def main(*args, **kwargs):
    utils.show_dict(kwargs)
    pprint.pprint(sys.modules)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))