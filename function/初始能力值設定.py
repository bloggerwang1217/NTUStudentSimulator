import random


class Status:
    pass
    


def ininial_set(self):  # 隨機設定初始值
    prob = random.randrange(50, 101)
    self.wisdom = prob
    prob = random.randrange(50, 101)
    self.charm = prob
    prob = random.randrange(50, 101)
    self.fitness = prob
    prob = random.randrange(50, 101)
    self.social = prob
    prob = random.randrange(50, 101)
    self.health = prob
    self.money = 40000
    prob = random.randrange(1, 101)
    self.luck = prob
    return self.wisdom, self.charm, self.fitness, self.social,\
           self.health, self.money, self.luck

a = Status()
print(ininial_set(a))


