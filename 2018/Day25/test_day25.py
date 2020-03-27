from Day25_classes import Sky

class TestConstellations():
    def test1(self):
        sky = Sky('test_input_1.txt')
        assert(sky.constellations() == 2)

    def test2(self):
        sky = Sky('test_input_2.txt')
        assert(sky.constellations() == 3)

    def test3(self):
        sky = Sky('test_input_3.txt')
        assert(sky.constellations() == 8)

