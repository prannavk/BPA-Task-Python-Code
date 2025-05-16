# src/mailmodule/emailprogram.py

import requests, base64, os, json
from mailersend import emails
import constants
from typing import List, Dict, Optional


class MailerSendClient1:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = constants.MAILERSEND_BASEURL

    def send_email(self, to_email: str, from_email: str, subject: str, text: str) -> bool:
        payload: Dict = {
            "from": {
                "email": from_email
            },
            "to": [
                {
                    "email": to_email
                }
            ],
            "subject": subject,
            "text": text
        }

        headers: Dict = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{self.base_url}/email", json=payload, headers=headers)
            if response.status_code == 202:
                print("[SUCCESS] Email sent!")
                return True
            else:
                print(f"[ERROR] Status {response.status_code}: {response.text}")
                return False
        except Exception as e:
            print(f"[EXCEPTION] Failed to send email: {e}")
            return False


class MailerSendAPIWrapper1:
    def __init__(self) -> None:
        self.api_key = constants.MAILERSEND_API_KEY
        self.base_url = constants.MAILERSEND_BASEURL
        self.mail_from_username = "PranavWeb1"
        self.mail_from_smtp_user_id = constants.MAILERSEND_SMTP_USER
        self.mail_from_smtp_password = constants.MAILERSEND_SMTP_USER_PASSWORD
        self.mailer = emails.NewEmail(self.api_key)
    
    def send_email(
        self,        
        recipient_email: str,
        recipient_name: str,
        subject: str,
        plain_text: str,
        html_text: str = "",
        reply_to_email: str = None,
        reply_to_name: str = None
    ) -> bool:
        try:
            mail_body: Dict = {}

            self.mailer.set_mail_from({
                "name": self.mail_from_username,
                "email": self.mail_from_smtp_user_id
            }, mail_body)

            self.mailer.set_mail_to([{
                "name": recipient_name,
                "email": recipient_email
            }], mail_body)

            self.mailer.set_subject(subject, mail_body)
            self.mailer.set_plaintext_content(plain_text, mail_body)

            if html_text:
                self.mailer.set_html_content(html_text, mail_body)

            if reply_to_email and reply_to_name:
                self.mailer.set_reply_to({
                    "name": reply_to_name,
                    "email": reply_to_email
                }, mail_body)
            else:
                self.mailer.set_reply_to({
                    "name": self.mail_from_username,
                    "email": self.mail_from_smtp_user_id
                }, mail_body)

            response = self.mailer.send(mail_body)
            print("[SUCCESS]", response)
            return True

        except Exception as e:
            print(f"[ERROR] Failed to send email: {e}")
            return False


    # def send_email_with_attachment(
    #     self,        
    #     recipient_email: str,
    #     recipient_name: str,
    #     subject: str,
    #     plain_text: str,
    #     html_text: str = "",
    #     reply_to_email: Optional[str] = None,
    #     reply_to_name: Optional[str] = None,
    #     attachment_path: Optional[str] = None,
    #     attachment_id: str = "my-attachment-id",
    #     personalization_vars: Optional[Dict[str, str]] = None
    # ) -> bool:
    #     try:
    #         mail_body: Dict = {}

    #         self.mailer.set_mail_from({
    #             "name": self.mail_from_username,
    #             "email": self.mail_from_smtp_user_id
    #         }, mail_body)

    #         self.mailer.set_mail_to([{
    #             "name": recipient_name,
    #             "email": recipient_email
    #         }], mail_body)

    #         self.mailer.set_subject(subject, mail_body)

    #         self.mailer.set_plaintext_content(plain_text, mail_body)

    #         if html_text:
    #             self.mailer.set_html_content(html_text, mail_body)

    #         if reply_to_email and reply_to_name:
    #             self.mailer.set_reply_to({
    #                 "name": reply_to_name,
    #                 "email": reply_to_email
    #             }, mail_body)
    #         else:
    #             self.mailer.set_reply_to({
    #                 "name": self.mail_from_username,
    #                 "email": self.mail_from_smtp_user_id
    #             }, mail_body)

    #         if personalization_vars:
    #             variables = [{
    #                 "email": recipient_email,
    #                 "substitutions": [
    #                     {"var": key, "value": value}
    #                     for key, value in personalization_vars.items()
    #                 ]
    #             }]
    #             self.mailer.set_personalization(variables, mail_body)

    #         if attachment_path and os.path.exists(attachment_path):
    #             with open(attachment_path, "rb") as f:
    #                 content_bytes = base64.b64encode(f.read()).decode("ascii")

    #             attachments = [{
    #                 "id": attachment_id,
    #                 "filename": os.path.basename(attachment_path),
    #                 "content": content_bytes,
    #                 "disposition": "attachment"
    #             }]
    #             self.mailer.set_attachments(attachments, mail_body)

    #         response = self.mailer.send(mail_body)
    #         print(f"[ERROR] Status Response -> {response} and {type(response)}")
    #         # if response != 200 or response != 202:
    #         #     print(f"[ERROR] Status Response -> {response} and {type(response)}")
    #         # else:
    #         #     print("[SUCCESS] Email sent successfully:", response)
    #         return True

    #     except Exception as e:
    #         print(f"[ERROR] Failed to send email: {e}")
    #         return False


    def send_email_with_attachment(
        self,        
        recipient_email: str,
        recipient_name: str,
        subject: str,
        plain_text: str,
        html_text: str = "",
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        attachment_path: Optional[str] = None,
        attachment_id: str = "file-attachment-id",
        attachment_disposition: str = "attachment",
        personalization_data: Optional[Dict[str, str]] = None  # e.g. {"company": "MailerSend", "name": "Krishna"}
    ) -> bool:
        try:
            mail_body: Dict = {}

            sender_email = self.mail_from_smtp_user_id
            sender_name = self.mail_from_username

            # From
            self.mailer.set_mail_from({
                "name": sender_name,
                "email": sender_email
            }, mail_body)

            # To
            self.mailer.set_mail_to([{
                "name": recipient_name,
                "email": recipient_email
            }], mail_body)

            # Subject and Content
            self.mailer.set_subject(subject, mail_body)
            self.mailer.set_plaintext_content(plain_text, mail_body)

            if html_text:
                self.mailer.set_html_content(html_text, mail_body)

            # Optional Reply-To            
            if reply_to_email and reply_to_name:
                self.mailer.set_reply_to({
                    "name": reply_to_name,
                    "email": reply_to_email
                }, mail_body)
            else:
                self.mailer.set_reply_to({
                    "name": sender_name,
                    "email": sender_email
                }, mail_body)

            # Optional Personalization
            # eg:    personalization_vars={"foo": "otsuka"}
            if personalization_data:
                personalization = [{
                    "email": recipient_email,
                    "data": personalization_data
                }]
                self.mailer.set_personalization(personalization, mail_body)

            # Optional Attachment
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("ascii")

                attachments = [{
                    "id": attachment_id,
                    "filename": os.path.basename(attachment_path),
                    "content": encoded,
                    "disposition": attachment_disposition
                }]
                self.mailer.set_attachments(attachments, mail_body)

            # Send
            response = self.mailer.send(mail_body)

            # Debug the type and content of response
            print(f"[DEBUG] Response type: {type(response)}")

            if isinstance(response, str):
                try:
                    parsed = json.loads(response)
                    print("[DEBUG] Response JSON:", parsed)
                except Exception:
                    print("[DEBUG] Response:", response)

            if response == 202 or "202" in str(response) or str(response).startswith("2"):
                print("[SUCCESS] Email sent successfully.")
                return True
            else:
                print(f"[ERROR] Unexpected Response: {response}")
                return False

        except Exception as e:
            print(f"[EXCEPTION] Failed to send email: {e}")
            return False
