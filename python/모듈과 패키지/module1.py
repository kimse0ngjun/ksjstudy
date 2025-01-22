import module
module.price(3)
module.price_morning(4)
module.price_soldier(5)

import module as mv # as 뒤에 쓰는 이름은 별명
mv.price(3)
mv.price_morning(4)
mv.price_soldier(2)

from module import *
price(3)
price_soldier(2)
price_morning(3)

from module import price, price_morning
price(5)
price_morning(4)
# price_soldier(5) price_soldier가 정의되어 있지 않음

from module import price_soldier as price
price(5)