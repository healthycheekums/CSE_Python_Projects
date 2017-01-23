##############################################################################  
#  Computer Project #5b
#    
#  Algorithm  
#     Establishment of constants 
#     Prompts for user inputs  
#     While loop to determine if correct user input has been input.       
#         While loop to perform slices and replacements of ( , ) in the string
#         Display of the decompressed string
##############################################################################


def open_file():
    while True:
        try:
            fl_name=str(input("name the file: "))
            fp = open(fl_name,'r')
            #fl_name=str(input("name the file: "))        
            return fp
            break
        except FileNotFoundError:
            print("please name a file that exists")
            
def process_file(op):
    while True:
        op.read()
        year_inp = int(input("Input a year: "))
        inc_inp = int(input("Input an income level {1,2,3,4}: "))
        total = 0
        count = 0
    
        if inc_inp == 1:
            inc = "WB_LI "
        if inc_inp == 2:
            inc = "WB_LMI"
        if inc_inp == 3:
            inc = "WB_UMI"
        if inc_inp == 4:
            inc = "WB_HI "   
        for line in op:
            year = int(line[68:74])
            income = str(line[:5])
            vaccination = int(line[74:])
            if (inc == income and year_inp == year):
                count += 1
                total +=vaccination
                print(line)
                print(vaccination,line)
        break
                   
                
        
def main():
    fp = open_file()
    process_file( op = fp )
    fp.close
#    year_inp = int(input("Input a year:"))
#    count = 0
#    total = 0
#    for line in fp:
#        year = int(line[68:74])
#        vaccination = int(line[74:])
#        if year_inp == year:
#            count += 1
#            total +=vaccination
#            print(line)
#            print(vaccination,line)
#fp = open('polio.txt','r')
#fp = open_file()
#
#print("count:", count)
#print("average:", total/count)
#fp.close()
#fp = open_file()
    
if __name__ == '__main__':
    main()
