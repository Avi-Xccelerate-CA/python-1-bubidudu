import pytest
from week0 import dose  # Ensure this points to the correct module

testdata = [
    ([250, 0, 250, 0, 0, 0], [(25, 0), (0, 0), (25, 0), (0, 0), (0, 0), (0, 0)]),
    ([40, 35, 23, 68, 45, 29], [(4, 0), (3, 5), (2, 3), (6, 8), (4, 5), (2, 9)]),
    ([223, 12, 126, 0, 37, 12], [(22, 3), (1, 2), (12, 6), (0, 0), (3, 7), (1, 2)]),
]

@pytest.mark.parametrize("case, expected", testdata)
def test_ex2(case, expected):
    assert dose(case) == expected
