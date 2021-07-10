import re

class Ingredients:
    '''
    Constructor
    '''
    def __init__(self,input_file):
        # ingredients is a dictionary - key is ingredient name, value is a list containing number of times it appears and the allergen it contains, if any
        self.foods = {}
        self.ingredients = {}
        self.dangerous_ingredients = {}
        with open(input_file,"r") as in_file:
            expr = re.compile(r'\w+')
            for food in [line.strip('\n') for line in in_file]:
                parts = expr.findall(food)
                contains_index = parts.index('contains')
                ingredients, allergens = parts[0:contains_index], parts[contains_index+1:]

                # update running total of number of times each ingredient appears
                # required for Part 1
                for ingredient in ingredients:
                    try:
                        self.ingredients[ingredient] += 1
                    except:
                        self.ingredients[ingredient] = 1

                # populate foods structure
                for allergen in allergens:
                    if allergen in self.foods.keys():
                        self.foods[allergen].append(set(ingredients))
                    else:
                        self.foods[allergen] = [set(ingredients)]

    # removes specificied ingredients from all sets
    def remove_ingredient(self,ingredient):
        for ingredient_sets in self.foods.values():
            for ingredient_set in ingredient_sets:
                try:
                    ingredient_set.remove(ingredient)
                except:
                    pass

    '''
    Return a list of allergen free ingredients
    '''
    def allergen_free(self):
        # for each allergen:
        #      check whether it has a single set with a single value -> match found (add to dangeround ingredients)
        #      or intersect all the sets, if intersect contains a single value -> match found (add to dangeround ingredients)
        # keep going until no further candidates found
        # Part 1: everything left is an ingredient with no allergens - total up number of times for each ingredient appears in ingredients lists
        # Part 2: sort dangerous ingredentients by allegren and concat all ingredients together into , seperated string
        while True:
            candidates_found = False
            for allergen, ingredient_sets in self.foods.items():
                if len(ingredient_sets) == 1 and len(ingredient_sets[0]) == 1:
                    ingredient = list(ingredient_sets[0])[0]
                    # Part 2: This is a dangerous ingredient
                    self.dangerous_ingredients[allergen] = ingredient
                    self.remove_ingredient(ingredient)
                    self.foods.pop(allergen)
                    candidates_found = True
                    break
                elif len(ingredient_sets) > 1:
                    i = set.intersection(*ingredient_sets)
                    if len(i) == 1:
                        # loop through all ingredient sets removing values
                        ingredient = list(i)[0]
                        self.remove_ingredient(ingredient)
                        # Part 2: This is a dangerous ingredient
                        self.dangerous_ingredients[allergen] = ingredient
                        candidates_found = True
                        break

            if not candidates_found:
                break

        # anything left cannot contain an allergen
        allergen_free = set()
        for ingredient_sets in self.foods.values():
            for ingredient_set in ingredient_sets:
                for ingredient in ingredient_set:
                    allergen_free.add(ingredient)
        
        # Part 1: total up number of times each allergen appears in all ingredient lists
        total = 0
        for i in allergen_free:
            total += self.ingredients[i]
        
        # Part 2: sort dangerous ingredients list by allergen. Return string containing all associated ingredients comma seperated
        dang_ings = ','.join([self.dangerous_ingredients[i] for i in sorted(self.dangerous_ingredients)])

        return total, dang_ings
