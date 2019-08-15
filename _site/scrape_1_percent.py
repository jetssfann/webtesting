import pandas as pd
from pandas import read_excel
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen
import numpy as np
from collections import defaultdict

##SET DATAFRAME VARIABLES

nationalRank = []
teamPoints = []
teamID = []
teamName = []
teamState = []

###### PANDAS DATA FRAMES

df1 = pd.DataFrame(nationalRank, columns =  ['Rank'])
df2 = pd.DataFrame(teamPoints, columns =  ['Ranking Points'])
df3 = pd.DataFrame(teamID, columns =  ['teamID'])
df4 = pd.DataFrame(teamName, columns =  ['team Name'])
df5 = pd.DataFrame(teamState, columns =  ['team State'])

## Reseting indexes to have columns align when joined (Will get NaN errors if we do not do this)
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
df3.reset_index(drop=True, inplace=True)
df4.reset_index(drop=True, inplace=True)
df5.reset_index(drop=True, inplace=True)

## Concat each DF into one DF
df6 = pd.concat([df1, df2, df3, df4, df5], axis=1)
df6.head()

## SET TEAM COUNT VARIABLE EQUAL TO NUMBER OF TEAMS IN DATA FRAME
teamCount = len(df6)
# print(teamCount)

## SET AGE GENDER & PERCENT PARAMS
age = '15'
gender = 'Boys'
percent = 1

## GET INTIAL LINK
source = requests.get('http://home.gotsoccer.com/rankings/results.aspx?Page=1&level=National&country=USA&gender=' + str(gender) +'&age=' +str(age)).text

soup = BeautifulSoup(source, 'lxml')

targetNumber = soup.find('span', {'class': 'SubHeading'}).text
targetNumber = targetNumber.split('of ')[1]
targetNumber = int(targetNumber)
targetNumber = targetNumber/100 * percent
# print(targetNumber)

i = 0

## WHILE LOOP INCREMENT PAGE NUMBER UNTIL TARGET NUMER IS EXCEDED
while targetNumber >= teamCount:
    i +=1
    # print(teamCount)

    ## LINK WITH INCREMENTING VARIABLE i
    source = requests.get('http://home.gotsoccer.com/rankings/results.aspx?Page=' + str(i) +'&level=National&country=USA&gender=' + str(gender) +'&age=' +str(age)).text

    soup = BeautifulSoup(source, 'lxml')

    ## Print full page html
    # print(soup.prettify())

    ##PARSE DATA INTO JUST THE WANTED TABLE DATA NO HEADERS
    table = soup.find ('tbody')

    # print(table.prettify())

    ## CREATE ROWS FOR EACH TEAM AND ITERATE THROUGH SCRAPER
    for teamRow in table.find_all('tr'):
        # print(teamRow)
        getnationalRank = teamRow.find('td').text
        ## ADD DATA INTO DATAFRAME
        nationalRank.append(getnationalRank)
        # print(getnationalRank)

        getteamPoints = teamRow.find('td')
        getteamPoints = getteamPoints.find_next('td').text
        # print(getteamPoints)
        ## ADD DATA INTO DATAFRAME
        teamPoints.append(getteamPoints)


        ## Get Team link
        getteamID = teamRow.find('a')
        ## Parse teamLink into Team ID
        getteamID = str(getteamID).split('teamid=')[1]
        getteamID = getteamID.split('">')[0]
        ## ADD DATA INTO DATAFRAME
        teamID.append(getteamID)

        ## GET TEAM NAME
        getteamName = teamRow.find('a').text
        ## ADD DATA INTO DATAFRAME
        teamName.append(getteamName)
        # print(getteamName)

        ## GET TEAM STATE PROBABLY A BETTER WAY BUT
        getteamState = teamRow.find('td')
        getteamState = getteamState.find_next('td')
        getteamState = getteamState.find_next('td')
        getteamState = getteamState.find_next('td').text
        getteamState = getteamState.split(':')[0]
        # print(getteamState)
        ## ADD DATA INTO DATAFRAME
        teamState.append(getteamState)
            # print()
            #
            # print(teamID)
            # print(teamName)
            #
        # print()

        ### RESET PANDAS DATA FRAMES WITH DATA

        df1 = pd.DataFrame(nationalRank, columns =  ['Rank'])
        df2 = pd.DataFrame(teamPoints, columns =  ['Rankings Points'])
        df3 = pd.DataFrame(teamID, columns =  ['teamID'])
        df4 = pd.DataFrame(teamName, columns =  ['team Name'])
        df5 = pd.DataFrame(teamState, columns =  ['team State'])

        ## Reseting indexes to have columns align when joined (Will get NaN errors if we do not do this)
        df1.reset_index(drop=True, inplace=True)
        df2.reset_index(drop=True, inplace=True)
        df3.reset_index(drop=True, inplace=True)
        df4.reset_index(drop=True, inplace=True)
        df5.reset_index(drop=True, inplace=True)

        ## Concat each DF into one DF
        df6 = pd.concat([df1, df2, df3, df4, df5], axis=1)
        df6.head()
        ## SET TEAM COUNT AND RECALCULATE AFTER SCRAPER RUN
        teamCount = len(df6)
        # print(teamCount)

    ## PRINT DATA FRAME IN TERMINAL
    print(df6)

    ## EXPORT DATAFRAME INTO EXCEL
    df6.to_excel("one_percent.xlsx")

    ## STOP SCRIPT IF SCRAPE HITS PAGE 5
    if i == 5:
        break
        i +=1
    # print(i)
