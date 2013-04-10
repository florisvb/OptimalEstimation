## PROBLEM 1.10

import numpy as np
import scipy.stats
from least_squares import LeastSquaresEstimator
from least_squares import H_LTI

def do_p_1_10():
    
    a = 1
    b = 1
    
    # zero mean gaussian noise with std .01 
    gaussian_noise = scipy.stats.norm(0,.01)
    
    # generate measurements
    nmeasurements = 101
    interval = 0.1
    finalval = nmeasurements*interval
    ts = np.linspace(0, finalval, nmeasurements)
    y = lambda t: a*np.sin(t) - b*np.cos(t) + gaussian_noise.rvs()
    measurements = y(ts)
    
    # define basis functions
    h1 = lambda t: np.sin(t)
    h2 = lambda t: np.cos(t)
    H = H_LTI([h1, h2])
    
    # instantiate least squares estimator, and run fit routine with no weights
    least_squares_estimator = LeastSquaresEstimator()
    xhat = least_squares_estimator.fit(measurements, H(ts))
    print 'unweighted -- xhat = ', xhat[0], xhat[1]
    
    # find y closest to zero, set to 1:
    i = np.argmin(np.abs(measurements))
    measurements_adj = measurements
    measurements_adj[i] = 1
    
    # unweighted least squares fit
    xhat = least_squares_estimator.fit(measurements_adj, H(ts))
    print 'unweighted, with adjustment -- xhat = ', xhat[0], xhat[1]
    
    # weighted least squares fit
    W = np.ones_like(ts).tolist() # default weight = 1
    W[i] = 0 # deweight bad measurement
    xhat = least_squares_estimator.fit(measurements_adj, H(ts), W=W)
    print 'weighted, with adjustment -- xhat = ', xhat[0], xhat[1]
    
    
if __name__ == '__main__':
    
    do_p_1_10()
    
    ''' 
    
    RESULTS from running this code:
    
    unweighted case -- xhat =  [[ 0.99823585]] [[-0.99938069]]
    unweighted case, with adjustment to measurement -- xhat =  [[ 1.01251665]] [[-0.98665676]]
    weighted case, with adjustment to measurement -- xhat =  [[ 0.99829367]] [[-0.99932917]]

    Thus, the "deweighting" brings the solution (almost) back to the original solution, as is expected.

    '''

