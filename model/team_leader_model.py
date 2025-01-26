from users.team import Team
from users.team_leader import TeamLeader


class TeamLeaderModel:
    def __init__(self, team: Team):
        self.team = team

    # 1 if is efficient,  0 if inefficient, 2 if there is no match
    def rule1(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "femmina":
            if "i" in team_leader.getMbti():
                if "j" in team_leader.getMbti():
                    return 1
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule2(self, team_leader: TeamLeader) -> int:
        if "e" in team_leader.getMbti():
            if "t" in team_leader.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

    def rule3(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "femmina":
            if "t" in team_leader.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

    def rule4(self, team_leader: TeamLeader) -> int:
        if "e" in team_leader.getMbti():
            if "s" in team_leader.getMbti():
                if "f" in team_leader.getMbti():
                    return 0
                else:
                    return 1
            else:
                return 1
        else:
            return 1

    def rule5(self, team_leader: TeamLeader) -> int:
        if "e" in team_leader.getMbti():
            if "n" in team_leader.getMbti():
                if "f" in team_leader.getMbti():
                    return 1
                else:
                    return 2
            else:
                return 2
        else: return 2

    def rule6(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "femmina":
            if "i" in team_leader.getMbti():
                if "n" in team_leader.getMbti():
                    return 1
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule7(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "maschio":
            if "s" in team_leader.getMbti():
                if "f" in team_leader.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule8(self, team_leader: TeamLeader) -> int:
        if "n" in team_leader.getMbti():
            if "p" in team_leader.getMbti():
                return 1
            else:
                return 2
        else:
            return 2

    def rule9(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "maschio":
            if "i" in team_leader.getMbti():
                if "j" in team_leader.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2

    def rule10(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "femmina":
            if "p" in team_leader.getMbti():
                return 0
            else:
                return 2
        else:
            return 2

    def rule11(self, team_leader: TeamLeader) -> int:
        if "e" in team_leader.getMbti():
            if "p" in team_leader.getMbti():
                return 0
            else:
                return 2
        else:
            return 2

    def rule12(self, team_leader: TeamLeader) -> int:
        if team_leader.getSex() == "maschio":
            if "i" in team_leader.getMbti():
                if "t" in team_leader.getMbti():
                    return 0
                else:
                    return 2
            else:
                return 2
        else:
            return 2