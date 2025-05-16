# src/mailmodule/emailprogram.py

import os
import base64
import requests
from msal import PublicClientApplication, SerializableTokenCache, ConfidentialClientApplication
from typing import Optional, Dict, Any, List


class OutlookEmailSender:
    def __init__(self, client_id: str, client_secret_value: str, tenant_id: str, scopes: List[str]) -> None:
        self.client_id = client_id
        self.client_secret_value = client_secret_value
        self.tenant_id = tenant_id
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scopes = scopes
        self.app = ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret_value,
            authority=self.authority,
            #token_cache=SerializableTokenCache()
        )

    def acquire_token(self) -> Optional[str]:
        try:
            result = self.app.acquire_token_for_client(scopes=self.scopes)

            if "access_token" in result:
                return result["access_token"]
            else:
                print(f"[ERROR] Token acquisition failed: {result.get('error_description')}")
                return None
        except Exception as e:
            print(f"[EXCEPTION] Failed during token acquisition: {e}")
            return None

    def create_email_payload(
        self,
        to_address: str,
        subject: str,
        body: str,
        attachment_path: Optional[str] = None
    ) -> Dict[str, Any]:
        message = {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": to_address
                    }
                }
            ]
        }

        if attachment_path and os.path.exists(attachment_path):
            try:
                with open(attachment_path, "rb") as file:
                    content_bytes = base64.b64encode(file.read()).decode()
                attachment = {
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": os.path.basename(attachment_path),
                    "contentBytes": content_bytes
                }
                message["attachments"] = [attachment]
            except Exception as e:
                print(f"[ERROR] Failed to attach file: {e}")

        return {
            "message": message,
            "saveToSentItems": True
        }

    def send_email(self, access_token: str, payload: Dict[str, Any], endpoint: str) -> bool:
        try:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }

            response = requests.post(
                url=endpoint,
                headers=headers,
                json=payload
            )

            if response.status_code == 202:
                print("[SUCCESS] Email sent successfully.")
                return True
            else:
                print(f"[ERROR] Email failed: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"[EXCEPTION] Error sending email: {e}")
            return False

