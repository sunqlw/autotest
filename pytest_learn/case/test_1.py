import pytest


class Test123:

    def test_a(self):
        assert 1 == 1

    @pytest.mark.last
    def test_b(self):
        assert 2 == 1