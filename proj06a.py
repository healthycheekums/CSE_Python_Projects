##############################################################################  
#  Computer Project #6a
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

import pylab

def draw_graph( x, y ):
    '''Plot x vs. y (lists of numbers of same length)'''

    # Title for the graph and labels for the axes
    pylab.title( "Change in Global Mean Temperature" )
    pylab.xlabel( "Year" )
    pylab.ylabel( "Temperature Deviation" )

    # Create and display the plot
    pylab.plot( x, y )
    pylab.show()

def open_file():
    while True:
        try:
            file_name=str(input("name the file: "))  #file name
            file_proc = open(file_name) #The file being processed
            return file_proc
            break
        except FileNotFoundError:
            print("Please name a file that exists")

def year_list(file):
    years = []
    average_dev = []
    for line in file:
       year = int(line[:4])
       dev = int(line[5:])       
       average_dev.append(dev)        
       years.append(year)       
    return years, average_dev       
        
def main():
    file_proc = open_file()
    listed_years,listed_dev = year_list(file_proc)
    file_proc.close()
    draw_graph( listed_years, listed_dev)
    
    
#Formal way of calling main as soon as the program is started.   
if __name__ == '__main__':
    main()
       
       
       
       
       
            