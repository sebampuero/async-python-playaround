import smtplib, os
import logging

logger = logging.getLogger(__name__)

class EmailNotifier:

    def __init__(self) -> None:
        self.email = os.getenv("EMAIL_USERNAME")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.from_addr = os.getenv("FROM_EMAIL_ADDR")

    def send_email(self, msg: str, recipient: str) -> None:
        logger.debug(f"Sending email to {recipient}")
        try:
            with smtplib.SMTP_SSL("smtp.strato.de") as server:
                server.login(self.email, self.email_password)
                logger.debug("Successfully logged in to SMTP")
                server.sendmail(self.from_addr, recipient, msg)
                logger.debug("Successfully sent email")
        except:
            logger.error("Could not send email notification", exc_info=True)