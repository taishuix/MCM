import pandas as pd
import numpy as np
import math

data1 = pd.read_excel("start-end.xlsx", engine='openpyxl')
df1 = pd.DataFrame(data1)

print(df1)

df2 = pd.read_excel("Data1.xlsx", engine='openpyxl')
data2 = np.array(df2)
data_list = data2.tolist()

fre = [['date', 'contest number', 'word', 'start_fre', 'start_scr', 'end_fre', 'end_scr', 'total_fre', 'total_scr', 'H_total', '_scr', '1st', '2nd', '3rd', '4th', '5th']]

print(data_list)

start_fre = df1.get('start_frequency')
start_scr = df1.get('start_score')
end_fre = df1.get('end_frequency')
end_scr = df1.get('end_score')
total_fre = df1.get('total_frequency')
total_scr = df1.get('total_score')


# ASCII: A-65, a-97

for i in np.arange(360):
    ss = start_scr[ord(data_list[i][2][0])-97]
    sf = start_fre[ord(data_list[i][2][0])-97]
    es = end_scr[ord(data_list[i][2][4])-97]
    ef = end_fre[ord(data_list[i][2][4])-97]
    tf1 = total_fre[ord(data_list[i][2][1])-97]
    tf2 = total_fre[ord(data_list[i][2][2]) - 97]
    tf3 = total_fre[ord(data_list[i][2][3]) - 97]
    ts1 = total_scr[ord(data_list[i][2][1]) - 97]
    ts2 = total_scr[ord(data_list[i][2][2]) - 97]
    ts3 = total_scr[ord(data_list[i][2][3]) - 97]

    fre.append([data_list[i][0], data_list[i][1], data_list[i][2], sf, ss, ef, es,
                 sf*ef*tf1*tf2*tf3, ss*es*ts1*ts2*ts3,
                 sf*math.log2(sf)+ef*math.log2(ef)+tf1*math.log2(tf1)+tf2*math.log2(tf2)+tf3*math.log2(tf3),
                1 / sf + 1 / ef +1 / tf1 + 1 / tf2 + 1 / tf3, data_list[i][2][0], data_list[i][2][1], data_list[i][2][2],
                data_list[i][2][3], data_list[i][2][4]])


dt = pd.DataFrame(fre)
dt.to_excel("A-Z.xlsx", index=False)
dt.to_csv("A-Z.csv", index=False)





