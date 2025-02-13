# 🎉 Birthday Email Automation

A simple Python script that automatically sends birthday wishes via email using the `smtplib` library. It extracts data from a CSV file using `pandas`, checks if today matches any birthday using `datetime`, and then selects a random email template to send a personalized message. 🎂📧

---

## 🚀 Features
- 📅 Reads birthdays from a CSV file
- 🛠 Uses `pandas` to extract the month and day
- ⏰ Compares with the current date using `datetime`
- ✨ Picks a random email template
- 📩 Sends a personalized email via SMTP

---

## 📂 Project Structure
```
📁 Birthday_Email_Automation
│-- 📄 main.py            # Main script
│-- 📄 birthdays.csv      # CSV file with birthday data
│-- 📄 letter_templates/  # Folder containing email templates
│-- 📄 readcsv.py         # Script to read csv using pandas
```

---

## 🔧 Installation & Usage
### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### 2️⃣ Prepare the CSV File
Your `birthdays.csv` should contain columns like this:
```csv
name,email,month,day
John Doe,johndoe@example.com,2,13
Jane Smith,janesmith@example.com,7,29
```

### 3️⃣ Run the Script
Simply execute the script:
```bash
python main.py
```

---

## 📧 Email Templates
The script picks one of three pre-written email templates and replaces `{{NAME}}` with the recipient’s name before sending.
Example:
```
Subject: Happy Birthday 

Hey [NAME],
Wishing you a fantastic birthday filled with joy and laughter! 🥳

```

---

## 🎯 Future Improvements
- ✅ Add support for attachments (e.g., birthday images)
- ✅ Fetch birthdays from an online database
- ✅ Send SMS or WhatsApp messages instead of emails

---
