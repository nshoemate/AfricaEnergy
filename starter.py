''First Try at picking python back up''

import numpy as np
import pandas as pd
import statsmodels as sm
from linearmodels import PanelOLS
from linearmodels import RandomEffects

df = pd.read_csv("C:\Users\shoem\Documents\GitHub\AfricaEnergy\GDP.csv")
df