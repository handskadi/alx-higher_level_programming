#!/usr/bin/python3
"""A matrix multiplicate module with help of NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multipy  of two matrices.

    Args:
        m_a (list of lists of ints/floats): First mtrx.
        m_b (list of lists of ints/floats): Second mtrx.
    """

    return (np.matmul(m_a, m_b))
