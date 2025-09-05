import random
import math

def pow(r,a):
    print("I am not that power")

def excercise_1():
    print("Hello, World!")
    radius = 4
    area = math.pi * math.pow(radius, 2)
    volume = (4/3) * math.pi * math.pow(radius, 3)
    print(f"Area of the circle with radius {radius}: {area}")
    print(f"Volume of the sphere with radius {radius}: {volume}")


def excercise_2():
    randomArray = []
    for i in range(20):
        randomArray.append(random.randrange(1,100))
    print(randomArray)

    sum = 0
    for i in randomArray:
        sum += i
    print(f"Sum of random numbers: {sum}")

    average = sum / len(randomArray)
    print(f"Average of random numbers: {average}")

def excercise_3():
    name = "aaaaaaaaa"
    counter = [0,0,0,0,0] # a,e,i,o,u
    for char in name:
        if(char == 'a'):
            counter[0] += 1
        elif(char == 'e'):
            counter[1] += 1
        elif(char == 'i'):
            counter[2] += 1
        elif(char == 'o'):
            counter[3] += 1
        elif(char == 'u'):
            counter[4] += 1
    print(f"Number of vowels in the name: {sum(counter)}")
    print(f"As {counter[0]}")
    print(f"Es {counter[1]}")
    print(f"Is {counter[2]}")
    print(f"Os {counter[3]}")
    print(f"Us {counter[4]}")

if __name__ == "__main__":
    excercise = input("Which excercise do you want to run? (1-5): ")
    if excercise == "1":
       excercise_1()
    elif excercise == "2":
        excercise_2()
    elif excercise == "3":
        excercise_3()