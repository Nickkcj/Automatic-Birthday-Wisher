import smtplib
from readcsv import check_birthday
import random

birthday_name, birthday_email = check_birthday()

if birthday_name:
    my_email = "nickcesar073@gmail.com"
    my_password = "password" #Here you can use the app password, making less secure apps able to access the email.
    birthday_letter = random.randint(1,3)

    with open(f"letter_templates/letter_{birthday_letter}.txt", "r") as letter:
        letter_data = letter.read()
    
    letter_data = letter_data.replace('[NAME]', f'{birthday_name}')
        
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                         to_addrs=f"{birthday_email}", 
                         msg=f"Subject:Happy Birthday!\n\n{letter_data}")
    