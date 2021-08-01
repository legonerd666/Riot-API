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
    index = len(r3['info']['participants'])
    for i in r3['info']['participants']:
        if index == len(r3['info']['participants']):
            print('Blue Team:')
        elif index == len(r3['info']['participants']) / 2:
            print('Red Team:')
        print('    ' + str(i['summonerName']) + '\'s: \n        ' + str(i['championName']) + '\'s Kills: ' + str(i['kills']) + '\n')
        # r4 = api.getSummonerByPuuid(i['puuid'], Consts.REGIONS['north_america'])
        # print(r4)
        index -= 1
if __name__ == "__main__":
    main()