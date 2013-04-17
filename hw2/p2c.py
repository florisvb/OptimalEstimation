import numpy as np
import matplotlib.pyplot as plt
import fly_plot_lib.plot as fpl

def get_page_number(npages):
    return np.random.randint(0,npages)
    
def get_next_digit_in_sequence(prev, npages):
    page_number = get_page_number(npages)
    page_number_str = str(page_number)
    page_number_str = '0' + page_number_str
    penultimate_digit = int(page_number_str[-2])
    new_number = prev+penultimate_digit
    new_number_str = str(new_number)
    new_digit = int(new_number_str[-1])
    return new_digit
    
def get_digits(n, npages):
    
    digits = [0]
    for i in range(n):
        digit = get_next_digit_in_sequence(digits[-1], npages)
        digits.append(digit)
    
    return digits
    
def plot_digits_distribution(n):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bins = np.arange(-.5,10.5,1)
    
    npages = [30,60,400,1500]
    colors = ['black', 'blue', 'green', 'red']
    digits = []
    for npage in npages:
        d = get_digits(n, npage)
        digits.append(np.array(d))
        
    xticks = [0,1,2,3,4,5,6,7,8,9]
    
    fpl.histogram(ax, digits, bins=bins, colors=colors, normed=True, show_smoothed=False)
    
    fpl.adjust_spines(ax, ['left', 'bottom'], xticks=xticks)
    
    ax.set_ylim(0,0.15)
    ax.set_xlim(-1,10)
    ax.set_xlabel('digit')
    ax.set_ylabel('probability')
    
if __name__ == '__main__':

    n = 100000
    
    plot_digits_distribution(n)
