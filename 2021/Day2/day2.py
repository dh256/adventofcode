from submarine import Submarine

sub = Submarine('input.txt')
sub.follow_course()
print(f'Part 1: {sub.v_pos * sub.h_pos}')
sub.follow_course2()
print(f'Part 2: {sub.v_pos * sub.h_pos}')
