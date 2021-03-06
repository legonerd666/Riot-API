URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'match_id_by_puuid': 'match/v{version}/matches/by-puuid/{puuid}/ids?start={start}&count={count}',
    'match_by_matchid': 'match/v{version}/matches/{matchid}',
    'summoner_by_puuid': 'summoner/v{version}/summoners/by-puuid/{puuid}'
}
API_VERSIONS = {
    'summoner': '4',
    'match': '5'
}

REGIONS = {
    'north_america': 'na1',
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'americas': 'americas'
}