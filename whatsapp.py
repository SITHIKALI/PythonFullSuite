'''
import pywhatkit
pywhatkit.sendwhatmsg("+918940542016","Welcome to WhatsApp Automation",22,40)
'''
import pywhatkit
import datetime
import time
import webbrowser
from urllib.parse import quote
import os
import sys

def send_whatsapp_message(phone_number, message, hour, minute):
    """Sends a WhatsApp message at a specified time.

    Args:
        phone_number (str): The recipient's phone number with country code (e.g., +15551234567).
        message (str): The message to send.
        hour (int): The hour (24-hour format) to send the message.
        minute (int): The minute to send the message.
    """
    try:
        # Calculate the delay until the specified time
        now = datetime.datetime.now()
        scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if scheduled_time < now:
            scheduled_time += datetime.timedelta(days=1)  # Schedule for the next day if the time has passed

        delay_seconds = (scheduled_time - now).total_seconds()

        if delay_seconds > 0:
            print(f"Waiting {delay_seconds:.0f} seconds to send the message...")
            time.sleep(delay_seconds)

        # Open WhatsApp web in a new browser window
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(10)  # Give WhatsApp Web time to load (adjust as needed)

        # Construct the WhatsApp message URL
        message_encoded = quote(message)  # URL encode the message
        whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message_encoded}"

         # Open the URL in the browser
        webbrowser.open(whatsapp_url)
        time.sleep(5)  # Allow time for the chat to open

        # Simulate pressing Enter to send the message (this might not work reliably)
        # You might need a more robust solution for sending the message automatically
        # using libraries like Selenium or PyAutoGUI for better control over the browser.
        # The following is a basic attempt and might require user interaction.

        print("Message should be in the textbox. Please send manually if it's not sent automatically.")
        # Optionally, you could add code here to try to send the message using
        # keyboard automation (e.g., using PyAutoGUI to focus the chat window
        # and press Enter).  However, this is highly dependent on the
        # specific layout of WhatsApp Web and might break easily.

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Get user input
    phone_number = input("Enter the recipient's phone number with country code (e.g., +15551234567): ")
    message = input("Enter the message to send: ")
    hour = int(input("Enter the hour (24-hour format) to send the message: "))
    minute = int(input("Enter the minute to send the message: "))

    send_whatsapp_message(phone_number, message, hour, minute)
    print("The program has finished.  Check WhatsApp Web to see if the message was sent.")