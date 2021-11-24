import numpy as np

def hello():
    print(f"Hello world!")

def print_artefact():
    with open('artifact.txt', 'r') as f:
        text = '\n'.join(f.readlines())
        print(f"Artifact content:\n{text}")

def main():
    print_artefact()

if __name__ == '__main__':
    main()
