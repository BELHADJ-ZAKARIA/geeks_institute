"""
Exercise 1 : Outputs

Predict the output of the following code snippets:
"""

3 <= 3 < 9                        >>> TRUE

3 == 3 == 3                       >>> TRUE

bool(0)                           >>> FALSE

bool(5 == "5")                    >>> FALSE

bool(4 == 4) == bool("4" == "4")  >>> TRUE

bool(bool(None))                  >>> FALSE

x = (1 == True)                   >>> TRUE
y = (1 == False)                  >>> FALSE
a = True + 4                      >>> 5
b = False + 10                    >>> 10

print("x is", x)                  >>> x is True
print("y is", y)                  >>> y is False
print("a:", a)                    >>> a: 5
print("b:", b)                    >>> b: 10

"""
Exercise 2 : Longest word without a specific character

Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
"""

import string

sentence = []
count = 0
score = 0

print("Longest word without a specific character")
print("Entre \"x\" for quit this challenge\n")

while (True):
  sentence = input("Enter the longest sentence you can without usnig the character \"A\" : ")
  
  if "A" in sentence.upper():
    print("Attention! there's in A character on your sentence.\n")
    continue

  if sentence.upper() == "X": break

  cleaned_list = list(filter(str.strip, sentence))

  for i in cleaned_list:
    for char in i:
      if char in string.punctuation:
        cleaned_list.remove(i)
  
  for i in cleaned_list:
    count += 1
    
  if count > score:
      score = count
      print("Congratulations you have NEW SCORE!\n")
  else:
    print("Try Again\n")

  count = 0
