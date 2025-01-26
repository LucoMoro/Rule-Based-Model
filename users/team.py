from users.programmer import Programmer
from users.team_leader import TeamLeader


class Team:
    def __init__(self, team_leader: TeamLeader = None, programmers: list[Programmer] = None):
        self.team_leader = team_leader
        if programmers is not None:
            self.programmers = programmers
        else:
            self.programmers = []

    def getTeamLeader(self) -> TeamLeader:
        return self.team_leader

    def setTeamLeader(self, team_leader: TeamLeader) -> None:
        self.team_leader = team_leader

    def getProgrammers(self) -> list[Programmer]:
        return self.programmers

    def setProgrammers(self, programmers: list[Programmer]) -> None:
        self.programmers = programmers

    def addProgrammer(self, programmer: Programmer) -> None:
        self.programmers.append(programmer)