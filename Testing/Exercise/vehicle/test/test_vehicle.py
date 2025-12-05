from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTests(TestCase):
    fuel = 4.5
    horse_power = 112.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(2)
        self.assertEqual(2, self.vehicle.fuel)

    def test_drive_failure(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(2.3)
        self.assertEqual(3.3, self.vehicle.fuel)

    def test_refuel_failure(self):
        self.vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(8.3)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.vehicle.fuel = 1.75
        expected_value = "The vehicle has 112.5 horse power with 1.75 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_value, str(self.vehicle))


if __name__ == '__main__':
    main()