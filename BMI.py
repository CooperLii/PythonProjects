#class call BMI
class BMI:
        #define a main
        def main():
                #ask for input the weight
                weight = eval(input("Enter your weight(in pounds): "))
                #ask for input the height
                height = eval(input("Enter your height(in inches): "))
                #calculate the BMI
                BMI = (weight*720)/height**2
                #print out the BMI
                print("Your BMI is " , BMI)
                #check if the BMI is on low side, high side or within the
                #healthy range
                if (int)(BMI)<=25 and (int)(BMI)>=19:
                        print("That's within the healthy range.",end="")
                elif (int)(BMI)<19:
                        print("That's on the low side.",end="")
                else:
                        print("That's on the high side.",end="")
#call the main
        main()
