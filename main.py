from bs4 import BeautifulSoup
import requests
import pandas as pd

print("Put some skill that you are familiar with")
familiar_skill = input("Enter you skill: ")
print(f'Filtering out jobs having skill {familiar_skill}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
data = {'Name': [], 'Skills': [], 'Location': [], 'Link':[]}
jobs = soup.find_all('li', {'class': 'clearfix job-bx wht-shd-bx'})

for job in jobs:
    company_name = job.find('h3',{'class':'joblist-comp-name'}).text.strip()
    skills = job.find('span',{'class':'srp-skills'}).text.strip()
    location = job.find('ul',{'class':'top-jd-dtl clearfix'}).span.text
    more_info = job.header.h2.a['href']
    
    #Filtering out the output  based on user entered skills
    if familiar_skill in  skills:
        # print(f'Company Name: {company_name}')
        data['Name'].append(company_name) #appending the company name into dictionary
        # print(f'Skills Required: {skills}')
        data['Skills'].append(skills) #appending the skills into dictionary
        # print(f'Location: {location}')
        data['Location'].append(location) #appending the location info into dictionary
        # print(f"More Info: {more_info}")
        data['Link'].append(more_info) #appending the link into dictionary
        # print("\n-----------------------------\n")

#Converting Dictionary to DataFrame and saving it as CSV file
df = pd.DataFrame.from_dict(data)
print(df)

df.to_excel('data.xlsx',index=False,header=True) #exporting the data into excel
