class employee:
    def __init__(self, name, salary, rate, age):
        self.name = name
        self.salary = salary
        self.rate = rate
        self.age = age

    def ratingRate(self):
        if self.rate > 4.5:
            return 'rating is good'
        else:
            return 'rating is bad'
        
    def bonus(self):
        if self.age >= 60:
            self.salary += 500
            print('thank you and your total now ' + str(self.salary))
        else:
            self.salary
            print('comming soon ' + str(self.salary))