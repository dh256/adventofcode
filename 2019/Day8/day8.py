from Image import Image
image_size = (25,6)
image_data = "input.txt"

image = Image(image_data,25,6)
part1_answer = image.part1()
print(f'Part 1 Answer: {part1_answer}')
part2_answer = image.part2()

