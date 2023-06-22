class MyClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y
    
    def diff(self):
        return self.x - self.y
    
    def prod(self):
        return self.x*self.y
    
    def other(self,x_new,y_new):
        return self.x + self.y - x_new - y_new


xy = MyClass(4,10)

print(xy.x)

print(xy.y)

print(xy.sum())

print(MyClass(4,10).sum())

print(xy.other(4,7))
    
print(MyClass(4,10).other(4,7))



class Cars:

    # class variable shared by all instances
    kind = 'sports car'

    # instance variable unique to each instance
    def __init__(self,name,make,horsepower):
        self.name = name
        self.make = make
        self.horsepower = horsepower
        self.models = []
    
    def add_model(self,year):
        self.models.append(year)



porsche = Cars('911','Porsche',350)
bmw = Cars('M3','BMW',250)
lambo = Cars('Gallardo','Lamborghini',400)

porsche.add_model(2022)
porsche.add_model(2015)
porsche.add_model(1980)






    