import numpy as np

#testing fenna
import pandas as pd
data = pd.io.stata.read_stata("C:Users\fenna\Downloads\cs13f_2.0p_EN\cs13f_2.0p_EN.dta")
data.to_csv('my_stata_file.csv')

#testing comments
#another test to show