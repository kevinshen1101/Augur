from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

def getPlayerData(player_url):
	#URL of player info for 2017-2018 season
	player_page = urlopen(player_url)

	#Load page into BeautifulSoup
	soup = BeautifulSoup(player_page, 'html.parser')

	#Get main table
	table = soup.find_all("tbody")

	#Parse into rows
	rows = table[0].find_all("tr")

	d = {'Reason': [], 'Index': [], 'Date': [], 'Age': [], 'Team': [], 'Opponent': [],
		 'Result': [], 'Starter': [], 'Minutes Played': [], 'Made Field Goals': [],
		 'Attempts': [], 'Field Goal Percentage': [], 'Made Threes': [], 
		 'Attempted Threes': [], 'Three Percentage': [], 'Made Free Throws': [],
		 'Free Throw Attempts': [], 'Free Throw Percentage': [], 'Offensive Rebounds': [],
		 'Defensive Rebounds': [], 'Total Rebounds': [], 'Assists': [], 'Steals': [],
		 'Blocks': [], 'Turnovers': [], 'Fouls': [], 'Points': [], 'Game Score': [],
		 'Plus Minus': []
		}

	for i in rows:
		reason = i.find(attrs={"data-stat": "reason"})
		index = i.find(attrs={"data-stat": "ranker"}).get_text()
		d['Index'].append(index)
		date = i.find(attrs={"data-stat": "date_game"}).get_text()
		d['Date'].append(date)
		age = i.find(attrs={"data-stat": "age"}).get_text()
		d['Age'].append(age)

		team = i.find(attrs={"data-stat": "team_id"}).get_text()
		d['Team'].append(team)
		opponent = i.find(attrs={"data-stat": "opp_id"}).get_text()
		d['Opponent'].append(opponent)
		result = i.find(attrs={"data-stat": "game_result"}).get_text()
		d['Result'].append(result)

		if reason is None:
			d['Reason'].append(None)
			starter = i.find(attrs={"data-stat": "gs"}).get_text()
			d['Starter'].append(bool(starter))
			minutes_played = i.find(attrs={"data-stat": "mp"}).get_text()
			d['Minutes Played'].append(minutes_played)

			made_fgs = i.find(attrs={"data-stat": "fg"}).get_text()
			d['Made Field Goals'].append(made_fgs)
			attempts = i.find(attrs={"data-stat": "fga"}).get_text()
			d['Attempts'].append(attempts)
			fg_pct = i.find(attrs={"data-stat": "fg_pct"}).get_text()
			d['Field Goal Percentage'].append(fg_pct)

			three = i.find(attrs={"data-stat": "fg3"}).get_text()
			d['Made Threes'].append(three)
			att_three = i.find(attrs={"data-stat": "fg3a"}).get_text()
			d['Attempted Threes'].append(att_three)
			perc_three = i.find(attrs={"data-stat": "fg3_pct"}).get_text()
			d['Three Percentage'].append(perc_three)

			ft = i.find(attrs={"data-stat": "ft"}).get_text()
			d['Made Free Throws'].append(ft)
			fta = i.find(attrs={"data-stat": "fta"}).get_text()
			d['Free Throw Attempts'].append(fta)
			ft_pct = i.find(attrs={"data-stat": "ft_pct"}).get_text()
			d['Free Throw Percentage'].append(ft_pct)

			o_reb = i.find(attrs={"data-stat": "orb"}).get_text()
			d['Offensive Rebounds'].append(o_reb)
			d_reb = i.find(attrs={"data-stat": "drb"}).get_text()
			d['Defensive Rebounds'].append(d_reb)
			tot_reb = i.find(attrs={"data-stat": "trb"}).get_text()
			d['Total Rebounds'].append(tot_reb)

			assists = i.find(attrs={"data-stat": "ast"}).get_text()
			d['Assists'].append(assists)
			steals = i.find(attrs={"data-stat": "stl"}).get_text()
			d['Steals'].append(steals)
			blocks = i.find(attrs={"data-stat": "blk"}).get_text()
			d['Blocks'].append(blocks)
			turnovers = i.find(attrs={"data-stat": "tov"}).get_text()
			d['Turnovers'].append(turnovers)
			fouls = i.find(attrs={"data-stat": "pf"}).get_text()
			d['Fouls'].append(fouls)
			points = i.find(attrs={"data-stat": "pts"}).get_text()
			d['Points'].append(points)
			game_score = i.find(attrs={"data-stat": "game_score"}).get_text()
			d['Game Score'].append(game_score)
			plus_minus = i.find(attrs={"data-stat": "plus_minus"}).get_text()
			d['Plus Minus'].append(plus_minus)

		else:
			d['Reason'].append(reason.get_text())
			d['Starter'].append(None)
			d['Minutes Played'].append(None)

			d['Made Field Goals'].append(None)
			d['Attempts'].append(None)
			d['Field Goal Percentage'].append(None)

			d['Made Threes'].append(None)
			d['Attempted Threes'].append(None)
			d['Three Percentage'].append(None)

			d['Made Free Throws'].append(None)
			d['Free Throw Attempts'].append(None)
			d['Free Throw Percentage'].append(None)

			d['Offensive Rebounds'].append(None)
			d['Defensive Rebounds'].append(None)
			d['Total Rebounds'].append(None)

			d['Assists'].append(None)
			d['Steals'].append(None)
			d['Blocks'].append(None)
			d['Turnovers'].append(None)
			d['Fouls'].append(None)
			d['Points'].append(None)
			d['Game Score'].append(None)
			d['Plus Minus'].append(None)

	return pd.DataFrame(d)

def getTeamData():
	#URL of team info for 2017-2018 season
	nba_page = urlopen('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1')

	#Load page into BeautifulSoup
	soup = BeautifulSoup(nba_page, 'html.parser')

	table = soup.find_all('tbody')
	print(table)



#getTeamData()
player_page = 'https://www.basketball-reference.com/players/d/duranke01/gamelog/2018/'
table = getPlayerData(player_page)
print(table)
