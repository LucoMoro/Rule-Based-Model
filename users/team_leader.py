from users.User import User


class TeamLeader(User):
    def __init__(self, team_name: str, project_name: str, sex: str, mbti: str, grade:int):
        super().__init__(team_name, project_name, sex, mbti, grade)