#program
#by Nitin and Aditya
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@___________IMPORTED MODULES__________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import colorama

import turtle

import time
from datetime import date

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@____________FUNCTIONS______________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def color(colr,text):
    
    '''function to colour the text
    parameters-colr(to set the colour)
              -text(text that is to be coloured)'''
    
    if colr=="blue":
        print colorama.Fore.BLUE+text,
    elif colr=="red":
        print colorama.Fore.RED+text,
    elif colr=="green":
        print colorama.Fore.GREEN+text,
    elif colr=="yellow":
        print colorama.Fore.YELLOW+text,
    elif colr=="white":
        print colorama.Fore.WHITE+text,
    elif colr=="magenta":
        print colorama.Fore.MAGENTA+text,
    elif colr=="cyan":
        print colorama.Fore.CYAN+text,
        
    decolor()

    
def decolor():
    
    '''function to decolor the text'''
    
    print colorama.Fore.WHITE+""

    
def line(Type,num=210,col="white"):
    
    '''function to print diff types of lines'''
    
    if Type==1:
        color(col,"$"*num)
    elif Type==2:
        color(col,"*"*num)
    elif Type==3:
        color(col,"@"*num)
    elif Type==4:
        print                      #blank line


def center(num=10):
    
    '''function to center align text'''
    
    print "\t"*num,

    
def main_menu():

    """function thats calls main menu which shows a list of operations"""
    
    line(2)
    center()
    color("yellow","MAIN MENU")
    line(2)
    line(4)
    color("cyan","[1] Now Showing")
    color("cyan","[2] Buy Ticket")
    color("cyan","[3] Login(only for officials)")
    color("cyan","[4] Exit")
    line(4)
    try:
        choice=int(raw_input("Please proceed with your choice: "))
        line(4)
        
        if choice==1:
            now_showing()
            delay=raw_input("Press enter to continue: ")
            main_menu()
                
        if choice==2:
            line(4)
            line(2)
            center()
            color("yellow","BUY TICKET")
            line(2)
            line(4)
            now_showing()
            file=open("movies.txt","r")
            movie_det=file.readlines()
            movie_buy=int(raw_input("Enter the movie number: "))-1
            tick_buy=int(raw_input("Enter the number of tickets: "))
            for i in range(0,len(movie_det)):
                if movie_buy==i:
                    mov=movie_det[i].split("~")
            total=int(mov[1])*tick_buy
            delay=raw_input("Press Enter to view the ticket: ")
            file.close()
            preview(mov[0],str(total),str(mov[2]))
                
        if choice==3:
            login()
                                
                                
    except:
        line(4)
        color("red","PLEASE ENTER VALID INPUT !!!!!!!!!!!!!!!!")
        line(4)
        main_menu()


def now_showing():

    '''function now_showing to view the movies available'''
    
    line(2)
    center()
    color("blue","NOW SHOWING")
    line(2)
    ofile=open("movies.txt","r")
    movies=ofile.readlines()
    i=1                                     #for numbered bullets
    for movie in movies:
        mov=movie.split("~")
        print "["+str(i)+"] "+mov[0]
        i=i+1
    ofile.close()
    line(2)

    
def login():
    
    '''function for editing the movie and login file'''

    line(2)
    center()
    color("yellow","LOGIN")
    line(2)
    ifile=open("logins.txt","a+")
    lines=ifile.readlines()
    name=raw_input("Enter the login name: ")
    password=raw_input("Enter the password: ")
    for logins in lines:
        logins.rstrip()
        details=logins.split("~")
        if name==details[0] and password==details[1]:
            ifile.close()
            line(4)
            print "Hello",name
            line(4)
            line(1)
            line(4)
            color("magenta","[1] Add movie ")
            color("magenta","[2] Add user ")
            color("magenta","[3] To return to the main menu ")
            line(4)
            line(1)
            line(4)
            ch=int(raw_input("Please proceed with your choice: "))
            line(4)
            if ch==1:
                ifile2=open("movies.txt","a")
                ans="y"
                while ans=="y":
                    mov_name=raw_input("Enter the new movie name: ")
                    mov_price=int(raw_input("Enter the ticket price: "))
                    mov_hall=raw_input("Enter the Hall number: ")
                    ifile2.write(mov_name+"~"+str(mov_price)+"~"+mov_hall+"~"+"\n")
                    ans=raw_input("do you want to add more movies?(y/n): ")
                    line(4)
                ifile2.close()
                main_menu()    
            
            elif ch==2:
                ifile=open("logins.txt","a")
                ans="y"
                while ans=="y":
                    tname=raw_input("Enter the new login name: ")
                    tpass=raw_input("Enter the new password: ")
                    ans=raw_input("do you want to add more users?(y/n): ")
                    ifile.write(tname+"~"+tpass+"~"+"\n")
                ifile.close()
                main_menu()
            elif ch==3:
               main_menu()

      
def preview(name,total,hall):

    """function preview to check the show details before printing ticket
        parameters-name(movie name)
                  -total(total price of tickets)
                  -hall(hall no.)"""
    
    t1= date.today()                        #to get the current date from the system                                      
    t=str(t1)
    
    turtle.begin_fill()                                                              
    turtle.bgcolor("black")
    turtle.pensize(5)
    turtle.pu()
    turtle.color("yellow")
    turtle.write("G  E  E  T   T  A  L  K  I  E  S ")
    turtle.lt(90)
    turtle.bk(40)
    turtle.color("white")
    turtle.write("M  O  V  I  E -"+name)
    turtle.bk(20)
    turtle.write("D  A  T  E -"+t)
    turtle.bk(20)
    turtle.write("H  A  L  L   N  U  M  B  E  R  - "+hall)
    turtle.bk(20)
    turtle.write("T  O  T  A  L -"+"R s ."+total)
    turtle.bk(20)
    turtle.color("green")
    turtle.write("Y  O  U  R   T  I  C  K  E  T   H  A  S   B  E  E  N   B  O  O  K  E  D")
    turtle.bk(20)
    turtle.color("yellow")
    turtle.write("T  H  A  N  K   Y  O  U")
    turtle.color("white")
    turtle.bk(20)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(450)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(450)
    
    
    
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@____________MAIN____________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

colorama.init()                     #to run colorama module in windows

line(3)
center(9)
color("green","CINEMA TICKET BOOKING SYSTEM")
line(3)
line(4)
line(4)

main_menu()

color("blue","THANK YOU FOR USING CINEMA BOOKING SYSTEM")
line(3)

delay=raw_input("Press enter to close the program: ")

