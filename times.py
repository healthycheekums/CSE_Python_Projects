##############################################################################   
#  Computer Project #11
#     
#  Class to define a Time object in UTC and methods to enact on it
#   UTC (Coordinated Universal Time) uses a 24-hour clock 
#   The notation hh:mm:ss+zz or hh:mm:ss-zz, where:
#       hh is a two-digit hour between 00 and 23
#       mm is a two-digit minute between 00 and 59
#       ss is a two-digit second between 00 and 59
#       zz is a two-digit offset from Coordinated Universal Time
#       08:30:00-03 represents 8 hours, 30 minutes and 0 seconds 
#       in the time zone 3 hours behind Coordinated Universal Time.
# 
############################################################################## 


class Time(object):   
    def __init__(self,hours =00 ,minutes = 00 ,seconds = 00,zone = 00):
        """
        initialize the time object (defaults to 00 if nothing is given)
        hours:hours between 00 and 23
        minutes:minutes between 00 and 59
        seconds:seconds between 00 and 59
        zone: time zone betweeen -12 and +12
        """
        if type( hours ) == int:
            if (0 <= hours <=23):
                if type( minutes) == int:
                    if (0 <= minutes <= 59):
                        if type( seconds ) == int:
                            if (0 <= seconds <= 59): 
                                if type( zone ) == int:
                                    if (-12 <= zone <=  12):
                                        self.__hours = hours
                                        self.__minutes = minutes
                                        self.__seconds = seconds
                                        self.__zone = zone
        else:
            raise ValueError
    def __repr__(self):
        """
        returns a printable representation of a Time object
        """
        #gets str representation of Time values
        hour_str = str(self.__hours)
        min_str = str(self.__minutes)
        sec_str = str(self.__seconds)
        zone_str = str(self.__zone)
        zone_str = zone_str.strip('-')
        #Adds the zero into the string if the number is less than 10
        if self.__hours < 10:
            hour_str = "0"+ str(self.__hours)      
        if self.__minutes < 10:
            min_str = "0"+ str(self.__minutes)
        if self.__seconds <10:
            sec_str = "0" +str(self.__seconds)
        if (-10 < self.__zone < 10):
            zone_str = zone_str.strip('-')
            zone_str = "0" + zone_str
        if (0 <= self.__zone):
            return "{}:{}:{}+{}".format( hour_str, min_str,sec_str,zone_str )
        else:
            return "{}:{}:{}-{}".format( hour_str, min_str,sec_str,zone_str )
        
    def __str__(self):
        """
        returns a 'readable' printable representation of a Time object
        """
        #gets str representation of Time object values
        hour_str = str(self.__hours)
        min_str = str(self.__minutes)
        sec_str = str(self.__seconds)
        zone_str = str(self.__zone)
        zone_str = zone_str.strip('-')
        #Adds the zero in if the number is less than 10
        if self.__hours < 10:
            hour_str = "0"+ str(self.__hours)        
        if self.__minutes < 10:
            min_str = "0"+ str(self.__minutes)
        if self.__seconds <10:
            sec_str = "0" +str(self.__seconds)
        if (-10 < self.__zone < 10):
            zone_str = zone_str.strip('-')
            zone_str = "0" + zone_str
        if (0 <= self.__zone):
            out_str = hour_str + ":" + min_str + ":" + sec_str + "+" + zone_str
        else:
            out_str = hour_str + ":" + min_str + ":" + sec_str + "-" + zone_str

        return out_str
        
    def from_str (self,string= ""):
        """
        Creates a Time object from a utc string
        utc_string: the string, defaults to an empty string
        """
        #validates the string is properly formatted then returns Time object
        if string[2] == ':':
            if string[5] == ':':
                if string[8] == '+' or '-':
                    hours =  int(string[0:2])
                    minutes = int(string[3:5])
                    seconds = int(string[6:8])
                    zone = int(string[8:])
                    return Time(hours,minutes,seconds,zone)
                    
        else:
            raise ValueError
        
    
    def get_as_local(self):
        """
        Returns the local time as a string
        """
        #Formats then adds and AM or PM to the end, or Midnight or Noon
        mins = str(self.__minutes)
        sec = str(self.__seconds)
        if 0 < self.__hours < 12: 
            hour = (self.__hours)
            if hour < 10:
                hour = "0"+ str(hour) 
            else:
                hour = str(hour)
            day_half = 'AM'
        if self.__hours > 12:
            hour = (self.__hours - 12)
            if hour < 10:
                hour = "0"+ str(hour)
            else:
                hour = str(hour)
            day_half = 'PM'
        if self.__hours == 12:
            if self.__minutes == 0:
                if self.__seconds == 0:
                    return('Noon')
        if self.__hours == 0:
            if self.__minutes == 0:
                if self.__seconds == 0:
                    return('Midnight')                  
        if self.__minutes < 10:
            mins = "0"+ str(self.__minutes)
        if self.__seconds <10:
            sec = "0" +str(self.__seconds)
        loc_str = hour + ":" + mins+ ":" + sec + " " + day_half
        return (loc_str)
        
    #comparison methods
    def __eq__(self, comp):
        """
        equality operator: ==
        comp: the comparison object
        returns: true or false
        """
        if type(comp) == Time:
            if self.__hours +self.__zone == comp.__hours+ comp.__zone:
                if self.__minutes == comp.__minutes:
                    if self.__seconds == comp.__seconds:
                           return True
        if type(comp) != Time:
            raise TypeError
        else:
            return False
        
    def __ne__(self, comp):
        """
        inequality operator: !=
        comp: the comparison object
        returns: true or false
        """
        if type(comp) == Time:
            if self.__hours +self.__zone == comp.__hours+ comp.__zone:
                if self.__minutes == comp.__minutes:
                    if self.__seconds == comp.__seconds:
                           return False
        if type(comp) != Time:
            raise TypeError
        else:
            return True
        
    def __lt__(self, comp):
        """
        less-than operator: <
        comp: the comparison object
        returns: true or false
        """
        if type(comp) == Time:
            if (self.__hours - self.__zone) < (comp.__hours -comp.__zone):
                return True
            if self.__hours -self.__zone == comp.__hours- comp.__zone:
                if self.__minutes < comp.__minutes:
                    return True
                if self.__minutes < comp.__minutes:
                    if self.__seconds < comp.__seconds:
                          return True
        if type(comp) != Time:
            raise TypeError
        else:
            return False
        
    def __le__(self, comp):
        """
        less-than-or-equal-to operator: <=
        comp: the comparison object
        returns: true or false
        """
 
        if type(comp) == Time:
            if (self.__hours -self.__zone) <= (comp.__hours - comp.__zone):
                return True
            if (self.__hours -self.__zone) == (comp.__hours-comp.__zone):
                if self.__minutes <= comp.__minutes:
                    return True
                if self.__minutes == comp.__minutes:
                    if self.__seconds <= comp.__seconds:
                        return True
        if type(comp) != Time:
            raise TypeError
        else:
            return False
        
    def __gt__(self, comp):
        """
        greater-than operator: >
        comp: the comparison object
        returns: true or false
        """
        if type(comp) == Time:
            if self.__hours -self.__zone > comp.__hours- comp.__zone:
                return True
            if self.__hours -self.__zone > comp.__hours- comp.__zone:
                if self.__minutes > comp.__minutes:
                    return True  
                if self.__minutes == comp.__minutes:
                    if self.__seconds > comp.__seconds:
                        return True
        if type(comp) != Time:
            raise TypeError
        else:
            return False
                
    def   __ge__(self, comp):
        """
        greater-than-or-equal-to operator: >=
        comp: the comparison object
        returns: true or false
        """
        if type(comp) == Time:
            if self.__hours -self.__zone >= comp.__hours- comp.__zone:
                return True
            if self.__hours -self.__zone >= comp.__hours- comp.__zone:
                if self.__minutes >= comp.__minutes:
                    return True
                if self.__minutes == comp.__minutes:
                    if self.__seconds >= comp.__seconds:
                        return True
        if type(comp) != Time:
            raise TypeError
        else:
            return False
        
    #addition and subtraction    
    def __add__(self,comp):
        """
        Adds an integer to a Time object
        self: time object to modified
        comp: computation to be done on the time object
        returns: the new time
        """
        #divides the seconds out into hour and minute representations
        if type(comp) != int:
            raise TypeError
        if type(comp) == int:        
            minutes = comp//60
            seconds = comp%60
            hours = minutes//60
            #if less than an hour is added calculations
            if hours == 0:
                new_min = (self.__minutes + minutes)
                new_hour = (self.__hours + new_min//60)
                if new_hour//24 > 0:
                    new_hour = (new_hour -24*(new_hour//24) )  
                if new_min//60 > 0:
                    new_min = (new_min -60*(new_min//60) )               
                new_seconds =(self.__seconds + seconds)
                if new_seconds//60 > 0:
                    new_seconds =(new_seconds - 60*(new_seconds//60))
                return Time(new_hour,new_min,new_seconds,self.__zone)
            #If a negative time amount is added
            if comp < 0:
                new_min = (self.__minutes + minutes)
                new_hour = (self.__hours + new_min//60)
                if new_hour//24 < 0:
                    new_hour = abs((new_hour -24*(new_hour//24) ))  
                if new_min//60 < 0:
                    new_min = ((new_min -60*(new_min//60) ))               
                new_seconds =(self.__seconds + seconds)
                if new_seconds//60 < 0:
                    new_seconds =abs((new_seconds - 60*(new_seconds//60)))
                return Time(new_hour,new_min,new_seconds,self.__zone)
            #all other cases    
            else:
                new_min = (self.__minutes + minutes)
                new_hour = (self.__hours + hours)
                if new_hour//24 > 0:
                    new_hour = (new_hour -24*(new_hour//24) )  
                
                if new_min//60 > 0:
                    new_min = (new_min -60*(new_min//60) )               
                new_seconds =(self.__seconds + seconds)
                if new_seconds//60 > 0:
                    new_seconds =(new_seconds - 60*(new_seconds//60))
                return Time(new_hour,new_min,new_seconds,self.__zone)
        
    def __sub__(self,time):
        """
        subtracts one Time object from another Time object to find difference
        time: the subtracted time object
        returns: the time difference in seconds
        """
        #constants for second conversions
        HR = 3600
        MN = 60
        #calculations for the difference
        if type(time) == Time:
            hour_dif = (self.__hours - time.__hours)*HR
            minute_dif =(self.__minutes - time.__minutes)*MN
            second_dif = (self.__seconds - time.__seconds)
            zone_dif = -(self.__zone - time.__zone)*HR
            difference = hour_dif + minute_dif + second_dif + zone_dif
            return (difference)
        else:
            raise TypeError
        
     