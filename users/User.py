
class User:
    def __init__(self, team_name: str, project_name: str, sex: str, mbti: str, grade: int):
        self.team_name = team_name
        self.project_name = project_name
        self.sex = sex
        self.mbti = mbti
        self.grade = grade

    def getTeamName(self) -> str:
        return self.team_name

    def setTeamName(self, team_name) -> None:
        self.team_name = team_name

    def getProjectName(self) -> str:
        return self.project_name

    def setProjectName(self, project_name) -> None:
        self.project_name = project_name

    def getSex(self) -> str:
        return self.sex

    def setSex(self, sex) -> None:
        self.sex = sex

    def getMbti(self) -> str:
        return self.mbti

    def setMbti(self, mbti) -> None:
        self.mbti = mbti

    def getGrade(self) -> int:
        return self.grade

    def setGrade(self, grade) -> None:
        self.grade = grade

    def __repr__(self):
        return f"TeamLeader(team={self.team_name}, project={self.project_name})"