class Underscore(object):
    #will go through each value and return a new array of those that comple the lambda function
    def map(self, list, function):
        newList = []
        for num in list:
            newList.append(function(num))
        return newList

    #will add each variable by the next variable within an array
    def reduce(self, list, function):
        reduction = 0
        for num in list:
            reduction = function(reduction,num)
        return reduction

    #will pass the first true value that passes through the defined lambda function
    def find(self, list, function):
        for num in list:
            if (function(num) == True):
                return num
        return None

    #will pass all values that pass through the defined lambda function
    def filter(self, list, function):
        newfilteredList = []
        for num in list:
            newfilteredList.append(function(num))
        return newfilteredList

    #will pass all values that return False from the defined lambda function
    def reject(self, list, function):
        newrejectedList = []
        for num in list:
            if (function(num) == False):
                newrejectedList.append(function(num))
        return newrejectedList

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

list = [1,2,3,4,5,6]
print _.map(list, lambda x: x ** 2)
print _.reduce(list, lambda x, y: x + y)
print _.find(list, lambda x: x % 2 == 0)
print _.filter(list, lambda x: x % 2 == 0)
print _.reject(list, lambda x: x % 2 == 0)
