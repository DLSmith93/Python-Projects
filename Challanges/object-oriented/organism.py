
class Organism:
    name = "null"
    species = "null"
    legs = None
    arms = None
    DNA = "sequanceA"
    origin = "null"
    carbon_based = True

    def information(self):
        msg = "\nName: {} \nSpecies: {} \nLegs: {} \nArms: {} \nDNA: {} \nOrigin: {} \nCarbon Based: {}"\
            .format(self.name, self.species, self.legs, self.arms, self.DNA, self.origin, self.carbon_based)
        return msg

class Human(Organism):
    name = "MacGuyvar"
    species = "Homosapian"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreates deadly weapons of mundane objects"
        return msg
    
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    DNA = "sequanceB"
    origin = "Earth"

    def bite(self):
        msg = "\nThe dog barks loudly before biting powerfully!"
        return msg
    
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    DNA = "sequenceC"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply"
        return msg

if __name__ == "__main__":

    human = Human()
    print(human.information())
    print(human.ingenuity())