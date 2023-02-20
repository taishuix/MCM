from wordfreq import zipf_frequency
import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np

df = pd.read_excel("Data1.xlsx", engine='openpyxl')

data = np.array(df)
data_list = data.tolist()
fre = []



for i in np.arange(359):
     fre.append(zipf_frequency(data_list[i][2], 'en', wordlist='large'))

dt = pd.DataFrame(fre)
dt.to_excel("result_xlsx.xlsx", index=False)
dt.to_csv("result_csv.csv", index=False)


fre.append(zipf_frequency("eerie", 'en', wordlist='large'))
print(fre)