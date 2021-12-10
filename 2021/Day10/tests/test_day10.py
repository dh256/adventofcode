import pytest
from nav import Nav

test_data = [('tests/test1.txt',26397,288957)]

@pytest.mark.parametrize('filename,part1_score,part2_score',test_data)
def test_calc_scores(filename,part1_score,part2_score):
    nav = Nav(filename)
    scores = nav.calc_scores()
    assert(scores[0] == part1_score)
    assert(scores[1] == part2_score)
