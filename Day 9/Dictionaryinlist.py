travel_log=[
    {
        "country":"France",
        "Visits":12,
        "cities":["paris","odisha","Cuttack"]
    },
    {
        "country":"Germany",
        "Visits":5,
        "cities":["Berlin","Bhubaneswar","Punjab"]
    }
]
def new_country(country_visited,times_visited,cities_visited):
    new_country1={}
    new_country1["country"]=country_visited
    new_country1["Visits"]=times_visited
    new_country1["cities"] = cities_visited
    travel_log.append(new_country1)

new_country("Russia",2,["Moscow","BBsr"])
print(travel_log)