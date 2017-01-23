##############################################################################  
#  Computer Project #7
#    
#  Algorithm
#     Call main function
#         Call function to open the file and grab columns
#             Conversion of list elements to int and float
#         Call function to grab hearing column data
#         For loop to convert these list values
#             Call function to adjust for inflation   
#         Call function to grab hearing names
#         Call function to graph data
#         Call function to write adjusted hearing data file 
#
##############################################################################
#constant used and importing of pylab
PER = 100 #percent conversion
import pylab

def draw_bar_graph(x,y):
    '''Draw a bar graph of y values with labels from x where
       x is a list of strings; y is a list of values associated with each x'''
    number_of_bars = len(x)
    bar_width = 0.5
    # create a list (array) of indices for bars
    x_values = pylab.linspace(0,number_of_bars-1,number_of_bars)
    # associate a string label (tick) from x with each bar
    # orient the string to the middle of the bar, and rotate the label 45 degrees
    pylab.xticks(x_values+bar_width/2, x, rotation=45)
    
    # Title for the graph and labels for the axes
    pylab.title( "Inflation-adjusted Cost for Hearings" )
    pylab.ylabel( "Cost (in millions of 2015 dollars)" )
    
    pylab.bar(x_values,y,width=bar_width)
    pylab.show()
    
def get_cols_from_file (name,list_indices,skip):
    """
    Get the indicated columns from a file.
    
    name: the name of the file
    list_indices: the list of indices to grab the columns from
    skip: the number of header lines to skip
    Returns: a list of lists of columns grabbed. 
    """
    
    #empty lists to be added to
    data_lists = [] #list of column lists
    col_list = [] #column list
    
    #opens the named file if possible
    try:
        data_file = open(name, 'r')  #working file
         
        #this skips the indicated lines
        for i in range(skip):
            next(data_file)
            
        #this copies the columns
        for line in data_file:
            line_list = line.split() #the line split into a list
            for n in range(len(list_indices)):
                data_col = line_list[list_indices[n]] #data column
                col_list.append(data_col)
            data_lists.append(col_list)
            col_list = []
        return data_lists
        data_file.close()
    except FileNotFoundError:
        print("files not found") 
        
def adjust_for_inflation (dollar,year,listed_data):
    """
    adjust the dollar value for inflation
    
    dollar: the dollar amount
    year: the starting year
    listed_data: the list of years and inflation values
    Returns: the adjusted dollar amount
    """    
    #this finds the starting point for inflation
    year_pos = int(find_index(year,listed_data)) #position of the year
    infl_list = listed_data[(year_pos + 1):] #list of inflation values used
    #applies the inflation to the  dollar amount
    for item in infl_list:
        infl_rate = item[1]
        dollar = dollar+(dollar * infl_rate/PER)
    return round(dollar,1)
        
def find_index( year, infl_list):
    """
    finds the index of the year
    
    year: the year to search for
    infl_list: the list of years and inflation values
    Returns: the index of the indicated year
    """    
    #This searches for the year in the list of lists
    for item in infl_list:
        if item [0] == year:
            return infl_list.index(item)
            
def write_file(adj_inf_list):
    """
    writes the adjusted hearings file properly formatted
    
    adj_inf_list: list of inflation adjusted values
    """    
    #opens the file to be written to and writes the header
    wr_file = open("adjusted_hearings.txt",'w')
    wr_file.write("         Congressional Hearing Cost\n")
    wr_file.write("Name         Cost ($Million)         Year\n")
    
    #calls this function to get a list of years and dollars
    hearings_list_form =get_cols_from_file ("hearings.txt",[0,1,2],2)
    
    #replaces the dollars with inflated dollars  
    for item in hearings_list_form:
        item[1] = adj_inf_list[hearings_list_form.index(item)]
        item.append('\n')
        
    #writes the remaining lines into the file
    for n in range(len(hearings_list_form)):
        hearing_line = hearings_list_form[n]  #the line of the specific hearing
        wr_file.write('{:<11} {:>4} {:>24} {:>1}'.format(*hearing_line))
        
    wr_file.close()
     
def main(): 
    """
    Calls all of the functions and runs calulations to properly format the
    variables for input into other functions.
    """   
    
    #Call to get the inflation averages and years
    infl_data = get_cols_from_file("inflation.txt",[0,-1],1)
    for item in infl_data:
            item[0] =int(item[0])
            item[1] = float(item[1])

    #Call to get the hearing money   
    hearing_data = get_cols_from_file("hearings.txt",[-1,1],2)
    adjusted_inf = []
    
    #conversion of strings to floats and ints
    for item in hearing_data:
        item[0] =int(item[0])
        item[1] = float(item[1])
        hring_year = item[0]   #hearing year
        hring_cost = item[1]   #hearing cost
        infl_dollar = adjust_for_inflation (hring_cost,hring_year,infl_data)
        adjusted_inf.append(infl_dollar)
    
    #list of the hearing titles
    hearing_titles = get_cols_from_file("hearings.txt",[0],2) #list form titles  
    titles= [j for i in hearing_titles for j in i]  #string titles in list
    
    #call the graphing function
    draw_bar_graph(titles,adjusted_inf)
    
    #write the file
    write_file(adjusted_inf)

       
#Formal way of calling main as soon as the program is started.   
if __name__ == '__main__':
    main()