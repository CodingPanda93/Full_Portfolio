class Animal(object)
  def __init__(self, name, health):
    self.name=name
    self.health = 100

  def walk(self):
    self.health -= 1
    return self

  def run(self):
    self.health -= 5
    return self

  def displayHealth(self):
    print self.name
    print self.health
    return self

#Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.
possum = Animal("Possum")
possum.walk().walk().walk().run().run().displayHealth

#create another class called Dog that inherits everything that the Animal does and has,
#but 1) have the default health be 150 and 2) add a new method called pet, which when invoked, increase the health by 5
class Dog(Animal)
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
#Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth()
kip = Dog("Kip")
kip.walk().walk().walk().run().run().pet().displayHealth()

#create another class called Dragon that also inherits everything from Animal,
#but 1) have the default health be 170 and 2) add a new method called fly, which when invoked, decreased the health by 10
class Dragon(Animal)
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    #have it say 'this is a dragon!' before it displays the default information
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "This is a dragon!", str(self.health)

#Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth()
draco = Dragon("Draco")
draco.walk().walk().walk().run().run().fly().fly().displayHealth()
