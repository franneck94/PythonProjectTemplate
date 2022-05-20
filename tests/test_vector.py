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


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, VectorND(1, -1)),
        (V1, V3, VectorND(-2.5, 2.5)),
        (V3, V2, VectorND(3.5, -3.5)),
    )
)
def test_sub(lhs: VectorND, rhs: VectorND, exp_res: VectorND) -> None:
    assert lhs - rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(lhs: VectorND, rhs: VectorND, exp_res: float) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, 2.0, VectorND(0.0, 0.0)),
        (V2, 2.0, VectorND(-2.0, 2.0)),
        (V3, 2.0, VectorND(5.0, -5.0)),
    )
)
def test_mul_float(lhs: VectorND, rhs: float, exp_res: VectorND) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.skip(reason="Not implemented")
def test_abs() -> None:
    pass


@pytest.mark.parametrize(
    ('x', 'y'),
    (
        (-1, None),
        (None, -1),
        (None, None),
    )
)
def test_raises(x: Any, y: Any) -> None:
    with pytest.raises(TypeError):
        _ = VectorND(x, y)


def test_repr(capture_stdout: dict) -> None:
    print(repr(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.VectorND(array('d', [1.0, 2.0]))\n"


def test_str(capture_stdout: dict) -> None:
    print(str(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "(array('d', [1.0, 2.0]))\n"


@pytest.mark.parametrize(
    ('v'),
    (
        VectorND(1, 1, 1),
    )
)
def test_len(v: VectorND) -> None:
    assert len(v) == 3
    assert len(v) == len(v.values)


@pytest.mark.parametrize(
    ('v', 'idx', 'exp'),
    (
        (VectorND(1, 2, 3), 0, 1),
        (VectorND(1, 2, 3), 1, 2),
        (VectorND(1, 2, 3), 2, 3),
    )
)
def test_get_item(v: VectorND, idx: int, exp: SupportsFloat) -> None:
    assert v[idx] == exp


@pytest.mark.parametrize(
    ('v', 'idx', 'exp'),
    (
        (VectorND(1, 2, 3), 0, 1),
        (VectorND(1, 2, 3), 1, 2),
        (VectorND(1, 2, 3), 2, 3),
    )
)
def test_set_item(v: VectorND, idx: int, exp: SupportsFloat) -> None:
    v[idx] = exp
    assert v[idx] == exp


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (VectorND(1, 1, dtype=uint32), VectorND(2, 2, dtype=uint32), VectorND(3, 3, dtype=uint32)),
        (VectorND(1, 1, dtype=int32), VectorND(-1, -2, dtype=int32), VectorND(0, -1, dtype=int32)),
    )
)
def test_add_dtypes(lhs: VectorND, rhs: VectorND, exp_res: VectorND) -> None:
    assert lhs + rhs == exp_res
