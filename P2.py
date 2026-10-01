def main():
    print("Units converter")

    while True:
        while True:
            quantity = get_input("Choose a quantity\n1. Length\n2. Mass\n3. Temparture\n")
            if quantity==1:
                print("Length converter")
                while True:
                    unit1 = get_input("Choose an unit converter\n1. cm-m\n2. m-cm\n")
                    if unit1 != 1 and unit1 != 2:
                        print("Enter the given options only")
                    elif unit1==1:
                        n1 = get_input("Enter the number in cm\n")
                        ans1 = n1/100
                        print(f"{n1}cm = {ans1}m")
                        break
                    else:
                        n2 = get_input("Enter the number in m\n")
                        ans2 =n2*100
                        print(f"{n2}m = {ans2}cm")
                        break
                break

            elif quantity==2:
                print("Mass converter")
                while True:
                    unit2 = get_input("Choose an unit converter\n1. g-kg\n2. kg-g\n")
                    if unit2 != 1 and unit2 != 2:
                        print("Enter the given options only")
                    elif unit2==1:
                        n3 = get_input("Enter the number in g\n")
                        ans3 = n3/1000
                        print(f"{n3}g = {ans3}kg")
                        break
                    else:
                        n4 = get_input("Enter the number in kg\n")
                        ans4 =n4*1000
                        print(f"{n4}kg = {ans4}g")
                        break
                break

            elif quantity==3:
                print("Temparature converter")
                while True:
                    unit3 = get_input("Choose an unit converter\n1. C-K\n2. K-C\n")
                    if unit3 != 1 and unit3 != 2:
                        print("Enter the given options only")
                    elif unit3==1:
                        n5 = get_input("Enter the number in C\n")
                        ans5 = n5+273.15
                        print(f"{n5}C = {ans5}K")
                        break
                    else:
                        n6 = get_input("Enter the number in K\n")
                        ans6 = n6-273.15
                        print(f"{n6}K = {ans6}C")
                        break
                break

            else:
                print("Enter from the given options only ")

        cont = input("Want to continue? Yes or No ")
        cont = cont.strip().title()
        if cont=="No":
            print("Thank you for using")
            break
            

def get_input(promt):
    while True:
        try:
            x = float(input(promt))
        except ValueError:
            print("Enter a number only")
        else:
            return x


main()