# 创造出狗类的过程
class Dog():
    role = 'dog'

    def __init__(self, name, d_type, life_val, attack_val):
        self.name = name
        self.life_val = life_val
        self.d_type = d_type
        self.attack_val = attack_val

    def bite(self, person_name, attack_val, person_life_val):
        self.attack_val = attack_val
        person_life_val -= self.attack_val
        print(person_name + "被咬了")
        print(person_name + "扣了" + str(self.attack_val))
        print(person_name + "还剩" + str(person_life_val))
        print("---------2")


def judge(d_type):
    if d_type == "京巴":
        return 30
    elif d_type == "藏獒":
        return 80
    else:
        return 50


d1 = Dog("zss", "京巴", 100, judge("京巴"))
d1.bite("zrl", 30, 100)


# 创造出人类的过程
class Person():
    role = 'person'

    def __init__(self, name, age, life_val):
        self.life_val = life_val
        self.name = name
        self.age = age
        if self.age < 18:
            self.attack_val = 20
        elif self.age >= 18:
            self.attack_val = 50

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print(dog.name + "被咬了")
        print(dog.name + "扣了" + str(self.attack_val))
        print(dog.name + "还剩" + str(dog.life_val))


def find(person_age):
    if person_age < 18:
        return 20
    elif person_age >= 18:
        return 50


p1 = Person("zxx", 21, 100)
p1.attack(d1)
