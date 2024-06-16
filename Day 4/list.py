names=["abhisek","ashwini","Biikun","Sendha","Gedu","Gudii"]
print(names[0:3]) #OUTPUT IS:-['abhisek', 'ashwini', 'Biikun']
print(names[0:]) #OUTPUT IS:-['abhisek', 'ashwini', 'Biikun', 'Sendha', 'Gedu', 'Gudii']
print(names[::2]) #OUTPUT IS:- ['abhisek', 'Biikun', 'Gedu']
print(names[:5:3]) #OUTPUT IS:-['abhisek', 'Sendha']

#For reverse
print(names[::-1]) #OUTPUT IS:- ['Gudii', 'Gedu', 'Sendha', 'Biikun', 'ashwini', 'abhisek']
print(names[:4:-2])

names[0]="Abhisek"
print(names) #OUTPUT IS :- ['Abhisek', 'ashwini', 'Biikun', 'Sendha', 'Gedu', 'Gudii']

#To add something inside the list
names.append("JAI SHREE RAM")
print(names) #OUTPUT IS:- ['Abhisek', 'ashwini', 'Biikun', 'Sendha', 'Gedu', 'Gudii', 'JAI SHREE RAM']