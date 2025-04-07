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

from IPython.display import display, IFrame

def show_def():
    src = "https://docs.google.com/presentation/d/e/2PACX-1vRKMMwGtrQOeLefj31fCtmbNOaJuKY32eBz1VwHi_5ui0AGYV3MoCjPUtQ_4SB1f9x4Iu6gbH0vFvmB/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960 
    height = 569
    display(IFrame(src, width, height))