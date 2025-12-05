from project.collectors.base_collector import BaseCollector

class PrivateCollector(BaseCollector):
    INITIAL_AVAILABLE_MONEY = 25_000.0
    INITIAL_AVAILABLE_SPACE = 3_000

    def __init__(self, name):
        super().__init__(name, self.INITIAL_AVAILABLE_MONEY, self.INITIAL_AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += 5000.0