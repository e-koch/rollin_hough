
from rollinghough import rht

import numpy as np
from numpy.testing import assert_allclose

def test_rht():
    test1 = np.eye(20)
    test2 = np.zeros((20,20))
    test2[10, :] = 1

    assert_allclose(rht(test1, 10)[2], (0.57268658477567103, 0.78609389334676461, 0.99950120191785796))
    assert_allclose(rht(test1[::-1], 10)[2], (-0.99481641542614818, -0.78301561713294787, -0.57121481883974756))

    assert_allclose(rht(test2, 10)[2], (1.4345916941974353, 1.5707963267948966, 1.7070009593923579))
    assert_allclose(rht(test2.T, 10)[2], (-0.13824075299774963, -1.2236762866959916e-16, 0.13824075299774935))
