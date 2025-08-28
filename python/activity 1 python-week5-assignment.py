# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Derived Class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # inherit from Device
        self.os = os
        self.storage = storage
    
    def call(self, number):
        return f"Calling {number} from {self.info()}..."
    
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.info()} ({self.os})"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", "512GB")

print(phone1.call("123-456-789"))
print(phone2.install_app("WhatsApp"))
