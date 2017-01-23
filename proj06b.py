##############################################################################  
#  Computer Project #6b
#    
#  Algorithm  
#     Function to open the file 
#         Prompts for user inputs  
#         While loop to determine if correct user input has been input.
#    Function to process the file       
#         While loop to determine inputs and if they are correct
#             For loop to find specific years and income levels
#                 Display of statistical results
#    Main Function to call both earlier functions
#    Main Function is invoked to excecute the program
#
##############################################################################
MONTHS = 12
while True:
    try:
        file_proc = open('data_full.txt','r') #File being opened 
        break
    except FileNotFoundError:
        print("file not found")
        input("Press enter after adding the file to this folder:")

user_list = str(input("name the output file:"))
open_file = open(user_list,'w') 

year_inp = str(input("Input a year ('all', 'ALL' for whole list):"))


#Simplifies the input to all lowercase for All
all_years = year_inp.lower()

while True:
    if all_years == 'all':
        for line in file_proc:
            try:
                year = int(line[:4])
                temps = line[7:]
                temps_list = temps.split()
                temps_int = map(int,temps_list)
                monthly_sum = sum(temps_int)
                monthly_dev = str(int(round(monthly_sum/MONTHS,0)))                
                proc_line = [line[:4],monthly_dev,"\n"]
                proc_line_list = '{:>4} {:>4} {:>1}'.format(*proc_line)
                open_file.write(proc_line_list)
            except ValueError:
                continue
           
        break
    else:   
        try:       
            #converts the year input to an integer
            year_inp = int(year_inp)
            count = 0
            while True:
                try:
                    int_count_inp = int(input("Input an integer:"))
                    if int_count_inp < 0:
                        print("Please input a positive integer")
                    else:
                        break
                except ValueError:
                        print("Please input an integer")
                        int_count_inp = input("Input an integer:")
            
            #this copies the partial and full years 
            for line in file_proc:
                try:
                    year = int(line[:4])
                    if int_count_inp == count:
                        break
                    if year_inp == year:
                        temps = line[7:]
                        temps_list = temps.split()
                        temps_int = map(int,temps_list)
                        monthly_sum = sum(temps_int)
                        monthly_dev = str(int(round(monthly_sum/MONTHS,0)))                       
                        proc_line = [line[:4],monthly_dev,'\n']
                        proc_line_list = '{:>4} {:>4} {:>1}'.format(*proc_line)
                        open_file.write(proc_line_list)
                        year_inp +=1
                        count +=1
                except ValueError:
                    continue
            break
       
        #an expected error from putting in an invalid input (characters)
        except ValueError:
            print("Please input a year" )
            year_inp = (input("Please input a year:"))
            
open_file.close()
file_proc.close()
