# src/main.py

from mailmodule.emailprogram import OutlookEmailSender
from mailersendmodule import MailerSendAPIWrapper1
import constants
from bpa_fulltask import send_email_with_the_generated_attachment_via_mailersend


# def main_mailer_1() -> None:
#     client = MailerSendClient1(api_key=constants.MAILERSEND_API_KEY)

#     client.send_email(
#         to_email=constants.TO_EMAIL,
#         from_email=constants.FROM_EMAIL,
#         subject=constants.SUBJECT,
#         text=constants.BODY
#     )


def main_mailer_api() -> None:
    client = MailerSendAPIWrapper1()

    client.send_email(        
        recipient_email=constants.TO_EMAIL,
        recipient_name=constants.TO_NAME,
        subject=constants.SUBJECT,
        plain_text=constants.PLAIN_BODY,
        html_text=constants.HTML_BODY
    )

def main_mailer_api2() -> None:
    client = MailerSendAPIWrapper1()

    client.send_email_with_attachment(        
        recipient_email=constants.TO_EMAIL,
        recipient_name=constants.TO_NAME,
        subject=constants.SUBJECT3,
        plain_text=constants.PLAIN_BODY3,
        html_text=constants.HTML_BODY3,
        attachment_path=constants.ATTACHMENT_PATH,
        personalization_data=constants.PERSONALIZATION_DATA  # Set to None to skip personalization
    )


def main_outlook_email_sender() -> None:
    email_sender = OutlookEmailSender(
        client_id=constants.CLIENT_ID,
        client_secret_value=constants.CLIENT_MYSECRETKEY_VALUE,
        tenant_id=constants.TENANT_ID,
        scopes=constants.SCOPES
    )

    token = email_sender.acquire_token()

    if token:
        payload = email_sender.create_email_payload(
            to_address=constants.TO_ADDRESS,
            subject=constants.SUBJECT,
            body=constants.BODY,
            attachment_path=constants.ATTACHMENT_PATH
        )

        email_sender.send_email(access_token=token, payload=payload, endpoint=constants.MICROSOFT_GRAPH_API_ENDPOINT)
    else:
        print("[FAILURE] No token available. Email not sent.")


if __name__ == "__main__":
    # main_outlook_email_sender()
    # main_mailer_api2()
    send_email_with_the_generated_attachment_via_mailersend(constants.AttachmentDisposition.ATTACHMENT)