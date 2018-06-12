from io import open
import pickle


class Character:

    def __init__(self, name, life_points, attack, defense, arms_range):
        self.name = name
        self.life_points = life_points
        self.attack = attack
        self.defense = defense
        self.arms_range = arms_range

    def __str__(self):
        return "{} => {} life points, {} attack, {} defense, {} arms range".format(self.name, self.life_points,
                                                                                   self.attack,
                                                                                   self.defense, self.arms_range)


class Manager:
    characters = []

    def __init__(self):
        self.load()

    def add(self, p):
        for pTemp in self.characters:
            if pTemp.name == p.name:
                return
        self.characters.append(p)
        self.save()

    def delete(self, name):
        for pTemp in self.characters:
            if pTemp.name == name:
                self.characters.remove(pTemp)
                self.save()
                print("\nCharacter {} deleted".format(name))
                return

    def show(self):
        if len(self.characters) == 0:
            print("The manager is empty")
            return
        for p in self.characters:
            print(p)

    def load(self):
        file = open('characters.pckl', 'ab+')
        file.seek(0)
        try:
            self.characters = pickle.load(file)
        # except:
        #     # print("El fichero está vacío")
        #     pass
        finally:
            file.close()
            print("{} characters have been loaded.".format(len(self.characters)))

    def save(self):
        file = open('characters.pckl', 'wb')
        pickle.dump(self.characters, file)
        file.close()


G = Manager()
G.agregar(Character("Knight", 4, 2, 4, 2))
G.agregar(Character("Fighter", 2, 4, 2, 4))
G.agregar(Character("Archer", 2, 4, 1, 8))
G.show()
