from project.collectors.base_collector import BaseCollector

class Museum(BaseCollector):
    INITIAL_AVAILABLE_MONEY = 15_000.0
    INITIAL_AVAILABLE_SPACE = 2_000

    def __init__(self, name):
        super().__init__(name, self.INITIAL_AVAILABLE_MONEY, self.INITIAL_AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += 1000.0
