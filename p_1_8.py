## PROBLEM 1.8

import numpy as np
import matplotlib.pyplot as plt

from least_squares import LeastSquaresEstimator # this is a python module I wrote for this class   
from least_squares import H_LTI # convenience class for working with linear time invariant H basis functions


def generate_synthetic_data(nsigfigs):

    # real x vals
    x1 = 1
    x2 = 1
    x3 = 1
    
    # measurements
    y = lambda t: x1 + x2*np.sin(10*t) + x3*np.exp(2*t**2)
    ts = np.arange(0,1.1,0.1).tolist()
    measurements = [y(t) for t in ts]
    
    # truncate measurements
    ndecimals = nsigfigs - 1
    truncated_measurements = [np.around(m,ndecimals) for m in measurements]

    return ts, truncated_measurements
    

def do_problem_1_8_for_nsigfigs(nsigfigs):
    
    # generate t's, measurements, and define H(t) 
    ts, measurements = generate_synthetic_data(nsigfigs)
    h1 = lambda t: 1
    h2 = lambda t: np.sin(10*t)
    h3 = lambda t: np.exp(2*t**2)
    H = H_LTI([h1, h2, h3]) # this is H(t)
    
    # initialize estimator    
    sequential_estimator = LeastSquaresEstimator()

    # run first batch
    first_batch_H = H(ts[0:3])
    first_batch_ys = measurements[0:3]
    sequential_estimator.initialize_from_data(first_batch_ys, first_batch_H)
    
    # run remaining sequential batches, each including 1 new measurement
    for i in range(3,len(ts)):
        t = ts[i]
        y = measurements[i]
        h = H(t)
        sequential_estimator.update(y, h)
        
    return ts, sequential_estimator
    

def do_problem_1_8():
    
    fig = plt.figure()
    fig.subplots_adjust(hspace=1)
    
    nsigfigs_list = [6,4,2,1]
    n = len(nsigfigs_list)
    
    axes = [fig.add_subplot(n,1,i) for i in range(1,n+1)]
    ylimrange = [1e-2, 1e-2, 1, 10]
    
    # do the same problem for the three different levels of sig figs, and plot the results of xhat with respect to the real values
    for i in range(n):
        
        ts, se = do_problem_1_8_for_nsigfigs(nsigfigs_list[i])
        ts = ts[2:]
        ax = axes[i]
        
        xhat = np.array(se.xhat_history)
        
        ax.plot(ts, xhat[:,0], 'red')
        ax.plot(ts, xhat[:,1], 'blue')
        ax.plot(ts, xhat[:,2], 'green')
    
        ax.plot(ts, np.ones_like(ts), 'black')
        
        ax.set_xlabel('time, sec')
        ax.set_ylabel('xhat estimates')
        
        title_str = 'nsigfigs: ' + str(nsigfigs_list[i])
        ax.set_title( title_str )
        ax.set_ylim(1-ylimrange[i], 1+ylimrange[i])
        
    plt.show()
    
if __name__ == '__main__':
    
    do_problem_1_8()
    
    '''
    RESULTS:
    
    see attached plots.
    
    '''
    
