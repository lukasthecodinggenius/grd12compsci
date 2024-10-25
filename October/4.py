class Cat():
    def make_sound(self):
        print('Meow Meow Meow')
        
class Dog():
    def make_sound(self):
        print('Bark Bark Bark')
        
animals = [Cat(), Dog()]
for animal in animals:
    animal.make_sound()
    
