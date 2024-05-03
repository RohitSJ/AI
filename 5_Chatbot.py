import random

vocabulary = {
    "hola": "hello",
    "adiós": "goodbye",
    "por favor": "please",
    "gracias": "thank you",
    "sí": "yes",
    "no": "no",
    "agua": "water",
    "comida": "food",
    "casa": "house",
    "libro": "book",
    "uno": "one",
    "dos": "two",
    "tres": "three",
    "amigo": "friend"   
}

def start_lesson():
    print("Welcome to the Spanish vocabulary lesson!")
    print("Translate the following words from Spanish to English:")
    words = list(vocabulary.keys())
    random.shuffle(words)
    for word in words[:5]: 
        translation = input(f"What is the English translation of '{word}'? ")
        if translation.lower() == vocabulary[word]:
            print("Correct!")
        else:
            print(f"Sorry, the correct translation of '{word}' is '{vocabulary[word]}'.")

def main():
    print("Welcome to the Language Learning Chatbot!")
    print("I can help you learn Spanish vocabulary.")
    print("Type 'lesson' to start a new vocabulary lesson or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Come back soon.")
            break
        elif user_input.lower() == "lesson":
            start_lesson()
        else:
            print("I'm sorry, I didn't understand that. Please type 'lesson' to start a new lesson or 'exit' to quit.")

if __name__ == "__main__":
    main()