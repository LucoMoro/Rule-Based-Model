
class User:
    def __init__(self, team_name: str, project_name: str, sex: str, mbti: str):
        self.team_name = team_name
        self.project_name = project_name
        self.sex = sex
        self.mbti = mbti

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