#This scraper does all the ESPN Power Rankings

from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib2
from Teams import *
from ESPN_URLs import espn_urls

def build_espn_rankings():
	response = []
	html = []
	soup = []
	team_order = []
	week = 0
	for each in espn_urls:
		site = espn_urls[week]
		response.append(urllib2.urlopen(site))
		html.append(response[week].read())
		only_H2_level = SoupStrainer('h2')
		soup.append( BeautifulSoup(html[week], 'html.parser', parse_only = only_H2_level))
		team_order.append(soup[week].find_all(string=TeamNames))
		for each in TeamSymbol:
			lst = ESPN_LstDict.get(each)
			indx = TeamDict.get(each)
			lst.append(team_order[week].index(indx)+1)
		week += 1
		if week == 2:
			print "Tightening the jock strap\n"
		elif week == 3:
			print "...\n"
		elif week == 4:
			print "Stretching out the glutes\n"
		elif week == 5:
			print "...\n"
		elif week == 6:
			print "Gameplanning the coin flip\n"
		elif week == 7:
			print "...\n"
		elif week == 8:
			print "Fly Eagles Fly!\n"
		elif week == 9:
			print "...\n"
		elif week == 10:
			print "Here we go!"

def get_rank(team_list, index):
	if ( index >= len(team_list) ):
		return 'N/A'
	else:
		return '#%s' % (team_list[index])

def print_weekly_rankings(team_list):
	for x in range(0, 17):
		print 'Week %s: %s' % (x + 1, get_rank(team_list, x))

def print_team_title(team_name):
	print 'ESPN ranked the %s as:' % (team_name)

def team_directory():
	SymKey = 0
	for each in TeamNames:
		print "Type %s for %s" % (TeamSymbol[SymKey], each)
		SymKey+=1

def run_espn_scraper():
	print '\nThis app lists ESPN experts\' rankings for the team of your choice.\n\nOne Moment while we stitch up our cleats and check ball pressure.\n'
	build_espn_rankings()
	req = True
	while req:
		user_choice = raw_input('\nEnter the 2-3 digit city code for your team.\nUnsure of your team\'s city code? Just type \'DIR\'\nWhen you\'re ready to exit simply enter \"XX\" ')
		user_choice = user_choice.upper()
		if ( len(user_choice) < 2 or len(user_choice) > 3):
			print 'You\'ve entered something a bit funky. Try again. If you\'d like to view a directory of team names enter \"DIR\" '
		elif user_choice == "XX":
			req = False
		elif user_choice == "DIR":
			team_directory()
		else:
			TeamList = ESPN_LstDict[user_choice]
			TeamName = TeamDict[user_choice]
			print_team_title(TeamName)
			print_weekly_rankings(TeamList)

run_espn_scraper()