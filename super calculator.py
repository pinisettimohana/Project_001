import numpy as np
import csv
insta_minutes=[]
study_minutes=[]
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader =csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row ["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))
insta_minutes=insta_minutes[:7]
study_minutes=study_minutes[:7]
instagram= np.array(insta_minutes)
study=np.array(study_minutes)
print(instagram,study)
#total=np.sum(instagram)
total=instagram.sum()
tot=study.sum()
average=instagram.mean()
avg=study.mean()
maximum=instagram.max()
max=study.max()
minimum=instagram.min()
min=study.min()
days=len(instagram)
days_study=len(study)
print(f"Total {total} , Average {average}, Maximum {maximum}, Minimum {minimum}, Days {days} ")
print(f"Total {tot} , Average {avg}, Maximum {max}, Minimum {min}, Days {days_study} ")
print(instagram[0],instagram[-1],instagram[2])
print(study[0],study[-1],study[2])
print(instagram[:3],instagram[-2:],instagram[1:4], instagram[::2])
print(study[:3],study[-2:],study[1:4], study[::2])
i_hours=instagram/60
s_hours=instagram/60
i_hours=i_hours.round(2)
s_hours=s_hours.round(2)
diff=study-instagram
#boolean=instagram>100
greater=instagram[instagram>100]
count=(instagram>100).sum()
value=instagram[instagram>average]