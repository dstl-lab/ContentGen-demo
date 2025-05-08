import numpy as np
import babypandas as bpd
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

import warnings
warnings.filterwarnings('ignore')

# New minimize function (wrapper around scipy.optimize.minimize)
from inspect import signature
from scipy import optimize

def minimize(function):
    n_args = len(signature(function).parameters)
    initial = np.zeros(n_args)
    return optimize.minimize(lambda x: function(*x), initial).x

# +
def standard_units(col):
    return (col - col.mean()) / np.std(col)

def calculate_r(df, x, y):
    '''Returns the average value of the product of x and y, 
       when both are measured in standard units.'''
    x_su = standard_units(df.get(x))
    y_su = standard_units(df.get(y))
    return (x_su * y_su).mean()

def slope(df, x, y):
    "Returns the slope of the regression line between columns x and y in df (in original units)."
    r = calculate_r(df, x, y)
    return r * np.std(df.get(y)) / np.std(df.get(x))

def intercept(df, x, y):
    "Returns the intercept of the regression line between columns x and y in df (in original units)."
    return df.get(y).mean() - slope(df, x, y) * df.get(x).mean()


# -

# All of the following code is for visualization.
def plot_regression_line(df, x, y, margin=.02):
    '''Computes the slope and intercept of the regression line between columns x and y in df (in original units) and plots it.'''
    m = slope(df, x, y)
    b = intercept(df, x, y)
    
    df.plot(kind='scatter', x=x, y=y, s=100, figsize=(10, 5), label='original data')
    left = df.get(x).min()*(1 - margin)
    right = df.get(x).max()*(1 + margin)
    domain = np.linspace(left, right, 10)
    plt.plot(domain, m*domain + b, color='orange', label='regression line', lw=4)
    plt.suptitle(format_equation(m, b), fontsize=18)
    plt.legend();

def format_equation(m, b):
    if b > 0:
        return r'$y = %.2fx + %.2f$' % (m, b)
    elif b == 0:
        return r'$y = %.2fx' % m
    else:
        return r'$y = %.2fx %.2f$' % (m, b)

def plot_errors(df, m, b, ax=None):
    x = df.get('x')
    y = m * x + b
    df.plot(kind='scatter', x='x', y='y', s=100, label='original data', ax=ax, figsize=(10, 5) if ax is None else None)
    
    if ax:
        plotter = ax
    else:
        plotter = plt
    
    plotter.plot(x, y, color='orange', lw=4)
    
    for k in np.arange(df.shape[0]):
        xk = df.get('x').iloc[k]
        yk = np.asarray(y)[k]
        if k == df.shape[0] - 1:
            plotter.plot([xk, xk], [yk, df.get('y').iloc[k]], linestyle=(0, (1, 1)), c='r', lw=4, label='errors')
        else:
            plotter.plot([xk, xk], [yk, df.get('y').iloc[k]], linestyle=(0, (1, 1)), c='r', lw=4)
    
    plt.title(format_equation(m, b), fontsize=18)
    plt.xlim(50, 90)
    plt.ylim(40, 100)
    plt.legend();
