from knockknock import email_sender


@email_sender(recipient_emails=["youremail@gmail.com", "your_teammate@address.com"], sender_email="anotheremail@gmail.com")
def main():
    even_arr = [i for i in range(10000) if i%2==0]

if __name__=='__main__':
    main()

