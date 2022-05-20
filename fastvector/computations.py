# pylint: disable=import-error
from .cython_computations import _cython_clip_vector
from .cython_computations import _naive_cython_clip_vector
from .dtypes import Number
from .vector import VectorND


def python_clip_vector(
    vector_in: VectorND,
    min_value: Number,
    max_value: Number,
    vector_out: VectorND,
) -> None:
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


def naive_cython_clip_vector(
    vector_in: VectorND,
    min_value: Number,
    max_value: Number,
    vector_out: VectorND,
) -> None:
    _naive_cython_clip_vector(
        vector_in.values, min_value, max_value, vector_out.values
    )


def cython_clip_vector(
    vector_in: VectorND,
    min_value: Number,
    max_value: Number,
    vector_out: VectorND,
) -> None:
    _cython_clip_vector(
        vector_in.values, min_value, max_value, vector_out.values
    )
