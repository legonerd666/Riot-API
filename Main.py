from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-16de9793-ce12-43f6-85b7-bf5b84be4f8d')
    r = api.getSummonerByName('Legonerd666')
    print(r)

if __name__ == "__main__":
    main()