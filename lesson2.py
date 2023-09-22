wsentence=input("Please enter a sentence:")
count=wsentence.split(" ")
print(len(count))

input("Press Enter to start MadLibs:")
name=input("Please enter your/a name:")
weather=input("Please enter a weather condition:")
noun1=input("Please enter a noun:")
noun2=input("Please enter another noun:")
verb1=input("Please enter a verb:")
verb2=input("Please enter another verb:")
number1=input("Please enter a number:")
number2=input("Please enter a greater number than the previous one before:")
celebrity=input("Please enter a celebrity to cameo in your story (preferably the Rock):")
input("Now, lets see what you've created:")
madlib = name, "was sleeping under a tree on a", weather, "day. Suddenly, a",  verb1, noun1,"and a", verb2, noun2, "appeared out of nowhere. After a while, the", verb1, noun1, "had started to a dance. This dance annoyed the,", verb2, noun2, "causing them to engage in a dance battle with you as the judge. Just a second, said a voice in the distance. As they came closer you started to make out the shape. It was", celebrity, "! I will help judge this intense dance battle.", noun1, "had started off strong by spinning on the ground giving it a rating of ", number1, ", but", noun2, "had done an advanced dancing technique by doing a backflip into breakdancing, giving it a ", number2, ". As the competition came to a close, you and", celebrity, "had to make a decision. And the winner is....., said", celebrity,". ", noun2, "! ", noun1, "had walked off into distance with their defeat while", noun2, "had celebrated."
print(madlib)

num=int(input("Please enter a number:"))
evenodd=num%2
if evenodd == 0:
    print("Even")
else:
    print("Odd")