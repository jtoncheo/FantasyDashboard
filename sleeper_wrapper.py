from site import getuserbase
from datetime import date
import requests
import json


def get_user(userID):
    getUser = userID
    url = f"https://api.sleeper.app/v1/user/{getUser}"
    response = requests.get(url).json()
    userName = response['username']
    userID = response['user_id']
    avatarID = response['avatar']
    print(response)
    print(f"\nUserName: {response['username']}, UserID: {response['user_id']}, Avatar: {response['avatar']}")

def get_avatar(avatarID):
    avatar = avatarID
    url = f"https://sleepercdn.com/avatars/thumbs/{avatar}"
    print(url)

def get_leagues(userID):
    user = userID 
    season = date.today().year
    sport = 'nfl'
    url = f"https://api.sleeper.app/v1/user/{user}/leagues/{sport}/{season}"
    response = requests.get(url).json()
    leagues = []
    leagueID = []
    for responses in response: 
        leagues.append(responses['name'])
        leagueID.append(response['league_id'])
    print(leagues)
    print(leagueID)

def get_league(leagueID):
    url = f"https://api.sleeper.app/v1/league/{leagueID}"
    response = requests.get(url).json()
    print(response['name'])

def update_players():
    filename = 'master_player_list.txt'
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url).json()
    with open(filename, 'w') as file_object: 
        file_object.write(json.dumps(response))
#Main part of the program

# message = input("Please input your Sleeper Username: ")
# get_user(message)
# get_leagues('470327246519791616')
# get_league()