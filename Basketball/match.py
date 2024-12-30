from team import *

class Match():
    def __init__(self):
        self.teamList = []
        self.team1 = ""
        self.team2 = ""

    def read_match_data_file(self,pad):
        with open(pad,'r',encoding='utf-8') as file:
            lines= file.readlines()
            teams_made = 0
            for i in range(len(lines)):
                words = lines[i].split()
                if words[0] =="Team":
                    teams_made+=1
                    if(teams_made>=2):
                        self.teamList.append(team)
                        self.team1 = team
                    ##make team
                    name = ''
                    for i in range(2,len(words)-1):
                        name+=words[i]+ ' '
                    abre = words[len(words)-1]
                    team = Team(name[:len(name)-3],abre)
                
                else:
                    ### player
                    number = words[0][1:]
                    name = f'{words[2]} {words[3]}'
                    team.add_player(name,number)
                    self.team2 = team

            #add last team
            self.teamList.append(team)


    def get_team(self,ab):
        for team in self.teamList:
            if(team.abbreviation == ab):
                return team


    def read_match_statistics_file(self,adres):
        with open(adres,'r',encoding='utf-8') as File:
            lines = File.readlines()
            for line in lines:
                words = line.split(',')
                abre =words[0] 
                myTeam = self.get_team(abre)
                myPlayer = myTeam.get_player(words[1][1:])
                option = words[2].strip()
                if(len(words) == 3):
              
                    if(option == 'RB'):
                        myPlayer.add_RB()
                    elif(option =='AS'):
                         myPlayer.add_AS()
                else:
                    if(option == '3P'):
                        myPlayer.add_P(words[3].strip())
                    elif(option == 'FG'):
                        myPlayer.add_FG(words[3].strip())
                    elif(option == 'FT'):
                        myPlayer.add_FT(words[3].strip())

    def display_match(self):

        teamAns1 = self.display_for_team(self.team1)
        teamAns2 = self.display_for_team(self.team2)
        with open("C://Users/matia/Downloads/Examenopgaves/Basketball/output.txt",'w',encoding='utf-8') as File:
            File.write(f'{teamAns1} \n{teamAns2}' )
    

    def display_for_team(slef,team):
        lijn ='-'
        ans = f'{lijn*90}\n'
        ans+= f'| {str.ljust(team.name,87)} |' + '\n'
        ans += f'{lijn*90}\n'
        ans+= f"| NBR | {str.ljust('Name',32)} | FGA | FGM | 3PA | 3MP | FTA | FTM | AS | RB |" + '\n'
        for player in team.players:
            ans+= f'|  {str.ljust(str(player.number),3)}| {str.ljust(player.name,32)} | {str.ljust(str(player.fga),3)} | {str.ljust(str(player.fgm),3)} | {str.ljust(str(player.pa),3)} | {str.ljust(str(player.pm),3)} | {str.ljust(str(player.fta),3)} | {str.ljust(str(player.ftm),3)} | {str.ljust(str(player.asp),3)}| {str.ljust(str(player.rb),2)} | \n'

        return ans
    
    


match = Match()
match.read_match_data_file("C://Users/matia/Downloads/Examenopgaves/Basketball/match_data.txt")
match.read_match_statistics_file("C://Users/matia/Downloads/Examenopgaves/Basketball/match_statistics.txt")
print(match.display_match())
