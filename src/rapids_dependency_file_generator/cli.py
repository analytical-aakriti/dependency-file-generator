import argparse

import yaml

from ._version import __version__ as version
from .constants import OutputTypes, default_dependency_file_path
from .rapids_dependency_file_generator import make_dependency_files


def validate_args(argv):
    pass


def generate_matrix(matrix_arg):
    if not matrix_arg:
        return {}
    matrix = {}
    for matrix_column in matrix_arg.split(";"):
        kv_pair = matrix_column.split("=")
        matrix[kv_pair[0]] = [kv_pair[1]]
    return matrix


def main(argv=None):
    args = validate_args(argv)


    

