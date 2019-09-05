#Takes a single cell as input and then returns None if REF is in the cell

import pandas as pd
import numpy as np


def cleanREF(cell):           # This takes the series as input and applies a conditional function to it using pd.Series.apply() through lambda x
    if 'REF' in cell:
        x = None
    else:
        x = cell
    return x

