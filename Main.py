from RiotAPI import RiotAPI
import RiotConsts as Consts

def main():
    api_file = open("../../API_Key.txt", 'r')
    api = RiotAPI(api_file.read())
    api_file.close()
    r = api.getSummonerByName('Legonerd666', Consts.REGIONS['north_america'])
    print(r)
    r2 = api.getMatchIdByPuuid(r['puuid'], Consts.REGIONS['americas'], 0, 1)
    print(r2)
    r3 = api.getMatchByMatchId(r2[0], Consts.REGIONS['americas'])
    print(r3)

if __name__ == "__main__":
    main()