import pytest
from Ingredients import Ingredients

test_data = [("test.txt",5,"mxmxvkd,sqjhc,fvjkl")]

# Tests Part 1 and Part 2
@pytest.mark.parametrize("input_file,appear,dang_ings",test_data)
def test_allergen_free(input_file,appear,dang_ings):
    ingredients = Ingredients(input_file)
    assert appear, dang_ings == ingredients.allergen_free()
    
