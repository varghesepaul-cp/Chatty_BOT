import sys

question = sys.argv[1]

# print("Q And A Engine Triggered ")


# print("Question is " , question)

if("weather" in question):
    print("Weather is very very sunny in the month of April in India. ")

elif("hi" in question):
    print("Hi there , Whats up !")

elif("hello" in question):
    print("Hello there , Whats up !")

elif("good evening" in question):
    print("Hello there , Good Evening Champ !")

else:
    print("Sorry , I didn't understand that ! Still in Learning Phase ")