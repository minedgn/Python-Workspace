#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Estimating the risk of death from coronavirus. Write a program that;

#Takes "Yes" or "No" from the user as an answer to the following questions :

#Are you a cigarette addict older than 75 years old? Variable → age

#Do you have a severe chronic disease? Variable → chronic

#Is your immune system too weak? Variable → immune

#Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).

age = input("Are you a cigarette addict older than 75 years old? (Yes / No): ").capitalize()



chronic = input("Do you have a severe chronic disease? (Yes / No): ").capitalize()



immune = input("Is your immune system too weak? (Yes / No): ").capitalize()



if age == "Yes":



    age = True



else:



    age = False



if chronic == "Yes":



    chronic = True



else:



    chronic = False



if immune == "Yes":



    immune = True



else:



    immune = False



if age and chronic or immune:



    print("You are in risk group")



else:



    print("You are not in risk group")








