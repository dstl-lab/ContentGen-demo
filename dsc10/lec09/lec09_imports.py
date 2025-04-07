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

def merging_animation():
    src="https://docs.google.com/presentation/d/e/2PACX-1vQ8NBJswhPdgN73JKS6a7uK9S5MH0y_qhnhMv1wSusMJXwBcI1CTj2T20zJ5vVH45lVPt06gH1oTr7H/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


def concept_check():
    src="https://docs.google.com/presentation/d/e/2PACX-1vQht9TpbcjvveNSN5B1N9m97MDIzP2C0R7XrLn_HLwDkhd-bF8P4Evi3jjpI0jajSEGfDAAUMLQqNsC/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


