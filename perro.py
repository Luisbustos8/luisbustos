class Perro():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
          
    def ladrar(self):
        if self.weight >=8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")

    def __str__(self):
        return "Soy el perro {}, tengo {} años y peso {} kilos".format(self.name, self.age, self.weight)
    
class PerroAsistencia(Perro):
    def __init__(self, name, age, weight, owner):
        Perro.__init__(self, name, age, weight)
        self.owner = owner
        self.working = False
        
    def __str__(self):
        return "Soy el perro {}, tengo {} años, peso {} kilos y mi dueño es {}".format(self.name, self.age, self.weight, self.owner)
    
    def pasear(self):
        print("Soy {}, ayudo a mi dueño, {} a pasear".format(self.name, self.owner))
        
    def ladrar(self):
        if self.working:
            print("shhh,no puedo ladrar")
        else:
            Perro.ladrar(self)
            