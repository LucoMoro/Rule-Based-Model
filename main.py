import pandas as pd
from dask.array import empty
from pyasn1_modules.rfc8017 import emptyString

from users.User import User
from users.team_leader import TeamLeader
from users.programmer import Programmer

team_leader_file_path = "MBTI - Team Leader (Risposte).xlsx"
programmer_file_path = "MBTI - Programmer (Risposte).xlsx"
team_leader_data = pd.read_excel(team_leader_file_path, engine='openpyxl')
programmer_data = pd.read_excel(programmer_file_path, engine='openpyxl')

team_leaders = []
programmers = []

for index, row in team_leader_data.iterrows():
    if row["Carica qui i tuoi risultati"] is not emptyString:
        team_name = row["Nome del team"]
        project_name = row["Nome del progetto"]
        sex = row["Sesso alla nascita"]
        mbti = row["In quale tipo di personalità ricadi?"]
        team_leader = TeamLeader(team_name, project_name, sex, mbti)
        team_leaders.append(team_leader)

for index, row in programmer_data.iterrows():
    if row["Carica qui i tuoi risultati"] is not emptyString:
        team_name = row["Nome del team"]
        project_name = row["Nome del progetto"]
        sex = row["Sesso alla nascita"]
        mbti = row["In quale tipo di personalità ricadi?"]
        programmer = Programmer(team_name, project_name, sex, mbti)
        programmers.append(programmer)

print(team_leaders)
print(programmers)


