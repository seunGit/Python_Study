# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# 별명 사용 가능
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from import 사용 방법
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from import 사용 메서드 정해줌
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as price
price(5)