import requests
from bs4 import BeautifulSoup

URL = "https://www.premierleague.com/stats/top/players/goals"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

player_names = soup.find_all(name="a", class_='playerName')
player_name = []
for names in player_names:
    player_name_ = names.getText().strip()
    player_name.append(player_name_)

goals = soup.find_all(name='td', class_='stats-table__main-stat')
player_goals = []
for goals in goals:
    player_goals_ = goals.getText().strip()
    player_goals.append(player_goals_)

clubs = soup.find_all(name='a', class_='stats-table__cell-icon-align')
player_clubs = []
for clubs in clubs:
    player_clubs_ = clubs.getText().strip()
    player_clubs.append(player_clubs_)

nationalities =  soup.find_all(name='div', class_='stats-table__cell-icon-align')
player_nationalities = []

for nation in nationalities:
    player_nationalities_ = nation.getText().strip()
    player_nationalities.append(player_nationalities_)
print(player_name)
print(player_goals)
print(player_clubs)
print(player_nationalities)

with open("player_stats.txt", "w") as file:
    for i in range(len(player_name)):
        file.write(f"Name: {player_name[i]}, Goals: {player_goals[i]}, Club: {player_clubs[i]}, Nationality: {player_nationalities[i]}\n")