
''' Importing required packages '''
import requests
import bs4
import pandas as pd

''' taking url of site to url1 vaiable'''
url1='https://www.rapid7.com/db/vulnerabilities'

'''get the url1 content using requests get method'''
res=requests.get(url1)
h=res.content

'''Parsing the page using BeautifulSoup'''
res1=bs4.BeautifulSoup(h,'html.parser')


#print(res1.prettify().encode('cp1252', errors='ignore'))

'''find class of vulnerabilities, published date and severity in website '''
k=res1.find_all('div', class_ = 'resultblock__info-title')
l=res1.find_all('div', class_='resultblock__info-meta')

a=[]
b=[]
c=[]
'''pass the strings above into lists'''
for i in range(len(k)):
    a.append(k[i].get_text().replace('\n',"").replace('\t',"")[33:])
    b.append(l[i].get_text().replace('\n',"").replace('\t',"")[44:65])
    c.append(l[i].get_text().replace('\n',"").replace('\t',"")[162:])

'''to show the data completely'''
pd.set_option('display.max_colwidth', None)

'''passing data to dataframe'''
df=pd.DataFrame({'Vulnarability name':a,'Published date':b,'Severity':c})

'''save the data to csv file'''
df.to_csv('Vul.csv', sep ='\t')



# loading the CSV file
