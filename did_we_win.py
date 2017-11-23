import sys
import json
import requests
from datetime import datetime, timedelta

ARGS = sys.argv
if len(ARGS) > 1:
    TEAM_TRI_CODE = ARGS[1].upper()
else:
    TEAM_TRI_CODE = 'GSW'

if len(ARGS) > 2:
    DAYS_AGO = int(ARGS[2])
else:
    DAYS_AGO = 1


TODAY = datetime.today()
URL_NO_DATE = 'https://data.nba.net/prod/v2/{}/scoreboard.json'
HEADERS = {
    'Accept-Encoding': ('gzip, deflate, br'),
    'Accept-Language': ('en-US,en'),
    'Host': ('data.nba.net'),
    'Upgrade-Insecure-Requests': ('1'),
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'),
    }


def did_we_win(parsed):
    for game in parsed:
        v_team = game['vTeam']
        h_team = game['hTeam']
        v_team_score = int(v_team['score'])
        h_team_score = int(h_team['score'])
        v_team_tri_code = v_team['triCode']
        h_team_tri_code = h_team['triCode']
        if v_team_tri_code == TEAM_TRI_CODE or h_team_tri_code == TEAM_TRI_CODE:
            if h_team_score != '':
                h_team_wins = h_team_score > v_team_score
                if h_team_wins:
                    return '{} beat {} at {}'.format(h_team_tri_code, v_team_tri_code, h_team_tri_code)
                else:
                    return '{} beat {} at {}'.format(v_team_tri_code, h_team_tri_code, h_team_tri_code)

def get_scoreboard():
    for days_back in range(DAYS_AGO, DAYS_AGO + 2):
        date_str = (TODAY - timedelta(days=days_back)).strftime('%Y%m%d')
        url = URL_NO_DATE.format(date_str)
        print('GET {}'.format(url))
        response = requests.get(url, headers=HEADERS, timeout=1)
        parsed = json.loads(response.text)['games']
        result = did_we_win(parsed)
        if result is not None:
            return result


print(get_scoreboard())

