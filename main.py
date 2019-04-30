import requests
import json
import datetime

id_list = {
    '241221633': '@TheOriginMS7',
    '68019342': 'Matt',
    '402638282': 'Петр',
    '122776092': '@PavlyukYurko',
    '252842952': 'RoflanDoge'
}

requestS = []
players = []
recent_match = []


def openDoto():
    for i in id_list:
        data = request(i)
        players.append(data)
        recent_match.append(recent_matches(str(data['profile']['account_id']))[0])


def request(player_id):
    url = 'https://api.opendota.com/api/players/' + player_id
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def recent_matches(player_id):
    url = 'https://api.opendota.com/api/players/' + player_id + '/recentMatches'
    response = requests.get(url)
    raw = json.loads(response.text)
    return raw


def detailed_match_stats(match_id):
    url = 'https://api.opendota.com/api/matches/' + match_id
    response = requests.get(url)
    res = json.loads(response.text)
    return res


# def check_party(match):
#     is_party = False
#     for game in recent_match:
#         if game['party_size'] > 1:
#             is_party = True


def match_result(match):
    player_slot = match['player_slot']
    radiant_win = match['radiant_win']
    result = False
    if player_slot < 128 and radiant_win:
        result = True
    elif player_slot > 127 and not radiant_win:
        result = True

    return result


def match_timestats(match):
    duration = match['duration'] / 60
    current_time = datetime.datetime.now()
    match_time = datetime.datetime.fromtimestamp(int(match['start_time']))
    start_time = (current_time - match_time).seconds / 3600
    return start_time, duration


openDoto()

raw = recent_matches('241221633')
print(raw)
print(match_timestats(raw))
print(detailed_match_stats(str(recent_match[0]['match_id'])))
print(players)
print(recent_match)
