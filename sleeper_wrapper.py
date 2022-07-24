from site import getuserbase
from datetime import date
import requests
import json


def get_user(username):
    getUser = username
    url = f"https://api.sleeper.app/v1/user/{getUser}"
    response = requests.get(url).json()
    userName = response['username']
    userID = response['user_id']
    avatarID = response['avatar']
    print(response)
    print(f"\nUserName: {response['username']}, UserID: {response['user_id']}, Avatar: {response['avatar']}")
    return userID

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
    leagues = {}
    for responses in response: 
        leagues[responses['name']] = responses['league_id']
    return leagues

def get_league(leagueID):
    url = f"https://api.sleeper.app/v1/league/{leagueID}"
    response = requests.get(url).json()
    print(response['name'])

def get_roster(leagueID):
    #league = leagueID
    url = f"https://api.sleeper.app/v1/league/{leagueID}/rosters"
    response = requests.get(url).json()
    rosters = {}
    starters = {}
    for responses in response:
        rosters[responses['owner_id']] = responses['players']
        starters[responses['owner_id']] = responses['starters']
    return rosters, starters

def get_finalroster(players, owner):
    roster = players
    owner = owner
    filename = 'player_list.txt'
    with open(filename, 'r') as file_object:
        data = json.load(file_object) 
    translated_roster = {}
    for items in roster[owner]:
        translated_roster[items] = data[items][0], data[items][1]
    print("Player List: \n")
    for items in translated_roster: 
        print(f"{translated_roster[items][0]} {translated_roster[items][1]}")


def create_playerdict():
    filename = 'master_player_list.json' 
    filename_curated = 'player_list.txt'
    player_dict = {}
    with open(filename) as file_object: 
        data = json.load(file_object)
    for items in data:
        key = items
        firstname = data[items]['first_name']
        lastname = data[items]['last_name']
        player_dict[key] = firstname, lastname
    with open(filename_curated, 'w') as file_object: 
        file_object.write(json.dumps(player_dict))



def update_playermaster():
    filename = 'master_player_list.json'
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url).json()
    with open(filename, 'w') as file_object: 
        file_object.write(json.dumps(response))

#Main part of the program
message = input("Please input your Sleeper Username: ")
userID = get_user(message)
leagues = get_leagues(userID)
print(leagues)
for items in leagues:
    if leagues[items] != None:
        print(leagues[items]) 
        roster, starters = get_roster(str(leagues[items]))
        print(roster)
        print(roster[userID])
        get_finalroster(roster[userID], userID)
    else: 
        print(f"{leagues[items]} has not drafted yet.")