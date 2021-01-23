#class called acronums
class acronums:
        #define the main
        def main():
                #print the header
                print ("This program builds acronyms")
                #ask for a input
                phrase =  input("Enter a phrase: ")
                #print the acronym
                print ("The acronym is: ",end="")
                list = phrase.split(" ")
                for str in range(len(list)):
                    print (list[str][0:1].upper(),end="")
#call the main
        main()
