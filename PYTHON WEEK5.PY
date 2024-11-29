# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def check_battery(self):
        print(f"Battery life is at {self.battery_life}%")

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, storage, camera_megapixels):
        super().__init__(brand, model, battery_life, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera")

# Assignment 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Example usage
smartphone = Smartphone("Apple", "iPhone 13", 85, "128GB")
smartphone.make_call("123-456-7890")
smartphone.send_message("123-456-7890", "Hello!")
smartphone.check_battery()

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 90, "256GB", 108)
camera_phone.take_photo()

car = Car()
plane = Plane()

car.move()
plane.move()