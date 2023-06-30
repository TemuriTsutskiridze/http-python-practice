import requests
# r=requests.get('https://xkcd.com/353/')
# print(r)
# print(dir(r))
# print(help(r))
# print(r.text)




# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('pic.png', 'wb') as f:
#     f.write(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)




# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params = payload)
# print(r.url)



# payload={'username':'Musk', 'password':'test'}
# r=requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# r_dict = r.json()
# print(r_dict['form'])

# r = requests.get('https://httpbin.org/basic-auth/Musk/test', auth = ('Musk', 'test'))
# print(r.text)
# print(r)






# r = requests.get('https://httpbin.org/delay/6', timeout = 3)
# print(r)








# url = 'https://crawler-test.com/'
# response = requests.get(url)
# print('URL:', response.url)
# print('Status code:', response.status_code)
# print('HTTP header:', response.headers)





# url = 'https://httpbin.org/post'
# AI = {
#     'name': 'Nicola',
#     'last_name': 'Tesla',
#     'website': 'https://btu.edu.ge/' 
# }
# r = requests.post(url, data = AI)
# print(r.json())




# url = 'https://crawler-test.com/'
# r = requests.get(url)
# print(r.status_code)
# for redirect in r.history:
#     print(redirect.url, redirect.status_code)
# print(r.url, r.status_code)




from bs4 import BeautifulSoup

# url = 'https://crawler-test.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.find('title'))
# # print(soup.find_all('meta'))
# print(soup.find_all('meta', attrs={'name':'description'})[0])




# url='https://crawler-test.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# title = soup.find('title')
# h1 = soup.find('h1')
# description = soup.find('meta', attrs = {'name': 'description'})
# meta_robots = soup.find('meta', attrs = {'name': 'robots'})
# canonical = soup.find('link', {'rel': 'canonical'})
# title = title.get_text() if title else ""
# h1 = h1.get_text() if h1 else ""
# description = description['content'] if description else ""
# canonical = canonical['href'] if canonical else ""
# meta_robots = meta_robots['content'] if meta_robots else ""
# print('Title:', title)
# print('h1:', h1)
# print('description:',description)
# print('meta_robots:', meta_robots)
# print('canonical', canonical)




# url='https://crawler-test.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# links = []
# for link in soup.find_all('a', href = True):
#     print(link['href'])





from urllib.parse import urljoin
# url='https://crawler-test.com/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# links = []
# for link in soup.find_all('a', href = True):
#     links.append(urljoin(url, link['href']))
# print(links[:2])




import urllib.request
from bs4 import BeautifulSoup as bs
import re #regular expression
import pandas as pd
page=urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup=bs(page)
names=soup.body.findAll('dt')
function_names=re.findall('id="random.\w+', str(names))
#item[4:]პირველი ოთხი სიმბოლოს მოშორება
function_names=[item[4:] for item in function_names]
description=soup.body.findAll('dd')
function_usage=[]
for item in description:
    item=item.text
    item=item.replace('\n', ' ')
    function_usage.append(item)
print(function_names)
print(function_usage)
print(len(function_names))
data=pd.DataFrame({'function name': function_names, 'function usage': function_usage})
print(data)
example=soup.body.findAll('div', attrs={'role':'note'})
print(example)
data.to_csv('tesla.csv')


