# Mr wang
import pandas as pd
with open ('mal_domains1.txt','r',encoding='utf-8') as f:
      reader=f.readlines()
      f.close()
result=[]
for i in reader:
    domain=i.split('\t')[0]
    result.append(domain)
df=pd.DataFrame(result,columns=['domain'])
print(df)
df['domain'].to_csv('mal_domains.csv')
