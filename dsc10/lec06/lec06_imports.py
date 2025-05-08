import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, YouTubeVideo

def show_grouping_animation():
    src = "https://docs.google.com/presentation/d/e/2PACX-1vTgVlFngQcLMYHP-z1vq5lVXjsBgcHebc-3TX7SW6L_gjX6TD1gsflvVDQUpWiDdeEPqJASenUIfBVd/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960
    height = 509
    display(IFrame(src, width, height))