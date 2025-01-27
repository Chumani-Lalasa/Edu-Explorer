class Leaderboard:
    def __init__(self):
        self.scores = {}  # Format: {username: score}

    def update_score(self, username, score):
        self.scores[username] = self.scores.get(username, 0) + score

    def get_leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return [(i + 1, user, score) for i, (user, score) in enumerate(sorted_scores)]

# Example Usage
if __name__ == "__main__":
    lb = Leaderboard()
    lb.update_score("Alice", 50)
    lb.update_score("Bob", 30)
    lb.update_score("Alice", 20)
    print(lb.get_leaderboard())
