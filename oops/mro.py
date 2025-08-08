class Aclass:
    label = "A: Base class"
    
class Bclass(Aclass):
    label = "B: inherited class"
    
class Cclass(Aclass):
    label = "C: inherited class"
    
class Dclass(Bclass,Cclass):
    pass

cup = Dclass()
print(cup.label)
