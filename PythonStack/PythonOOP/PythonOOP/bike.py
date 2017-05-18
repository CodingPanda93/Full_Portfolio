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
  def ride(self):
    print "Riding!"
    self.miles= self.miles + 10
  def reverse(self):
    if self.miles >= 0:
        print "Reversing!"
        self.miles= self.miles - 5
    else:
        print "You can not reverse any further!"
#instances
bike1 = Bike(400, "55mph")
bike2 = Bike(250, "25mph")
bike3 = Bike(500, "65mph")

#operating the functions, first instance: ride three times, reverse once and have it displayInfo()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.display_info()

#operating the functions, second instance ride twice, reverse twice and have it displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.display_info()

#operating the functions, third instance reverse three times and displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.display_info()
