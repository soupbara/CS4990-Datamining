import pandas as pd

def parseCSV() :
    # grab class, archetype 1, archetype 2, and each HP/ATK/DEF
    cols = ['Class', 'Archetype 1', 'Full HP', 'Full ATK', 'Full DEF']

    archetype1 = []
    archetype2 = []
    fullHPMean = []
    fullHPMedian = []
    fullATKMean = []
    fullATKMedian = []
    fullDEFMean = []
    fullDEFMedian = []

    # due to the fact that archetype separations are arbitary, I'll only parse through Archetype 1

    # CASTERS
    casterDF = pd.read_csv("separated_types/casters.csv")

    aoe = casterDF[casterDF['Archetype 1'] == "AoE"]
    archetype1.append("AoE Caster")
    archetype2.append("Splash Caster")
    aoeFullHP = aoe['Full HP']
    aoeFullATK = aoe['Full ATK']
    aoeFullDEF = aoe['Full DEF']
    fullHPMean.append(aoeFullHP.mean())
    fullHPMedian.append(aoeFullHP.median())
    fullATKMean.append(aoeFullATK.mean())
    fullATKMedian.append(aoeFullATK.median())
    fullDEFMean.append(aoeFullDEF.mean())
    fullDEFMedian.append(aoeFullDEF.median())

    burninator = casterDF[casterDF['Archetype 1'] == "Burninator"]
    archetype1.append("Burninator")
    archetype2.append("Blast Caster")
    burninatorFullHP = burninator['Full HP']
    burninatorFullATK = burninator['Full ATK']
    burninatorFullDEF = burninator['Full DEF']
    fullHPMean.append(burninatorFullHP.mean())
    fullHPMedian.append(burninatorFullHP.median())
    fullATKMean.append(burninatorFullATK.mean())
    fullATKMedian.append(burninatorFullATK.median())
    fullDEFMean.append(burninatorFullDEF.mean())
    fullDEFMedian.append(burninatorFullDEF.median())

    chainCaster = casterDF[casterDF['Archetype 1'] == "Chain Caster"]
    archetype1.append("Chain Caster")
    archetype2.append("N/A")
    chainCasterFullHP = chainCaster['Full HP']
    chainCasterFullATK = chainCaster['Full ATK']
    chainCasterFullDEF = chainCaster['Full DEF']
    fullHPMean.append(chainCasterFullHP.mean())
    fullHPMedian.append(chainCasterFullHP.median())
    fullATKMean.append(chainCasterFullATK.mean())
    fullATKMedian.append(chainCasterFullATK.median())
    fullDEFMean.append(chainCasterFullDEF.mean())
    fullDEFMedian.append(chainCasterFullDEF.median())

    charge = casterDF[casterDF['Archetype 1'] == "Charge"]
    archetype1.append("Charge")
    archetype2.append("Mystic Caster")
    chargeFullHP = charge['Full HP']
    chargeFullATK = charge['Full ATK']
    chargeFullDEF = charge['Full DEF']
    fullHPMean.append(chargeFullHP.mean())
    fullHPMedian.append(chargeFullHP.median())
    fullATKMean.append(chargeFullATK.mean())
    fullATKMedian.append(chargeFullATK.median())
    fullDEFMean.append(chargeFullDEF.mean())
    fullDEFMedian.append(chargeFullDEF.median())

    drone = casterDF[casterDF['Archetype 1'] == "Drone"]
    archetype1.append("Drone")
    archetype2.append("Mech-Accord")
    droneFullHP = drone['Full HP']
    droneFullATK = drone['Full ATK']
    droneFullDEF = drone['Full DEF']
    fullHPMean.append(droneFullHP.mean())
    fullHPMedian.append(droneFullHP.median())
    fullATKMean.append(droneFullATK.mean())
    fullATKMedian.append(droneFullATK.median())
    fullDEFMean.append(droneFullDEF.mean())
    fullDEFMedian.append(droneFullDEF.median())

    modal = casterDF[casterDF['Archetype 1'] == "Modal"]
    archetype1.append("Modal")
    archetype2.append("Phalanx Caster")
    modalFullHP = modal['Full HP']
    modalFullATK = modal['Full ATK']
    modalFullDEF = modal['Full DEF']
    fullHPMean.append(modalFullHP.mean())
    fullHPMedian.append(modalFullHP.median())
    fullATKMean.append(modalFullATK.mean())
    fullATKMedian.append(modalFullATK.median())
    fullDEFMean.append(modalFullDEF.mean())
    fullDEFMedian.append(modalFullDEF.median())

    st = casterDF[casterDF['Archetype 1'] == "ST"]
    archetype1.append("ST")
    archetype2.append("Core Caster")
    stFullHP = st['Full HP']
    stFullATK = st['Full ATK']
    stFullDEF = st['Full DEF']
    fullHPMean.append(stFullHP.mean())
    fullHPMedian.append(stFullHP.median())
    fullATKMean.append(stFullATK.mean())
    fullATKMedian.append(stFullATK.median())
    fullDEFMean.append(stFullDEF.mean())
    fullDEFMedian.append(stFullDEF.median())

    # SNIPERS
    sniperDF = pd.read_csv("separated_types/snipers.csv")

    longRange = sniperDF[sniperDF['Archetype 1'] == "Long-Range"]
    archetype1.append("Long-Range")
    archetype2.append("Deadeye")
    longRangeFullHP = longRange['Full HP']
    longRangeFullATK = longRange['Full ATK']
    longRangeFullDEF = longRange['Full DEF']
    fullHPMean.append(longRangeFullHP.mean())
    fullHPMedian.append(longRangeFullHP.median())
    fullATKMean.append(longRangeFullATK.mean())
    fullATKMedian.append(longRangeFullATK.median())
    fullDEFMean.append(longRangeFullDEF.mean())
    fullDEFMedian.append(longRangeFullDEF.median())

    boomstick = sniperDF[sniperDF['Archetype 1'] == "Boomstick"]
    archetype1.append("Boomstick")
    archetype2.append("Spreadshooter")
    boomstickFullHP = boomstick['Full HP']
    boomstickFullATK = boomstick['Full ATK']
    boomstickFullDEF = boomstick['Full DEF']
    fullHPMean.append(boomstickFullHP.mean())
    fullHPMedian.append(boomstickFullHP.median())
    fullATKMean.append(boomstickFullATK.mean())
    fullATKMedian.append(boomstickFullATK.median())
    fullDEFMean.append(boomstickFullDEF.mean())
    fullDEFMedian.append(boomstickFullDEF.median())

    antiAir = sniperDF[sniperDF['Archetype 1'] == "Anti-Air"]
    archetype1.append("Anti-Air")
    archetype2.append("Marksman")
    antiAirFullHP = antiAir['Full HP']
    antiAirFullATK = antiAir['Full ATK']
    antiAirFullDEF = antiAir['Full DEF']
    fullHPMean.append(antiAirFullHP.mean())
    fullHPMedian.append(antiAirFullHP.median())
    fullATKMean.append(antiAirFullATK.mean())
    fullATKMedian.append(antiAirFullATK.median())
    fullDEFMean.append(antiAirFullDEF.mean())
    fullDEFMedian.append(antiAirFullDEF.median())

    aftershock = sniperDF[sniperDF['Archetype 1'] == "Aftershock"]
    archetype1.append("Aftershock")
    archetype2.append("Flinger")
    aftershockFullHP = aftershock['Full HP']
    aftershockFullATK = aftershock['Full ATK']
    aftershockFullDEF = aftershock['Full DEF']
    fullHPMean.append(aftershockFullHP.mean())
    fullHPMedian.append(aftershockFullHP.median())
    fullATKMean.append(aftershockFullATK.mean())
    fullATKMedian.append(aftershockFullATK.median())
    fullDEFMean.append(aftershockFullDEF.mean())
    fullDEFMedian.append(aftershockFullDEF.median())

    heavyweight = sniperDF[sniperDF['Archetype 1'] == "Heavyweight"]
    archetype1.append("Heavyweight")
    archetype2.append("Besieger")
    heavyweightFullHP = heavyweight['Full HP']
    heavyweightFullATK = heavyweight['Full ATK']
    heavyweightFullDEF = heavyweight['Full DEF']
    fullHPMean.append(heavyweightFullHP.mean())
    fullHPMedian.append(heavyweightFullHP.median())
    fullATKMean.append(heavyweightFullATK.mean())
    fullATKMedian.append(heavyweightFullATK.median())
    fullDEFMean.append(heavyweightFullDEF.mean())
    fullDEFMedian.append(heavyweightFullDEF.median())

    aoe = sniperDF[sniperDF['Archetype 1'] == "AoE"]
    archetype1.append("AoE Sniper")
    archetype2.append("Artilleryman")
    aoeFullHP = aoe['Full HP']
    aoeFullATK = aoe['Full ATK']
    aoeFullDEF = aoe['Full DEF']
    fullHPMean.append(aoeFullHP.mean())
    fullHPMedian.append(aoeFullHP.median())
    fullATKMean.append(aoeFullATK.mean())
    fullATKMedian.append(aoeFullATK.median())
    fullDEFMean.append(aoeFullDEF.mean())
    fullDEFMedian.append(aoeFullDEF.median())

    closeRange = sniperDF[sniperDF['Archetype 1'] == "Close Range"]
    archetype1.append("Close Range")
    archetype2.append("Artilleryman")
    closeRangeFullHP = closeRange['Full HP']
    closeRangeFullATK = closeRange['Full ATK']
    closeRangeFullDEF = closeRange['Full DEF']
    fullHPMean.append(closeRangeFullHP.mean())
    fullHPMedian.append(closeRangeFullHP.median())
    fullATKMean.append(closeRangeFullATK.mean())
    fullATKMedian.append(closeRangeFullATK.median())
    fullDEFMean.append(closeRangeFullDEF.mean())
    fullDEFMedian.append(closeRangeFullDEF.median())

    # Convert to CSV
    exportedData = pd.DataFrame({
        'Archetype 1' : archetype1,
        'Archetype 2': archetype2,
        'Full HP Mean': fullHPMean,
        'Full HP Median': fullHPMedian,
        'Full ATK Mean': fullATKMean,
        'Full ATK Median': fullATKMedian,
        'Full DEF Mean': fullDEFMean,
        'Full DEF Median': fullDEFMedian,
    })

    return exportedData

def main() :
    exportedData = parseCSV()
    print(exportedData)
    exportedData.to_csv("csMeanMedian.csv")

# run
if __name__ == '__main__':
    main()