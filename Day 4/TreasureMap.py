row1=["😍","😍","😍"]
row2=["😍","😍","😍"]
row3=["😍","😍","😍"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
Position=input("Where do you want to put the traesure?")
horizontal=int(Position[0])
vertical=int(Position[1])
selected_row=map[vertical-1]
selected_row[horizontal-1]="X"





print(f"{row1}\n{row2}\n{row3}\n")