class Box:
    def __init__(self, line):
        dimensions = line.split('x')
        self.l = int(dimensions[0])
        self.w = int(dimensions[1])
        self.h = int(dimensions[2])

        self.side_areas = []
        self.side_areas.append(self.l * self.h)
        self.side_areas.append(self.l * self.w)
        self.side_areas.append(self.w * self.h)

        self.side_perims = []
        self.side_perims.append(2 * self.l + 2 * self.w)
        self.side_perims.append(2 * self.w + 2 * self.h)
        self.side_perims.append(2 * self.l + 2 * self.h)


        self.volume = self.l * self.h * self.w
        self.surface_area = 2 * sum(self.side_areas)
        self.smallest_side_area = min(self.side_areas)
        self.smallest_side_perim = min(self.side_perims)
    
    def sheets(self):
        return self.surface_area + self.smallest_side_area

    def ribbon(self):
        return self.volume + self.smallest_side_perim

class Boxes:
    def __init__(self, filename):
        with open(filename, "r") as data:
            self.boxes = [Box(line.strip('\n')) for line in data]

    def total_sheets_ribbon(self):
        sheets = 0
        ribbon = 0
        for box in self.boxes:
            sheets += box.sheets()
            ribbon += box.ribbon()
        return (sheets, ribbon)

boxes = Boxes("input.txt")
sheets_ribbon = boxes.total_sheets_ribbon()
print(f'Total Sheets: {sheets_ribbon[0]} Total Ribbon: {sheets_ribbon[1]}')
