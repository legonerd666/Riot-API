import requests

def requestSummonerData(region, summoner_name, API_key):
    URL = "https://" + region + ".api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summoner_name + "?api_key=" + API_key
    response = requests.get(URL)
    return response.json()

