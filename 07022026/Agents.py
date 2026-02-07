class Agents:
    def __init__(self, name,role):
        self.name = name
        self.role = role
    
    def printAgnet(self):
        print(f"Agent Name: {self.name}, Role: {self.role}")


if __name__ == "__main__":
    agent1 = Agents("Alice", "Spy")
    agent2 = Agents("Bob", "Analyst")

    agent1.printAgnet()
    agent2.printAgnet()