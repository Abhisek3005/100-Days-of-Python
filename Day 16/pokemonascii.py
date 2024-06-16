# import prettytable
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table.align)
table.align = "r"
print(table)
