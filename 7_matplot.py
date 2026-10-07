import pandas
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
df=pandas.read_csv('digital_behaviour.csv')
df['Total_Screen_Time']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['Study_Minutes']
df['day_label']=[f"Day {i+1}" for i in range(len(df))]
plt.figure(figsize=(12,6))
plt.bar(df['day_label'],df['Total_Screen_Time'],color='blue')
plt.title("My Screen Time My Day")
plt.xlabel('Days')
plt.ylabel('Total Screen Time(minutes)')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.savefig('My Screen Time My Day.png') #chart1
plt.close()
apps=['Instagram','Whatsapp','Youtube','LinkedIn']
app_totals={
    "Instagram" : df['Instagram_Minutes'].sum(),
    "WhatsApp" : df['WhatsApp_Minutes'].sum(),
    "YouTube" : df['YouTube_Minutes'].sum(),
    "LinkedIn" : df['LinkedIn_Minutes'].sum()
}
plt.figure(figsize=(12,6))
plt.bar(app_totals.keys(),app_totals.values(),color='green')
plt.title('Total Time By App')
plt.xlabel('Apps')
plt.ylabel('Time')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.savefig("Total time by app.png") #chart2
plt.close()
plt.figure(figsize=(12,6))
plt.plot(df['day_label'],df['Study_Minutes'],marker='o',label='Study',color='red')
plt.plot(df['day_label'],df['Total_Screen_Time'],marker='s',label='Screen Time',color='green')
plt.legend()
plt.title('Study & ScreenTime per day')
plt.xlabel('Days')
plt.ylabel('Time')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.savefig('Study & Screen Time per day.png')#chart3
plt.close()
plt.figure(figsize=(12,6))
plt.pie(app_totals.values(),labels=app_totals.keys(),autopct='%1.1f%%',startangle=90)
plt.title('Total apps')
plt.tight_layout()
plt.savefig('Total apps.png') #chart4
plt.close()