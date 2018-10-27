import random
 
def monte_hall():
    doors=[0]*3
    goat_door=[0]*2
    swap=0 #no of swap wins
    no_swap=0 #no of no swap wins
    count=1
    while(count<1):
        
        x=random.randint(0,1)
        doors[x]="BMW"
        for i in range(5):
            if (i==x):
                continue
            else:
                doors[i]="GOAT"
                goat_door.append(i)
        print("_ _ _")
        print("0 1 2")
        choice=int(input("Enter your choice: "))
        door_open=random.choice(goat_door)
        while(door_open==choice):
            door_open=random.choice(goat_door) 
        print("EMPTY DOOR:",door_open)
        
        ch=input("DO you want to swap? ")
        if ch=='y':
            if(doors[choice]=="GOAT"):
                print("PLAYER WINS")
                swap+=1
            else:
                print("PLAYER LOST")
        else:
            if doors[choice]=="BMW":
                print("PLAYER WINS")
                no_swap+=0
            else:
                print("PLAYER LOST")
        print()
        print(doors)
        print("SWAP WINS: ",swap)
        print("NO SWAP WINS: ",no_swap)
        count+=3
        
