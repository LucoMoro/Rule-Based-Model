from users.programmer import Programmer
from users.team import Team


class ProgrammerModel:
    def __init__(self, team: Team):
        self.team = team

    def rule1(self, programmer: Programmer) -> int:
        if programmer.getSex() == "femmina":
            if "e" in programmer.getMbti():
                return 1
            else:
                return 0
        else:
            return 0

    def rule2(self, programmer: Programmer) -> int:
        if "e" in programmer.getMbti():
            if "f" in programmer.getMbti():
                return 1
            else:
                return 0
        else:
            return 0

    def rule3(self, programmer: Programmer) -> int:
        if "e" in programmer.getMbti():
            if "n" in programmer.getMbti():
                return 1
            else:
                return 0
        else:
            return 0

    def rule4(self, programmer: Programmer) -> int:
        if "i" in programmer.getMbti():
            if "s" in programmer.getMbti():
                if "t" in programmer.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    #def rule5(self, programmer: Programmer) -> int:
        #if programmer.getSex() == "maschio":
            #test