# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:41:40 2016

@author: RAVI TEJA
"""
#To Calculate the age of the person till date
from datetime import date
print " "
print "Please enter year, month and date in numerical values"

#Manual Input of Date of Birth
xyear = int(raw_input('Birth Year is - '))
xmonth = int(raw_input('Birth Month is - '))
xday = int(raw_input('Birth Day is (Number) - '))

#Current year, month and day
currentyear = date.today().year
currentmonth = date.today().month
currentday = date.today().day

#Basic Input Verification
if (xmonth > 12) or (xmonth < 1):
    print "invalid input"
elif (xyear > currentyear) or (xyear < 1):
    print "Invalid Input"
elif (xday < 1) or (xday > 31):
    print "Invalid Input"
elif (xmonth == 2) and ((xyear%4)==0) and (xday > 29):
       print "Invalid Input"
elif ((xyear%100 == 0) and (xyear%400) > 0) and (xmonth == 2) and (xday > 28) :
       print "Invalid Input"
elif (xmonth == 2) and ((xyear%4) > 0) and (xday > 28):
    print "Invalid Input"
elif ((xmonth == 4) or (xmonth == 6) or (xmonth == 9) or (xmonth == 11)) and (xday > 30):
    print "Invalid Input"
  
  #Age Calculation  
else:    
  if (xmonth < currentmonth):
    yrs = currentyear - xyear #Valid for current year also.
    
    if (xday < currentday):
        days = currentday - xday
        mns = currentmonth - xmonth
        print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
        
    elif (xday > currentday):
        mns = currentmonth - xmonth-1
        days = currentday + ( 30 - xday)
#        if (xmonth == 1)
        print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
    else:
        
        mns = currentmonth - xmonth
        days = currentday - xday
        print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
        
  elif(xmonth > currentmonth):
      if (xyear == currentyear): #Future Dates
          
             print "Invalid Input" 
                   
      else:
        yrs = currentyear - xyear - 1
        if (xday > currentday):
                   days = currentday+ 30 - xday
                   mns = 11 + currentmonth - xmonth 
        elif (xday < currentday):
                   days = currentday - xday
                   mns = 12 + currentmonth - xmonth
        else:
                  days = currentday - xday
                  mns = 12 + currentmonth - xmonth 
        print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
          
  else:
      if (xyear == currentyear):
          if (xday > currentday): #Future Dates
               print "Invalid Input" 
          else:
              yrs = currentyear - xyear
              mns = 0 
              days = currentday - xday
              print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
      else:
          if (xday > currentday):
             yrs = currentyear - xyear-1
             mns = 11
             days = 30 - (xday-currentday)
             print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
          
          elif(xday < currentday):
            yrs = currentyear - xyear
            mns = 0 
            days = currentday - xday
            print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))
        
          else:
            yrs = currentyear - xyear
            mns = 0 
            days = 0
            print 'Today is his/her birthday'

            print ("The persons age is [%s] Years [%s] Months [%s] Days" % (yrs,mns,days))

 
#To determine the weekday of the birthday of the person
 #For this the assumption considered is that the first day of the calendar has started with SATURDAY
 #The Source for this assumption is - http://www.webexhibits.org/calendars/year-history.html
 # Another Source is - https://en.wikipedia.org/wiki/History_of_calendars
 
 #This Alogorith works perfectly from 14th September 1752. Because there 11 missing in september of 1752..
 #The Calendar has been changed. From September 2nd to September  to 14th September Missing 11 days.
 # Source -1: - http://www.timeanddate.com/calendar/?year=1752
 #Source 2 : - http://mentalfloss.com/article/51370/why-our-calendars-skipped-11-days-1752
 
 #So this logic has been developed considering tha fact that 14th September 1752 is considered as THURSDAY instead of Monday
 #http://www.genealogytoday.com/columns/everyday/030902.html
 
  def weekday(xday, xmonth, xyear):
      #If given year is a non leap Year
    if ((xyear%4) > 0) or (((xyear%100) == 0) and ((xyear%400) > 0)):
        list1 = [31,28,31,30,31,30,31,31,30,31,30,31] #Days of respective month
        countdays = 0
        for i in range (0,xmonth): #Day Count
            countdays = countdays + list1[i]
            
        excessdays = list1[xmonth-1] - xday #To remove additional days during count
        totdays = countdays - excessdays 
        yeardays = xyear * 365
        #a = 1
        leapcount = 0
        leap1count = 0
        null = 0
        for a in range (1,xyear): # To count the number of leap years
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif (a%4 == 0) and (a%400 == 0):
                leap1count = leap1count + 1
            else:
                null +=1;
        totaldays = yeardays + totdays + leapcount + leap1count
                
        troll = totaldays%7 #To determine the day
        
        if (troll == 0):
            print "Your Birthday is on  Saturday"
        elif (troll == 1):
            print "Your Birthday is on  Sunday"
        elif (troll == 2):
            print "Your Birthday is on  Monday"
        elif (troll == 3):
            print "Your Birthday is on  Tuesday"
        elif (troll == 4):
            print "Your Birthday is on  Wednesday"
        elif (troll == 5):
            print "Your Birthday is on  Thursday"
        else:
            print "Your Birthday is on  Friday"
        print " "    
        print "This date/weekday may vary with Gregorian Calender due to conventional methodlogies followed at this time in past"    
        print "As no standard weekdays and dates were followed during this period"
        print "Each country had its own calendar and Conventions"
    else:       
        #If given Year is a leap year
      if ((xyear%4) == 0):
        list1 = [31,29,31,30,31,30,31,31,30,31,30,31] #Days in a month of leap year
        countdays = 0
        for i in range (0,xmonth):
            countdays = countdays + list1[i]
            
        excessdays = list1[(xmonth) -1] - xday
        totdays = countdays - excessdays
        yeardays = (xyear) * 365
        a = 1
        leapcount = 0
        leap1count = 0
        null =0
        for a in range (1,xyear):
            
            if ((a%4) == 0) and ((a%100) > 0):
                leapcount = leapcount + 1
            elif ((a%4) == 0) and ((a%400) == 0):
                leap1count = leap1count + 1
                
            else:
                null += 1
        totaldays = yeardays + totdays + leapcount + leap1count
        
        troll = totaldays%7
        
        if (troll == 0):
            print "Your Birthday is on Saturday"
        elif (troll == 1):
            print "Your Birthday is on Sunday"
        elif (troll == 2):
            print "Your Birthday is on Monday"
        elif (troll == 3):
            print "Your Birthday is on Tuesday"
        elif (troll == 4):
            print "Your Birthday is on Wednesday"
        elif (troll == 5):
            print "Your Birthday is on Thursday"
        else:
            print "Your Birthday is on Friday"
        
        print " "
        print "This date/weekday may vary with Gregorian Calender due to conventional methodlogies followed at this time in past"    
        print "As no standard weekdays and dates were followed during this period"
        print "Each country had its own calendar and Conventions"
  weekday(xday, xmonth, xyear)
       
       
       

        