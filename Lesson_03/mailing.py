from address import Address


class Mailing:

    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):

        self.to_address = to_address
        self.from_address = from_address
        self.track = track
        self.cost = cost

    def __str__(self):
        return f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей."
