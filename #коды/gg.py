import random



def NachaloBoya():
    global VragLvl, VragHP, VragUron, Vragi, Vrag, VragSpeed
    VragLvl = random.randint(1, 5)
    VragHP = VragLvl*10
    VragUron = VragLvl*5
    Vragi = ["Octane", "Crypto", "Horizon", "Loba", "Caustic"]
    Vrag = random.choice(Vragi)
    VragSpeed = random.randint(5, 20)
    print("Fight! Your enemy: ", Vrag, ", enemy's HP is: ", VragHP, ", enemy's level is: ", VragLvl, ", enemy's damage is: ", VragUron, ". Your enemy's speed is unknown :) :) :)")
while True:
    while True:
        name = input("Past your name: ")
        if name == "":
            name = input("Past your name >:( : ")
        else:
            break

    champion = int(input("You can choose who you will play for: Revenant, Lifeline, Mad Maggie, Fuse, Wattson: "))
    date = {1:"Revenant", 2:"Lifeline", 3:"Mad Maggie", 4:"Fuse", 5:"Wattson"}
    if champion == 1:
        atk = 15
        HP = 30
        speed = 12
        specialAbility = "Second life"
        print("Your characteristic: ", "\n","Attack =", atk, "\n", "HP =", HP , "\n", "Speed =", speed, "\n", "Special ability: " , specialAbility)

    elif champion == 2:
        atk = 10
        HP = 35
        speed = 10
        specialAbility = "Heal"
        print("Your characteristic: ", "\n", "Attack =", atk, "\n", "HP =", HP, "\n", "Speed =", speed, "\n", "Special ability: " , specialAbility)
    elif champion == 3:
        atk = 16
        HP = 28
        speed = 15
        specialAbility = "SUPER SPEED"
        print("Your characteristic: ", "\n", "Attack =", atk, "\n", "HP =", HP, "\n", "Speed =", speed, "\n", "Special ability: ", specialAbility)
    elif champion == 4:
        atk = 16
        HP = 29
        speed = 13
        specialAbility = "Bombardment"
        print("Your characteristic: ", "\n", "Attack =", atk, "\n", "HP =", HP, "\n", "Speed =", speed, "\n", "Special ability: ", specialAbility)
    elif champion == 5:
        atk = 16
        HP = 29
        speed = 13
        specialAbility = "You are just cute :)"
        print("Your characteristic: ", "\n", "Attack =", atk, "\n", "HP =", HP, "\n", "Speed =", speed, "\n", "Special ability: ", specialAbility)

    NachaloBoya()

    specAb = 0

    if champion == 3:
        specialAb = input("You can use special ability only once. You gonna use it?")
        if specialAb == "yes" and specAb == 0:
            speed = speed * 10
            specAb = 1
        elif specAb == 1:
            print("You can't use special ability twice.")
        elif specialAb == "no":
            specAb = 0

    if champion == 4:
        specialAb = input("You can use special ability only once. You gonna use it?")
        if specialAb == "yes" and specAb == 0:
            atk = atk * 10
            specAb = 1
        elif specAb == 1:
            print("You can't use special ability twice.")
        elif specialAb == "no":
            specAb = 0

    if champion == 5:
        hehe = input("You are just cute. You wanna win the fight?")
        if hehe == "Yes":
            VragHP = -9999
        elif hehe == "no":
            specAb = 0

    while VragHP > 0:
        choice = input("You can run or attack your enemy. What you gonna do?(run/attack): ").lower()
        if choice == "run":
            if speed<VragSpeed:
                print("You got bamboozled, look at you hahaha!!! Your enemy's speed was greater!")
                HP = HP - 10
                print("Your HP = ", HP)
            elif speed>VragSpeed:
                print("Congratulations! You were able to escape.")
                break
        if choice == "attack":
            VragHP -= atk
            print("You attacked the enemy! Enemy's HP =", VragHP)

        else:
            continue

        if VragHP > 0:
            HP -= VragUron
            print("You have been attacked! Your HP =", HP)
            if HP <= 0:
                if champion == 2:
                    HP += 20
                    print("Your special ability is Heal! HP =", HP)
                elif champion == 1:
                    HP = 30
                    print("Your special ability is Second Life! HP =", HP)
                else:
                    print("Fail! Don't cry :)")
        if VragHP <= 0:
            print("Congratulations! You win!")
        continue
