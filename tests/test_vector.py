from typing import Any
from typing import SupportsFloat

from fastvector.vector import Vector2D

import pytest


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)


####################
###     INIT     ###
####################


@pytest.mark.parametrize(
    ("x", "y"),
    (
        (-1, None),
        (1, None),
        (None, 1),
        (None, -1),
    ),
)
def test_init_raises(x: SupportsFloat, y: SupportsFloat) -> None:
    with pytest.raises(TypeError):
        _ = Vector2D(x, y)


@pytest.mark.parametrize(
    ("x", "y", "exp"),
    (
        (-1, 1, Vector2D(-1, 1)),
        (1, -1, Vector2D(1, -1)),
        (1, 1, Vector2D(1, 1)),
    ),
)
def test_from_values(x: SupportsFloat, y: SupportsFloat, exp: Vector2D) -> None:
    assert exp == Vector2D(x, y)


####################
###   STRINGS    ###
####################


def test_repr(capture_stdout: dict) -> None:
    print(repr(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.Vector2D(1.0, 2.0)\n"


def test_str(capture_stdout: dict) -> None:
    print(str(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "(1.0, 2.0)\n"


####################
### COMPUTATIONS ###
####################


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
    ),
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(1, -1)),
        (V1, V3, Vector2D(-2.5, 2.5)),
        (V3, V2, Vector2D(3.5, -3.5)),
    ),
)
def test_sub(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs - rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    ),
)
def test_mul_vec(lhs: Vector2D, rhs: Vector2D, exp_res: float) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-2.0, 2.0)),
        (V3, 2.0, Vector2D(5.0, -5.0)),
    ),
)
def test_mul_float(lhs: Vector2D, rhs: float, exp_res: Vector2D) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(1, 1), None),
        (Vector2D(1, 1), "1"),
    ),
)
def test_mul_raises(rhs: Vector2D, lhs: Any) -> None:
    with pytest.raises(TypeError):
        rhs * lhs


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-0.5, 0.5)),
        (V3, 2.0, Vector2D(1.25, -1.25)),
    ),
)
def test_div(lhs: Vector2D, rhs: float, exp_res: Vector2D) -> None:
    assert lhs / rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs"), ((Vector2D(0.0, 0.0), Vector2D(0.0, 0.0)),)
)
def test_div_raises(lhs: Vector2D, rhs: float) -> None:
    with pytest.raises(TypeError):
        lhs / rhs


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(1, 1), (0, 1)),
        (Vector2D(1, 1), [1, 0]),
    ),
)
def test_operators_raises(rhs: Vector2D, lhs: Vector2D) -> None:
    with pytest.raises(TypeError):
        rhs < lhs
    with pytest.raises(TypeError):
        rhs + lhs
    with pytest.raises(TypeError):
        rhs - lhs


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(0, 0), 0),
        (Vector2D(0, 1), 1),
        (Vector2D(1, 0), 1),
    ),
)
def test_abs(rhs: Vector2D, lhs: SupportsFloat) -> None:
    assert abs(rhs) == lhs


####################
### COMPARISONS  ###
####################


@pytest.mark.parametrize(
    ("lhs", "rhs"),
    (
        (Vector2D(1, 1), (1, 1)),
        (Vector2D(1, 1), [1, 1]),
    ),
)
def test_equality_other_class(lhs: Vector2D, rhs: object) -> None:
    assert not (lhs == rhs)


@pytest.mark.parametrize(
    ("lhs", "rhs"),
    (
        (Vector2D(1, 1), Vector2D(0, 1)),
        (Vector2D(1, 1), Vector2D(1, 0)),
    ),
)
def test_less_than(lhs: Vector2D, rhs: Vector2D) -> None:
    assert rhs < lhs
