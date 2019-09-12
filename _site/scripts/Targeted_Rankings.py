## IMPORT NECESSARY PACKAGES

import pandas as pd
from pandas import read_excel
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen
import numpy as np
from collections import defaultdict


## GET TARGET ID's and Names
BU19IDs = "Teams.xlsx"
iD_DF = read_excel(BU19IDs)
iD_DF = iD_DF[['GotSoccer Team ID', 'Full Team Name']]
iD_DF.head()

## CREATE TARGET LIST
for index, row in iD_DF.iterrows():
    teamList.append((row['GotSoccer Team ID']))

#print(teamList)

##SET DATAFRAME VARIABLES

nationalRank = []
teamPoints = []
teamID = []
teamName = []
teamState = []
teamgenderAge = []

# For all Team ID's, parse through URL and scrape Ranking Points and National (USA/Canada) Ranking
for items in teamList:

    # URL for parsing
    baseURL = "https://home.gotsoccer.com/rankings/team.aspx?teamid=" + str(items)

    # Fetching content from GotSoccer URL using requests library
    page_response = requests.get(baseURL, timeout=5)

    # page_resonpse (HTML Parser) store's info GotSoccer info in a variable page_content.
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # Tags are nested. Searching for correct tags and classes. Appending the values we want into the lists.
    rankings = page_content.findAll("div", {'class': 'tab-content'})

    for items in rankings:
        getNationalRanking = page_content.find("text", {'class': 'number'})
        nationalRanking.append(getNationalRanking.text)
        getRankingPoints = page_content.find("span", {'class': 'badge badge-club-color'})
        rankingPoints.append(getRankingPoints.text)



# print(nationalRanking)
# print(rankingPoints)

# Creating DF's and placing the scrapped information into each category
df1 = pd.DataFrame(nationalRanking, columns =  ['National Ranking'])
df2 = pd.DataFrame(rankingPoints, columns =  ['Ranking Points'])
df3 = pd.DataFrame(teamList, columns =  ['Team ID'])

# Reseting indexes to have columns align when joined (Will get NaN errors if we do not do this)
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
df3.reset_index(drop=True, inplace=True)

# Concat each DF into one DF
df4 = pd.concat([df1, df2, df3], axis=1)
df4.head()

## EXPORT DATAFRAME INTO EXCEL
df4.to_excel("target.xlsx", index=False)
