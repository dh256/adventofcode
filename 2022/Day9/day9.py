from RopeBridge import Rope

rope = Rope('input.txt')
rope.move()
print(rope.tail_visit_at_least_once)