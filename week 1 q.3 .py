print("PATTERN.......")

k=5

for i in range(12):

    if i<=5:

        for j in range(i+1):

            print(" * ",end="")

        print("\n")

    elif i>5 :

        for j in range(k+1):

            print(" * ",end="")

        print("\n")

        k=k-1