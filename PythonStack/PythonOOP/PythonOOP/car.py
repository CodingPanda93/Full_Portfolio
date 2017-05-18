class Car(object):
  def __init__(self, price, speed, fuel, mileage, tax):
      self.price = price
      self.speed = speed
      self.mileage = mileage
      if self.price > 10000:
         self.tax = 0.15
      else:
         self.tax = 0.12
      self.display_all()

  def display_all(self):
      print "Price:", str(self.price)
      print "Speed:", str(self.speed) + "mph"
      print "Fuel:", str(self.fuel)
      print "Mileage:", str(self.mileage) + "mpg"
      print "Tax:", str(self.tax)

car1 = Car(5530, 80, "Full", 35)
car2 = Car(3304, 85, "Empty", 15)
car3 = Car(12000, 65, "Kind of Full", 25)
car4 = Car(6500, 95, "Empty", 33)
car5 = Car(2200, 75, "Full", 13)
car6 = Car(35000, 105, "Empty", 30)
