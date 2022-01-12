import random

def ininial_set():  # 隨機設定初始值
    prob = random.randrange(50, 101)
    wisdom = prob

    prob = random.randrange(50, 101)
    charm = prob

    prob = random.randrange(50, 101)
    fitness = prob

    prob = random.randrange(50, 101)
    social = prob

    prob = random.randrange(50, 101)
    health = prob

    prob = random.randrange(1, 101)
    luck = prob
    return wisdom, charm, fitness, social, health, luck