from itertools import islice

def processInput(filename):
    with open(filename, "r") as file_input:
        return file_input.read()

input_data = processInput('day8_full.txt')
it = iter(int(x) for x in input_data.split(" "))  # input_data is the entire input string

def recurse():
    """return (sum, value)"""
    child_count = next(it)
    metadata_count = next(it)
    if child_count == 0:
        total_value = total_sum = sum(islice(it, metadata_count))
        return total_sum, total_value

    total_sum = total_value = 0
    child_values = []
    for _ in range(child_count):
        child_sum, child_value = recurse()
        total_sum += child_sum
        child_values.append(child_value)
    for metadatum in islice(it, metadata_count):
        total_value += child_values[metadatum - 1] if 0 <= metadatum - 1 <= child_count - 1 else 0
        total_sum += metadatum
    return total_sum, total_value

final_sum, final_value = recurse()
print(f"A: {final_sum}, B: {final_value}")