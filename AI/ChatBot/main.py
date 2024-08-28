import nltk
from nltk.chat.util import Chat, reflections
import datetime


def get_current_time():
    return datetime.datetime.today().strftime('%H:%M:%S')


def get_current_date():
    return datetime.datetime.today().strftime('%Y-%m-%d')


# Você pode definir pares de padrões e respostas aqui
pairs = [
    (r'hi|hello', ['Hello! How can I assist you today?', 'Hi there!']),
    (r'what is your name?', ['I am a chatbot created to assist you.']),
    (r'how are you?', ['I am just a program, but I am doing well. How about you?']),
    (r'what date is today?', [f'Today is: {get_current_date()}', ]),
    (r'what time is it?', [f'Now is: {get_current_time()}'])
]

# Cria um chabot com as respostas definidas
chatbot = Chat(pairs, reflections)


def chat():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()
