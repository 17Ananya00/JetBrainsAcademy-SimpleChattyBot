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
