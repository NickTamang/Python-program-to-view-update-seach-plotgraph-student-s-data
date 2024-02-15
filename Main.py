### Main File ###
from matplotlib import pyplot as plt #importing pyplot from matplotlib for bargraph
from operator import itemgetter #importing itemgetter function from library 'operator'
import numpy as np #imprting numpy library as np

#creating a class to store data
class student:
    def __init__(self, student_id, firstname, lastname, age, country ): #creating class title
        self.id = student_id 
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        #function to print the data stored in class as object in firstname, lastname....country
    def print(self):
        print("","Full Name:" + self.firstname + " " + self.lastname )
        print("",'ID:', self.id)
        print("",'Age:',self.age)
        print("",'Country:',self.country)
        print('_________________________________')
 #this is a list to store students object
students_list=[]
#function to read the file
def read_file():
    f=open("students.txt","rt") ###opening the text file in a read mode
    for each_line in f: #for loop to excute the data in readable form
        each_line=each_line.rstrip("\n") #splits the data in .txt file as a each line
        student_id, lastname, firstname, age, country=each_line.split(", ") #splits the data in each line with condition (", ")
        data=student(student_id, lastname, firstname, age, country) #excutes data from .txt fie to add in a class title
        students_list.append(data) #this will add or store an object in list from file
    f.close() #This will close the file

#function to print the  student details one time so the output won't look messy
def student_detail_title():
        print(' _________________________________________')
        print('|             Students Details            |')
        print('|_________________________________________|')

#defining fucntion 1 as(1a and 1b) to excute (summary_report)  in function 5 later        
#function to print the details of the students from the module
def student_details():
    #initial values are kept on zero
    wales=0
    england=0
    scotland=0
    count=0 #here we will count the students numbers
    for obj in students_list:# for loop with a conditon(obj.country==anycountry, count as 1)
        count=count+1
        if obj.country=="Wales":
            wales=wales+1
        if obj.country=="England":
            england=england+1
        if obj.country=="Wales":
            scotland=scotland+1
            #everytime the conditon meets data get stored in print()function 
        obj.print()#printing the objects stored in class

#function to print the summary report
def summary_report():  
    #initial values kept at 0, records the no. of students from each country
    wales=0
    england=0
    scotland=0
    count=0 #here we will count the students numbers
    for obj in students_list:
        count=count+1
        if obj.country=="Wales":
            wales=wales+1
        if obj.country=="England":
            england=england+1
        if obj.country=="Wales":
            scotland=scotland+1
            #everytime for loop meets the conditon, counts as +1
        #skipping {obj.print()} command to avoid double print of the details
    print(' ___________________________________')
    print('|           Summary Report          |')
    print('|___________________________________|')
    print('Total numbers of students is:',count) #this will count the total no. of students
    print('Total numbers of students from Wales:',wales)#this will count the no. of students from Wales 
    print('Total numbers of students from England:',england)#this will count the no. of students from England
    print('Total numbers of students from Scotland:',scotland)#this will count the no. of students from Scotland     "         " "        ""

#eldest_youngest to print the youngest and eldest student and thier respective details
def eldest_youngest():
    print(' ___________________________________')
    print('|        Eldest & Youngest          |')
    print('|___________________________________|')
    eldest=students_list[0].age #taking the obj data from students_list
    youngest=students_list[0].age 
    for x in students_list: #excuting for loop with certain condition
        if(x.age>eldest): #value in x.age > eldest then it's the eldest age
            eldest=x.age
        if(x.age<youngest): #value in x.age < eldest then it's the youngest age
            youngest=x.age
    print(' ___________________________________')#printing the necessary output
    print('The eldest student(s) age is', eldest)
    print('The youngest student age is', youngest)
    print(' ___________________________________')
    for x in students_list: # for loop for printing the output output from above loop 
        if (x.age==youngest or x.age==eldest):
         x.print() #printing the output of eldest and youngest student(s)


def student_add():
    old_total_age=0 #initial value=0, records the totalage)
    old_count=len(students_list) #returning the length of students_list
    for x in students_list: #forloop with centain conditon 
      old_total_age=old_total_age+int(x.age) #calculating total age by adding total age+ (int) data in x.age
    old_avg_age=old_total_age/old_count #calculating the mean of the  Old students total age
    print(' ___________________________________')#menu to add new student
    print('|      Adding new students Data     |')
    print('|___________________________________|')
    id=input("Enter the New student's ID:")  #input command to add id
    fn=input("Enter the stdent's Firstname:")#   ""                fn
    ln=input("Enter the stdent's Lastname:") #    ""               ln
    age=input("Enter the stdent's Age:")     #    ""               age
    age=int(age)  #takes the (int) value only
    country=input("Enter the stdent's Origin:")#      ""          country
    new_student_data=student(id, fn, ln, age, country)
    students_list.append(new_student_data) #appends the old (students_list) data into (new_student_data)
    print("___________________________________")
    print("Data Added Successfully in the list")
    print("___________________________________")
    new_total_age=old_total_age+age #storing new data in variabe(new_total_age)
    new_avg_age=new_total_age/(old_count+1) #Calculating the mean of new total age
    print("The increase in the number of students: 1")
    print("Previous age average: ", round(old_avg_age, 2)) # printing & roundingup old age avrage
    print("New age average: ", round(new_avg_age, 2)) #printing & rounding up new average age
    print("Difference age average: ", round(new_avg_age-old_avg_age, 2)) #printing difference in (old average age- new average age)

#function 4 to search the student details using student's ID
def student_search():
    found=False #conditon using boolian
    id=input("Enter the student ID to search:") #userinput(ID)
    for x in students_list: #for loop to scan the ID given in each ID data of list
        if(x.id==id): #condition: given id== ids)
            print("Found and it's details are as follow")#prints found message to user
            x.print() #prints the detail that matches the ID 
            found=True  #meets the conditon TRUE
            break #breaks the loop
    if (found==False): #if not found,creates the conditon userinput==false & excutes this code 
     print("Sorry! The data you have entered does not match our record")#prints #not found message to user

#function to re-arrage the student details alphabetically using surname
def  sortby_age():
  n=len(students_list)  #returning the length of students_list
  for i in range (0,n): #for loop to see the value in each line[list i]
    for j in range(i+1,n): #for loop to see the value in each case[listj]
        #if stored value students_list[i].age>stuents_list[j].age, smaller value is kept on first
        if (students_list[i].age>students_list[j].age): #use this conditon unless every value is scanned and arranged
         c=students_list[i].age
         students_list[i].age=students_list[j].age
         students_list[j].age=c #comparing with data in [list c]
  print("___________________________________________________________")#printing the message
  print("All the data is sorted according to youngest to eldest age")
  print("___________________________________________________________")
  student_details() #excuting the (student_details) to rearrage according to codndition  

#bargraph to plot the barchart with: no. of students and their origin   
def bargraph():
    num_w=0 #This will record the number of students from wales 
    num_e=0
    num_s=0
    for x in students_list: #for loop with the codition (x.coutry==given country, count as +1)
        if(x.country=="Wales"):
            num_w=num_w+1
        if(x.country=="England"):
            num_e=num_e+1
        if(x.country=="Scotland"):
            num_s=num_s+1
    list_x=['Wales','England','Scotland'] #list to store the data of x-axis
    list_y=[num_w,num_e,num_s] #list to store the data of y-axis
    
    plt.title("'Students from different Country'",fontdict={'fontname': 'Rockwell', 'fontsize':"18"}) #giving the title of the bargraph with resppective font and text size
    plt.xlabel('Country of Origin',fontdict={'fontname': 'Arial', 'fontsize':"12"})          # giving the title of x label ""         ""               ""
    plt.ylabel('No. of Students',fontdict={'fontname': 'Arial', 'fontsize':"12"})          # giving the title of y label ""         ""               ""
    #label=wales labels the bar as indicator
    plt.bar('Wales',num_w, fill=False, hatch='..',label='Wales') #giving specefic design to bar "wales" with patten hatch'..' 
    plt.bar('England',num_e, fill=False, hatch='.O',label='England')  #giving specefic design to bar "England" with patten hatch'.O' 
    plt.bar('Scotland',num_s, fill=False, hatch='*', label='Scotland') #giving specefic design to bar "Scotland" with patten hatch'**' 
    plt.legend()
    plt.xticks(rotation=10) #gives specefic tilt design to the bottom title of country
    plt.grid(color='#000000',alpha=1, linestyle='--', linewidth=0.5) #pattern drawn with style='--' with width 0.5 and choosing colour black as code #000000 
    
    plt.show() #this will input the bargraph

#defining the mainmenu funciton to recall them with short code
def mainFunction(rt):
    #printing mainmenu with parameter (+rt+) just for extra style when we call the funciton again
    print(' ___________________________________________' )
    print("|     _______________________________       |")
    print("|    |Welcome "+rt+" to Sharad's Program|   |") 
    print("|    '--------------------------------'     |")
    print('|___________________________________________|')
    print('')
    print(" 1. View details of list of Students") #printing the mainmenu option 
    print(" 2. View details of the eldest and youngest student(s)")
    print(" 3. Option to add a new student and present a summary report")
    print(" 4. Search for the student on module output their details")
    print(" 5. Query the list to return students ordered in alphabetic order")
    print(" 6. Plot a labbelled bar chart of the students from each country")
    print(" 7. Exit")
    #(Userinput option from 1-7)
    userInput = input("Please make the selection from (1-7) to execute respective the task:")
    while(userInput): #(use of while loop with userinput condition)
     
        if(int(userInput)==1): #excutes (student_details() & summary_report() ), if user input==1 
            student_detail_title()#function to print the title only
            student_details() #student_details() to print details of students
            summary_report() #summary_report() to print summary report
            print("")
            print("")
            print("")
            mainFunction("back") # calling back main function with new title text(+rt+ as back)
        elif(int(userInput)==2): #excutes (eldest_youngest(), if user input==2 
            eldest_youngest()          #function to print the eldest and youngest student(s)
            print("")
            print("")
            mainFunction("back")# calling back main function with tect(+rt+ as back)
        elif(int(userInput)==3):#excutes (student_add(), if user input==3 
            student_add()         #function to add the data and print summary report
            print("")
            mainFunction("back") # calling back main function with tect(+rt+ as back)
            print("")
        elif(int(userInput)==4):#excutes student_search() , if user input==3 
            student_search()          #function 4 to search the student details using student's ID 
            print("")
            mainFunction("back") # calling back main function with tect(+rt+ as back)
            print("")
        elif(int(userInput)==5):#excutes sortby_age(), if user input==5 
            sortby_age()
            print("")
            mainFunction("back") 
            print("")
        elif(int(userInput)==6):#excutes student_add(), if user input==6 
            bargraph() #fucntion6() plots the bargraph
            mainFunction("back") # calling back main function with tect(+rt+ as back)
        if(int(userInput)==7): #breaks the while loop, if (userinput==7)       
             break #break while loop
        else:
            print('Please Wait! Exiting Program') #exits the programs if (user input==7)
            break     #breaks while loop with the exiting message
        
    
read_file() #This will read the file and store data in list of objects
#_______________________________Main Stars here________________________________
try: #Using try except to excute error message
 mainFunction("") #mainmenu starts here
except: #whenever program crashes, it will print this message and exit
    print("Either you made a mistake or gave wrong input")
    mainFunction("")


