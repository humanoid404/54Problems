# multiply
import pandas as pd
import numpy as np
from IPython.display import display

mmdic={i:[i*j for j in range(13)] for i in range(13)}
m_dic={}
# for i in range(13)
#     m_dic[i]=mi
# m_dic[1]=m1
# m_dic[2]=m2
# m_dic[3]=m3
# m1=[1*x for x in range(0, 13)]
# m2=[2*x for x in range(0, 13)]
# m3=[3*x for x in range(0, 13)]

print(mmdic)
display(pd.DataFrame(mmdic).T)