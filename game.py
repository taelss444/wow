import turtle
import random

rules_turn = input("Нажмите 'Enter' для начала игры.")
print("Правила игры: добраться до домика черепашки раньше противника.","\n",
      "Количество шагов определяется броском кубика.")

turtle.bgcolor("pink")
turtle.title("Game")
one = input("Введите имя первого игрока: ")
o = turtle.Turtle()
o.color("red")
o.shape("turtle")
o.shapesize(2, 2, 2)
o.penup()
o.goto(-200, 100)

two = input("Введите имя второго игрока: ")
t = o.clone()
t.color("yellow")
t.penup()
t.goto(-200, -100)

o.goto(300, 60)
o.pendown()
o.circle(40)
o.penup()
o.goto(-200, 100)
t.goto(300, -140)
t.pendown()
t.circle(40)
t.penup()
t.goto(-200, -100)

dice = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if o.pos() >= (260, 60):
        print(one, "выигрывает!")
        break
    elif t.pos() >= (260, -140):
        print(two, "выигрывает!")
        break
    else:
        o_turn = input("Нажмите 'Enter' для броска кубика ")
        dice_outcome = random.choice(dice)
        print("Количество шагов:", dice_outcome, "\n")
        o.fd(20*dice_outcome)
        t_turn = input("Нажмите 'Enter' для броска кубика")
        dice_outcome = random.choice(dice)
        print("Количество шагов:", dice_outcome, "\n")
        t.fd(20*dice_outcome)
turtle.mainloop()