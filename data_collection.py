# April Trinh
# CS 4990
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/

from bs4 import BeautifulSoup
from requests import get
import pandas as pd

# web scraper
def web_scraper(rows) :
    url = 'https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##stats'
    response = get(url)
    # print(response.text[:500])
    # this prints out the first 500 characters of the HTML

    soup = BeautifulSoup(response.text, 'html.parser')
    type(soup)

    # list containers
    name = []
    typeclass = []
    archetype1 = []
    archetype2 = []
    rarity = []

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

    count = 0 # keeps track of how many rows traversed
    max = rows if rows != None else len(operator_info)

    for operator in operator_info :
        if count == max :
            break

        # basic operator information
        op = operator
        op_name = op.find('div', class_="operator-title").a.text
        op_type = op.find_all('div', class_="info-div")
        op_maintype = op_type[0].span.text
        op_archetype = op_type[1].find('span', "prof-title").text

        name.append(op_name)
        typeclass.append(op_maintype)

        if ' / ' not in op_archetype :
            archetype1.append(op_archetype)
            archetype2.append("N/A")
        else :
            temp = op_archetype.split(" / ")
            archetype1.append(temp[0])
            archetype2.append(temp[1])

        op_rarity = operator.find('div', class_="rarity-div").find_all('img')
        rarity.append(len(op_rarity))

        count += 1

    operator_all_stats = soup.find_all('td', class_="stats-section")

    count = 0 # reset count for next loop
    # max value should be the same

    for operator in operator_all_stats :
        if count == max :
            break

        op_stats = operator
        op_allstats = op_stats.div.div.find_all('table', class_="stats-table")

        # op_allstats[0] returns HP, ATK, and DEF, and cost

        op_HADCstats = op_allstats[0].tbody.find('tr', class_="baseStat").find_all('td', class_="stat-cell")
        op_hp = 0 if '-' in op_HADCstats[0].text else int(op_HADCstats[0].text)
        op_atk = 0 if '-' in op_HADCstats[1].text else int(op_HADCstats[1].text)
        op_def = 0 if '-' in op_HADCstats[2].text else int(op_HADCstats[2].text)
        
        base_hp.append(op_hp)
        base_atk.append(op_atk)
        base_def.append(op_def)

        op_potentialstats = op_allstats[0].tbody.find('tr', class_="potentialStat").find_all('td', class_="stat-cell")
        op_pothp = int(op_potentialstats[0].text)
        op_potatk = int(op_potentialstats[1].text)
        op_potdef = int(op_potentialstats[2].text)

        pot_hp.append(op_pothp)
        pot_atk.append(op_potatk)
        pot_def.append(op_potdef)

        op_truststats = op_allstats[0].tbody.find('tr', class_="trustStat").find_all('td', class_="stat-cell")
        op_trusthp = int(op_truststats[0].text)
        op_trustatk = int(op_truststats[1].text)
        op_trustdef = int(op_truststats[2].text)

        trust_hp.append(op_trusthp)
        trust_atk.append(op_trustatk)
        trust_def.append(op_trustdef)

        op_fullstats = op_allstats[0].tbody.find('tr', class_="fullStat").find_all('td', class_="stat-cell")
        op_fullhp = int(op_fullstats[0].text)
        op_fullatk = int(op_fullstats[1].text)
        op_fulldef = int(op_fullstats[2].text)

        full_hp.append(op_fullhp)
        full_atk.append(op_fullatk)
        full_def.append(op_fulldef)

        op_cost = op_allstats[0].tbody.find('tr', class_="fullStat").find_all('td')
        op_basecost = int(op_cost[3].find('span', class_="base-potential-cell").text) if op_cost[3].find('span', class_="base-potential-cell").text != '' else 0
        op_maxcost = int(op_cost[3].find('span', class_="max-potential-cell").text) if op_cost[3].find('span', class_="max-potential-cell").text != '' else 0

        base_cost.append(op_basecost)
        max_cost.append(op_maxcost)

        # op_allstats[1] returns Res, Block, Redeploy, and Interval
        op_RBRI = op_allstats[1].tbody.tr.find_all('td')

        op_res = 0 if '-' in op_RBRI[0].text else int(op_RBRI[0].text)
        op_block = 0 if '-' in op_RBRI[1].text else int(op_RBRI[1].text)

        op_baseredeploy = 0 if '-' in op_RBRI[2].find('span', class_="base-potential-cell").text else int(op_RBRI[2].find('span', class_="base-potential-cell").text)
        op_maxredeploy = 0 if '-' in op_RBRI[2].find('span', class_="max-potential-cell").text else int(op_RBRI[2].find('span', class_="max-potential-cell").text)

        op_interval = op_RBRI[3].text.replace("\n", "")
        op_interval = op_interval.replace("s", "")
        op_interval = op_interval.replace(" ", "")
        if op_interval == "" :
            op_interval = 0

        res.append(op_res)
        block_num.append(op_block)
        base_redeploy.append(op_baseredeploy)
        max_redeploy.append(op_maxredeploy)
        interval_num.append(op_interval)

        # target number and damage type
        op_TD = op_stats.find('div', class_="target-damage-type")
        op_target = op_TD.find('div', class_="target-cell").text
        op_target = op_target.replace("Target:", "")
        op_target = op_target.replace("\n", "")
        if op_target == '' :
            op_target = 0

        op_dmgtype = op_TD.find('div', class_="damage-type-cell").a.text
        op_dmgtype = op_dmgtype.replace("\n", "")

        target_num.append(op_target)
        dmg_type.append(op_dmgtype)

        count += 1

    exportedData = pd.DataFrame({
        'Name' : name,
        'Class' : typeclass,
        'Archetype 1' : archetype1,
        'Archetype 2' : archetype2,
        'Rarity' : rarity,

        'Base HP' : base_hp,
        'Base ATK' : base_atk,
        'Base DEF' : base_def,

        'HP (Max Potential)' : pot_hp,
        'ATK (Max Potential)' : pot_atk,
        'DEF (Max Potential)' : pot_def,

        'HP (Max Trust)' : trust_hp,
        'ATK (Max Trust)' : trust_atk,
        'DEF (Max Trust)' : trust_def,

        'Full HP' : full_hp,
        'Full ATK' : full_atk,
        'Full DEF' : full_def,

        'Resistance' : res,

        'Base Cost' : base_cost,
        'Max Cost' : max_cost,

        'Block Count' : block_num,
        'Base Redeployment Time (s)' : base_redeploy,
        'Max Redeployment Time (s)' : max_redeploy,
        'Attack Interval (s)' : interval_num,

        'Target Number' : target_num,
        'Damage Type' : dmg_type,
    })

    print(exportedData)
    return exportedData

# if the rows parameter is None, all available data should be saved, otherwise save only the first "rows" rows
def get_dataset(filename, rows=None):
    open(filename, 'w')
    web_scraper(rows).to_csv(filename)


# main method
def main() :
    filename = input("Enter CSV filename, no .csv extention.\n\t:: ")
    rows = input("Enter the number of rows of data desired. Enter no input for all.\n\t:: ")
    rows = None if rows == '' else int(rows)

    get_dataset(filename + '.csv', rows)

# run
if __name__ == '__main__':
    main()