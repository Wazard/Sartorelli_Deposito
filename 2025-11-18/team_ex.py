class TeamMember:
    def __init__(self, name: str, age: int): # Takes respectively string and int
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"


class Player(TeamMember): # inherits from @TeamMember
    def __init__(self, name: str, age: int, role: str): # Takes respectively string, int and string
        super().__init__(name, age)
        self.role = role

    def play_game(self):
        return f"{self.name} plays as {self.role}."


class Coach(TeamMember): # inherits from @TeamMember
    def __init__(self, name: str, age: int, coaching_years: int): # Takes respectively string, int and int
        super().__init__(name, age)
        self.coaching_years = coaching_years

    def coaching_method(self):
        return f"{self.name} has {self.coaching_years} years of coaching experience and uses strategic planning."


class Assistant(TeamMember): # inherits from @TeamMember
    def __init__(self, name: str, age: int, specialization: str): # Takes respectively string, int and string
        super().__init__(name, age)
        self.specialization = specialization

    def support_team(self):
        return f"{self.name} supports the team with specialization in {self.specialization}."


#examples

player = Player("Alice", 25, role="Forward")
coach = Coach("Bob", 45, coaching_years=20)
assistant = Assistant("Charlie", 30, specialization="Fitness & Nutrition")

team = [player, coach, assistant]

for member in team:
    print(member.description())

print(player.play_game())
print(coach.coaching_method())
print(assistant.support_team())