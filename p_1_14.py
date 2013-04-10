## PROBLEM 1.14

import numpy as np
import scipy.stats
from least_squares import LeastSquaresEstimator

def generate_synthetic_data(x, u, noise_mean, noise_std_dev):
    '''
    n = 2
    p = 2
    '''
    
    nmeasurements = len(u)
    ks = np.arange(0, nmeasurements)
    
    # initialize y and H
    y = [0, 0]
    H = []
    
    # make x a matrix
    x = np.matrix(x).T
    
    # zero mean gaussian noise
    noise = scipy.stats.norm(noise_mean, noise_std_dev)
    
    # iterate to calculate and save yk, Hk
    for i, k in enumerate(ks):
        if i < 2:
            continue
            
        hk = [y[i-1], y[i-2], u[i-1], u[i-2]]
        hk = np.matrix(hk)
        
        H.append(hk)
        
        yk = hk*x + noise.rvs()
        
        y.append(yk[0,0])
    
    # ignore first two data points, since we have no H for them
    y = y[2:]
    u = u[2:]
    
    # return yk's and Hk's 
    return y, H
    
    
def sequential_estimation_with_data(y, H):
    # initialize estimator
    least_squares_estimator = LeastSquaresEstimator()
    
    # set initial values, and large covariance    
    xhat0 = [0,0,0,0]
    P0 = np.matrix(np.eye(4))*1000
    least_squares_estimator.initialize_with_guess(xhat0, P0)
    
    # for each of our measurements, run the kalman update
    for i in range(len(y)):
        least_squares_estimator.update(y[i], H[i])
        
    # return the final xhat value
    return least_squares_estimator.xhat
    

def do_p_1_14(model):
    '''
    This function does the defined problem for two different models, described below.
    '''

    ## MODEL 1
    if model == 1:
        # generate synthetic data
        real_x = [-0.9,0.1,-0.3,-0.1]
        ks = np.arange(0,1000)
        u = np.sin(ks) # sinusoidal control
        noise_mean = 0
        noise_std_dev = 1
        y, H = generate_synthetic_data(real_x, u, noise_mean, noise_std_dev)

        # run sequential estimation algorithm
        xhat = sequential_estimation_with_data(y, H)
        print xhat.T
        
    ## MODEL 2: same as model 1 with step input control, instead of sinusoidal
    if model == 2:
        # generate synthetic data
        real_x = [-0.9,0.1,-0.3,-0.1]
        ks = np.arange(0,1000)
        u = np.ones_like(ks) # u=1, then u=2 after k=300
        u[300:] = 2
        noise_mean = 0
        noise_std_dev = 1
        y, H = generate_synthetic_data(real_x, u, noise_mean, noise_std_dev)

        # run sequential estimation algorithm
        xhat = sequential_estimation_with_data(y, H)
        print xhat.T
    

    
        
    
        
if __name__ == '__main__':

    '''
    Description of code: the function d_p_1_14() runs the sequential ("realtime") least squares estimation routine on different models. 
    
    To draw a somewhat meaningful (interesting) conclusion from this problem, I used two different control inputs on the same model. Model 1 uses a sinusoidal input, whereas Model 2 uses a step input, but is otherwise identical.
    
    In both cases I used a real x of [-0.9,0.1,-0.3,-0.1], and 1000 measurement points (used sequentially). 
    
    It would be trivial, but kind of pointless, to run this code on other models, so I stuck with just these two.
    
    '''

    
    do_p_1_14(model=1)
    '''
    RESULTS:
    
    xhat = [-0.88422968  0.11672174 -0.30291225 -0.07017602]
    
    Works reasonably well. Recall: this model used a sinusoidal input for the controls.
    '''
    
    do_p_1_14(model=2)
    '''
    RESULTS:
    
    xhat = [-0.9185425   0.08111079 -1.70966561  1.3151672 ]
    
    Works ok for the first two parameters, however, the second two are very wrong. This is likely due to the fact that I used a step input control here, rather than a sinusoidal input. This means there is less diversity in the measurements, in other words, the measurements, and thus the H matrix, is more linearly dependent than in model 1.
    
    '''
    
    
    
