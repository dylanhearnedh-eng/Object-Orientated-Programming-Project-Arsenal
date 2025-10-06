#OOP practice with Arsenal 25/26 squad

class Team():

    team = 'Arsenal' #not def so can be used accross all classes

    def __init__(self):
        self.starting_11 = []

    def add_player(self, starter):
        self.starting_11.append(starter)

    def print_all(self):
        return(f'TEAM: {Team.team}')


class Person(Team): #this will be the base class
    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def print_all(self):
        print('FIRST NAME:',self.first_name)
        print('SURNAME:',self.surname)
        print('AGE:',self.age)
        print('TEAM',Team.team)


class Manager(Person): #inheritance can be linked down the generations, here it goes Vehcile - Motor - Car
    def __init__(self,first_name,surname,age,formation):
        super().__init__(first_name,surname,age)
        self.formation = formation

    def display_manager(self):
        return (f'MANAGER \nNAME: {self.first_name} {self.surname} \nAGE: {self.age} \nTEAM: {self.team} \nFORMATION: {self.formation}')
    def display_manager_prematch(self):
        return (f'MANAGER: {self.first_name} {self.surname} \nFORMATION: {self.formation}')

class Player(Person): #child class

    def __init__(self,first_name,surname,age,position,squad_number):
        super().__init__(first_name,surname,age) #this is how you link the parent to the child class
        self.position = position
        self.squad_number = squad_number

    def display_player(self):
        return (f'PLAYER \nNAME: {self.first_name} {self.surname} \nAGE: {self.age} \nTEAM: {self.team} \nPOSITION: {self.position} \nSQUAD NUMBER: {self.squad_number}')


    def shoot(self):
        return (f'{self.surname} Shoots')
    def forward_pass(self):
        return (f'{self.surname} Passes the ball forward')
    def back_pass(self):
        return (f'{self.surname} Makes a tackle')
    def clear(self):
        return (f'{self.surname} Kicks the ball out for a corner')
    def save(self):
        return (f'{self.surname} Makes an important save')

#teams
team = Team()

#managers
manager = Manager('Mikel','Arteta', 43,'4-3-3')

#list of players
calafiori = Player('Ricciardo','Calafiori',23,'LB',33) 
timber = Player('Jurrien','Timber',24,'RB',12)
raya = Player('David','Raya',29,'GK',1)
mosquera = Player('Cristhian','Mosquera',21,'CB',3)
hincapie = Player('Piero','Hincapié',25,'CB',5)
saliba = Player('William','Saliba',24,'CB',2)
gabriel = Player('Gabriel','Magalhães',27,'CB',6)
white = Player('Ben','White',27,'RB',4)
rice = Player('Declan','Rice',26,'CM',41)
odegaard = Player('Martin','Ødegaard',26,'CM',8)
zubimendi = Player('Martín','Zubimendi',26,'CM',36)
norgaard = Player('Christian','Nørgaard',31,'CDM',16)
merino = Player('Mikel','Merino',29,'CM',23)
saka = Player('Bukayo','Saka',24,'RW',7)
martinelli = Player('Gabriel','Martinelli',24,'LW',11)
gyokeres = Player('Viktor','Gyökeres',27,'ST',14)
madueke = Player('Noni','Madueke',23,'RW/LW',20)
havertz = Player('Kai','Havertz',26,'CF',29)
eze = Player('Eberechi','Eze',27,'LW',10)
trossard = Player('Leandro','Trossard',30,'FW',19)


squad = [1,33,2,6,12,41,36,8,10,14,7]
bench = [11,3,5,4,16,23,20,29,19]


team.add_player(raya)
team.add_player(calafiori)
team.add_player(saliba)
team.add_player(gabriel)
team.add_player(timber)
team.add_player(rice)
team.add_player(zubimendi)
team.add_player(odegaard)
team.add_player(eze)
team.add_player(gyokeres)
team.add_player(saka)
team.add_player(martinelli)
team.add_player(mosquera)
team.add_player(hincapie)
team.add_player(white)
team.add_player(norgaard)
team.add_player(merino)
team.add_player(madueke)
team.add_player(havertz)
team.add_player(trossard)


print(saka.shoot())
print(raya.save())
print(saka.display_player())



print ('\n')
print (team.print_all())
print (manager.display_manager_prematch())

#subsitution
#here we can sub players off and on

squad.remove(14)
squad.append(29)
bench.remove(29)
bench.append(14)

#ensures that only 11 players are on the pitch at the same time
if len(squad) != 11:
    raise ValueError('THE TEAM MUST HAVE 11 PLAYERS TO START THE MATCH')

print ('\nStarting 11')
for starter in team.starting_11: #look iterated through the list of players and adds them
    if starter.squad_number in squad: #adds them to the squad list if their number is on the list
        print (f'{starter.squad_number}: {starter.first_name} {starter.surname}: {starter.position}')
    else:
        pass #skips them if not


print ('\nBench')
for starter in team.starting_11: #look iterated through the list of players and adds them
    if starter.squad_number in bench: #adds them to the bench list if their number is on the list
        print(f'{starter.squad_number}: {starter.first_name} {starter.surname}: {starter.position}')
    else:
        pass
#update for/if loop to add starters to 1 list and bench players to another
#need to update attributes to state that some are starters and other are bench
print('\n')
print (f'    GK    \n' \
'LB CB CB RB\n' \
' CM CM CM \n' \
' LW ST RW \n')

