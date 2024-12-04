#Створіть клас Rectangle через констуктор клас має приймати довжину і ширину і зберігає їх в атрибутиах
# height weight відповідно. І створіть два методи які будуть рахувати та повертати площо і периметр фігури
# продемонструйте роботу

class Rectangle:
    def __init__(self, w, l):
        self.height = w
        self.lenght = l

    def area(self):
        return self.lenght * self.height

    def perimetr(self):
        pass



figura1 = Rectangle(2,3)
figura2 = Rectangle(5,10)
print(figura1.area())
print(figura2.area())