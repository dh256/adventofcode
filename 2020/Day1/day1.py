from ExpenseReport import ExpenseReport

report = ExpenseReport("input.txt")
part1_result = report.find_entries_sum_to(2020,2)
print(part1_result)

part2_result = report.find_entries_sum_to(2020,3)
print(part2_result)