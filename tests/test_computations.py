from typing import Any
from typing import SupportsFloat

from fastvector import VectorND
from fastvector import int32
from fastvector import uint32

import pytest


V1 = VectorND(0, 0)
V2 = VectorND(-1, 1)
V3 = VectorND(2.5, -2.5)


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, VectorND(-1, 1)),
        (V1, V3, VectorND(2.5, -2.5)),
        (V3, V2, VectorND(1.5, -1.5)),
    )
)
def test_add(lhs: VectorND, rhs: VectorND, exp_res: VectorND) -> None:
    assert lhs + rhs == exp_res
