# Need to come back and complete part2
# Requires recursion
import re
from typing import Container

class Bags():
    def __init__(self,file_name):
        self.bags = {}
        with open(file_name,"r") as input_file:
            bag_descs = [line.strip('\n') for line in input_file]
            for bag_desc in bag_descs:
                colour = Bags._get_colour(bag_desc)
                contents = Bags._get_contents(bag_desc)
                self.bags[colour] = contents

    @staticmethod
    def _get_colour(bag_desc):
        m = re.match(r"(\w+ \w+) (?:bags contain)",bag_desc)
        return m.group(1)
    
    @staticmethod
    def _get_contents(bag_desc):
        m = re.match(r"(?:\w+ \w+ bags contain) (.+)",bag_desc)
        contents_desc = m.group(1)
        if contents_desc == "no other bags.":
            return None
        else:
            bags = contents_desc.split(", ")
            contents = []
            for bag in bags:
                m = re.match(r"(\d+) (\w+ \w+) bag",bag)
                colour = m.group(2) 
                num_bags = int(m.group(1))
                contents.append((colour,num_bags))
            return contents

    def find(self,colour):
        return self.bags[colour]
        
    def contains(self,bags=0):
        '''
        Returns number of bags that contain at least one shiny gold bag
        '''
        bags = 0
        for (colour,contents) in self.bags.items():
            # check bag contents
            # if chain of contents at least one shiny gold, increment by 1
            if self.contains_gold_bag(contents):
                print(colour)
                bags += 1
        return bags

    def contains_gold_bag(self,contents):
        if contents == None:
            return False
        if len(list(filter(lambda c : c[0] == "shiny gold",contents))) > 0:
            return True
        else:
            result = False
            for c in contents:
                result = result or self.contains_gold_bag(self.find(c[0]))
            return result

    def bags_inside_shiny_gold_bag(self,contents=None):
        '''
        Return the total number of bags inside shiny gold bag
        '''
        total_bags = 0
        for c in self.bags['shiny gold']:
            total_bags += c[1] * self.bags_inside(c[1],)
        return total_bags

    def bags_inside(self,contents,multiple):
        if contents == None:
            return multiple
        else:
            return contents[1] * bags_inside()