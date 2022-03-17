import random 
level = 90
power = 110
a = 205
d = 188

target = 1
weather = 1 
badge = 1
critical = 1
ran = random.uniform(0.85 , 1 )
stab = 1.5
types = 0.5

modifier = target * weather * badge * critical * ran * stab * types 

damage =  ((((((2 * level / 5)  + 2) * power) * (a/d))) / (50 + 2) * modifier)


print(round(damage))