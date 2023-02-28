## Print a text art image of a robot
print(r"""
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\) 
""")

## The robot outputs a message to the user when the program runs using the print statement
print("I'm a Binary Chatbot!")

## The robot outputs a message to the user when the program runs asking the user to input a question
## The user can type text, and press return to send the text as input to the python program
user_input = input("Ask me a question and I'll answer in Binary ")

## The Python program recieves the user message input and stores them in a variable called user_words, 
user_words = user_input

## Create a variable called bot_response set to a response the binarybot will output
bot_response = ("Wow you know a lot about ")

## Covert the bot_response string to binary. 
bot_response_binary = ' '.join(map(bin,bytearray(bot_response,'utf8')))

## Covert the user_words string to binary
user_words_binary = ' '.join(map(bin,bytearray(user_words,'utf8')))

## Prints the binary conversion of bot_response and the user_words variables as output. 
print(bot_response_binary + user_words_binary)