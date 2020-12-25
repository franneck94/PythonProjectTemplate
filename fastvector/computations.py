'''Implementation of vector computations.
'''
# pylint: disable=import-error
from .cython_computations import _cython_clip_vector
from .cython_computations import _naive_cython_clip_vector
from .dtypes import Number
from .vector import VectorND


def python_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND) -> None:
    '''Clip the vector values.

    Args:
        vector_in (VectorND): Input vector.
        min_value (Number): Min value.
        max_value (Number): Max value.
        vector_out (VectorND): Output vector.

    Raises:
        ValueError: If min_value is less than max_value.
    '''
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    if min_value >= max_value:
        raise ValueError('min_value must be less than max_value')
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


def naive_cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND) -> None:
    '''Clip the vector values.

    Args:
        vector_in (VectorND): Input vector.
        min_value (Number): Min value.
        max_value (Number): Max value.
        vector_out (VectorND): Output vector.

    Raises:
        ValueError: If min_value is less than max_value.
    '''
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    if min_value >= max_value:
        raise ValueError('min_value must be less than max_value')
    _naive_cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)


def cython_clip_vector(vector_in: VectorND, min_value: Number, max_value: Number, vector_out: VectorND) -> None:
    '''Clip the vector values.

    Args:
        vector_in (VectorND): Input vector.
        min_value (Number): Min value.
        max_value (Number): Max value.
        vector_out (VectorND): Output vector.

    Raises:
        ValueError: If min_value is less than max_value.
    '''
    VectorND.check_vector_types(vector_in)
    VectorND.check_vector_types(vector_out)
    if min_value >= max_value:
        raise ValueError('min_value must be less than max_value')
    _cython_clip_vector(vector_in.values, min_value, max_value, vector_out.values)
