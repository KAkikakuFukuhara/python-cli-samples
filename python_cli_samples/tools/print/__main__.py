""" print tools
"""
from argparse import ArgumentParser, _SubParsersAction

import _add_path

def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    subparsers: _SubParsersAction = parser.add_subparsers()
    _add_print_syspath(subparsers)
    _add_print_modules(subparsers)
    return parser


def main(*args, **kwargs):
    if 'handler' in kwargs.keys():
        handler = kwargs.pop('handler')
        handler(**kwargs)
    else:
        parser = ArgumentParser(description=__doc__)
        parser: ArgumentParser = add_arguments(parser)
        parser.print_help()


def _add_print_syspath(subparsers: _SubParsersAction):
    from python_cli_samples.tools.print import print_syspath
    parser: ArgumentParser = subparsers.add_parser("syspath", help=print_syspath.__doc__)
    parser = print_syspath.add_arguments(parser)
    parser.set_defaults(handler=print_syspath.main)


def _add_print_modules(subparsers: _SubParsersAction):
    from python_cli_samples.tools.print import print_modules
    parser: ArgumentParser = subparsers.add_parser("modules", help=print_modules.__doc__)
    parser = print_modules.add_arguments(parser)
    parser.set_defaults(handler=print_modules.main)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description=__doc__)
    parser = add_arguments(parser)
    main(**vars(parser.parse_args()))