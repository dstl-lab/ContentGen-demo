import numpy as np
import babypandas as bpd
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, HTML

def show_permutation_testing_intro():
    src="https://docs.google.com/presentation/d/e/2PACX-1vT3IfZAbqXtscEPu-nTl6lWZcXh6AWfjKsXZpWDNc0UhueXsOYQ7ivShlwbn-PW1EZm7CunTLtq7rmt/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 965
    height = 635
    display(IFrame(src, width, height))
    
def show_permutation_testing_summary():
    src = "https://docs.google.com/presentation/d/e/2PACX-1vSovXDonR6EmjrT45h4pY1mwmcKFMWVSdgpbKHC5HNTm9sbG7dojvvCDEQCjuk2dk1oA4gmwMogr8ZL/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960
    height = 569
    display(IFrame(src, width, height))