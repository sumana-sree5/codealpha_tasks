import time
import random

def chatbot():
    print("🤖 Chatbot: Hello! I am a rule-based assistant created for my CodeAlpha Internship. Type 'bye' to exit.")
   
    responses = {
        "hello": ["Hi there!", "Greetings!", "Hello! How can I help you today?"],
        "how are you": ["I'm doing well, running smoothly!", "Great! Ready to assist you."],
        "what is your name": ["I am the CodeAlpha Python Bot.", "You can call me AlphaBot!"],
        "tell me a joke": [
            "Why do programmers wear glasses? Because they can't C#!",
            "There are 10 types of people: those who understand binary, and those who don't."
        ],
        "career advice": ["Keep building projects, push your code to GitHub, and never stop learning!"],
    }

    while True:
        user_input = input("\nYou: ").lower().strip()
       
        if user_input == 'bye':
            print("🤖 Chatbot: Goodbye! Have a fantastic day!")
            break
           
        # Fallback conditional logic matching keys
        matched = False
        for key in responses:
            if key in user_input:
                time.sleep(0.3) # Simulates thinking delay
                print(f"🤖 Chatbot: {random.choice(responses[key])}")
                matched = True
                break
               
        if not matched:
            print("🤖 Chatbot: I am a simple bot and didn't quite catch that. Try asking for a 'joke' or 'career advice'.")

if __name__ == "__main__":
    chatbot()
