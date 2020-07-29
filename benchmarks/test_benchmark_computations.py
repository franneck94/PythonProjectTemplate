import random

import numpy as np

import fastvector

v = fastvector.VectorND([random.random() for _ in range(100_000)])
a = np.array([random.random() for _ in range(100_000)])

NUM_ROUNDS = 10
NUM_ITERATIONS = 50

def test_python_clip_vector(benchmark):
    benchmark.pedantic(fastvector.python_clip_vector, args=(v, -1, 1, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_naive_cython_clip_vector(benchmark):
    benchmark.pedantic(fastvector.naive_cython_clip_vector, args=(v, -1, 1, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector, args=(v, -1, 1, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_np_clip(benchmark):
    benchmark.pedantic(np.clip, args=(a, -1, 1, a), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)
