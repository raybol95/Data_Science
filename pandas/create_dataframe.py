import pandas as pd
import numpy as np
'''
class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

Parameters

data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order.

Changed in version 0.25.0: If data is a list of dicts, column order follows insertion-order.

index : Index or array-like
Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.

columns : Index or array-like
Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, …, n) if no column labels are provided.

dtype : dtype, default None
Data type to force. Only a single dtype is allowed. If None, infer.

copy : bool, default False
Copy data from inputs. Only affects DataFrame / 2d ndarray input.
'''

# From Dictionary
data = {'fruit':['banana', 'apple', 'grape', 'orange', 'durian', 'pineapple'], 'value':[10, 5, 40, 12, 2, 4]} # make a dictionary data with columns and rows
df = pd.DataFrame(data) # convert dictionary data to dataframe with pandas
df.head() # show the first 5 rows dataframe

# From ndarray
data_array = pd.DataFrame(np.array([['banana', 'apple', 'grape', 'orange', 'durian', 'pineapple'], [10, 5, 40, 12, 2, 4]]), columns=['fruit', 'value']) # make dataframe from ndarray
data_array.head() # show first 5 rows dataframe
