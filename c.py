secret=5
count=0
ch=3
for i in range(3):
    print("Remaining chances : ",ch)
    guess=int(input("Enter your guesss : "))
    count+=1
    if(secret==guess):
        print("You won!! ,the no: is ",secret)
        print(f"You have done in your {count} attempts")
        break
    else:
        print("Your guess i wrong!!")
        ch-=1
        if(ch==0):
            print("Chances over!!")
            print("secret number is ",secret)
            break
        print(f"{i+1} attempt fail")
        if(secret>guess):
            print("Secret no: is higher")
        else:
            print("Secret no: is lower")
