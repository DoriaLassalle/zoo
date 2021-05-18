class Animal:

    def __init__(self, name, age, health, happyness):
        self.name=name
        self.age=age       
        self.health=health
        self.happyness=happyness        

    def display_animal_info(self):
        print(f"Nombre: {self.name}\nEdad:{self.age}\nEstado de Salud: {self.health}\nNivel de Felicidad: {self.happyness}\n")
        return self
        
    def feed(self):
        # metodo que aumente la salud y la felicidad en 10
        self.health+=10
        self.happyness+=10
        return self


class Tiger(Animal):

    def __init__(self, name, age, health=5, happyness=10 ):
        super().__init__(name, age, health, happyness)

    def display_animal_info(self):
        super().display_animal_info()
        return self
    
    def feed(self):
        super().feed()
        return self



class Wolf(Animal):

    def __init__(self, name, age, health=2, happyness=8):
        super().__init__(name, age, health, happyness)

    def display_animal_info(self):
        super().display_animal_info()
        return self
    
    def feed(self):
        super().feed()
        return self


class Elephant(Animal):

    def __init__(self, name, age, health=10, happyness=18):
        super().__init__(name, age, health, happyness)

    def display_animal_info(self):
        super().display_animal_info()
        return self
    
    def feed(self):
        super().feed()
        return self


class Giraffe(Animal):

    def __init__(self, name, age, neck_size, health=15, happyness=20):
        super().__init__(name, age, health, happyness)
        self.neck_size=neck_size

    def display_animal_info(self):
        super().display_animal_info()
        return self
    
    def feed(self):
        super().feed()
        return self


# Creo animales
shiva=Tiger("shiva", 8)
shiva.feed().feed().feed()

lucian=Wolf("lucian", 6)
lucian.feed().feed().feed()

tantor=Elephant("tantor", 12)
tantor.feed()

fresia=Elephant("fresia", 21, )

melman=Giraffe("melman", 7, 5)


class Zoo:

    def __init__(self, zoo_name):
        self.animals=[]
        self.zoo_name=zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def display_zoo_animals(self):      
        print(f"\n*** En el {self.zoo_name} puedes visitar a los siguientes animales: ***\n")
        for animal in self.animals:
            print(f"* Nombre: {animal.name}, es un {animal.__class__.__name__} y tiene {animal.age} años,\n   tiene una salud de: {animal.health} y es {animal.happyness}mil % felíz :)")
        return self

# Agrego 2 zoologicos y agrego animales 
zoo1=Zoo("Buin Zoo")
zoo1.add_animal(lucian).add_animal(tantor)

zoo2=Zoo("San Diego Zoo")
zoo2.add_animal(shiva).add_animal(melman).add_animal(fresia)


### Bonus ###
# Funcion interactiva
def visiting_zoo():
    while True:
        print(f"\n***  BIENVENID@ A LOS ZOOLOGICOS DE DORIA  ***")
        print("   *** ¿Cuál zoo quieres visitar? ***\n")
        zoo_option=input(f"1. {zoo1.zoo_name}\n2. {zoo2.zoo_name}\n\n")
        if zoo_option=="1":
            chosen_zoo=zoo1
        elif zoo_option=="2":
            chosen_zoo=zoo2
        elif zoo_option not in ["1", "2"]:
                print("Ooops...opción no válida!!")
                continue 
        
        print(f"** Estás en el  {chosen_zoo.zoo_name}!! **")
        print("  ¿Qué actividad deseas realizar?\n")
        activity=input("1. Ingresar un Animal\n2. Alimentar un animal\n3. Ver los Animales del zoo\n4. **Salir**\n")
        if activity =="4":
            print("*** HAS SALIDO DEL PROGRAMA ***")
            break         
        elif activity not in ["1", "2", "3"]:
            print("Ooops...opción no válida!!")
            continue 

        if activity=="1":           
            print(f"\n** Elije qué tipo de animal deseas ingresar al {chosen_zoo.zoo_name}: **\n")
            option=input("1. Tiger\n2. Wolf\n3. Elephant\n4. Giraffe\n5. **Salir**\n")
            if option =="5":
                print("*** HAS SALIDO DEL PROGRAMA ***")
                break         
            elif option not in ["1", "2", "3", "4"]:
                print("Ooops...opción no válida!!")
                continue  

            animal_name=input("Ingresa el nombre del animal:\n")
            animal_age=input("Ingresa la edad del animal:\n")                                         

            if option =="1":
                animal_name=Tiger(animal_name, animal_age)
            elif option =="2":
                animal_name=Wolf(animal_name, animal_age)
            elif option =="3":
                animal_name=Elephant(animal_name, animal_age)
            else:
                animal_neck=input("Ingrese el largo del cuello de su jirafa:\n")
                animal_name=Giraffe(animal_name, animal_age, animal_neck)

            chosen_zoo.add_animal(animal_name)
            print("\n*** HAS INGRESADO EXITOSAMENTE UN ANIMAL!! ***/\n")
            print(f"** El {chosen_zoo.zoo_name} le da la bienvenida a: {animal_name.name} **")
            print("*** Gracias por confiar en nosotros!! ***")

        elif activity=="2":
            print("** ¿A quién quieres alimentar para hacerlo más feliz? **\n")
            for anim in chosen_zoo.animals:
                print(f"- {anim.name}, su felicidad está en: {anim.happyness}")
            print("")    
            to_feed=input("Ingresa el nombre: \n")
            for animalito in chosen_zoo.animals:
                if to_feed==animalito.name:
                    animalito.feed()
                    print(f"***** Gracias!!! *****\nLa felicidad de {animalito.name} ahora esta en {animalito.happyness} :)")

        else:
            chosen_zoo.display_zoo_animals()


    print("Tu visita por el zoológico ha terminado, see you soon!!")
        

if __name__ == '__main__':
    visiting_zoo()

# END
