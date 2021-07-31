from RiotAPI import RiotAPI
import RiotConsts as Consts

def main():
    api = RiotAPI('RGAPI-16de9793-ce12-43f6-85b7-bf5b84be4f8d')
    r = api.getSummonerByName('Legonerd666', Consts.REGIONS['north_america'])
    print(r)
    r2 = api.getMatchByPuuid(r['puuid'], Consts.REGIONS['americas'])
    print(r2)

if __name__ == "__main__":
    main()