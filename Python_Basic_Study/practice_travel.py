# import travel.thailand # 맨뒤에는 모듈이나 패키지만 가능하다. 클래스는 안됨.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 이건 클래스가 가능하다.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import * # 공개범위를 설정해야한다.
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))