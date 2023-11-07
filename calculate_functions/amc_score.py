def calculate_amc_score(squad_rawdata, amc_core):
    #Default: 1
    squad_rawdata['amc'] = (
        (squad_rawdata['Vis'] * 4) +
        (squad_rawdata['OtB'] * 4) +
        (squad_rawdata['Pas'] * 4) +
        (squad_rawdata['Dec'] * 3) +
        (squad_rawdata['Ant'] * 3) +
        (squad_rawdata['Cmp'] * 3) +
        (squad_rawdata['Tec'] * 3) +
        (squad_rawdata['Dri'] * 1) +
        (squad_rawdata['Fir'] * 1) +
        (squad_rawdata['Fla'] * 1) +
        (squad_rawdata['Lon'] * 1) +
        (squad_rawdata['Agi'] * 1) +
        (squad_rawdata['Fin'] * 1)
        ) * amc_core
    squad_rawdata.amc = squad_rawdata.amc.round(0)
    return squad_rawdata
