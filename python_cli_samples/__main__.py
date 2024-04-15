""" python cli samples
"""
from argparse import ArgumentParser, _SubParsersAction

try:
    from . import _add_path
except:
    import _add_path

def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    subparsers: _SubParsersAction = parser.add_subparsers()
    _add_find_imgs(subparsers)
    _add_print(subparsers)
    return parser


def main(*args, **kwargs):
    if 'handler' in kwargs.keys():
        handler = kwargs.pop('handler')
        handler(**kwargs)
    else:
        parser = ArgumentParser(description=__doc__)
        parser: ArgumentParser = add_arguments(parser)
        parser.print_help()


def _add_find_imgs(subparsers: _SubParsersAction):
    from python_cli_samples.tools import find_imgs
    parser: ArgumentParser = subparsers.add_parser("find_imgs", help=find_imgs.__doc__)
    parser = find_imgs.add_arguments(parser)
    parser.set_defaults(handler=find_imgs.main)


def _add_print(subparsers: _SubParsersAction):
    from python_cli_samples.tools import print
    parser: ArgumentParser = subparsers.add_parser("print", help=print.__doc__)
    parser = print.add_arguments(parser)
    parser.set_defaults(handler=print.main)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description=__doc__)
    parser = add_arguments(parser)
    main(**vars(parser.parse_args()))