
import random
number = ['2', '3', '5', '7', '11', '13', '17', '19', '101']
lucky_number = random.choice(number)
print(f"Welcom To Coding-Decoding! Your Lucky Number is: {lucky_number}\n")


symbols=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '"', 
         '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
         ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']





def magic_code(text,encode_decode,shift_value):

    output_text=""
    if encode_decode =="decode":
        shift_value *= -1

    for char in text:
        if char not in symbols:
            output_text += char
        else:
            shifted_position = symbols.index(char) + shift_value
            shifted_position %= len(symbols)
            output_text += symbols[shifted_position]

    print(f"Your {direction}d message is : {output_text}. \n")


should_continue = True
while should_continue:

    direction = str(input("Type 'encode' for encoding or Type 'decode' for decoding:  \n")).lower()
    plain_text = (input("Type your message:  \n")).lower()
    shift = int(input("Type your shift number:  \n"))
    magic_code(text=plain_text, encode_decode=direction, shift_value=shift)

    restart = str(input("Type 'yes' for continue; or Type 'no' for stop:  \n" ))
    if restart =="no":
        should_continue = False
        print("Good byee!")



