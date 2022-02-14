# https://www.dataquest.io/blog/web-scraping-beautifulsoup/

from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##stats'
response = get(url)
# print(response.text[:500])
# this prints out the first 500 characters of the HTML

soup = BeautifulSoup(response.text, 'html.parser')
type(soup)

# list containers
name = []
archtype = []
subtype = []

base_hp = []
base_atk = []
base_def = []

pot_hp = []
pot_atk = []
pot_def = []

trust_hp = []
trust_atk = []
trust_def = []

full_hp = []
full_atk = []
full_def = []

base_cost = []
max_cost = []

res = []
block_num = []
base_redeploy = []
max_redeploy = []
interval_num = []

target_num = []
dmg_type = []

operator_info = soup.find_all('td', class_= "operator-cell")
operator_all_stats = soup.find_all('td', class_="stats-section")

for operator in operator_info :
    # basic operator information
    
    op = operator
    op_name = op.find('div', class_="operator-title").a.text
    op_type = op.find_all('div', class_="info-div")
    op_maintype = op_type[0].span.text
    op_subtype = op_type[1].find('span', "prof-title").text

    name.append(op_name)
    archtype.append(op_maintype)
    archtype.append(op_subtype)

for operator in operator_all_stats :
    op_stats = operator
    op_allstats = op_stats.div.div.find_all('table', class_="stats-table")

    # op_allstats[0] returns HP, ATK, and DEF, and cost
    op_HADCstats = op_allstats[0].tbody.find('tr', class_="baseStat").find_all('td', class_="stat-cell")
    op_hp = int(op_HADCstats[0].text) if type(op_HADCstats[0].text) == int else 0
    op_atk = int(op_HADCstats[1].text) if type(op_HADCstats[1].text) == int else 0
    op_def = int(op_HADCstats[2].text) if type(op_HADCstats[2].text) == int else 0
    
    base_hp.append(op_hp)
    base_atk.append(op_atk)
    base_def.append(op_def)

    op_potentialstats = op_allstats[0].tbody.find('tr', class_="potentialStat").find_all('td', class_="stat-cell")
    op_pothp = int(op_potentialstats[0].text) if type(op_potentialstats[0].text) == int else 0
    op_potatk = int(op_potentialstats[1].text) if type(op_potentialstats[1].text) == int else 0
    op_potdef = int(op_potentialstats[2].text) if type(op_potentialstats[2].text) == int else 0

    pot_hp.append(op_pothp)
    pot_atk.append(op_potatk)
    pot_def.append(op_potdef)

    op_truststats = op_allstats[0].tbody.find('tr', class_="trustStat").find_all('td', class_="stat-cell")
    op_trusthp = int(op_truststats[0].text) if type(int(op_truststats[0].text)) == int else 0
    op_trustatk = int(op_truststats[1].text) if type(int(op_truststats[1].text)) == int else 0
    op_trustdef = int(op_truststats[2].text) if type(int(op_truststats[2].text)) == int else 0

    trust_hp.append(op_trusthp)
    trust_atk.append(op_trustatk)
    trust_def.append(op_trustdef)

    op_fullstats = op_allstats[0].tbody.find('tr', class_="fullStat").find_all('td', class_="stat-cell")
    op_fullhp = int(op_fullstats[0].text) if type(op_fullstats[0].text) == int else 0
    op_fullatk = int(op_fullstats[1].text) if type(op_fullstats[1].text) == int else 0
    op_fulldef = int(op_fullstats[2].text) if type(op_fullstats[2].text) == int else 0

    full_hp.append(op_fullhp)
    full_atk.append(op_fullatk)
    full_def.append(op_fulldef)

    op_cost = op_allstats[0].tbody.find('tr', class_="fullStat").find_all('td')
    op_basecost = int(op_cost[3].find('span', class_="base-potential-cell").text) if type(op_cost[3].find('span', class_="base-potential-cell").text) == int else 0
    op_maxcost = int(op_cost[3].find('span', class_="max-potential-cell").text) if type(op_cost[3].find('span', class_="max-potential-cell").text) == int else 0

    base_cost.append(op_basecost)
    max_cost.append(op_maxcost)

    # op_allstats[1] returns Res, Block, Redeploy, and Interval
    op_RBRI = op_allstats[1].tbody.tr.find_all('td')

    op_res = int(op_RBRI[0].text) if type(op_RBRI[0].text) == int else 0
    op_block = int(op_RBRI[1].text) if type(op_RBRI[1].text) == int else 0

    op_baseredeploy = int(op_RBRI[2].find('span', class_="base-potential-cell").text) if type(op_RBRI[2].find('span', class_="base-potential-cell").text) == int else 0
    op_maxredeploy = int(op_RBRI[2].find('span', class_="max-potential-cell").text) if type(op_RBRI[2].find('span', class_="max-potential-cell").text) == int else 0

    op_interval = op_RBRI[3].text
    op_interval = op_interval[1:len(op_interval) - 1]

    res.append(op_res)
    block_num.append(op_block)
    base_redeploy.append(op_baseredeploy)
    max_redeploy.append(op_maxredeploy)
    interval_num.append(op_interval)

    # target number and damage type
    op_TD = op_stats.find('div', class_="target-damage-type")
    op_target = op_TD.find('div', class_="target-cell").text
    op_target = op_target[9:len(op_target) - 1]

    op_dmgtype = op_TD.find('div', class_="damage-type-cell").a.text
    op_dmgtype = op_dmgtype[1:len(op_dmgtype) - 1]

    target_num.append(op_target)
    dmg_type.append(op_dmgtype)

# test_def = pd.DataFrame(
#     {'name' : name   
# })

# test print, with operator being at index 10

# print(op_name) # Pallas
# print(op_maintype) # Guard
# print(op_subtype) # Support / Instructor

# print(op_hp) # 1963
# print(op_atk) # 687
# print(op_def) # 455

# print(op_pothp) # 1963
# print(op_potatk) # 712
# print(op_potdef) # 455

# print(op_trusthp) # 2263
# print(op_trustatk) # 737 
# print(op_trustdef) # 455

# print(op_fullhp) # 2263
# print(op_fullatk) # 762 
# print(op_fulldef) # 455

# print(op_basecost) # 17
# print(op_maxcost) # 15

# print(op_res) # 0
# print(op_block) # 2

# print(op_baseredeploy) # 70
# print(op_maxredeploy) # 66

# print(op_interval) #1.05s

# print(op_target) # Target: 1
# print(op_dmgtype) # Physical


# test print lists

# print(name)
# print(archtype)
# print(subtype)

# print(base_hp)
# print(base_atk)
# print(base_def)

# print(pot_hp)
# print(pot_atk)
# print(pot_def)

# print(trust_hp)
# print(trust_atk)
# print(trust_def)

# print(full_hp)
# print(full_atk)
# print(full_def)

# print(base_cost)
# print(max_cost)

# print(res)
# print(block_num)
# print(base_redeploy)
# print(max_redeploy)
# print(interval_num)

# print(target_num)
# print(dmg_type)