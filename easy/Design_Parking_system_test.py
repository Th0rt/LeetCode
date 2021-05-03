# https://leetcode.com/problems/design-parking-system/

from unittest import TestCase


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        index = carType - 1
        if self.slots[index] == 0:
            return False
        self.slots[index] -= 1
        return True


class TestParkingSystem(TestCase):
    def test_it(self):
        parkingSystem = ParkingSystem(*[1, 1, 0])
        assert parkingSystem.addCar(*[1])
        assert parkingSystem.addCar(*[2])
        assert not parkingSystem.addCar(*[3])
        assert not parkingSystem.addCar(*[1])


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
