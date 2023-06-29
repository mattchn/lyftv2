from tires.tires import Tires
from utils import add_years_to_date


class OctoprimeTires(Tires):
    def __init__(self, wheels):
        self.wheels = wheels  # array size 4 containing 1 tire per index

    def needs_service(self):
        sum_tires = sum(self.wheels)
        if sum_tires >= 3:
            return True
        else:
            return False
