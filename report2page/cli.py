import argparse
#import click
from report2page import main

def report_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help='Path to config.yaml file',
                        default="config.yaml", nargs="?")

    args = parser.parse_args()

    config_path = args.config

    doc = main(config_path)

    print(doc)
#
# @click.command()
# def cli():
#     """Example script."""
#     click.echo('Hello World!')