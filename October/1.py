class Animal():
    def __init__(self, sound):
        self.sound = sound
        
    def make_sound(self, sound):
        print(sound)
        
class Dog(Animal):
    def make_sound(self):
        for i in range(3):
            print('Bark')
        
def main():
    
    sound = input('What sound would you like to make? ')
    animal = Animal(sound)
    animal.make_sound(sound)  
    dog = Dog(sound)  
    dog.make_sound()  
    
main()
