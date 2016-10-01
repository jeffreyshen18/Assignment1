# File Name: Part2.py
# AUthor: Jeffrey Shen
# Student Identification: 10153021
# Tutorial number: T04

print("Please enter your marks below.")
#prompt user for mini A1 grade
minia1input = input("Mini A1:")
minia1 = float(minia1input)
#prompt user for mini A2 grade
minia2input = input("Mini A2:")
minia2 = float(minia2input)
#prompt user for mini A3 grade
minia3input = input("Mini A3:")
minia3 = float(minia3input)
#promt user for mini A4 grade
minia4input = input("Mini A4:")
minia4 = float(minia4input)
#promt user for mini A5 grade
minia5input = input("Mini A5:")
minia5 = float(minia5input)
#promt user for mini A6 grade
minia6input = input("Mini A6:")
minia6 = float(minia6input)
#promt user for mini A7 grade
minia7input = input("Mini A7:")
minia7 = float(minia7input)
#promt user for mini A8 grade
minia8input = input("Mini A8:")
minia8 = float(minia8input)
#promt user for full A1
A1input = input("Full A1:")
a1= float(A1input)
#promt user for full A2
A2input = input("Full A2:")
a2 = float(A2input)
#promt user for full A3
A3input = input("Full A3:")
a3 = float(A3input)
#promt user for full A4
A4input = input("Full A4:")
a4 = float(A4input)
#promt user for full A5
A5input = input("Full A5:")
a5 = float(A5input)
#Prompt user for midterm grade
midterminput = input("Midterm exam:")
midterm = float(midterminput)
#prompt user for final grade
finalexaminput = input("Final exam:")
finalexam = float(finalexaminput)
#provide user with weighted grades
print("-------------------------------------------")
minigrade = minia1*0.005+minia2*0.005+minia3*0.005+minia4*0.005+minia5*0.005+minia6*0.005+minia7*0.005+minia8*0.005
print("Weighted mini assignment grade: ", format (minigrade, ".2f"))
assignmentgrade = a1 * 0.02 + a2 * 0.05 + a3 * 0.06 + a4 * 0.1 +a5 *0.08
print("Weighted full assignment grade: ", format (assignmentgrade, ".2f"))
midtermgrade = midterm *0.25
print("Weighted midterm exam grade: ",format(midtermgrade, ".2f"))
finalexamgrade = finalexam*0.4
print("Weighted final exam grade: ", format (finalexamgrade, ".2f"))
#provide user with weighted term grade
print("------------------------------------------")
termgrade = minigrade + assignmentgrade + midtermgrade + finalexamgrade
print("Weighted term grade: ", format(termgrade, ".2f"))
