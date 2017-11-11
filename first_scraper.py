'''This scraper accesses the most recent NFL Rankings Page from ESPN,
	scrapes its HTML, compares against an alphabetical list of 32 NFL
	teams (imported from 'Team Names Current' in order to prepare for
	future team moves and possibly historical data where, for example,
	the Los Angeles Chargers don't yet exist) and returns the team 
	names in order of NFL Power Ranking; Future iterations will then
	figure out how to use this list'''
from bs4 import BeautifulSoup
import re
import urllib2
# The following will pull team names from another doc depending on year...
#
# TeamNames=[]
# with open('TeamNamesCurrent.txt', 'r') as L:
# 	for each in L:
# 		TeamNames.append(each)
#		print each
#
TeamNames=['Arizona Cardinals',
'Atlanta Falcons',
'Baltimore Ravens',
'Buffalo Bills',
'Carolina Panthers',
'Chicago Bears',
'Cincinatti Bengals',
'Cleveland Browns',
'Dallas Cowboys',
'Denver Broncos',
'Detroit Lions',
'Green Bay Packers',
'Houston Texans',
'Indianapolis Colts',
'Jacksonville Jaguars',
'Kansas City Chiefs',
'Los Angeles Chargers',
'Los Angeles Rams',
'Miami Dolphins',
'Minnesota Vikings',
'New England Patriots',
'New Orleans Saints',
'New York Giants',
'New York Jets',
'Oakland Raiders',
'Philadelphia Eagles',
'Pittsburgh Steelers',
'San Francisco 49ers',
'Seattle Seahawks',
'Tampa Bay Buccaneers',
'Tennessee Titans',
'Washington Redskins'
]
response = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171107/nfl-2017-week-10-power-rankings-biggest-risers-faller-preseason-philadelphia-eagles-new-england-patriots-pittsburgh-steelers-top-board')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
#H2 = soup.find_all("h2")
TeamOrder = soup.find_all(string=TeamNames)


print TeamOrder