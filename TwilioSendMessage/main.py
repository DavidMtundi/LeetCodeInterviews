# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from twilio.rest import Client


def print_hi(name):
    account_sid = 'ACf680bd0754107cf04ca2505c7a3ee1de'
    auth_token = '4961fb696ec8f8a0f02058c82e57ee71'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12029525927',
        body='name: John Main, ward No:5, Bed No: 13 Condition: (Breathing rate:10, Temperature:37,Pressure:120/80, '
             'Heart Rate: 40, Camera Vision: OK), Status: Ready for Discharge',
        to='+254740204736'
    )

    print(message.sid)

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, Message sent job has {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Completed Successfully')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
