"""Taller evaluable"""

# pylint: disable=broad-exception-raised

import fileinput
import glob
import os.path
import string
import time
from itertools import groupby

from toolz.itertoolz import concat, pluck


def copy_raw_files_to_input_folder(n):
    """Generate n copies of the raw files in the input folder"""

    create_directory("files/input")

    for file in glob.glob("files/raw/*"):

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        for i in range(1, n + 1):
            filename = f"{os.path.basename(file).split('.')[0]}_{i}.txt"
            with open(f"files/input/{filename}", "w", encoding="utf-8") as f2:
                f2.write(text)


def load_input(input_directory):
    """Funcion load_input"""

    sequence = []
    files = glob.glob(f"{input_directory}/*")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))
    return sequence


def preprocess_line(x):
    """Preprocess the line x"""
    text = x[1]
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.replace("\n", "")
    return (x[0], text)


def map_line(x):
    x = preprocess_line(x)
    x = x[1].split()
    x = [(w, 1) for w in x[1].split()]
    return x


def mapper(sequence):
    """Mapper"""
    sequence = map(map_line, sequence)
    sequence = concat(sequence)
    return sequence


def shuffle_and_sort(sequence):
    """Shuffle and Sort"""


def compute_sum_by_group(group):
    pass


def reducer(sequence):
    """Reducer"""


def create_directory(directory):
    """Create Output Directory"""

    if os.path.exists(directory):
        for file in glob.glob(f"{directory}/*"):
            os.remove(file)
        os.rmdir(directory)

    os.makedirs(directory)


def save_output(output_directory, sequence):
    """Save Output"""


def create_marker(output_directory):
    """Create Marker"""


def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_directory(output_directory)
    save_output(output_directory, sequence)
    create_marker(output_directory)


if __name__ == "__main__":

    copy_raw_files_to_input_folder(n=1000)

    start_time = time.time()

    run_job(
        "files/input",
        "files/output",
    )

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
