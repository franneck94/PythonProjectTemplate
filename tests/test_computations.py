from fastvector.computations import cython_clip_vector
from fastvector.computations import naive_cython_clip_vector
from fastvector.computations import python_clip_vector
from fastvector.dtypes import Number
from fastvector.vector import VectorND

import pytest


@pytest.mark.parametrize(
    ('lhs', 'min_', 'max_', 'out', 'exp_res'),
    (
        (VectorND(-2, 0, 2), -1, 1, VectorND(0, 0, 0), VectorND(-1, 0, 1)),
    )
)
def test_python_clip(lhs: VectorND, min_: Number, max_: Number, out: VectorND, exp_res: VectorND) -> None:
    python_clip_vector(lhs, min_, max_, out)
    assert out == exp_res


@pytest.mark.parametrize(
    ('lhs', 'min_', 'max_', 'out', 'exp_res'),
    (
        (VectorND(-2, 0, 2), -1, 1, VectorND(0, 0, 0), VectorND(-1, 0, 1)),
    )
)
def test_cython_clip(lhs: VectorND, min_: Number, max_: Number, out: VectorND, exp_res: VectorND) -> None:
    cython_clip_vector(lhs, min_, max_, out)
    assert out == exp_res


@pytest.mark.parametrize(
    ('lhs', 'min_', 'max_', 'out', 'exp_res'),
    (
        (VectorND(-2, 0, 2), -1, 1, VectorND(0, 0, 0), VectorND(-1, 0, 1)),
    )
)
def test_naive_cython_clip(lhs: VectorND, min_: Number, max_: Number, out: VectorND, exp_res: VectorND) -> None:
    naive_cython_clip_vector(lhs, min_, max_, out)
    assert out == exp_res
