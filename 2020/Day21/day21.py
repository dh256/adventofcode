from Ingredients import Ingredients

ingredients = Ingredients('input.txt')
allergen_free,dang_ings = ingredients.allergen_free()
print(f'Part 1: {allergen_free}')
print(f'Part 2: {dang_ings}')

