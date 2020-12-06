from CustomForm import Groups

groups = Groups("input.txt")
answers = groups.total_number_of_questions_answered_by_anyone()
print(answers)

answers = groups.total_number_of_questions_answered_by_everyone()
print(answers)