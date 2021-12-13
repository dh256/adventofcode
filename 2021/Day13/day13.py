from paper import Paper

paper = Paper('input.txt')
print(f'Part 1: {paper.do_folds()}')

paper2 = Paper('input.txt')
print(f'Part 2:\n\n {paper2.do_folds(all=True)}')