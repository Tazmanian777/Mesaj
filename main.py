from flask import Flask, jsonify
from datetime import datetime, timedelta
import pytz
import os
import random

app = Flask(__name__)

def generate_message():
    # Set the Romanian timezone
    romania_tz = pytz.timezone("Europe/Bucharest")
    
    # Get the current date and time in Romania
    current_time = datetime.now(romania_tz)
    
    # Add 91 minutes to calculate the expiration time
    expiration_time = current_time + timedelta(minutes=91)
    
    # Format the expiration date and time
    expiration_date = expiration_time.strftime("%d/%m/%Y")
    expiration_hour = expiration_time.strftime("%H:%M")
    
    # Generate a random ticket code with the format x-xxxxxxx-x
    random_code = f"{random.randint(1, 9)}-{random.randint(1000000, 9999999)}-{random.randint(1, 9)}"
    
    # Generate the message with actual new lines
    message = (
        f"Biletul pe liniile metropolitane a fost activat. "
        f"Valabil pana in {expiration_date} ora {expiration_hour}. "
        f"Cost 0.65 EUR+TVA. Cod {random_code}.\n"
        f"Detalii 021-9391\n"
        f"Calatorie placuta!"
    )
    
    return message

@app.route("/generate", methods=["GET"])
def generate():
    message = generate_message()
    return message, 200, {"Content-Type": "text/plain"}

import os

if __name__ == "__main__":
    # Get the PORT environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

