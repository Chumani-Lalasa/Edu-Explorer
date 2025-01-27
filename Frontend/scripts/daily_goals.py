from datetime import date

class DailyGoals:
    def __init__(self):
        self.goals = {}  # Format: {username: {date: goal_completed}}

    def set_goal(self, username):
        today = str(date.today())
        if username not in self.goals:
            self.goals[username] = {}
        self.goals[username][today] = False

    def complete_goal(self, username):
        today = str(date.today())
        if username in self.goals and today in self.goals[username]:
            self.goals[username][today] = True
            return "Goal completed for today!"
        return "No goal set for today."

    def check_streak(self, username):
        if username in self.goals:
            streak = sum(self.goals[username].values())
            return f"You have a streak of {streak} days."
        return "No streak found."

# Example Usage
if __name__ == "__main__":
    dg = DailyGoals()
    dg.set_goal("Alice")
    print(dg.complete_goal("Alice"))
    print(dg.check_streak("Alice"))
