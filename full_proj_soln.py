import csv
APP="Instagram"
minutes=[]
with open("digital_behaviour.csv", "r",  encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
                minutes.append(int(row["Instagram_Minutes"]))
minutes=minutes[0:7]
tot=sum(minutes)
avg=tot//len(minutes)
highest=max(minutes)
lowest=min(minutes)
count=0
for value in minutes:
        if value>avg :
                count+=1
print(f"App Name:{APP},Total Minutes:{tot},Average Minutes:{avg},Highest Day:{highest},Lowest Day:{lowest},Days Above Average:{count}")