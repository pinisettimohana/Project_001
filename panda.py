import pandas as pd
#DataFrame - collection of rows and columns
#series - for columns 
#index- no of rows(0 - indexed)

#load your data
df=pd.read_csv('digital_behaviour.csv') #df is a reference to dataframe object
first_five=df.head()

last_five=df.tail()

columns_names=list(df.columns)

rc=(df.shape)

total_insta=print(df['Instagram_Minutes'].sum())
#print(df[['Instagram_Minutes','Videos_Watched']].describe())

top_insta=df.sort_values('Instagram_Minutes',ascending=False).head(10)

top_study=df.sort_values('Study_Minutes',ascending=False).head(10)

df['Total_Screen_Time']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes']

df['Screen_Hours']=(df['Total_Screen_Time']/60).round(2)

df['Digital_Balance']=(df['Study_Minutes']/df['Total_Screen_Time']).round(2)

df['Day_Type']="Normal"
#df.loc[which row, which column]
df.loc[df['Total_Screen_Time']>300,'Day_Type']="Heavy"

#mask - it does not update original - standard operation
#df[df['Total_Screen_Time']>300]['Day_Type']="Heavy"

app_totals={
    "Instagram" : df['Instagram_Minutes'].sum(),
    "WhatsApp" : df['WhatsApp_Minutes'].sum(),
    "YouTube" : df['YouTube_Minutes'].sum(),
    "LinkedIn" : df['LinkedIn_Minutes'].sum()
}

Highest_Screen_Time=max(app_totals,key=app_totals.get)

(df['Day_Type']=="Heavy").sum()

Study_day=df['Study_Minutes'].idxmax()

s=df.loc[df['Total_Screen_Time'].idxmax(),'Study_Minutes']