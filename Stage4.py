print("Hello! My name is Aid." + "\n" +
      "I was created in 2020.");
print("Please, remind me your name.")
userName = input();
print("What a great name you have, " + userName + "!");
print("Let me guess your age." + "\n" +
      "Enter remainders of dividing your age by 3, 5 and 7.");
remainder3 = int(input());
remainder5 = int(input());
remainder7 = int(input());
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
stringAge = str(age);
print("Your age is " + stringAge + ";" + " that's a good time to start programming!");
print("Now I will prove to you that I can count to any number you want.");
number = int(input());
for i in range(0, number + 1):
    print(str(i) + " " + "!");
print("Completed, have a nice day!");