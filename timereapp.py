import time
import smtplib

# Get user input in seconds
total_seconds = int(input("Enter the number of seconds: "))

# Print remaining time every second
while total_seconds > 0:
    print(f"Remaining time: {total_seconds} seconds")
    time.sleep(1)
    total_seconds -= 1

# Print "Time's up!"
print("Sending email........")


#enter your email here for sender
email = ''

#enter your email here for receiver
receiver_email = ''

#Enter your subject for email here
subject = ''

#enter your message here
message = ''

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# go to your gamil account and endable two factor authentica
#on the search bar , search for app passwords 
# create new app. give it a  name copy the name and paste it
server.login(email, "")

server.sendmail(email, receiver_email, text)

print("Email has been sent to " + receiver_email)

print("Good bye!!!")