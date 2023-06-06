# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test_example():
    marker_args = test_example.pytestmark[0].args
    print('\n>>>', *marker_args)


test_example()
