# tutorial5

# term1 input
print("# # # Term 1 # # #")
A=int(input("AES:"))
M=int(input("Maths 1:"))
P=int(input("Physics 1:"))
C=int(input("Computer Programming 1:"))
print("Thank you, Term 1 is inputted.")

#term2 input
print("# # # Term 2 # # #")
A2=int(input("AES:"))
M2=int(input("Maths 2:"))
P2=int(input("Physics 2:"))
C2=int(input("Computer Programming 2:"))
print("Thank you, Term 2 is inputted.")

#term3 input
print("# # # Term 3 # # #")
A3=int(input("AES:"))
M3=int(input("Maths 3:"))
P3=int(input("Physics 3:"))
C3=int(input("Computer Programming 3:"))
print("Thank you, Term 3 is inputted.")
Average=(A+M+P+C+A2+M2+P2+C2+A3+M3+P3+C3)/12

#check the score
if A<0 or A>100 or M<0 or M>100 or P<0 or P>100 or C<0 or C>100 or A2<0 or A2>100 or M2<0 or M2>100 or P2<0 or P2>100 or C2<0 or C2>100 or A3<0 or A3>100 or M3<0 or M3>100 or P3<0 or P3>100 or C3<0 or C3>100:
    print("That is not a valid input. Goodbye.")
elif A<40 or M<40 or P<40 or C<40 or A2<40 or M2<40 or P2<40 or C2<40 or A3<40 or M3<40 or P3<40 or C3<40:
    print("Sorry, you don't progress because you must have at least 40%.")
elif Average<60:
    print("Sorry, you don't progress because you must have at least an average of 60%.")
elif ((M2+M3)/2)<65:
    print("Sorry, you don't progress because you must have at least an average of 65% of maths.")
elif A3<60:
    print("Sorry, you don't progress because you must have at least 60% of AES.")
else:
    print("WELL DONE! YOU PROGRESS!")
    if A==100 and M==100 and P==100 and C==100 and A2==100 and M2==100 and P2==100 and C3==100 and A3==100 and M3==100 and P3==100 and C3==100:
        print("WOW, you are so smart! 100 in everything.")

quit()
