import pandas as pd
from pyasn1_modules.rfc8017 import emptyString


from users.User import User
from users.team import Team
from users.team_leader import TeamLeader
from users.programmer import Programmer

team_leader_file_path = "MBTI - Team Leader (Risposte).xlsx"
programmer_file_path = "MBTI - Programmer (Risposte).xlsx"
team_leader_data = pd.read_excel(team_leader_file_path, engine='openpyxl')
programmer_data = pd.read_excel(programmer_file_path, engine='openpyxl')

team_leaders = []
programmers = []
teams = []

for index, row in team_leader_data.iterrows():
    if row["Carica qui i tuoi risultati"] is not emptyString:
        team_name = row["Nome del team"]
        project_name = row["Nome del progetto"]
        sex = row["Sesso alla nascita"]
        mbti = row["In quale tipo di personalità ricadi?"]
        team_leader = TeamLeader(team_name.lower(), project_name.lower(), sex.lower(), mbti.lower())
        team_leaders.append(team_leader)

for index, row in programmer_data.iterrows():
    if row["Carica qui i tuoi risultati"] is not emptyString:
        team_name = row["Nome del team"]
        project_name = row["Nome del progetto"]
        sex = row["Sesso alla nascita"]
        mbti = row["In quale tipo di personalità ricadi?"]
        programmer = Programmer(team_name.lower(), project_name.lower(), sex.lower(), mbti.lower())
        programmers.append(programmer)

print(programmers.__len__())
print(team_leaders.__len__())

for team_leader in team_leaders:
    team = Team(team_leader)
    l_team_name = team_leader.getTeamName()
    l_project_name = team_leader.getProjectName()
    for programmer in programmers:
        p_team_name = programmer.getTeamName()
        p_project_name = programmer.getProjectName()
        if(p_team_name == l_team_name) or (p_project_name == l_project_name):
            team.addProgrammer(programmer)
    teams.append(team)

for team in teams:
    if team.getTeamLeader().getTeamName() == "sldl4":
        team.setProgrammers([])
    if team.getTeamLeader().getTeamName() == "adg4":
        team.setProgrammers([])

print(teams.__getitem__(0).getTeamLeader().getTeamName())
print("i" in teams.__getitem__(0).getTeamLeader().getMbti())
#result = 0

#for team in teams:
    #print(team.getTeamLeader().getTeamName())
    #print(team.getProgrammers().__len__())
    #result = result + team.getProgrammers().__len__()
#print(result)