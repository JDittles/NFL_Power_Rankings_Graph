'''This scraper accesses the most recent NFL Rankings Page from ESPN,
	scrapes its HTML, compares against an alphabetical list of 32 NFL
	teams (imported from 'Team Names Current' in order to prepare for
	future team moves and possibly historical data where, for example,
	the Los Angeles Chargers don't yet exist) and returns the team 
	names in order of NFL Power Ranking; Future iterations will then
	figure out how to use this list'''
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
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
'Cincinnati Bengals',
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
TeamDict={ 'ARI' : 'Arizona Cardinals',
'ATL' : 'Atlanta Falcons',
'BAL' : 'Baltimore Ravens',
'BUF' : 'Buffalo Bills',
'CAR' : 'Carolina Panthers',
'CHI' : 'Chicago Bears',
'CIN' : 'Cincinnati Bengals',
'CLE' : 'Cleveland Browns',
'DAL' : 'Dallas Cowboys',
'DEN' : 'Denver Broncos',
'DET' : 'Detroit Lions',
'GB' : 'Green Bay Packers',
'HOU' : 'Houston Texans',
'IND' : 'Indianapolis Colts',
'JAX' : 'Jacksonville Jaguars',
'KC' : 'Kansas City Chiefs',
'LAC' : 'Los Angeles Chargers',
'LAR' : 'Los Angeles Rams',
'MIA' : 'Miami Dolphins',
'MIN' : 'Minnesota Vikings',
'NE' : 'New England Patriots',
'NO' : 'New Orleans Saints',
'NYG' : 'New York Giants',
'NYJ' : 'New York Jets',
'OAK' : 'Oakland Raiders',
'PHI' : 'Philadelphia Eagles',
'PIT' : 'Pittsburgh Steelers',
'SF' : 'San Francisco 49ers',
'SEA' : 'Seattle Seahawks',
'TB' : 'Tampa Bay Buccaneers',
'TEN' : 'Tennessee Titans',
'WAS' : 'Washington Redskins'
}

ARI_list = []
ATL_list = []
BAL_list = []
BUF_list = []
CAR_list = []
CHI_list = []
CIN_list = []
CLE_list = []
DAL_list = []
DEN_list = []
DET_list = []
GB_list = []
HOU_list = []
IND_list = []
JAX_list = []
KC_list = []
LAC_list = []
LAR_list = []
MIA_list = []
MIN_list = []
NE_list = []
NO_list = []
NYG_list = []
NYJ_list = []
OAK_list = []
PHI_list = []
PIT_list = []
SF_list = []
SEA_list = []
TB_list = []
TEN_list = []
WAS_list = []

LstDict = { 'ARI' : ARI_list,
'ATL' : ATL_list,
'BAL' : BAL_list,
'BUF' : BUF_list,
'CAR' : CAR_list,
'CHI' : CHI_list,
'CIN' : CIN_list,
'CLE' : CLE_list,
'DAL' : DAL_list,
'DEN' : DEN_list,
'DET' : DET_list,
'GB' : GB_list,
'HOU' : HOU_list,
'IND' : IND_list,
'JAX' : JAX_list,
'KC' : KC_list,
'LAC' : LAC_list,
'LAR' : LAR_list,
'MIA' : MIA_list,
'MIN' : MIN_list,
'NE' : NE_list,
'NO' : NO_list,
'NYG' : NYG_list,
'NYJ' : NYJ_list,
'OAK' : OAK_list,
'PHI' : PHI_list,
'PIT' : PIT_list,
'SF' : SF_list,
'SEA' : SEA_list,
'TB' : TB_list,
'TEN' : TEN_list,
'WAS' : WAS_list,
}

def GetTeamName(user_choice):
	return (TeamDict[user_choice])

#WEEK1
response1 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx170815/2017-preseason-nfl-power-rankings-new-england-patriots-atlanta-falcons-seattle-seahawks-front')
html1 = response1.read()
#Then we strain away all the bullshit
only_H2_level1 = SoupStrainer('h2')
soup1 = BeautifulSoup(html1, 'html.parser', parse_only = only_H2_level1)
#Then we compare it against our team names to create a list in the same order as the rankings
TeamOrder1 = soup1.find_all(string=TeamNames)
#The next function adds the number to the list for each team, slowly building the list from which we'll plot our graph
ARI_list.append((TeamOrder1.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder1.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder1.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder1.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder1.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder1.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder1.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder1.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder1.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder1.index('Denver Broncos') + 1))
DET_list.append((TeamOrder1.index('Detroit Lions') + 1))
GB_list.append((TeamOrder1.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder1.index('Houston Texans') + 1))
IND_list.append((TeamOrder1.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder1.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder1.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder1.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder1.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder1.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder1.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder1.index('New England Patriots') + 1))
NO_list.append((TeamOrder1.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder1.index('New York Giants') + 1))
NYJ_list.append((TeamOrder1.index('New York Jets') + 1))
OAK_list.append((TeamOrder1.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder1.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder1.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder1.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder1.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder1.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder1.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder1.index('Washington Redskins') + 1))

#WEEK2
response2 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx170912/nfl-2017-week-2-power-rankings-overreaction-edition-pittsburgh-steelers-green-bay-packers-kansas-city-chiefs-make-early-moves')
html2 = response2.read()
only_H2_level2 = SoupStrainer('h2')
soup2 = BeautifulSoup(html2, 'html.parser', parse_only = only_H2_level2)
TeamOrder2 = soup2.find_all(string=TeamNames)
ARI_list.append((TeamOrder2.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder2.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder2.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder2.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder2.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder2.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder2.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder2.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder2.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder2.index('Denver Broncos') + 1))
DET_list.append((TeamOrder2.index('Detroit Lions') + 1))
GB_list.append((TeamOrder2.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder2.index('Houston Texans') + 1))
IND_list.append((TeamOrder2.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder2.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder2.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder2.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder2.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder2.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder2.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder2.index('New England Patriots') + 1))
NO_list.append((TeamOrder2.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder2.index('New York Giants') + 1))
NYJ_list.append((TeamOrder2.index('New York Jets') + 1))
OAK_list.append((TeamOrder2.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder2.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder2.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder2.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder2.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder2.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder2.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder2.index('Washington Redskins') + 1))

#WEEK3
response3 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx170919/nfl-2017-week-3-power-rankings-let-optimistic-atlanta-falcons-kansas-city-chiefs-pittsburgh-steelers-top-our-board')
html3 = response3.read()
only_H2_level3 = SoupStrainer('h2')
soup3 = BeautifulSoup(html3, 'html.parser', parse_only = only_H2_level3)
TeamOrder3 = soup3.find_all(string=TeamNames)
ARI_list.append((TeamOrder3.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder3.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder3.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder3.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder3.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder3.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder3.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder3.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder3.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder3.index('Denver Broncos') + 1))
DET_list.append((TeamOrder3.index('Detroit Lions') + 1))
GB_list.append((TeamOrder3.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder3.index('Houston Texans') + 1))
IND_list.append((TeamOrder3.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder3.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder3.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder3.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder3.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder3.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder3.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder3.index('New England Patriots') + 1))
NO_list.append((TeamOrder3.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder3.index('New York Giants') + 1))
NYJ_list.append((TeamOrder3.index('New York Jets') + 1))
OAK_list.append((TeamOrder3.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder3.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder3.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder3.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder3.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder3.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder3.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder3.index('Washington Redskins') + 1))

#WEEK4
response4 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx170926/nfl-2017-week-4-power-rankings-atlanta-falcons-kansas-city-chiefs-new-england-patriots-quarterbacks')
html4 = response4.read()
only_H2_level4 = SoupStrainer('h2')
soup4 = BeautifulSoup(html4, 'html.parser', parse_only = only_H2_level4)
TeamOrder4 = soup4.find_all(string=TeamNames)
ARI_list.append((TeamOrder4.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder4.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder4.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder4.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder4.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder4.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder4.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder4.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder4.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder4.index('Denver Broncos') + 1))
DET_list.append((TeamOrder4.index('Detroit Lions') + 1))
GB_list.append((TeamOrder4.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder4.index('Houston Texans') + 1))
IND_list.append((TeamOrder4.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder4.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder4.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder4.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder4.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder4.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder4.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder4.index('New England Patriots') + 1))
NO_list.append((TeamOrder4.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder4.index('New York Giants') + 1))
NYJ_list.append((TeamOrder4.index('New York Jets') + 1))
OAK_list.append((TeamOrder4.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder4.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder4.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder4.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder4.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder4.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder4.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder4.index('Washington Redskins') + 1))

#WEEK5
response5 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171003/nfl-2017-week-5-power-rankings-kansas-city-chiefs-green-bay-packers-atlanta-falcons-top-our-board')
html5 = response5.read()
only_H2_level5 = SoupStrainer('h2')
soup5 = BeautifulSoup(html5, 'html.parser', parse_only = only_H2_level5)
TeamOrder5 = soup5.find_all(string=TeamNames)
ARI_list.append((TeamOrder5.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder5.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder5.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder5.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder5.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder5.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder5.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder5.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder5.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder5.index('Denver Broncos') + 1))
DET_list.append((TeamOrder5.index('Detroit Lions') + 1))
GB_list.append((TeamOrder5.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder5.index('Houston Texans') + 1))
IND_list.append((TeamOrder5.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder5.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder5.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder5.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder5.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder5.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder5.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder5.index('New England Patriots') + 1))
NO_list.append((TeamOrder5.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder5.index('New York Giants') + 1))
NYJ_list.append((TeamOrder5.index('New York Jets') + 1))
OAK_list.append((TeamOrder5.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder5.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder5.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder5.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder5.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder5.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder5.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder5.index('Washington Redskins') + 1))

#WEEK6
response6 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171010/nfl-2017-week-6-power-rankings-kansas-city-chiefs-green-bay-packers-atlanta-falcons-lead-playoff-chances')
html6 = response6.read()
only_H2_level6 = SoupStrainer('h2')
soup6 = BeautifulSoup(html6, 'html.parser', parse_only = only_H2_level6)
TeamOrder6 = soup6.find_all(string=TeamNames)
ARI_list.append((TeamOrder6.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder6.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder6.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder6.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder6.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder6.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder6.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder6.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder6.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder6.index('Denver Broncos') + 1))
DET_list.append((TeamOrder6.index('Detroit Lions') + 1))
GB_list.append((TeamOrder6.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder6.index('Houston Texans') + 1))
IND_list.append((TeamOrder6.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder6.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder6.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder6.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder6.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder6.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder6.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder6.index('New England Patriots') + 1))
NO_list.append((TeamOrder6.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder6.index('New York Giants') + 1))
NYJ_list.append((TeamOrder6.index('New York Jets') + 1))
OAK_list.append((TeamOrder6.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder6.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder6.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder6.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder6.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder6.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder6.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder6.index('Washington Redskins') + 1))

#WEEK7
response7 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171017/nfl-2017-week-7-power-rankings-kansas-city-chiefs-philadelphia-eagles-new-england-patriots-top-our-board-remaining-schedules')
html7 = response7.read()
only_H2_level7 = SoupStrainer('h2')
soup7 = BeautifulSoup(html7, 'html.parser', parse_only = only_H2_level7)
TeamOrder7 = soup7.find_all(string=TeamNames)
ARI_list.append((TeamOrder7.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder7.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder7.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder7.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder7.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder7.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder7.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder7.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder7.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder7.index('Denver Broncos') + 1))
DET_list.append((TeamOrder7.index('Detroit Lions') + 1))
GB_list.append((TeamOrder7.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder7.index('Houston Texans') + 1))
IND_list.append((TeamOrder7.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder7.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder7.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder7.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder7.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder7.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder7.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder7.index('New England Patriots') + 1))
NO_list.append((TeamOrder7.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder7.index('New York Giants') + 1))
NYJ_list.append((TeamOrder7.index('New York Jets') + 1))
OAK_list.append((TeamOrder7.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder7.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder7.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder7.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder7.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder7.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder7.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder7.index('Washington Redskins') + 1))

#WEEK8
response8 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171024/nfl-2017-week-8-power-rankings-new-england-patriots-unseat-kansas-city-chiefs-no-1-chances-win-division')
html8 = response8.read()
only_H2_level8 = SoupStrainer('h2')
soup8 = BeautifulSoup(html8, 'html.parser', parse_only = only_H2_level8)
TeamOrder8 = soup8.find_all(string=TeamNames)
ARI_list.append((TeamOrder8.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder8.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder8.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder8.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder8.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder8.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder8.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder8.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder8.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder8.index('Denver Broncos') + 1))
DET_list.append((TeamOrder8.index('Detroit Lions') + 1))
GB_list.append((TeamOrder8.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder8.index('Houston Texans') + 1))
IND_list.append((TeamOrder8.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder8.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder8.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder8.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder8.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder8.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder8.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder8.index('New England Patriots') + 1))
NO_list.append((TeamOrder8.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder8.index('New York Giants') + 1))
NYJ_list.append((TeamOrder8.index('New York Jets') + 1))
OAK_list.append((TeamOrder8.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder8.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder8.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder8.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder8.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder8.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder8.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder8.index('Washington Redskins') + 1))

#WEEK9
response9 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171031/nfl-2017-week-9-power-rankings-scariest-trends-all-32-teams-philadelphia-eagles-new-england-patriots-kansas-city-chiefs-top-board')
html9 = response9.read()
only_H2_level9 = SoupStrainer('h2')
soup9 = BeautifulSoup(html9, 'html.parser', parse_only = only_H2_level9)
TeamOrder9 = soup9.find_all(string=TeamNames)
ARI_list.append((TeamOrder9.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder9.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder9.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder9.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder9.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder9.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder9.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder9.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder9.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder9.index('Denver Broncos') + 1))
DET_list.append((TeamOrder9.index('Detroit Lions') + 1))
GB_list.append((TeamOrder9.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder9.index('Houston Texans') + 1))
IND_list.append((TeamOrder9.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder9.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder9.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder9.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder9.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder9.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder9.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder9.index('New England Patriots') + 1))
NO_list.append((TeamOrder9.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder9.index('New York Giants') + 1))
NYJ_list.append((TeamOrder9.index('New York Jets') + 1))
OAK_list.append((TeamOrder9.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder9.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder9.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder9.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder9.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder9.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder9.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder9.index('Washington Redskins') + 1))

#WEEK10
response10 = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171107/nfl-2017-week-10-power-rankings-biggest-risers-faller-preseason-philadelphia-eagles-new-england-patriots-pittsburgh-steelers-top-board')
html10 = response10.read()
only_H2_level10 = SoupStrainer('h2')
soup10 = BeautifulSoup(html10, 'html.parser', parse_only = only_H2_level10)
TeamOrder10 = soup10.find_all(string=TeamNames)
ARI_list.append((TeamOrder10.index('Arizona Cardinals') + 1))
ATL_list.append((TeamOrder10.index('Atlanta Falcons') + 1))
BAL_list.append((TeamOrder10.index('Baltimore Ravens') + 1))
BUF_list.append((TeamOrder10.index('Buffalo Bills') + 1))
CAR_list.append((TeamOrder10.index('Carolina Panthers') + 1))
CHI_list.append((TeamOrder10.index('Chicago Bears') + 1))
CIN_list.append((TeamOrder10.index('Cincinnati Bengals') + 1))
CLE_list.append((TeamOrder10.index('Cleveland Browns') + 1))
DAL_list.append((TeamOrder10.index('Dallas Cowboys') + 1))
DEN_list.append((TeamOrder10.index('Denver Broncos') + 1))
DET_list.append((TeamOrder10.index('Detroit Lions') + 1))
GB_list.append((TeamOrder10.index('Green Bay Packers') + 1))
HOU_list.append((TeamOrder10.index('Houston Texans') + 1))
IND_list.append((TeamOrder10.index('Indianapolis Colts') + 1))
JAX_list.append((TeamOrder10.index('Jacksonville Jaguars') + 1))
KC_list.append((TeamOrder10.index('Kansas City Chiefs') + 1))
LAC_list.append((TeamOrder10.index('Los Angeles Chargers') + 1))
LAR_list.append((TeamOrder10.index('Los Angeles Rams') + 1))
MIA_list.append((TeamOrder10.index('Miami Dolphins') + 1))
MIN_list.append((TeamOrder10.index('Minnesota Vikings') + 1))
NE_list.append((TeamOrder10.index('New England Patriots') + 1))
NO_list.append((TeamOrder10.index('New Orleans Saints') + 1))
NYG_list.append((TeamOrder10.index('New York Giants') + 1))
NYJ_list.append((TeamOrder10.index('New York Jets') + 1))
OAK_list.append((TeamOrder10.index('Oakland Raiders') + 1))
PHI_list.append((TeamOrder10.index('Philadelphia Eagles') + 1))
PIT_list.append((TeamOrder10.index('Pittsburgh Steelers') + 1))
SF_list.append((TeamOrder10.index('San Francisco 49ers') + 1))
SEA_list.append((TeamOrder10.index('Seattle Seahawks') + 1))
TB_list.append((TeamOrder10.index('Tampa Bay Buccaneers') + 1))
TEN_list.append((TeamOrder10.index('Tennessee Titans') + 1))
WAS_list.append((TeamOrder10.index('Washington Redskins') + 1))

req = True
while req:
	print 'This app lists ESPN experts\' rankings for the team of your choice.'
	user_choice = raw_input('Simply enter the 2-3 digit city code for the team from which you would like data.\n If you\'d like to exit simply enter \"XX\" ')
	user_choice = user_choice.upper()
	if ( len(user_choice) < 2 or len(user_choice) > 3 ):
		print 'You\'ve entered something a bit funky. Try again. If you want Jacksonville for example, enter JAX.'
	elif user_choice == "XX":
		req = False
	else:
		TeamList = LstDict[user_choice]
		TeamName = TeamDict[user_choice]
		print 'ESPN ranked the %s as:\n#%s week one,\n#%s week two,\n#%s week three,\n#%s week four\n#%s week five\n#%s week six\n#%s week seven\n#%s week eigth\n#%s week nine\n#%s week ten.' % (TeamName, TeamList[0], TeamList[1], TeamList[2], TeamList[3], TeamList[4], TeamList[5], TeamList[6], TeamList[7], TeamList[8], TeamList[9])






