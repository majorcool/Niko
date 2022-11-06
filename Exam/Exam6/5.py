class Course:
    def __init__(self, name= '', difficulty = 0):
        self.name = name
        self.difficulty = difficulty
    def __str__(self):
        return self.name + ", its difficulty=" + self.difficulty
    def get_name(self):
        return self.name
    def set_difficulty(self, newdifficulty):
        self.difficulty = newdifficulty

