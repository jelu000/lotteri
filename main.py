import lotter

lotteriet = lotter.Lotteri()
looping = True

while looping:

    antal_lotter = input("\n\t\tHur många lotter vill du ha? Max 3st! : ")

    
    try: 
        int_antal_lotter = int(antal_lotter)
        i = 0
        if (int_antal_lotter < 4):

            print("\n\t\tGrattis du vann det här! ")
            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print("\t\t" + vinst)
                i += 1 
            
    
        elif (int_antal_lotter > 3):
            print("\n\t\tDu har valt för många lotter!")
    except ValueError:
        print("\n\t\tEndast siffror tillåtet!")
    

    print("--------------------------------------------------------")
    spela_igen = input("\n\t\tVill du spela igen? j/n: ")
    
    if  (spela_igen == "n" ):
        break