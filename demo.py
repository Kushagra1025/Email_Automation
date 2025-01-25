import pandas as pd
import email_functions
import main_file


# Exporting email data to MySQL
ls=email_functions.fetch_emails_from_folder("[Gmail]/Spam")
df = pd.DataFrame(ls, columns=[ 'Subject','From','Date'])
email_functions.export_to_mysql(ls, "spamEmails")


# Example query to read from MySQL
query = "SELECT Sender, COUNT(Sender) FROM spamEmails GROUP BY Sender"
# storing the fetched information into DataFrame s1
s1 = email_functions.read_sql_to_dataframe(query)
print(s1)


# Defining recipient emails and recipient names
recipient_emails = ["emailfortesting1025@gmail.com", "kushagraofficialpurpose@gmail.com","10.feelatitspeak.25@gmail.com","emailforprivacy9@gmail.com"]
names=["Kushagra","Anshul","Shreyansh","Akshat"];


# Sending a bulk of common emails
email_functions.send_common_emails(recipient_emails, "Test Email", "Hi, this is a test email" )


# Sending a bulk of distinct emails
email_functions.send_distinct_emails(recipient_emails,names,"Test Email")


# Establishing connection with Gmail
imap=main_file.connect_to_imap("imap.gmail.com")
# Fetching emails from the desired folder
starred_emails=main_file.fetch_emails(imap,"[Gmail]/Starred")
# Moving the required email to the desired folder
main_file.move_email(imap,starred_emails[0], "[Gmail]/Spam")