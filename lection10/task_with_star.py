# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    marker = pytest.mark.id_check
    args = marker.args
    print(*args)
    # Здесь пишем остальной код тестовой функции
    pass
