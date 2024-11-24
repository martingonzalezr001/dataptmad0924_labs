import random

a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def randomStringGenerator(num,list_input):
    my_str = ''
    list_output = []
    for x in range(num):
        
        len_str = random.randint(min_len, max_len)
        for y in range(len_str):
            my_str += random.choice(list_input)
        list_output.append(my_str)
        my_str = ''
    return list_output

num_strings = int(input("¿How many random strings do you want?\n"))
min_len = int(input("Enter minimum string length: "))
max_len = int(input("Enter maximum string length: "))
try:
    print(randomStringGenerator(num_strings,a))
except:
    print("The parameters are not correct")
