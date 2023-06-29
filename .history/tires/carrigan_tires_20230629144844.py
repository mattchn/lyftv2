from tires.tires import Tires
from utils import add_years_to_date


class CarriganTires(Tires):
    def __init__(self, wheels):
        self.wheels = wheels  # array size 4 containing 1 tire per index

    def needs_service(self):
        num_faulty_tires = 0
        for each_tire in self.wheels:
            if each_tire >= 0.9:
                num_faulty_tires += 1

        if num_faulty_tires >= 1:
            return True
        else:
            return False
