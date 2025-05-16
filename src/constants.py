# src/constants.py

from enum import Enum

# Load environment variables from .env file
# load_dotenv()

MAILERSEND_API_KEY = "" 

MAILERSEND_BASEURL = "https://api.mailersend.com/v1/"

class AttachmentDisposition(Enum):
    ATTACHMENT = 1
    INLINE = 2

# FROM_EMAIL = "your_verified_sender@yourdomain.com"
TO_EMAIL = "" # "recipient@example.com"
TO_NAME = ""

SUBJECT = "API SDK Test Email"
BODY = "Hi"
PLAIN_BODY = "Hi"
HTML_BODY = "<p>Hi</p>"

SUBJECT2 = "Test Mail from {$company} Client"
PLAIN_BODY2 = "This is the plain text content for {$name}. Has Problem Solving Agents pdf Attachment"
HTML_BODY2 = "<p>This is the HTML content for {$name}.</p>"

SUBJECT3 = "Ok Test Mail Local Python"
PLAIN_BODY3 = "Plain Text pdf Attachment - Ok"
HTML_BODY3 = "<p>HTML Text pdf Attachment - Ok</p>"

MAILERSEND_SMTP_USER=""# os.getenv("MAILERSEND_SMTP_USER")
MAILERSEND_SMTP_USER_PASSWORD="" #os.getenv("MAILERSEND_SMTP_USER_PASSWORD")

# ATTACHMENT_PATH_DMY = "C:\\Users\\Administrator\\Documents\\testsdir\\dummytestpdf.pdf"
# ATTACHMENT_PATH_T = "C:\\Users\\Administrator\\Documents\\testsdir\\lpalgo.pdf" #"example.xlsx"  # Set to None if you don't want to attach anything
# ATTACHMENT_PATH_PSA = "C:\\Users\\Administrator\\Documents\\testsdir\\psa.pdf" #"example.xlsx"  # Set to None if you don't want to attach anything
# ATTACHMENT_PATH_NL = "C:\\Users\\Administrator\\Documents\\testsdir\\SampleMonthlyBudget.xlsx"
ATTACHMENT_PATH = "" # ATTACHMENT_PATH_NL

PERSONALIZATION_DATA = {
    "company": "MailerSend",
    "name": "Krishna"
}

# OUTLOOK EMAIL SEND APPROACH
# DID NOT WORK OUT AS NEED Microsot 365 Developer E5 Sandbox Subscription, which is difficult to get
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# # SCOPES = ["Mail.Send"]
# SCOPES = ["https://graph.microsoft.com/.default"]

# SENDER_EMAIL = ""
# MICROSOFT_GRAPH_API_ENDPOINT = F"https://graph.microsoft.com/v1.0/users/{SENDER_EMAIL}/sendMail"

# TO_ADDRESS = "" #"recipient@example.com"
# SUBJECT = "Script Test Email with Attachment"
# BODY = """Hello,
# ---MAIL 1---
# This is a test email with an attachment sent via Microsoft Graph API using Python.
# """

# ATTACHMENT_PATH = "C:\\Users\\Administrator\\Documents\\testsdir\\lpalgo.pdf" #"example.xlsx"  # Set to None if you don't want to attach anything
# ---------------------------------------------------------------------------------------------------