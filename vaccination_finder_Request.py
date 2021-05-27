import requests
import time
import telegram_send

#define your get requests for the different vaccines here
astra="your astra zeneca GET request string here"
johnson = "your johnson and johnson GET request string here"

while True:
    try:
        resultAstra = requests.get(astra).text
        resultJohnson = requests.get(johnson).text
        if resultAstra != "[]": #check if result is not empty -> there should be an appointment available
            print("Astra appointment found!")
            telegram_send.send(messages=["There is a free vaccination appointment (astra zeneca)!"])   #send success message
            telegram_send.send(messages=["Link to the appointment service"])   #send link to appointment service
        elif resultJohnson != "[]": #check if result is not empty -> there should be an appointment available
            print("Johnson appointment found!")
            telegram_send.send(messages=["There is a free vaccination appointment (J&J)!"])    #send success message
            telegram_send.send(messages=["Link to the appointment service"])   #send link to appointment service
        else:
            print("no appointment found")
    except Exception as e:
        print(e)
    time.sleep(60)