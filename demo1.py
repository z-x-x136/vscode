#创造出狗类的过程
class Dog():
    role = 'dog'

    def __init__(self, name, d_type, life_val):
        self.name = name
        self.life_val = life_val
        self.d_type = d_type
        #self.attack_val= attack_val#这是函数与方法的区别之一。类方法里面所有变量都必须要提及到，而函数可以不提及。函数不提及不会报错类，类不提及会报错

    def bite(self, person_name, attack_val, person_life_val):
        self.attack_val = attack_val
        person_life_val -= self.attack_val
        print(person_name+"被咬了")
        print(person_name, self.attack_val,  sep="扣了")
        print(person_name, person_life_val,  sep="还剩")
        print("---------2")


def judge(d_type):  # 迫于无奈，只好把这个原属于类的方法改为内外面的函数，这样的话attack_val可以不提及,也可以输出了
    if d_type == "京巴":
        Dog.attack_val = 30
    elif d_type == "藏獒":
        Dog.attack_val = 80
    else:
        Dog.attack_val = 50
    print("---------1")
    return Dog.attack_val


d1 = Dog("zss", "京巴", 100)
print(judge("京巴"))  # 先查找对应种类的狗的攻击力是多少
print(d1.bite("zrl", 30, 100))


#创造出人类的过程
class Person():
    role = 'person'

    def __init__(self, name, age, life_val):
        self.life_val = 100
        self.name = name
        self.age = age
        if self.age < 18:
            self.attack_val = 20
        elif self.age >= 18:
            self.attack_val = 50

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print(dog.name+"被咬了")
        print(dog.name+"扣了"+self.attack_val)
        print(dog.name+"还剩"+dog.life_val)
