class Group:
    def __init__(self):
        # Group consists of dictionary of key:value pairs
        # each key:value represents a letter from a to z and number of times question answered
        self.answers = {}
        self.members = 0
        for a in range(97,123):
            self.answers[chr(a)] = 0

    def add(self,answers):
        # adds a set of answers to a group
        # go through each letter in answers set and increment answers count by 1
        self.members += 1
        for l in answers:
            self.answers[l] += 1

class Groups:
    def __init__(self,file_name):
        with open(file_name,"r") as input_file:
            self.groups = []
            group = Group()
            for line in input_file:
                line = line.strip('\n')
                if len(line) == 0:
                    # new group found
                    self.groups.append(group)
                    group = Group()
                else:
                    group.add(line)

            # always append last group
            self.groups.append(group)
    
    def total_number_of_questions_answered_by_anyone(self):
        total = 0
        for group in self.groups:
            total += len(list(filter(lambda v : v > 0, group.answers.values())))
        return total

    def total_number_of_questions_answered_by_everyone(self):
        total = 0
        for group in self.groups:
            total += len(list(filter(lambda v : v == group.members, group.answers.values())))
        return total 