name =input("enter your name: ")
print(f"welcome chatbot dear {name},\nhow can i help you {name} \nwrite  \"exit\" to leave from our chatbot ")
responses ={
  "hi":"hi there!",
    "hello":f"hello there! {name}",
    "assalam u alaikum":f"wa alaikum assalam {name}",
    "how are you?": f"i am fine dear {name}, how about you?",
    "what are you doing?":f"i am talking with you {name} now.",
    "what's up?":f"i am talking with you {name} now."
}
while True:
    user_input = input("you: ").lower().strip()
    if user_input == "exit":
        print(f"good bye {name}")
        break 
    elif user_input in responses:
        print(f"Chatbot: {responses[user_input]}")
        continue
    found = False
    for key in responses:
        if key in user_input or user_input in key:
            print(f"bot:{responses[key]}")
            found = True
            break
    if not found:
        print(f"Chatbot: I don't understand {user_input}, {name}")