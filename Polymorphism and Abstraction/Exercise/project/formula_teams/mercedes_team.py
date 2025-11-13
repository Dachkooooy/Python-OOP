from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    FIRST_PETRONAS = 1_000_000
    THIRD_PETRONAS = 500_000
    FIFTH_TEAM_VIEWER = 100_000
    SEVENTH_TEAM_VIEWER = 50_000
    EXPENSES_PER_RACE = 200_000

    def __init__(self, name:str, budget:int):
        super().__init__(name, budget)
        self.revenue = 0

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            self.revenue += self.FIRST_PETRONAS
        elif race_pos == 3:
            self.revenue += self.THIRD_PETRONAS
        elif race_pos == 5:
            self.revenue += self.FIFTH_TEAM_VIEWER
        elif race_pos == 7:
            self.revenue += self.SEVENTH_TEAM_VIEWER
        self.revenue -= self.EXPENSES_PER_RACE
        self.budget += self.revenue
        return f"The revenue after the race is {self.revenue}$. Current budget {self.budget}$"