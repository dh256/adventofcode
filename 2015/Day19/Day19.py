from collections import defaultdict
import re

class Day19:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # replacements all lines up to 3rd from end
        self.replacements: dict[str, list[str]] = defaultdict(list)
        for line in lines[0:-2]:
            line_parts = line.split(' => ')
            self.replacements[line_parts[0]].append(line_parts[1])
        
        # calibration molecule is last line    
        self.calibration_molecule = lines[-1]
            
    def part1(self) -> int:
        possible_molecules: set[str] = set()
        for source_mol, replacement_mols in self.replacements.items():
            for replacement_mol in replacement_mols:
                # find all matches for source_mol in calibration molecules
                # for each match, replace source_mol with replacement_mol and add to possible molecules set
                for match in re.finditer(rf'{source_mol}',self.calibration_molecule):
                    new_molecule = self.calibration_molecule[0:match.start()] + replacement_mol + self.calibration_molecule[match.end():]
                    possible_molecules.add(new_molecule) 
        
        return len(possible_molecules)

    def part2(self) -> int:
        return 0
                        
