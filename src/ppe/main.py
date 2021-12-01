import numpy as np

import os
import pkg_resources

artifacts_path = os.path.abspath(pkg_resources.resource_filename(__name__, '../../../../ppe/artifacts'))

def hello():
    print(f"Hello world!")

def print_artefact():
    from pudb import set_trace as st; st()
    with open(os.path.join(artifacts_path, 'artifact.txt'), 'r') as f:
        text = '\n'.join(f.readlines())
        print(f"Artifact content:\n{text}")

def main():
    print_artefact()

if __name__ == '__main__':
    main()
