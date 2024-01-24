import pandas as pd
import pickle

# Colocar el XSLX de Base Socios en el directorio
data = pd.read_excel('./socios.xlsx')

cuit_list = list(set(data['CUIT'].to_list()))

if '-' in cuit_list:
    cuit_list.remove('-')

urls=[]

for c in cuit_list:
    pro = 'https://www.cuitonline.com/detalle/'+str(c)+'/'
    urls.append(pro)

urls = urls[1600:1800]

sub_list = []

for i in range(0, len(urls), 50):
    sublist = urls[i:i+50]
    sub_list.append(sublist)

print(len(sub_list))

for j in sub_list:
    print(len(j))

urls_pickle = './urls.pkl'

with open(urls_pickle, 'wb') as archivo_pickle:
    pickle.dump(sub_list, archivo_pickle)