import numpy as np
from typing import Type

class Validator():
    def __init__(self, entry):
        self.entry = entry
    
    def add_all_vertical(self):
        results = [''.join(secuence[i] for secuence in self.entry) for i in range(6)]
        return results
    
    def add_all_diagonals(self):
        matrix = np.array([list(row) for row in self.entry])
        diagonal_normal = [''.join(matrix.diagonal(i)) for i in range(-2, 3)]
        anti_diagonal = [''.join(np.fliplr(matrix).diagonal(i)) for i in range(-2, 3)]

        diagonals = diagonal_normal + anti_diagonal
        return diagonals
    
    def get_all_combinatios(self):
        verticals = self.add_all_vertical()
        diagonals = self.add_all_diagonals()
        
        results = verticals + diagonals
        return results

class DnaTester():

    def __init__(self):
        self.dna = ["AAAA", "TTTT", "CCCC", "GGGG"]
    
    def isMutant(self, entry):
        print(entry)
        results = entry.copy()
        validator = Validator(entry)
        results += validator.get_all_combinatios()

        mutants = list(filter(lambda x: any(substr in x for substr in self.dna), results))

        return True if len(mutants) > 0 else False

