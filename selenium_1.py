#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver=webdriver.Chrome(r'C:\Users\hanis\Downloads\chromedriver_win32\chromedriver.exe')


# In[ ]:


#Question 1


# In[ ]:


driver.get('https://www.amazon.in/')


# In[ ]:


search=input("Enter which product you want to search ")


# In[ ]:


search_tag=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search_tag.send_keys(search)


# In[ ]:


click=driver.find_element(By.ID,'nav-search-submit-button')
click.click()


# In[ ]:





# In[ ]:





# In[ ]:


#Question 2


# In[ ]:


price=[]
j=1
while(j<=3):
    tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
    for i in tags:
        if(i.text):
            price.append(i.text)
            
        else:
            price.append('-')
            
    j=j+1
    print('page completed')
    button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    click=button.get_attribute('href')
    driver.get(click)
len(price)    


# In[ ]:


#Brand_name=[]
i=1
links=[]
b_name=[]
while(i<=3):
    tags=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for j in tags:
        href=j.get_attribute('href')
        links.append(href)
    i=i+1 
    button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    click=button.get_attribute('href')
    driver.get(click)
    
print(len(links))        
for i in links:
    try:
        
        driver.get(i)
        tags=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]')
        b_name.append(tags.text)
    except:
        b_name.append('-')
    
len(b_name)   
    


# In[ ]:


#expected_delivery
exp_del=[]
i=1
while(i<=3):
    tags=driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')
    for j in tags:
        if(j.text):
            exp_del.append(j.text)
        else:
            exp_del.append('-')
        
    i=i+1 
    button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    click=button.get_attribute('href')
    driver.get(click)
    
len(exp_del)   


# In[ ]:


exp_del


# In[ ]:


#URL
i=1
URL=[]

while(i<=3):
    tags=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for j in tags:
        href=j.get_attribute('href')
        URL.append(href)
    i=i+1 
    button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    click=button.get_attribute('href')
    driver.get(click)
len(URL)    


# In[ ]:


URL


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Question 3


# In[ ]:


driver.get('https://images.google.com/')


# In[ ]:


#Fruits
search_bar=driver.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys('fruits')
search=driver.find_element(By.CLASS_NAME,'Tg7LZd')
search.click()


# In[ ]:


img_url=[]
img_tags=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
i=1
for j in img_tags:
    if(i<=10):
        src=j.find_element(By.TAG_NAME,'img').get_attribute('src')
        img_url.append(src)
        i+=1
    else:
        break
        
len(img_url)        


# In[ ]:


#cars
search_bar=driver.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys('cars')
search=driver.find_element(By.CLASS_NAME,'Tg7LZd')
search.click()


# In[ ]:


img_url=[]
img_tags=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
i=1
for j in img_tags:
    if(i<=10):
        src=j.find_element(By.TAG_NAME,'img').get_attribute('src')
        img_url.append(src)
        i+=1
    else:
        break
        
len(img_url)        


# In[ ]:


#Machine Learning
search_bar=driver.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys('Meachine Learning')
search=driver.find_element(By.CLASS_NAME,'Tg7LZd')
search.click()


# In[ ]:


img_url=[]
img_tags=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
i=1
for j in img_tags:
    if(i<=10):
        src=j.find_element(By.TAG_NAME,'img').get_attribute('src')
        img_url.append(src)
        i+=1
    else:
        break
        
len(img_url)        


# In[ ]:


#guitar
search_bar=driver.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys('Guitar')
search=driver.find_element(By.CLASS_NAME,'Tg7LZd')
search.click()


# In[ ]:


img_url=[]
img_tags=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
i=1
for j in img_tags:
    if(i<=10):
        src=j.find_element(By.TAG_NAME,'img').get_attribute('src')
        img_url.append(src)
        i+=1
    else:
        break
        
len(img_url)       


# In[ ]:


#cakes
search_bar=driver.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys('Cakes')
search=driver.find_element(By.CLASS_NAME,'Tg7LZd')
search.click()


# In[ ]:


img_url=[]
img_tags=driver.find_elements(By.XPATH,'//div[@class=" bRMDJf islir"]')
i=1
for j in img_tags:
    if(i<=10):
        src=j.find_element(By.TAG_NAME,'img').get_attribute('src')
        img_url.append(src)
        i+=1
    else:
        break
        
len(img_url)       


# In[ ]:





# In[ ]:





# In[ ]:


#Question 4


# In[ ]:


driver.get('http://www.flipkart.com/')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('One plus Nord')
button=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
button.click()


# In[ ]:





# In[ ]:


sphone_tags=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
sphone_name=[]
for i in sphone_tags:
    sphone_name.append(i.text)
    
len(sphone_name)    


# In[ ]:


price=[]
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for i in price_tags:
    try:
        price.append(i.text)
    except:
        price.append('-')
    
price 


# In[ ]:


product_url_tags=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
product_url=[]

for i in product_url_tags:
    href=i.get_attribute('href')
    product_url.append('href')
    
len(product_url)    


# In[ ]:


links=[]
d_size=[]
secondary_camera=[]
battery=[]
tags=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in tags:
    href=i.get_attribute('href')
    links.append(href)
    
len(links)   
for i in links:
    driver.get(i)
    tag=driver.find_element(By.XPATH,'//div[@class="_2418kt"]')
    li_tags=tag.find_elements(By.TAG_NAME,'li')
    d_size.append(li_tags[1].text)
    secondary_camera.append(li_tags[2].text)
    battery.append(li_tags[3].text)


# In[ ]:



links=[]
colour=[]
tags=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in tags:
    href=i.get_attribute('href')
    links.append(href)
    
for i in links:
    try:
        driver.get(i)
        value=driver.find_elements(By.XPATH,'//li[@class="_21lJbe"]')
        print(value[3].text)
        colour.append(value[3].text)
    except: 
        driver.append('-')
len(colour)        


# In[ ]:


#RAM,ROM
links=[]
ram=[]
rom=[]
primary_camera=[]
tags=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in tags:
    href=i.get_attribute('href')
    links.append(href)
    
for i in links:
    driver.get(i)
    button=driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    button.click()
    value1=driver.find_elements(By.XPATH,'//li[@class="_21lJbe"]')
    ram.append(value1[15].text)
    rom.append(value1[14].text)
    primary_camera.append(value1[17].text)
    print(value1[15].text," ",value1[14].text)
    
print(len(ram))   


# In[ ]:


len(primary_camera)


# In[ ]:


import pandas as pd


# In[ ]:


df=pd.DataFrame(columns=['Brand Name','Smart Phone Name','Colour','RAM','ROM','Primary Camera','Secondary Camera','Display Size','Battery capacity','Price','product URL'])


# In[ ]:


df['Smart Phone Name']=sphone_name
df['Colour']=colour
df['RAM']=ram
df['ROM']=rom
df['Primary Camera']=primary_camera
df['Secondary Camera']=secondary_camera
df['Display Size']=d_size
df['Battery capacity']=battery
df['Price']=price
df['product URL']=product_url
df['Brand Name']='One Plus Nord'


# In[ ]:


df


# In[ ]:


csv_data=df.to_csv('One_plus.csv',index=True)


# In[ ]:





# In[ ]:


#Question 5


# In[ ]:


driver.get('https://www.google.com/maps')


# In[ ]:


search=driver.find_element(By.ID,'searchboxinput')
search.send_keys('Hyderabad')
button=driver.find_element(By.ID,'searchbox-searchbutton')
button.click()


# In[ ]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10)
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//html/body")).context_click().perform()
print(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='menu']>li div div[class*='text']:nth-of-type(1)"))).text)


# In[ ]:


#Question 6


# In[ ]:


import time


# In[ ]:


driver.get('https://trak.in/stories/')


# In[ ]:


funding=driver.find_element(By.ID,'menu-item-1237902')
funding.click()


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'search_icon img-responsive')
search.click()


# In[ ]:





# In[ ]:


#Question 7


# In[ ]:


driver.get('https://www.digit.in/')


# In[ ]:


click=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[5]/span')
click.click()


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[5]/div[2]/div/div[2]/div/ul[3]/li[4]/a')
search.click()


# In[ ]:


tags=driver.find_elements(By.XPATH,'//div[@class="article_row"]')
links=[]
best_laptops=[]
for i in tags:
    a_tag=i.find_element(By.TAG_NAME,'a').get_attribute('href')
    
    links.append(a_tag)
    
print(links)   

for i in links:
    driver.get(i)
    print(i)
    h3_tags=driver.find_elements(By.XPATH,'//div[@class="article_row big-image"]')
    for j in h3_tags:
        
        a_tag=j.find_element(By.TAG_NAME,'a')
        print(a_tag.text)
        best_laptops.append(a_tag.text)
        
print(best_laptops) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Question 8


# In[ ]:


driver.get('http://www.forbes.com/')


# In[ ]:


tags=driver.find_element(By.TAG_NAME,'svg')
tags.click()


# In[ ]:


button=driver.find_element(By.XPATH,'//li[@class="TjJgrPSg _2bNo56RE secondary"][1]')
a=button.find_element(By.TAG_NAME,'a')
href=a.get_attribute('href')
driver.get(href)


# In[ ]:


#Name
name=[]

for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"][2]')
    for i in tags:
        name.append(i.text)
    


# In[ ]:


#Rank
rank=[]
for page in range(1,10):
    div_tag=driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')

    
    for i in div_tag:
        rank.append(i.text)
    
  
rank


# In[ ]:


#Net Worth
net_worth=[]
for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="Table_netWorth___L4R5 Table_dataCell__2QCve"]')
    for i in tags:
        net_worth.append(i.text)
    
net_worth    


# In[ ]:


#Age
age=[]

for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"][4]')
    for i in tags:
        age.append(i.text)
age    


# In[ ]:


#citizenship
citizenship=[]

for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"][5]')
    for i in tags:
        citizenship.append(i.text)
citizenship    


# In[ ]:


#Source
Source=[]

for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"][6]')
    for i in tags:
        Source.append(i.text)
Source 


# In[ ]:


#Industry

Industry=[]

for page in range(1,10):
    tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"][7]')
    for i in tags:
        Industry.append(i.text)
Industry 


# In[ ]:





# In[ ]:





# In[ ]:


#Question 9


# In[3]:


driver.get('https://www.youtube.com/watch?v=X3paOmcrTjQ')


# In[ ]:


comment=[]
n=1
for i in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
tags=driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-comment-renderer"]')
while(n<=500):
    for i in tags:
        comment.append(i.text)
    n=n+1    
    
len(comment)


# In[5]:


time=[]
n=1
tags=driver.find_elements(By.XPATH,'//a[contains(@src,'ago')])
while(n<=500):
    for i in tags:
        time.append(i.text)
    n=n+1
    
len(time)    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Question 10


# In[ ]:


driver.get('http://www.hostelworld.com/')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'field-inner')
search.click()


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'search-input')
search.send_keys('London')


# In[ ]:


tag=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/ul/li[2]/div')
tag.click()


# In[ ]:


click=driver.find_element(By.ID,'search-button')
click.click()


# In[ ]:


name=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
    for i in tags:
        j=i.find_element(By.TAG_NAME,'a')
        name.append(j.text)

len(name)


# In[ ]:


distance=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//span[@class="description"]')
    
    for i in tags:
        j=i.find_element(By.TAG_NAME,'span')
        distance.append(j.text)
    
len(distance)    


# In[ ]:


rating=[]
for page in range(1,3):
    try:
        tags=driver.find_elements(By.XPATH,'//div[@class="score orange big"]')
        for i in tags:
        
            rating.append(i.text)
    except:
        rating.append('-')
        
    
    
        
len(rating)        


# In[ ]:


privates=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//div[@class="price title-5"]')
    for i in tags:
        if(i):
            privates.append(i.text)
        else:
            continue
        
len(privates)        
privates        


# In[ ]:


dorms=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//div[@class="price title-5"]')
    for i in tags:
        dorms.append(i.text)
        
len(dorms)        


# In[ ]:


description=[]
links=[]
facilities=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
    for j in tags:
        href=j.find_element(By.TAG_NAME,'a').get_attribute('href')
        links.append(href)

for i in links:
    driver.get(i)
    try:
        
        tags=driver.find_element(By.XPATH,'//div[@class="content collapse-content"]')
        description.append(tags.text)
    except:
        continue

        


        
len(description)   


# In[ ]:


facilities=[]
links=[]
link1=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
    for j in tags:
        href=j.find_element(By.TAG_NAME,'a').get_attribute('href')
        links.append(href)
        
for i in links:
    driver.get(i)
    try:
        tags=driver.find_element(By.CLASS_NAME,'facilities')
        facilities.append(tags.text)
        print(tags.text)
    except:
        facilities.append('-')
        
len(facilities)        


# In[ ]:


fac=[]
tags=driver.find_element(By.CLASS_NAME,'facilities')
tags.text


# In[ ]:


total_reviews=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//div[@class="reviews"]')
    for i in tags:
        total_reviews.append(i.text)
    
len(total_reviews)    


# In[ ]:


overall_reviews=[]
for page in range(1,3):
    tags=driver.find_elements(By.XPATH,'//div[@class="keyword"]')
    for i in tags:
        span=i.find_element(By.TAG_NAME,'span')
       
        overall_reviews.append(span.text)
    
len(overall_reviews)    


# In[ ]:




