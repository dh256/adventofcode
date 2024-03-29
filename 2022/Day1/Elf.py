class Elf:

    def __init__(self, file_name) -> None:
        self.elves = []
        with open(file_name) as input_file:
            for line in input_file:
                try:
                    cals = int(line.strip('\n'))
                    self.elves[-1] += cals
                except:
                    self.elves.append(0)

        # sort by calorie count, descending
        self.elves = sorted(self.elves, key=lambda cal: cal, reverse=True)


    def topn_most_calorific(self, n: int) -> int:
        return sum(self.elves[0:n])