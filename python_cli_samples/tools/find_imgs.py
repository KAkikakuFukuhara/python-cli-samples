""" find imgs in dir
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path

try:
    import _add_path
except:
    try:
        from . import _add_path
    except Exception as e:
        raise e
from python_cli_samples import utils


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    parser.description = __doc__
    parser.formatter_class = RawDescriptionHelpFormatter
    parser.add_argument("file_dir", type=str, help="file dir")
    return parser


def main(*args, **kwargs):
    utils.show_dict(kwargs)

    file_dir = Path(kwargs['file_dir'])

    assert file_dir.exists()
    find_imgs(file_dir)


def find_imgs(file_dir: Path):
    pass


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))