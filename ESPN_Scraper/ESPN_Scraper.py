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

#First We Grab The Website
response = urllib2.urlopen('http://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171107/nfl-2017-week-10-power-rankings-biggest-risers-faller-preseason-philadelphia-eagles-new-england-patriots-pittsburgh-steelers-top-board')
html = response.read()
#Then we strain away all the bullshit
only_H2_level = SoupStrainer('h2')
soup = BeautifulSoup(html, 'html.parser', parse_only = only_H2_level)
#Then we compare it against our team names to create a list in the same order as the rankings
TeamOrder = soup.find_all(string=TeamNames)

#This is the function that prints the team being asked for
def find_team_index(user_team):
    user_team_ranking = TeamOrder.index(user_team) + 1
    print "The %s were ranked %s by ESPN's experts for week 10. " % (user_team, user_team_ranking)

#Here it goes!
print "Top five spots this week belong to %s, %s, %s, %s and %s" % (TeamOrder[0], TeamOrder[1], TeamOrder[2], TeamOrder[3], TeamOrder[4])
#Ask them what team they want to know the place of...
user_team = raw_input('To see where your team stacks up enter their two or three digit city code. For example, PHI for Philadelphia or LAC for Los Angeles Chargers: ')
user_team = user_team.upper()
#Verify it's the right length
if (len(user_team) < 2 or len(user_team) > 3):
    print "It seems you've made a mistake. Try Again. "
elif user_team == 'ARI':
    find_team_index('Arizona Cardinals')
elif user_team == 'ATL':
    find_team_index('Atlanta Falcons')
elif user_team == 'BAL':
    find_team_index('Baltimore Ravens')
elif user_team == 'BUF':
    find_team_index('Buffalo Bills')
elif user_team == 'CAR':
    find_team_index('Carolina Panthers')
elif user_team == 'CHI':
    find_team_index('Chicago Bears')
elif user_team == 'CIN':
    find_team_index('Cincinatti Bengals')
elif user_team == 'CLE':
    find_team_index('Cleveland Browns')
elif user_team == 'DAL':
    find_team_index('Dallas Cowboys')
elif user_team == 'DEN':
    find_team_index('Denver Broncos')
elif user_team == 'DET':
    find_team_index('Detroit Lions')
elif user_team == 'GB':
    find_team_index('Green Bay Packers')
elif user_team == 'HOU':
    find_team_index('Houston Texans')
elif user_team == 'IND':
    find_team_index('Indianapolis Colts')
elif user_team == 'JAX':
    find_team_index('Jacksonville Jaguars')
elif user_team == 'KC':
    find_team_index('Kansas City')
elif user_team == 'LAC':
    find_team_index('Los Angeles Chargers')
elif user_team == 'LAR':
    find_team_index('Los Angeles Rams')
elif user_team == 'MIA':
    find_team_index('Miami Dolphins')
elif user_team == 'MIN':
    find_team_index('Minnesota Vikings')
elif user_team == 'NE':
    find_team_index('New England Patriots')
elif user_team == 'NO':
    find_team_index('New Orleans Saints')
elif user_team == 'NYG':
    find_team_index('New York Giants')
elif user_team == 'NYJ':
    find_team_index('New York Jeys')
elif user_team == 'OAK':
    find_team_index('Oakland Raiders')
elif user_team == 'PHI':
    find_team_index('Philadelphia Eagles')
elif user_team == 'PIT':
    find_team_index('Pittsburgh Steelers')
elif user_team == 'SF':
    find_team_index('San Francisco 49ers')
elif user_team == 'SEA':
    find_team_index('Seattle Seahawks')
elif user_team == 'TB':
    find_team_index('Tampa Bay Buccaneers')
elif user_team == 'TEN':
    find_team_index('Tennessee Titans')
elif user_team == 'WAS':
    find_team_index('Washington Redskins')
else:
    "It seems you've made an error, here's a handy list of options! [handy list of options here]"



