

class Car:
    def __init__(self, make, model):
        
        self.make = make
        self.model = model
        self.state = 'stopped'
        
    def start(self):
        
        self.state = 'running'
        print(f"The {self.make} {self.model} is now running.")

    def stop(self):
        self.state = 'stopped'
        print(f"The {self.make} {self.model} is now stopped.")

    def display_state(self):
        print(f"The {self.make} {self.model} is currently {self.state}.")
