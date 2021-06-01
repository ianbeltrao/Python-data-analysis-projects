"""This is a little project I made based on a Codecademy challenge"""


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
def updated_damage(lst):
  for i in lst:
    if i == 'Damages not recorded':
      updated_damages.append(i)
    if i[-1] == "M":
      updated_damages.append(float(i[:-1])*conversion["M"])
    if i[-1] == "B":
      updated_damages.append(float(i[:-1])*conversion["B"])
  return updated_damages

# test function by updating damages
updated_damage(damages)
#print(updated_damages)

# 2 
# Create a Table
hurricanes = {}
def hurricanes_function(names, months, years, max_sustained_winds, areas_affected, deaths):
  for i in range(0, 34):
    deaths[i] = {"Name": names[i],
    "Month": months[i],
    "Year": years[i],
    "Max Sustained Wind": max_sustained_winds[i],
    "Areas Affected": areas_affected[i],
    "Damage": updated_damages[i],
    "Deaths": deaths[i]}
    
    hurricanes[names[i]] = deaths[i]
# Create and view the hurricanes dictionary
hurricanes_function(names, months, years, max_sustained_winds, areas_affected, deaths)
#print(hurricanes)

# 3
# Organizing by Year
hurricanes_by_year = {}
def organizing_by_year(hurricanes):
  for cane in hurricanes:
    current_year = hurricanes[cane]["Year"]
    current_cane = hurricanes[cane]
    if current_year in hurricanes_by_year.keys():
      hurricanes_by_year[current_year].append(current_cane)
    else:
      hurricanes_by_year[current_year] = [current_cane]

# create a new dictionary of hurricanes with year and key
organizing_by_year(hurricanes)
#print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas
area_count = {}
def counting_areas(areas_affected):
  repeated = []
  list_of_areas = []
  for areas in areas_affected:
    for area in areas:
      repeated.append(area)
      if area not in list_of_areas:
        list_of_areas.append(area)
  
  for a in list_of_areas:
    area_count[a] = repeated.count(a)

# create dictionary of areas to store the number of hurricanes involved in
counting_areas(areas_affected)
#print(area_count)

# 5 
# Calculating Maximum Hurricane Count
def calculating_max_count(area_count):
  sort = sorted(area_count.items(), key=lambda x: x[1], reverse=True)
  
  for i in sort:
    return i[0], i[1] 
# find most frequently affected area and the number of hurricanes involved in
#print(calculating_max_count(area_count))

# 6
# Calculating the Deadliest Hurricane
def calculating_deaths(hurricanes):
  death_count = 0
  name = "a"
  for cane in hurricanes: 
    if hurricanes[cane]["Deaths"] > death_count:
      death_count = hurricanes[cane]["Deaths"]
      name = hurricanes[cane]["Name"]
  return name, death_count
# find highest mortality hurricane and the number of deaths
#print(calculating_deaths(hurricanes))

# 7
# Rating Hurricanes by Mortality
hurricanes_by_mortality = {}
def rating_canes(hurricanes):
  hurricanes_by_mortality[0] = []
  hurricanes_by_mortality[1] = []
  hurricanes_by_mortality[2] = []
  hurricanes_by_mortality[3] = []
  hurricanes_by_mortality[4] = []
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] < 100:
      hurricanes_by_mortality[0].append(hurricanes[cane])
    if 100 <= hurricanes[cane]["Deaths"] < 500:
      hurricanes_by_mortality[1].append(hurricanes[cane])
    if 500 <= hurricanes[cane]["Deaths"] < 1000:
      hurricanes_by_mortality[2].append(hurricanes[cane])
    if 1000 <= hurricanes[cane]["Deaths"] < 10000:
      hurricanes_by_mortality[3].append(hurricanes[cane])
    else:
      hurricanes_by_mortality[4].append(hurricanes[cane])
      
# categorize hurricanes in new dictionary with mortality severity as key
rating_canes(hurricanes)
#print(hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage
def calculating_max_damage(hurricanes):
  dest_count = 0
  name = "a"
  for cane in hurricanes: 
    if hurricanes[cane]["Damage"] == "Damages not recorded":
      pass
    else:
      if hurricanes[cane]["Damage"] > dest_count:
        dest_count = hurricanes[cane]["Damage"]
        name = hurricanes[cane]["Name"]
  return name, dest_count
# find highest damage inducing hurricane and its total cost
#print(calculating_max_damage(hurricanes))


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
hurricanes_by_damage = {}
def rating_canes(hurricanes):
  hurricanes_by_damage[0] = []
  hurricanes_by_damage[1] = []
  hurricanes_by_damage[2] = []
  hurricanes_by_damage[3] = []
  hurricanes_by_damage[4] = []
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] < 100000000:
      hurricanes_by_damage[0].append(hurricanes[cane])
    if 100000000 <= hurricanes[cane]["Deaths"] < 1000000000:
      hurricanes_by_damage[1].append(hurricanes[cane])
    if 1000000000 <= hurricanes[cane]["Deaths"] < 10000000000:
      hurricanes_by_damage[2].append(hurricanes[cane])
    if 10000000000 <= hurricanes[cane]["Deaths"] < 50000000000:
      hurricanes_by_damage[3].append(hurricanes[cane])
    else:
      hurricanes_by_damage[4].append(hurricanes[cane])
  
# categorize hurricanes in new dictionary with damage severity as key
rating_canes(hurricanes)
#print(hurricanes_by_damage)