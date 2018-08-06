quit_counter="r"
while quit_counter.lower()!='q':
    name=input("What's your name? ")
    age=int(input("What's your age? "))
    car_status=input("Do you own car? (yes/no): ")
    quit_counter=input("Quit q, or Continue c: ")
    if car_status.lower()=='yes':
        car_status=True
    elif car_status.lower()=='no':
        car_status=False

print("Thanks for your time {} and providing your details!\n".format(name))
print("Your details stored with us are as follows\n Name:    \t{}\n Age:    \t{}\n Car ower:\t{}".format(name,age,car_status))