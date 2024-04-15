""" python cli samples
"""
from argparse import ArgumentParser, _SubParsersAction


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    subparsers: _SubParsersAction = parser.add_subparsers()
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


def _add_print_modules(subparsers: _SubParsersAction):
    from tools import print_modules
    parser: ArgumentParser = subparsers.add_parser("print_modules", help=print_modules.__doc__)
    parser = print_modules.add_arguments(parser)
    parser.set_defaults(handler=print_modules.main)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description=__doc__)
    parser = add_arguments(parser)
    main(**vars(parser.parse_args()))