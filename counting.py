prompt="Choose from below options: \n1: Print Odd numbers\n2: Print Event numbers"
prompt+="\nEnter your choice: "

choice=input(prompt)
max_bound=int(input("Enter number range (example: 10 or 5 ): "))
counter=0
while counter<max_bound:
    counter+=1
    if choice=='1':
        if counter%2==0:
            continue
        print(counter, " ")
    if choice=='2':
        if counter%2!=0:
            continue
        print(counter, " ")
