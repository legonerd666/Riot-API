import RiotConsts as Consts
import requests

class RiotAPI(object):
    
    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, region, params={}):
        self.region = region
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                url=api_url
            ),
            params=args
        )
        print(response.url)
        return response.json()

    def getSummonerByName(self, name, region):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url, region)

    def getSummonerByPuuid(self, puuid, region):
        api_url = Consts.URL['summoner_by_puuid'].format(
            version=Consts.API_VERSIONS['summoner'],
            puuid=puuid
        )
        return self._request(api_url, region)

    def getMatchIdByPuuid(self, puuid, region, start, count):
        if count > 100:
            count = 100

        elif count < 0:
            count = 0

        if start < 0:
            start = 0

        elif start > count - 1:
            start = count -1

        api_url = Consts.URL['match_id_by_puuid'].format(
            version=Consts.API_VERSIONS['match'],
            puuid=puuid,
            start=start,
            count=count
        )
        return self._request(api_url, region)

    def getMatchByMatchId(self, matchid, region):
        api_url = Consts.URL['match_by_matchid'].format(
            version=Consts.API_VERSIONS['match'],
            matchid=matchid
        )
        return self._request(api_url, region)