class Experiments:
    societyName="ABC Welfare Society"
    def __init__(self,name=None):
        self.newName="amit"
        self.oldName="Rajesh"
        
    def displayNames(self):
        societyName="local Society"
        print(self.newName)
        print(self.oldName)
        print(societyName)
        print(f"local variable {societyName}")
        print(f"global variable {self.societyName}")

if __name__ == "__main__":
    print(__name__)
    exp=Experiments()
    exp.displayNames()        