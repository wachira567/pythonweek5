#Assignment 1: Design Your Own Class!
class Smartphone:
    def __init__(self, brand, model, battery_life):
        """Constructor to initialize the smartphone attributes."""
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def display_info(self):
        """Display the smartphone's information."""
        print(f"Smartphone Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def use_app(self, app_name):
        """Simulate using an app and reduce battery life."""
        print(f"Using {app_name}...")
        self.battery_life -= 1
        print(f"Battery life remaining: {self.battery_life} hours")

# Inheritance Example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu):
        """Constructor to initialize the gaming smartphone attributes."""
        super().__init__(brand, model, battery_life)
        self.gpu = gpu  # Graphics Processing Unit

    def display_info(self):
        """Override the display_info method to include GPU information."""
        super().display_info()
        print(f"GPU: {self.gpu}")

# Example usage
my_phone = Smartphone("Apple", "iPhone 13", 20)
my_phone.display_info()
my_phone.use_app("Instagram")

print("\n--- Gaming Smartphone ---")
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 18, "Adreno 660")
gaming_phone.display_info()
gaming_phone.use_app("Call of Duty")

#Activity 2: Polymorphism Challenge!

class Vehicle:
    def move(self):
        """Base method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        """Override the move method for Car."""
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        """Override the move method for Plane."""
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        """Override the move method for Bicycle."""
        print("Riding a bicycle 🚲")

# Example usage
def make_vehicle_move(vehicle):
    vehicle.move()

# Create instances of each vehicle
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

# Demonstrate polymorphism
make_vehicle_move(my_car)      # Output: Driving 🚗
make_vehicle_move(my_plane)    # Output: Flying ✈️
make_vehicle_move(my_bicycle)  # Output: Riding a bicycle 🚲