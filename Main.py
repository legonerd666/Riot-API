from RiotAPI import RiotAPI
import RiotConsts as Consts
from tkinter import *


root = Tk()
root.title('API App')
kills_label = Label(root)

def main():

    def checkKills():
        api_file = open("../../API_Key.txt", 'r')
        api = RiotAPI(api_file.read())
        api_file.close()
        if region_field.get() == '1':
            region = 'north_america'
            r = api.getSummonerByName(username_field.get(), Consts.REGIONS[region])
            print(r)
            match_region = 'americas'
            r2 = api.getMatchIdByPuuid(r['puuid'], Consts.REGIONS[match_region], 0, 1)
            print(r2)
            r3 = api.getMatchByMatchId(r2[0], Consts.REGIONS[match_region])
            index = len(r3['info']['participants'])
            for i in r3['info']['participants']:
                if index == len(r3['info']['participants']):
                    print('Blue Team:')
                elif index == len(r3['info']['participants']) / 2:
                    print('Red Team:')
                print('    ' + str(i['summonerName']) + '\'s: \n        ' + str(i['championName']) + '\'s Kills: ' + str(i['kills']) + '\n')

                if i['summonerName'] == username_field.get():
                    global kills_label
                    kills_label.destroy()
                    kills_label = Label(root, text='Your Kills as ' + str(i['championName']) + ' were: ' + str(i['kills']))
                    kills_label.grid(row=5, column=0)
                index -= 1


        else:
            print('Enter Valid region number')

    #Creates the intro text
    intro_text = Label(root, text="Check the kills from your most recent league match!")
    intro_text.grid(row=0, column=0)

    #Asks for a Username
    username_field_label = Label(root, text='Username:')
    username_field_label.grid(row=1, column=0)

    username_field = Entry(root)
    username_field.grid(row=1, column=1)

    #Asks for Region
    region_field_label = Label(root, text='Region Number:')
    region_field_label.grid(row=2, column=0)

    region_field = Entry(root)
    region_field.grid(row=2, column=1)

    regions = Label(root, text='Regions:\n1. North America')
    regions.grid(row=3, column=1)

    #Sends in data
    input_user_data_button = Button(root, text='Check my Kills!', command=checkKills)
    input_user_data_button.grid(row=4, column=0)

    root.mainloop()

if __name__ == "__main__":
    main()