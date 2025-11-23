from address import Address
from mailing import Mailing

to_address = Address(390045, "Москва", "Кутузова", 15, 37)
from_address = Address(425602, "Казань", "Весенняя", 154, 345)
mailing1 = Mailing(to_address, from_address, 180, "TRN67348784")
print(mailing1)
