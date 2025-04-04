import pandas as pd
from pyasn1_modules.rfc8017 import emptyString
from model.programmer_model import ProgrammerModel
from model.team_leader_model import TeamLeaderModel
from users.team_leader import TeamLeader
from users.programmer import Programmer
from users.team import Team


class TeamDataProcessor:
    def __init__(self, team_leader_file: str, programmer_file: str):
        self.team_leader_file = team_leader_file
        self.programmer_file = programmer_file
        self.team_leaders = []
        self.programmers = []
        self.teams = []
        self.effective_team_leaders = []
        self.effective_programmers = []
        self.members1 = []
        self.excluded_teams = {"c05", "nc31", "nc04", "nc03", "nc13", "nc30", "nc02", "nc26", "nc21", "nc15", "nc34", "nc20", "nc22", "nc1", "nc10", "nc12", "nc09", "nc32", "nc07"}

    def load_data(self):
        team_leader_data = pd.read_excel(self.team_leader_file, engine='openpyxl')
        programmer_data = pd.read_excel(self.programmer_file, engine='openpyxl')

        self._process_team_leaders(team_leader_data)
        self._process_programmers(programmer_data)
        self._assign_teams()
        self._evaluate_effective_leaders()
        self._evaluate_effective_programmers()

    def _process_team_leaders(self, data):
        for _, row in data.iterrows():
            if row["Carica qui i tuoi risultati"] is not emptyString:
                team_leader = TeamLeader(
                    row["Nome del team"].lower(),
                    row["Nome del progetto"].lower(),
                    row["Sesso alla nascita"].lower(),
                    row["In quale tipo di personalità ricadi?"].lower()
                )
                self.team_leaders.append(team_leader)

    def _process_programmers(self, data):
        for _, row in data.iterrows():
            if row["Carica qui i tuoi risultati"] is not emptyString:
                programmer = Programmer(
                    row["Nome del team"].lower(),
                    row["Nome del progetto"].lower(),
                    row["Sesso alla nascita"].lower(),
                    row["In quale tipo di personalità ricadi?"].lower()
                )
                self.programmers.append(programmer)

    def _assign_teams(self):
        for team_leader in self.team_leaders:
            team = Team(team_leader)
            l_team_name = team_leader.getTeamName()
            l_project_name = team_leader.getProjectName()
            for programmer in self.programmers:
                p_team_name = programmer.getTeamName()
                p_project_name = programmer.getProjectName()
                if p_team_name == l_team_name or p_project_name == l_project_name:
                    team.addProgrammer(programmer)
            self.teams.append(team)

        for team in self.teams:
            if team.getTeamLeader().getTeamName() in ["sldl4", "adg4"]:
                team.setProgrammers([])

    def _evaluate_effective_leaders(self):
        for team in self.teams:
            team_leader_name = team.getTeamLeader().getTeamName()
            if team_leader_name in self.excluded_teams:
                print(f"[INFO] The team '{team_leader_name}' has no leaders.")
            else:
                team_leader_model = TeamLeaderModel(team)
                if team_leader_model.simulate_model() == 1:
                    self.effective_team_leaders.append(team.getTeamLeader())

    def _evaluate_effective_programmers(self):
        for team in self.teams:
            programmer_model = ProgrammerModel(team)
            effectiveness_sum = 0
            if team.getTeamLeader().getTeamName() in ["sldl4", "adg4"]:
                print(f"[INFO] The team '{team.getTeamLeader().getTeamName()}' has no members.")
            else:
                for programmer in team.getProgrammers():
                    effectiveness = programmer_model.simulate_model(programmer)
                    effectiveness_sum += effectiveness
                if effectiveness_sum == len(team.getProgrammers()) - 1:
                    self.effective_programmers.extend(team.getProgrammers())

    def print_summary(self):
        print("\n========== TEAM SUMMARY ==========")
        print(f"Total Programmers: {len(self.programmers)}")
        print(f"Total Team Leaders: {len(self.team_leaders)}")
        self._print_gender_distribution()
        self._print_effective_leaders()
        self._print_effective_programmers()
        self._print_team_information()

    def _print_gender_distribution(self):
        print("\n========== GENDER DISTRIBUTION ==========")
        tm_males = sum(1 for tl in self.team_leaders if tl.getSex() == "maschio")
        tm_females = sum(1 for tl in self.team_leaders if tl.getSex() == "femmina")
        print(f"Total Male Team Leaders: {tm_males}")
        print(f"Total Female Team Leaders: {tm_females}")

        p_males = sum(1 for p in self.programmers if p.getSex() == "maschio")
        p_females = sum(1 for p in self.programmers if p.getSex() == "femmina")
        print(f"Total Male Programmers: {p_males}")
        print(f"Total Female Programmers: {p_females}")

    def _print_effective_leaders(self):
        print("\n========== EFFECTIVE TEAM LEADERS ==========")
        if not self.effective_team_leaders:
            print("No effective team leaders found.")
        else:
            for leader in self.effective_team_leaders:
                print(f" - {leader.getTeamName()}")

    def _print_effective_programmers(self):
        print("\n========== EFFECTIVE PROGRAMMERS ==========")
        males = 0
        females = 0
        if not self.effective_programmers:
            print("No effective programmers found.")
        else:
            for programmer in self.effective_programmers:
                if programmer.getSex() == "maschio":
                    males = males + 1
                if programmer.getSex() == "femmina":
                    females = females + 1
                print(f" - {programmer}")
        print(f"Total Effective Programmers: {len(self.effective_programmers)}")
        print(f"Total Effective Male Programmers: {males}")
        print(f"Total Effective Female Programmers: {females}")

    def _print_team_information(self):
        print("\n========== TEAM SIZE DISTRIBUTION ==========")
        members2, members3, members4, members5 = [], [], [], []
        for team in self.teams:
            programmers = team.getProgrammers()
            leader = team.getTeamLeader()
            #if leader.getTeamName() not in ["sldl4", "adg4"]:
            team_size = len(programmers) + (1 if leader.getSex() != "false" else 0)
            if team_size == 1:
                self.members1.append(leader.getTeamName())
            if team_size == 2:
                members2.append(leader.getTeamName())
            elif team_size == 3:
                members3.append(leader.getTeamName())
            elif team_size == 4:
                members4.append(leader.getTeamName())
            elif team_size == 5:
                members5.append(leader.getTeamName())
        print(f"Teams with 1 members: {self.members1}")
        print(f"Teams with 2 members: {members2}")
        print(f"Teams with 3 members: {members3}")
        print(f"Teams with 4 members: {members4}")
        print(f"Teams with 5 members: {members5}")

    def get_programmer_effectiveness_matrix(self):
        row = ""
        matrix = []
        for team in self.teams:
            leader_row = []
            if team.getTeamLeader().getTeamName() not in self.excluded_teams:
                leader_model = TeamLeaderModel(team)
                leader_result = leader_model.simulate_model()
                leader_row.append(leader_result)
            else:
                leader_row.append("-1")
            programmer_row = []
            programmer_model = ProgrammerModel(team)
            for programmer in team.getProgrammers():
                effectiveness = programmer_model.simulate_model(programmer)
                programmer_row.append(effectiveness)
            row = f"{leader_row} & {programmer_row}"
            matrix.append(row)
        return matrix


if __name__ == "__main__":
    processor = TeamDataProcessor("MBTI - Team Leader (Risposte).xlsx", "MBTI - Programmer (Risposte).xlsx")
    processor.load_data()
    processor.print_summary()

    matrix = processor.get_programmer_effectiveness_matrix()
    print("\n========== PROGRAMMER EFFECTIVENESS MATRIX ==========")
    for i, row in enumerate(matrix):
        print(f"Team {processor.teams[i].getTeamLeader().getTeamName()}: {row}")


