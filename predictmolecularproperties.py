import numpy as np
import pandas as pd
import pickle as pk
import math
import json

INPUT_FILE = r"\moleculardata\test_input.json"
OUTPUT_FILE = r"\moleculardata\output.txt"
PERIODIC_TABLE = {
    'H':[1, 1.0079],
    'C':[6, 12.0107],
    'N':[7, 14.0067],
    'O':[8, 15.9994],
    'S':[16, 32.065],
    'F':[9, 18.9984],
    'Si':[14, 28.0855],
    'P':[15, 30.9738],
    'Cl':[17, 35.453],
    'Br':[35, 79.904],
    'I': [53, 126.9045]
}

def load_molecule():
    with open(INPUT_FILE) as f:
        data = json.load(f)
        return data[0]
    
def distance_matrix(molecule):
    coords = [np.array(atom["xyz"]) for atom in molecule["atoms"]]
    n_atoms = len(coords)
    distance_matrix = np.zeros((n_atoms, n_atoms))
    for x in range(n_atoms):
        for y in range(n_atoms):
            distance_matrix[x][y] = math.sqrt(np.sum(np.power(coords[x] - coords[y], 2)))
    
    return distance_matrix

def coulomb_matrix(molecules, distance_matrix):
    # TODO
    pass

def pretty_print(arr):
    with open(OUTPUT_FILE, "+wt") as f:
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                f.write(f"{arr[i][j]:.5f} ")
            f.write("\n")

molecule = load_molecule()
print(molecule["En"])

pretty_print(distance_matrix(molecule))