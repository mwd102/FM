def calculate_inverted_winger_score(squad_rawdata, iw_core):
    #Default: 34
    squad_rawdata['amrl'] = ((
        (squad_rawdata['Acc'] * 5) +
        (squad_rawdata['Pac'] * 5) +
        (squad_rawdata['Wor'] * 5) +
        (squad_rawdata['Dri'] * 3) +
        (squad_rawdata['Pas'] * 3) +
        (squad_rawdata['Tec'] * 3) +
        (squad_rawdata['OtB'] * 3) +
        (squad_rawdata['Cro'] * 1) +
        (squad_rawdata['Fir'] * 1) +
        (squad_rawdata['Cmp'] * 1) +
        (squad_rawdata['Dec'] * 1) +
        (squad_rawdata['Vis'] * 1) +
        (squad_rawdata['Agi'] * 1) +
        (squad_rawdata['Sta'] * 1))
        / iw_core)
    squad_rawdata.amrl = squad_rawdata.amrl.round(1)
    return squad_rawdata
