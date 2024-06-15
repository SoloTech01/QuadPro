import time
import sys
import os
os.system("clear")
print(""" \033[92m
░██████╗░██╗░░░██╗░█████╗░██████╗░██████╗░██████╗░░█████╗░
██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╗██║██║░░░██║███████║██║░░██║██████╔╝██████╔╝██║░░██║
╚██████╔╝██║░░░██║██╔══██║██║░░██║██╔═══╝░██╔══██╗██║░░██║
░╚═██╔═╝░╚██████╔╝██║░░██║██████╔╝██║░░░░░██║░░██║╚█████╔╝
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░  
""")
print("\033[1;33;40mLoading....")
time.sleep(2)
print("\033[1;36;40m======" * 10)
print("""\033[1;36;40m[+] Created by Solomon Adenuga
[✓] QuadPro is a mathematical tool for solving quadratic equations""")
def quadpro(x,y,z):
    	     valid = False
    	     while not valid:
    	     	try:
    	     		 root_one = (-y +  (((y ** 2) - (4 * x * z)) ** 0.5)) / (2*x)
    	     		 root_two = (-y -  (((y ** 2) - (4 * x * z)) ** 0.5)) / (2*x)
    	     		 l = (y ** 2) - (4 * x * z)
    	     		 print("\033[92mCalculating......")
    	     		 time.sleep(2)
    	     		 print(f"The roots of the quadratic equation in real numbers are: {root_one.real:,.2f} and {root_two.real:,.2f}")
    	     		 print(f"The roots of the quadratic equation in complex numbers are: {complex(root_one):,.6f} and {complex(root_two):,.6f}")
    	     		 response = input("\nTo see a detailed solution to this equation,enter 's' or 'q' to quit: ")
    	     		 if response.lower().strip() == "s":
    	     		 	print("\033[1;33;40mGenerating Solution....")
    	     		 	time.sleep(2)
    	     		 	print(f"""\n\033[92mSOLUTION:
FORMULA: (-b ± √(b^2 - 4ac)) / 2a
a = {x}, b = {y}, c = {z}
SOLVING b² - 4ac: {y}² - (4 x {x} x {z}) = {y**2} - {4*x*z} = {l}
(-{y} + √{l}) / (2 x {x}) or (-{y} - √{l}) / (2 x {x})
-{y} + {(l**0.5).real:,.2f} / {2*x} or -{y} - {(l**0.5).real:,.2f} / {2*x}
{-y + (l**0.5).real:,.2f} / {2*x} or {-y - (l**0.5).real:,.2f} / {2*x}
ANSWER: {root_one.real:,.2f} or {root_two.real:,.2f}
                          OR
IN COMPLEX NUMBERS: -{y} + {l**0.5:.2f} / {2*x} or -{y} - {l**0.5:.2f} / {2*x}
{-y + (l**0.5):,.6f} / {2*x} or {-y - (l**0.5):,.6f} / {2*x}
ANSWER: {complex(root_one):,.6f} and {complex(root_two):,.6f}
""")
    	     		 elif response.lower().strip() == "q":
    	     		 	print("\033[1;31;40mquitting....")
    	     		 	time.sleep(2)
    	     		 valid = True
    	     	except ZeroDivisionError:
    	     		print("\033[1;31;40m An error occured!")
    	     		print("\033[92m`  Detecting error.....")
    	     		time.sleep(3)
    	     		print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
    	     
def program_intro():
    	print("\033[1;36;40m======" * 10)
    	valid = False
    	while not valid:
    		try:
    			time.sleep(2)
    			print("\n")
    			a = int(input("\033[1;36;40mEnter the value of a: "))
    			b = int(input("Enter the value of b: "))
    			c = int(input("Enter the value of c: "))
    			valid = True
    		except (ValueError,TypeError):
    			print("\033[1;31;40m An error occured!")
    			print("\033[92m`  Detecting error.....")
    			time.sleep(3)
    			print("\033[1;31;40m ENTER VALID NUMBERS!!")
    		except ZeroDivisionError:
    			print("\033[1;31;40m An error occured!")
    			print("\033[92m`  Detecting error.....")
    			time.sleep(3)
    			print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
    	print(f"\033[1;33;40mThe quadratic equation is {a}x² + {b}x + {c} = 0")
    	confirm = input("Enter 'c' to continue or 'q' to quit: ")
    	if confirm == "c":
    		quadpro(a,b,c)
    	else:
    		time.sleep(2)
    		print("\033[1;31;40mOPERATION CANCELLED!")
    		sys.exit()
while True:
	program_intro()