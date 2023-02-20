import aiosmtplib, os
import logging
from email.message import EmailMessage

logger = logging.getLogger(__name__)

class EmailNotifier:

    def __init__(self) -> None:
        self.email = os.getenv("EMAIL_USERNAME")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.from_addr = os.getenv("FROM_EMAIL_ADDR")

    async def send_email(self, msg: str, recipient: str) -> None:
        logger.debug(f"Sending email to {recipient}")
        try:
           message = EmailMessage()
           message["From"] = self.from_addr
           message["To"] = recipient
           message["Subject"] = "Price alarm notification"
           message.set_content(msg)
           await aiosmtplib.send(
               message,
               hostname="smtp.strato.de",
               port=465,
               username=self.email,
               password=self.email_password,
               use_tls=True
           )
           logger.debug("Successfully sent email")
        except:
            logger.error("Could not send email notification", exc_info=True)