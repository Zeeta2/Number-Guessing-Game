import numpy as np
random=np.random.randint(1,100)
print(random)
user=""
attempts=10
while attempts>=0:
    user=int(input("Guess a number: "))
    if user==random:
        print("You are right!")
        break
    if attempts==0:
        print("Better luck next time! ")
    else:
        print(f"Not this think again! \n{attempts} attempts left")
    attempts-=1
    print("\n")
    