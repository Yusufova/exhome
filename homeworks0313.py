#TASK1
# class Shiritori:
#     def __init__(self):
#         self.words = []
#         self.game_over = False
#
#     def play(self, word):
#         if self.game_over:
#             return "game over"
#
#         if not self.words or word[0] == self.words[-1][-1] and word not in self.words:
#             self.words.append(word)
#             return self.words
#         else:
#             self.game_over = True
#             return "game over"
#
#     def restart(self):
#         self.words = []
#         self.game_over = False
#         return "Game restarted"
#
#
#
# game = Shiritori()
#
# print(game.play("word"))
# print(game.play("dowry"))
# print(game.play("yodel"))
# print(game.play("leader"))
# print(game.play("righteous"))
# print(game.play("serpent"))
#
# print(game.play("motive"))
# print(game.play("beach"))
# print(game.play("hive"))
#
# game.restart()
#
# print(game.game_over)

#TASK2

# class Employee:
#     def __init__(self):
#         self.employees = []
#
#     def john(self, lastname):
#          return lastname
#     def mary(self,age):
#         return age
#     def richard(self,height):
#         return height
#     def giancarlo(self,nation):
#         return nation
#
# employe = Employee
#
#
# j = employe.john("John","Doe")
# m = employe.mary("Mary",43)
# r = employe.richard("Richard",178)
# g = employe.giancarlo("Giancarlo", "Italian")
#
# print(f"John's lastname: {j}")
# print(f"Mary's age: {m}")
# print(f"Richard's height: {r}")
# print(f"Giancarlo's nationality: {g}")


#TASK3
# class Country:
#     def __init__(self, country, population, area):
#         self.country = country
#         self.population = population
#         self.area = area
#         if self.population > 250000 and self.area > 3000:
#             self.is_big = True
#         else:
#             self.is_big = False
#
#     def compare(self, other):
#         if self.population < other.population:
#             return f" {self.country} has larger population density than {other.country}"
#
# aus = Country("Australia", 23545500,7692024)
# ando =Country("Andorra",76098,468)
#
# print(aus.is_big)
# print(ando.is_big)
# print(ando.compare(aus))
#

#TASK4
# class Magic:
#     def __init__(self, replace, length):
#         self.replace = replace
#         self.length = length
#
#     def length(self, string):
#         return len(string)
#     def magic_replace(self, string, ):
#         for x in string:
#             if x.upper():
#                 r = x.replace("E", "e")
#                 print(r)
#
#
# magic = Magic
# print(magic.length("ewgf", "hello world"))
# print(magic.magic_replace("string", "AzErty-QwErty"))


#Task5

# class Calculator:
#     def __init__(self, nums, other):
#         self.nums = nums
#         self.other = other
#     def add(self, other):
#         return self.nums + self.other
#     def subtract(self,other):
#         return self.nums - self.other
#     def multiply(self,other):
#         return self.nums * self.other
#     def divide(self,other):
#         return self.nums - self.other
#
# calculate = Calculator
#
# print(calculate.add(10,5))
# print(calculate.subtract(10,5))
# print(calculate.multiply(10,5))
# print(calculate.divide(10,5))

#Task6
class Usernames:
    def __init__(self, users):
        self.users = users



    def u1(self):
        d = "Johnsmith10"
        for x in d:
            s = x.count(x)
            return s

    def u2(self):
        e = "marysue1989"
        for y in e:
            f = y.count(y)
            return f
    def u3(self):
        t = "milan rodrick"
        for g in t:
            a = g.count(g)
            return a

user = Usernames

# print(user.u1)
# print(user.u2())
# print(user.u3())

#task7

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age < other.age:
            comparison = "older than"
        elif self.age > other.age:
            comparison = "younger than"
        else:
            comparison = "the same age as"

        return f"{other.name} is {comparison} {self.name}."


# obj = Person("Samuel", 24)
# obj1 = Person("Joel", 36)
# obj2 = Person("Lily", 23)
#
# print(obj.compare(obj1))
# print(obj2.compare(obj1))
# print(obj2.compare(obj))






