class Vehicle():
   COLOR = "White"
   def __init__(self,mileage:float,capacity:float,name:str):
      self.mileage= mileage
      self.capacity = capacity
      self.name = name
      
   def seating_capacity(self, capacity):
      return f"The seating capacity of a {self.name} is {capacity} passengers"
   
   def fare(self):
      return self.capacity * 100
      
class Bus(Vehicle):
   def fare(self):
      amount = super().fare()
      amount += amount * 0.10
      return amount

school_bus = Bus(20,50,"bus")
print(isinstance(school_bus,Vehicle))
      
