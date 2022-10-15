a = int(input("Enter the first term of the AP: "))
d = int(input("Enter the common difference of the AP: "))
n = int(input("Enter the number of terms in the AP: "))

print("Select An Option")
print("1. Sum Of The AP")
print("2. Nth Term Of The AP")
print("3. Get The Required AP")


while True :
    choise = int(input("Enter your choise: "))
    if choise == 1:
        print()
        print("Sum of the AP: ", (n/2)*(2*a+(n-1)*d))
    elif choise == 2:
        print()
        print("nth term of the AP: ", a+(n-1)*d)
    elif choise == 3:
        print()
        print("The Required AP: ", end="")
        for i in range(n):
            print(a, end=" ")
            a = a+d
    else:
        print("Invalid Input")
    print()
    print("Do you want to continue? (y/n)")
    if input() == 'n':
        break

        
