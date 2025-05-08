import numpy as np
import babypandas as bpd
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

def draw_cutoff(results):
    cutoff = np.percentile(results, 5)
    
    ax = bpd.DataFrame().assign(results=results).plot(kind='hist', bins=np.arange(160, 240, 4), 
                                             density=True, figsize=(10, 5),
                                             title='Empirical Distribution of the Number of Heads in 400 Flips of a Fair Coin')
    for bar in ax.containers[0]:
        x = bar.get_x() + 0.5 * bar.get_width()
        if x < cutoff:
            bar.set_color('#796fb3')
    plt.annotate('likely biased\ntowards tails', (160, 0.007), size=16, color='#796fb3', weight='bold')
    plt.annotate('likely fair', (225, 0.008), size=16, color='#e24a33', weight='bold');