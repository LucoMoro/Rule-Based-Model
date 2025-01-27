from users.programmer import Programmer
from users.team import Team


class ProgrammerModel:
    def __init__(self, team: Team):
        self.team = team

    #1 if is efficient,  0 if inefficient, 2 if there is no match
    def rule1(self, programmer: Programmer) -> int:
        if programmer.getSex() == "femmina":
            if "e" in programmer.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

    def rule2(self, programmer: Programmer) -> int:
        if "e" in programmer.getMbti():
            if "f" in programmer.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

    def rule3(self, programmer: Programmer) -> int:
        if "e" in programmer.getMbti():
            if "n" in programmer.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

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

    def rule5(self, programmer: Programmer) -> int:
        if programmer.getSex() == "maschio":
            if "i" in programmer.getMbti():
                if "t" in programmer.getMbti():
                    if "j" in programmer.getMbti():
                        return 0
                    else:
                        return 2
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule6(self, programmer: Programmer) -> int:
        if "e" in programmer.getMbti():
            if "p" in programmer.getMbti():
                return 0
            else:
                return 2
        else:
            return 2

    def rule7(self, programmer: Programmer) -> int:
        if programmer.getSex() == "maschio":
            if "i" in programmer.getMbti():
                if "f" in programmer.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule8(self, programmer: Programmer) -> int:
        if programmer.getSex() == "maschio":
            if "i" in programmer.getMbti():
                if "p" in programmer.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule9(self, programmer: Programmer) -> int:
        if programmer.getSex() == "femmina":
            if "i" in programmer.getMbti():
                if "n" in programmer.getMbti():
                    if "t" in programmer.getMbti():
                        return 1
                    else:
                        return 2
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule10(self, programmer: Programmer) -> int:
        if programmer.getSex() == "maschio":
            if "e" in programmer.getMbti():
                if "s" in programmer.getMbti():
                    if "t" in programmer.getMbti():
                        if "j" in programmer.getMbti():
                            return 0
                        else:
                            return 2
                    else:
                        return 2
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def simulate_model(self, programmer: Programmer) -> int:
        if (self.rule4(programmer) == 0) or (self.rule5(programmer) == 0) or (self.rule6(programmer) == 0) or (self.rule7(programmer) == 0) or (self.rule8(programmer) == 0) or (self.rule10(programmer) == 0):
            return 0
        if (self.rule1(programmer) == 1) or (self.rule2(programmer) == 1) or (self.rule3(programmer) == 1) or (self.rule9(programmer) == 1):
            return 1
        else:
            return 0

