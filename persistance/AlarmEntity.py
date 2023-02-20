from dataclasses import dataclass

@dataclass
class AlarmEntity:
    url: str
    email: str
    price_from: int
    price_to: int

    def to_dict(self):
        return {
            'url': self.url,
            'email': self.email,
            'price_from': self.price_from,
            'price_to': self.price_to
        }