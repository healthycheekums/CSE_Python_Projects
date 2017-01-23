##############################################################################  
#  Computer Project #6c
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

while True:
    try:
        file_proc = open('data_full.txt','r') #File being opened 
        break
    except FileNotFoundError:
        print("file not found")
        input("Press enter after adding the file to this folder:")
        
data_set = []
months = []

for line in file_proc:
    if line[:4] == "Year":
        months = line.split()
    else:
        line_list = line.split()
        year = line_list[1:]
        for s in year:
            dev = (s)
            month_pos =line_list.index(dev)
            deviation = [int(dev),line_list[0],months[month_pos]]
            data_set.append(deviation)
data_set.sort(reverse=True)    
while True:
    try:
        int_count_inp = int(input("Input N, a Positive integer:"))
        if int_count_inp <= 0:
            print("Please input a positive integer")
        else:
            break
    except ValueError:
            print("Please input a Positive integer")
            int_count_inp = input("Input a Positive integer:")
header = ["Year", "Month",  "Deviation"]
print('{:>4} {:>6} {:>10}'.format(*header))
for i in range (int_count_inp):
    
    data_position = data_set[i]
    n_warmest =[data_position[1],data_position[2],data_position[0]]
    print('{:>4} {:>6} {:>10}'.format(*n_warmest))  
file_proc.close()