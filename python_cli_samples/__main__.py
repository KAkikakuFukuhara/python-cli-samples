""" python cli samples main
"""
from argparse import ArgumentParser

try:
    from . import _add_path
except:
    import _add_path
from python_cli_samples.tools import main, add_arguments


if __name__ == "__main__":
    parser = ArgumentParser()
    parser: ArgumentParser = add_arguments(parser)
    main(**vars(parser.parse_args()))