import random
class Bike(object):
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0

  def display_info(self):
    print "Bike Pricing:", self.price
    print "Bike Max-Speed:", self.max_speed
    print "Bike Miles:", self.miles
    return self

  def ride(self):
    print "Riding!"
    self.miles= self.miles + 10
    return self

  def reverse(self):
    if self.miles >= 0:
        print "Reversing!"
        self.miles= self.miles - 5
    else:
        print "You can not reverse any further!"
    return self
#instances
bike1 = Bike(400, "55mph")
bike2 = Bike(250, "25mph")
bike3 = Bike(500, "65mph")

#Chaining methods together
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
