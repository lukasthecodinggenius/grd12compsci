#Method overiding allows a subclass to provide a specific implementation of a method that is already defined in its superclass# Base class

#superclass/base class
class Bird:
    def speak(self):
        print("Bird is making a sound")

# Subclass
class Parrot(Bird):
    def speak(self):
        print("Parrot is saying 'Hello!'")


bird = Bird()
parrot = Parrot()


bird.speak()    
parrot.speak()  
