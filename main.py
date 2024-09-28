def find_prob(a,b):
    if a==1:
        prob_a=0.2
        if b==2:
          prob_bga=0.85
        elif b==2:
           prob_bga==0.15
        else:
           print("invalid")
        prob_a_and_b=prob_a * prob_bga
        print("probablity of b given  a",prob_bga)
        print("probablity of both the events occuring :",prob_a_and_b)
    elif a==2:
        prob_a=0.8
        if b==1:
          prob_bga=0.02
        elif b==2:
          prob_bga=0.98
        else:
           print("invalid")
        prob_a_and_b=prob_a * prob_bga
        print("probablity of b given  a",prob_bga)
        print("probablity of both the events occuring :",prob_a_and_b)
    else:
       print("invalid choice ")
    
print("lets calculate probablity . please enter choices for the events")
print("person has step throat? \n1.yes \n2.no")
a=int(input("enter your choices (1/2):"))

print("Person has tested positive ? \n 1.yes \n2.no?")
b=int(input("enter your choices (1/2):"))

print("probablities for event aand b:")
find_prob(a,b)