#class called Syracuse
class Syracuse:
    #define a main
    def main():
        #print the header
        print("This program outputs a Syracuse sequence")
        #ask to input a initial value
        num = eval(input("Enter the initial value (an int >= 1): "))
        #calculate and print the sequence
        print(num,end=" ")
        while num!=1:
            if num%2==0:
                num=num/2
                print(num,end=" ")
            else:
                num=(num*3)+1
                print(num,end=" ")
#call the main
    main()
