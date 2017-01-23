##############################################################################  
#  Computer Project #4 
#    
#  Algorithm  
#     Print introduction  
#     Prompts for user inputs 
#     Establishment of constants and importing of random library 
#     For loop of if statements to determine the outputs and output count         
#     Calculation of percentiles needed for outputs 
#         Display of indicated outputs of distrobution 
##############################################################################

BACKSLASH = "\\"


while True:
    inp_str = str(input("Enter a string to decompress (or return to quit): "))
    dec_str = inp_str.replace(BACKSLASH,'\n')
    sec_start = 0
    if dec_str == '':
        print('Nothing to decompress. \nExiting program.')
        break
    if dec_str.find('(') == -1:
        print("Please enter a valid input") 
        continue
    else:
        while True:                  
            slc_start = dec_str.find('(', sec_start)
            if slc_start == -1:
                break
            slc_sub = dec_str.find(',',slc_start)
            sub_dist = int(dec_str[(slc_start + 1):slc_sub])
            slc_end = dec_str.find(')',slc_sub)
            slc_ln = int(dec_str[(slc_sub + 1):slc_end])
            comp_start = slc_start-sub_dist
            comp_end = comp_start + slc_ln
            repl = dec_str[comp_start:comp_end]
            dec_str = dec_str[:slc_start] + repl + dec_str[(slc_end+1):]
            sec_start = slc_end
            
            #print("clarity\n\n")
        
        print('\nThe decompressed string is:\n\n',dec_str)
