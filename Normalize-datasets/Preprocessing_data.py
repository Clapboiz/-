#Import Lib
import pandas as pd
import numpy as np

print("----------------------------CVE Info------------------------------------")

dataset_info_pre = pd.read_csv('D://Users//Desktop//Reinforcement-Learning-for-Automating-Pentest//Data//CVE_Info.csv', delimiter = ',')
print("Rows:",dataset_info_pre.shape[0],"Columns:",dataset_info_pre.shape[1])

print("----------------------------------------------------------------")

print(dataset_info_pre)

print("----------------------------Web Vulnerability------------------------------------")

dataset_vul_pre = pd.read_csv('D://Users//Desktop//Reinforcement-Learning-for-Automating-Pentest//Data//Web_Vulnerability.csv', delimiter = ',')
print("Rows:",dataset_vul_pre.shape[0],"Columns:",dataset_vul_pre.shape[1])

print("----------------------------------------------------------------")

print(dataset_vul_pre)
