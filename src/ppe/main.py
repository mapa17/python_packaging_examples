import numpy as np

import os
import pkg_resources

artifacts1_path = os.path.abspath(pkg_resources.resource_filename(__name__, '../../../../ppe/artifacts/artifact.txt'))
artifacts2_path = os.path.abspath(pkg_resources.resource_filename(__name__, 'data/artifact2.txt'))

def hello():
    print(f"Hello world!")

def print_artefact():
    with open(artifacts1_path, 'r') as f:
        text = '\n'.join(f.readlines())
        print(f"Artifact 1 content:\n{text}")

    with open(artifacts2_path, 'r') as f:
        text = '\n'.join(f.readlines())
        print(f"Artifact 2 content:\n{text}")


def main():
    print_artefact()

if __name__ == '__main__':
    main()
