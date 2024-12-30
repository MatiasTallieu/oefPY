
class Player():
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.__fga = 0
        self.__fgm =0
        self.__fta =0
        self.__ftm =0
        self.__pa =0
        self.__pm =0
        self.__asp =0
        self.__rb =0
        self.statistics = {
              'FGA':0,
              'FGM' :0 ,
               'FTA':0 ,
               'FTM' :0,
               '3PA' :0 ,
               '3PM' :0 ,
               'AS' :0,
               'RB' :0,
        }

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,val):
        if(isinstance(val,str)):
            self.__name = val
        else:
            raise ValueError('Not a string')

    @property
    def fga(self):
        return self.__fga
    
    @fga.setter
    def fga(self,val):
        self.__fga +=val
    
    @property
    def fgm(self):
        return self.__fgm
    
    @fgm.setter
    def fgm(self,val):
        self.__fgm +=val
    
    @property
    def fta(self):
        return self.__fta
    
    @fta.setter
    def fta(self,val):
        self.__fta +=val
    
    @property
    def ftm(self):
        return self.__ftm
    
    @fta.setter
    def ftm(self,val):
        self.__ftm +=val

    @property
    def pa(self):
        return self.__pa
    
    @pa.setter
    def pa(self,val):
        self.__pa +=val
    
    @property
    def pm(self):
        return self.__pm
    
    @pm.setter
    def pm(self,val):
        self.__pm +=val
    
    @property
    def asp(self):
        return self.__asp
    
    @asp.setter
    def asp(self,val):
        self.__asp +=val
    
    @property
    def rb(self):
        return self.__rb
    
    @rb.setter
    def rb(self,val):
        self.__rb +=val


    def add_FG(self,val):
        self.__fga +=1
        if val =="Scored":
            self.__fgm+=1
        self.updateStats()

    def add_FT(self,val):
        self.__fta +=1
        if val =="Scored":
            self.__ftm+=1
        self.updateStats()
    
    def add_P(self,val):
        self.__pa +=1
        if val =="Scored":
            self.__pm+=1
        self.updateStats()
    
    def add_AS(self):
        self.__asp +=1

    def add_RB(self):
        self.__rb +=1


    def updateStats(self):
        self.statistics['FGA'] = self.__fga
        self.statistics['FGM'] = self.__fgm
        self.statistics['FTA'] = self.__fta
        self.statistics['FTM'] = self.__ftm
        self.statistics['3PA'] = self.__pa
        self.statistics['3PM'] = self.__pm
        self.statistics['AS'] = self.__asp
        self.statistics['RB'] = self.__rb



p1= Player("Matias",10)
stats = p1.statistics
p1.add_FG("Scored")
print(p1.name)

print(stats['FGA'])
    