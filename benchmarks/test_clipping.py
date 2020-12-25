import random
from typing import Any

import numpy as np  # pylint: disable=import-error

import fastvector


v = fastvector.VectorND([random.random() for _ in range(100_000)])
a = np.array([random.random() for _ in range(100_000)])

NUM_ROUNDS = 100
NUM_ITERATIONS = 10


def test_python_clip_vector(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.python_clip_vector,
        args=(v, -1, 1, v),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_naive_cython_clip_vector(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.naive_cython_clip_vector,
        args=(v, -1, 1, v),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_cython_clip_vector(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.cython_clip_vector,
        args=(v, -1, 1, v),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_np_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        np.clip,
        args=(a, -1, 1, a),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )
