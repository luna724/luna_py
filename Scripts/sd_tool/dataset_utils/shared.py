import os
import argparse
import sys

BASE_DIR = os.getcwd()
sys.path.append(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument("--colab",action="store_true")
arg = parser.parse_args()

isColab = arg.colab