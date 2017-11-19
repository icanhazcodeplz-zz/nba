import sys
import json
import requests
from datetime import datetime, timedelta

args = sys.argv
if len(args) > 1:
    TEAM_TRI_CODE = args[1]
else:
    TEAM_TRI_CODE = 'GSW'

TODAY = datetime.today()
URL_NO_DATE = 'https://data.nba.net/prod/v2/{}/scoreboard.json'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('http://stats.nba.com'),
    'referer': ('http://stats.nba.com/scores/')
    }


def did_we_win(parsed, tri_code):
    for game in parsed:
        v_team = game['vTeam']
        h_team = game['hTeam']
        v_team_score = v_team['score']
        h_team_score = h_team['score']
        v_team_tri_code = v_team['triCode']
        h_team_tri_code = h_team['triCode']
        if v_team_tri_code == tri_code or h_team_tri_code == tri_code:
            h_team_wins = h_team_score > v_team_score
            if h_team_wins:
                return '{} beat {}'.format(h_team_tri_code, v_team_tri_code)
            else:
                return '{} beat {}'.format(v_team_tri_code, h_team_tri_code)

def get_scoreboard(tri_code='GSW'):
    for days_back in range(1, 4):
        date_str = (TODAY - timedelta(days=days_back)).strftime('%Y%m%d')
        url = URL_NO_DATE.format(date_str)
        print('GET {}'.format(url))
        response = requests.get(url, headers=HEADERS)
        parsed = json.loads(response.text)['games']
        result = did_we_win(parsed, tri_code)
        if result is not None:
            return result


print(get_scoreboard(TEAM_TRI_CODE))

