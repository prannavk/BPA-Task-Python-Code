import os
from mailersendmodule import MailerSendAPIWrapper1
from .remote_data_fetch import fetch_and_parse_suppliers
from .excel_prepare import write_suppliers_to_excel
import constants

def send_email_with_the_generated_attachment_via_mailersend(
    att_disposition: constants.AttachmentDisposition,
    custom_subject: str = "",
    custom_body: str = ""
) -> None:
    # Generating the Needed Excel File
    target_attachment_file_name = "Northwind_Suppliers.xlsx"
    write_suppliers_to_excel(fetch_and_parse_suppliers(), target_attachment_file_name)
    # Excel Savepath in my pc: C:\Users\Administrator\Documents\newcodeprojects\pybtptask\src\Northwind_Suppliers.xlsx
    target_excel_path = os.path.abspath(target_attachment_file_name)
    print(f"Excel Attachment file picked from Full Path: {target_excel_path}\nsending email now...\n")
    att_disposition_parameter = "attachment" if att_disposition == constants.AttachmentDisposition.ATTACHMENT else "inline"
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