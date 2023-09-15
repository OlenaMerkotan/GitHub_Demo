class Dog:
    biology_class = 'Animal' #Static method
    def __init__(self, name, weight, color, appetite):
        self._name = name
        self.weight = weight
        self.color = color
        self._appetite = appetite


    def run(self):
        return 'I can run!'
    def get_name(self):
        return f'Hello! My name is {self._name}'

    def set_name(self, new_name):
        set_name = new_name

dog1 = Dog('Bobik', 15, 'brown', 'good')
print(dog1._appetite)
# print(dog1.run())
# print(dog1.biology_class)

# dog2 =Dog('Rex', 12, 'white', 'bad')  #private and protected
# print(dog2.weight)


# class Cat:
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def jump(self):
#         return 'I can jump!'
#
#     def get_name(self):
#         return f'Hello! My name is {self.name}'
#     def set_name(self, new_name):
#         set_name = new_name
#
# cat1 = Cat('Murzik', 12, 'street_cat')
# print(cat1.name)
# print(cat1.age)
# print(cat1.breed)
# print(cat1.jump())
# print(cat1.set_name('Marta'))


'''прямое переназначение переменных не приветствуется, а используется метод set'''
'''Наследование подкласс будет наследовать все свойства суперкласса'''
'''Инкапсуляция методы используюися только внутри класса'''
'''Полиморфизм разное поведение отдного метода в разных классах'''
'''Абстракция - выделение основных, наиболее значимых характеристик обекта'
и игнорирование второстепенных'''









