# PART 1
numRecipes = 540391
elf1Index = 0
elf2Index = 1
recipes = [3,7]
while len(recipes) < numRecipes + 11:
    elf1Recipe = recipes[elf1Index]
    elf2Recipe = recipes[elf2Index]
    nextRecipe = elf1Recipe + elf2Recipe
    if nextRecipe < 10:
        recipes.append(nextRecipe)
    else:
        recipes.append(nextRecipe // 10)
        recipes.append(nextRecipe % 10)
    elf1Index = (elf1Index + elf1Recipe + 1) % len(recipes)  # % wraps if goes off end 
    elf2Index = (elf2Index + elf2Recipe + 1) % len(recipes)      

last10Recipes = recipes[numRecipes:numRecipes+10]
answer = ""
for recipe in last10Recipes:
    answer += str(recipe)
print(f'Part 1 Answer: {answer}')

# PART 2 similar to above but run until numRecipes is first found in recipes
# The count number of recipes to left of this
strToFind = "54039" # Note: "540391" given on web site doesn't work
lenStrToFind = len(strToFind)
lstToFind = [int(c) for c in strToFind]
elf1Index = 0
elf2Index = 1
recipes = [3,7]
while True:
    elf1Recipe = recipes[elf1Index]
    elf2Recipe = recipes[elf2Index]
    nextRecipe = elf1Recipe + elf2Recipe
    if nextRecipe < 10:
        recipes.append(nextRecipe)
    else:
        recipes.append(nextRecipe // 10)
        recipes.append(nextRecipe % 10)
    
    if recipes[lenStrToFind * -1:] == lstToFind:
        recipesToLeft = len(recipes) - lenStrToFind
        print(f'Part 2 answer: {recipesToLeft}')
        break    
    else:
        elf1Index = (elf1Index + elf1Recipe + 1) % len(recipes)  # % wraps if goes off end 
        elf2Index = (elf2Index + elf2Recipe + 1) % len(recipes)

