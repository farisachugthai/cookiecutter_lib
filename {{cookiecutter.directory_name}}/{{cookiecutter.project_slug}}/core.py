"""Main module.

Console script for {{cookiecutter.project_slug}}.
"""
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import logging
import sys

# Install using pip to uncomment this and the parser argument `__version__`.
# from . import __version__

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}


def _parse_args():
    """Parse arguments given by the user.

    Returns
    -------
    args : :class:`argparse.NameSpace()`
        Arguments provided by the user and handled by argparse.

    """
    parser = argparse.ArgumentParser(
        prog="{{cookiecutter.project_slug}}",
        description="{{cookiecutter.project_short_description}}",
    )

    # parser.add_argument('_', nargs='*')

    parser.add_argument(
        "-l",
        "--log",
        action="store_false",
        help="Where to write log records to. Defaults to stdout.",
    )

    parser.add_argument(
        "-ll",
        "--log-level",
        dest="log_level",
        choices=[10, 20, 30, 40, 50],
        type=int,
        help="Log level. If logging is specified with '-l', defaults to 30.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_false",
        help="Shorthand to enable verbose logging and increase level to `debug`.",
    )

    # parser.add_argument("--version", action="version", version=__version__)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")

    # handle a few of our args
    if args.log_level is None:
        # no LOG_LEVEL specified but -l was specified
        if args.log is not None:
            LOG_LEVEL = logging.WARNING
        else:
            # Don't log
            LOG_LEVEL = 99
    else:
        LOG_LEVEL = args.log_level

    logging.basicConfig(level=LOG_LEVEL)

    return args


def main():
    """Console script for {{cookiecutter.project_slug}}."""
    args = _parse_args()


{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

# Vim: set ft=jinja.python:
