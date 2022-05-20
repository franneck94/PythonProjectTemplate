from typing import Any

from fastvector.dtypes import Number
from fastvector.vector import VectorND

import pytest


V1 = VectorND(0, 0)
V2 = VectorND(-1, 1)
V3 = VectorND(2.5, -2.5)


####################
###     INIT     ###
####################

def test_init_raises() -> None:
    with pytest.raises(TypeError):
        _ = VectorND()


@pytest.mark.parametrize(
    ('x', 'y', 'exp'),
    (
        (-1, 1, VectorND(-1, 1)),
        (1, -1, VectorND(1, -1)),
        (1, 1, VectorND(1, 1)),
    )
)
def test_from_values(x: Number, y: Number, exp: VectorND) -> None:
    assert exp == VectorND(x, y)


####################
###   STRINGS    ###
####################

def test_repr(capture_stdout: dict) -> None:
    print(repr(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.VectorND(array('d', [1.0, 2.0]))\n"


def test_str(capture_stdout: dict) -> None:
    print(str(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "(array('d', [1.0, 2.0]))\n"


####################
###  CONTAINER   ###
####################

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
def test_get_item(v: VectorND, idx: int, exp: Number) -> None:
    assert v[idx] == exp


@pytest.mark.parametrize(
    ('v', 'idx', 'exp'),
    (
        (VectorND(1, 2, 3), 0, 1),
        (VectorND(1, 2, 3), 1, 2),
        (VectorND(1, 2, 3), 2, 3),
    )
)
def test_set_item(v: VectorND, idx: int, exp: Number) -> None:
    v[idx] = exp
    assert v[idx] == exp


####################
### COMPUTATIONS ###
####################

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


@pytest.mark.parametrize(
    ('rhs', 'lhs'),
    (
        (VectorND(1, 1), None),
        (VectorND(1, 1), "1"),
    )
)
def test_mul_raises(rhs: VectorND, lhs: Any) -> None:
    with pytest.raises(TypeError):
        rhs * lhs


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, 2.0, VectorND(0.0, 0.0)),
        (V2, 2.0, VectorND(-0.5, 0.5)),
        (V3, 2.0, VectorND(1.25, -1.25)),
    )
)
def test_div(lhs: VectorND, rhs: float, exp_res: VectorND) -> None:
    assert lhs / rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs'),
    (
        (VectorND(0.0, 0.0), VectorND(0.0, 0.0)),
    )
)
def test_div_raises(lhs: VectorND, rhs: float) -> None:
    with pytest.raises(TypeError):
        lhs / rhs


@pytest.mark.parametrize(
    ('rhs', 'lhs'),
    (
        (VectorND(1, 1), (0, 1)),
        (VectorND(1, 1), [1, 0]),
    )
)
def test_operators_raises(rhs: VectorND, lhs: VectorND) -> None:
    with pytest.raises(TypeError):
        rhs < lhs
    with pytest.raises(TypeError):
        rhs + lhs
    with pytest.raises(TypeError):
        rhs - lhs


@pytest.mark.parametrize(
    ('rhs', 'lhs'),
    (
        (VectorND(0, 0), 0),
        (VectorND(0, 1), 1),
        (VectorND(1, 0), 1),
    )
)
def test_abs(rhs: VectorND, lhs: Number) -> None:
    assert abs(rhs) == lhs


####################
### COMPARISONS  ###
####################

@pytest.mark.parametrize(
    ('lhs', 'rhs'),
    (
        (VectorND(1, 1), (1, 1)),
        (VectorND(1, 1), [1, 1]),
    )
)
def test_equality_other_class(lhs: VectorND, rhs: object) -> None:
    assert not (lhs == rhs)


@pytest.mark.parametrize(
    ('lhs', 'rhs'),
    (
        (VectorND(1, 1), VectorND(0, 1)),
        (VectorND(1, 1), VectorND(1, 0)),
    )
)
def test_less_than(lhs: VectorND, rhs: VectorND) -> None:
    assert rhs < lhs
