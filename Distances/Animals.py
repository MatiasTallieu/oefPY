import math
class Animals:
    def __init__(self):
        self. animal_data = {}
        self.location_data = {}
        self.unique_animals = set()
    # @property
    # def dictAnimals(self):
    #     return self.__dictAnimals
    
    # @dictAnimals.setter
    # def dictAnimals(self,val):
    #     self.__dictAnimals = self.read_animal_data("sample_animals.txt")

    def read_animal_data(self,file):
        animalDict = {}
        with open(f"C://Users/matia/Downloads/Examenopgaves/Distances/{file}",'r',encoding='utf-8') as File:
            Lines = File.readlines()
            for Line in Lines:
                keyVal_combination = Line.split(',')
                animalDict[keyVal_combination[0]] = keyVal_combination[1][:len(keyVal_combination[1])-1]
        self. animal_data = animalDict

    def  read_location_data(self,file):
        locationDict = {}
        with open(f"C://Users/matia/Downloads/Examenopgaves/Distances/{file}",'r',encoding='utf-8') as File:
            lines = File.readlines()
            #get uique names animals 
            unique_names= set()
            for Line in lines:
                values = Line.split(',')
                unique_names.add(values[1])

            for name in unique_names:
                locationDict[name] = []

            self.unique_animals = unique_names
            for line in lines:
                values = line.split(',')
                timeAndPos = (values[0],values[2],values[3][:len(values[3])-1])
                locationDict[values[1]].append(timeAndPos) 
                
        self.location_data = locationDict             

    def calculate_travelled_distance (self,distances):
        distance =0
        for i in range(len(distances)-1):
            x1 = int(distances[i][1])
            y1 = int(distances[i][2])

            x2 = int(distances[i+1][1])
            y2 = int(distances[i+1][2])

            distance+= self.__equationCalcDistance(x1,y1,x2,y2)     

        return distance

    def __equationCalcDistance(self,x1,y1,x2,y2):
        return(math.sqrt((math.pow((x2-x1),2)+math.pow((y2-y1),2)))) 

    def most_active_animal(self,location_data):
        nameAnimal = ''
        distance = 0.0
        for name in self.unique_animals:
          actualDistance =  self.calculate_travelled_distance(location_data[name])
          if(actualDistance>distance):
              distance = actualDistance
              nameAnimal = name 
        return (nameAnimal,distance)

    def most_lazy_animal(self,location_data):
        nameAnimal = ''
        distance = 10000
        for name in self.unique_animals:
          actualDistance =  self.calculate_travelled_distance(location_data[name])
          if(actualDistance<distance):
              distance = actualDistance
              nameAnimal = name 
        return (nameAnimal,distance)

    def flag_predator_prey_contact(self,location_data,animal_data):
        predatorSet ={'Lion','Tiger','Bear','Snake','Crocodile','Panther'}
        preySet = {'Elephant','Zebra','Giraffe','Monke','Cow'}
        ans =""
        
        #loops through all animals 
        for predator, typePredator in animal_data.items():

          if typePredator in predatorSet: 
                # if predator found loop on all animals again to find a prey
              for prey, preyType in animal_data.items():
                  if preyType in preySet:
                        # loop through all locations and get a predator, it has to be the same one as the previous one                   
                      for keyPredator, valPredator in location_data.items():
                         if keyPredator == predator:
                           # if found loop through the VALUE of dict location_data  of predator
                             for timePredaor, xPredator,yPredator in valPredator:
                                # loop through all locations and get a PREY , it has to be the same one as the previous one          
                                for keyprey, valprey in location_data.items():
                                    if keyprey == prey:
                                        # if found loop through the VALUE of dict location_data  of PRAY
                                        for timeprey, xprey,yprey in valprey:
                                                d = self.__equationCalcDistance(int(xPredator),int(yPredator),int(xprey),int(yprey))
                                                # PRAY and predator need to be on the same time at a distance of less dan 2km
                                                if(timeprey == timePredaor and d<2 ):
                                                    ans+=f'Time {timePredaor}, {predator} ({typePredator}), {prey} ({preyType}), Distance {round(d,2)}\n'                                     

        
        with open(f"C://Users/matia/Downloads/Examenopgaves/Distances/contactsTest.txt" ,'w+',encoding='utf-8') as File:
            File.writelines(ans)





animal = Animals()
animal.read_animal_data("animals.txt")
animal.read_location_data("locations.txt")
# print(animal.location_data)


most_active, active_distance = animal.most_active_animal(animal.location_data)
print(f"Most active animal: {most_active} with distance {active_distance:.2f}")

most_lazy, lazy_distance = animal.most_lazy_animal(animal.location_data)
print(f"Most lazy animal: {most_lazy} with distance {lazy_distance:.2f}")


print(animal.flag_predator_prey_contact(animal.location_data, animal. animal_data))