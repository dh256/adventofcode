from RopeBridge import Rope

rope = Rope('input.txt',2)
rope.move()
print(rope.tail_visit_at_least_once)

rope = Rope('input.txt',10)
rope.move()
print(rope.tail_visit_at_least_once)