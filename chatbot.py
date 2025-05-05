# Install necessary packages
# !pip install gTTS ipywidgets --quiet
# run in google colab
# import necessary libraries
from gtts import gTTS
from IPython.display import Audio, display, clear_output
import re
import ipywidgets as widgets

# Response dictionary
responses = {
    "hi": "Hello! How can I assist you today Musthak?",
    "hello": "Hi there! What would you like to know or talk about?",
    "how are you": "I'm just a bot, but I'm running smoothly! How about you?",
    "what is your name": "I'm ChatBot, your friendly assistant here to help with anything.",
    "help": "I'm here to assist you! You can ask me things like 'hi', 'how are you', 'what is your name', or even 'bye' to exit. How can I help?",
    "thanks": "You're very welcome! Let me know if you need more help.",
    "thank you": "Glad I could help! If you have more questions, feel free to ask.",
    "default": "I'm sorry, I didn't quite catch that. Could you please rephrase your question?",
}

# Chatbot response logic
def chat_bot_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if re.search(rf'\b{keyword}\b', user_input):
            return responses[keyword]
    return responses["default"]

# Speak the response
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    display(Audio("response.mp3", autoplay=True))

# Interactive chatbot UI
def chatbot():
    print("Chatbot 🤖: Hello! I'm here to assist you. Type 'bye' to exit.")
    speak("Hello! I'm here to assist you. Type bye to exit.")

    input_box = widgets.Text(
        value='',
        placeholder='Type your message and press Enter...',
        description='You:',
        disabled=False
    )

    output_area = widgets.Output()

    def on_enter(sender):
        with output_area:
            clear_output(wait=True)
            user_input = input_box.value.strip()
            if user_input.lower() == "bye":
                print("Chatbot 🤖: Goodbye! 👋 Have a great day!")
                speak("Goodbye! Have a great day!")
                input_box.disabled = True
            else:
                response = chat_bot_response(user_input)
                print(f"You 🙋: {user_input}")
                print(f"Chatbot 🤖: {response}")
                speak(response)
                input_box.value = ""  # Clear for next input

    input_box.on_submit(on_enter)

    display(input_box, output_area)

# Run the chatbot
chatbot()
