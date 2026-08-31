import random
greetings_input = ["HELLO", "HI", "HEY", "GREETINGS", "GOOD MORNING", "GOOD AFTERNOON", "GOOD EVENING"]
greetings_reply = ["Hi!", "Hello", "Hey there", "Good to see you"]
wel_being = ["I'M FINE, THANK YOU", "I'M DOING WELL", "I'M GOOD"]
goodbye_input = ["BYE", "GOODBYE", "SEE YOU"]
goodbye_reply = ["Goodbye", "See you later", "Bye bye"]
while True:
    user_input = input("Enter your message: ").upper()
    if user_input in greetings_input:
        print(random.choice(greetings_reply))
    elif "HOW ARE YOU" in user_input:
        print(random.choice(wel_being))
    elif user_input in goodbye_input:
        print(random.choice(goodbye_reply))
        break
    else:
        print("I don't understand that.")