from collections import defaultdict, deque
import re

class Day19:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # replacements all lines up to 3rd from end
        # self.replacements: list containing replacement (source and replacement) as a tuple
        self.replacements: list[tuple[str, str]] = list()
        for line in lines[0:-2]:
            line_parts = line.split(' => ')
            self.replacements.append((line_parts[0],line_parts[1]))
        
        # medicine molecule is last line    
        self.medicine_molecule = lines[-1]
            
    def part1(self) -> int:
        '''
        Find each occurrence of source_mol in medicine_molecule
        For each occurence replace with replacement_mol. If new molecule not already found, add to possible_molecules
        When finished return number of possible molecules
        '''
        possible_molecules: set[str] = set()   # use a set ensures only distinct molecules are captured
        for source_mol, replacement_mol in self.replacements:
            # find all matches for source_mol in medicine_molecule
            # for each match, replace source_mol with replacement_mol and add to possible molecules set
            for match in re.finditer(rf'{source_mol}',self.medicine_molecule):
                new_molecule = self.medicine_molecule[0:match.start()] + replacement_mol + self.medicine_molecule[match.end():]
                possible_molecules.add(new_molecule) 
        
        return len(possible_molecules)

    def part2(self) -> int:
        '''
        Needed help with this one.
        Originally tried to use a BFS to build up molecule from e. Although worked for test cases not effective for actual input.
        Knew the idea was to work backwards from medicine molecule replacing molecules in molecule with source molecules until left with a single molecule that could only be replaced by e
        Could not figure out algo - solution below based on https://aoc.just2good.co.uk/2015/19.html 
        Note: Solution assumes that there's only one possible way of making medicince_molecule
        '''
        replacements: list[tuple[int,str]] = list()
        current_molecule = self.medicine_molecule
        molecule_changed = True
        while molecule_changed:
            molecule_changed = False
            for source_molecule, replacement_molecule in self.replacements:
                if source_molecule == 'e':
                    continue
                
                num_replacements = current_molecule.count(replacement_molecule)
                if num_replacements > 0:
                    current_molecule = current_molecule.replace(replacement_molecule,source_molecule)
                    replacements.append((num_replacements,current_molecule))
                    molecule_changed = True    

        # only a single e left - sum up all num_replacments and add 1 for e replacement
        return sum(replacements for replacements, molecule in replacements) + 1
    
   
                        
