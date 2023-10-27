from auto import Human
from auto import Auto
from auto import AutoType
from auto import HumanRole

humans = list()
studone = Human('studone', HumanRole.DRIVER)
studtwo = Human('studtwo', HumanRole.PASSENGER)
studthree = Human('studthree', HumanRole.PASSENGER)
studfour = Human('studfour', HumanRole.PASSENGER)
humans.append(studone)
humans.append(studtwo)
humans.append(studthree)
humans.append(studfour)

audi = Auto("etron", AutoType.CAR)
for human in humans:
    audi.AddPassengers(human)
    audi.AddDrivers(human)

'''
for driver in audi.Drivers:
    print(driver)
for passenger in audi.Passengers:
    print(passenger)
'''
print(audi)

''''''