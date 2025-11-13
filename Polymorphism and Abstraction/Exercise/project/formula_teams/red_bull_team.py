from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    FIRST_ORACLE = 1_500_000
    SECOND_ORACLE = 800_000
    EIGHT_HONDA = 20_000
    TENTH_HONDA = 10_000
    EXPENSES_PER_RACE = 250_000

    def __init__(self, name:str, budget:int):
        super().__init__(name, budget)
        self.revenue = 0

    def calculate_revenue_after_race(self, race_pos:int):
        if race_pos == 1:
            self.revenue += self.FIRST_ORACLE
        elif race_pos == 2:
            self.revenue += self.SECOND_ORACLE
        elif race_pos == 8:
            self.revenue += self.EIGHT_HONDA
        elif race_pos == 10:
            self.revenue += self.TENTH_HONDA
        self.revenue -= self.EXPENSES_PER_RACE
        self.budget += self.revenue
        return f"The revenue after the race is {self.revenue}$. Current budget {self.budget}$"