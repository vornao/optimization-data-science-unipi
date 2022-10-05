# simple script for generating fancy matrix Q.
import numpy as np
from random import uniform

"""
Generate matriz with given max and min eigenvalues. Uses QR decompositions, quite inefficient
"""
def generate_matrix(n, lambda_max, lambda_min):
    A = np.random.rand(n,n)        # matrix of random numbers
    Q, R = np.linalg.qr(A)         # QR decomposition for getting Q hortogonal and quite random

    ecc = (lambda_max - lambda_min) / (lambda_max + lambda_min)
    eigs=[]

    for i in range(0, n-2):
        eigs.append(uniform(lambda_min, round(lambda_max)))
    
    eigs.append(lambda_max)
    eigs.append(lambda_min)

    L = np.diag(eigs)              # matrix containing eigenvalues

    Q = Q @ L @ np.transpose(Q)


    x = 2 * np.abs(1) * np.random.rand(n, 1) - np.abs(1)
    q = np.dot(-1*Q, x);

    return Q, q, eigs, ecc