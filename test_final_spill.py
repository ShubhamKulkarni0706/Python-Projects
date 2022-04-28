import pandas as pd
#import numpy as np
from scipy.interpolate import interp1d


df = pd.read_excel("Test_Python.xlsx", usecols=["Alt Ref", "Storage", "Annual Average EA Spills"])
unq = list(df['Alt Ref'].unique())
csos_list = list(range(0, len(unq),1))

# What spills to look out for
spills = [0, 10, 20, 40]

#Make clean dataframe
def make_dataframe(df, unq, cso):
    df1 = []
    df1.append(df[df['Alt Ref'] == unq[cso]])
    Y = list(df1[0].loc[:, "Storage"].values)
    X = list(df1[0].loc[:, "Annual Average EA Spills"].values)
    return Y, X

# Get direct storage for corresponding values
def get_dstorage(Y, X, spills, spill_index):
    index_y = X.index(spills[spill_index])
    spill_storage = Y[index_y]
    return spill_storage

# Get interpolated storage for corresponding values
def get_istorage(Y, X, spill_val):
    
    #arry = np.asarray(X)
    if spill_val < max(X): #np.max(arry)
        y_interp = interp1d(X, Y)
        q = round(y_interp(spill_val), 3)
        return q
    else:
        return 0

#new_list = []


dict =  {'CSO_ref': unq, '0_spill_storage': [], '10_spill_storage': [], '20_spill_storage': [], '40_spill_storage': []}  


for i in csos_list:
    Y, X = make_dataframe(df, unq, i)
    dtemp = get_dstorage(Y, X, spills, 0)
    dict['0_spill_storage'].append(dtemp)
    itemp_ten = get_istorage(Y, X, 10)
    dict['10_spill_storage'].append(itemp_ten)
    itemp_twenty = get_istorage(Y, X, 20)
    dict['20_spill_storage'].append(itemp_twenty)
    itemp_forty = get_istorage(Y, X, 40)
    dict['40_spill_storage'].append(itemp_forty)


dfn = pd.DataFrame(dict)

dfn.to_csv("xxxcatchmentnamexxx_spill.csv")
