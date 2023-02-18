from dataclasses import dataclass

@dataclass
class AlarmEntity:
    email: str
    price_range: tuple

    def validate_email_addr(self) -> bool:
        # Validate the email address with regex
        pass