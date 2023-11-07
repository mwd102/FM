def calculate_winger_score(squad_rawdata, wing_core, wing_secondary):
    #Default: 6
    squad_rawdata['w_core'] = (
        squad_rawdata['Acc'] + squad_rawdata['Cro'] +
        squad_rawdata['Dri'] + squad_rawdata['OtB'] +
        squad_rawdata['Pac'] + squad_rawdata['Tec']) / wing_core
    #Default: 5
    squad_rawdata['w_secondary'] = (
        squad_rawdata['Agi'] + squad_rawdata['Fir'] +
        squad_rawdata['Pas'] + squad_rawdata['Sta'] +
        squad_rawdata['Wor']) / wing_secondary
    squad_rawdata['w'] = ((squad_rawdata['w_core'] * 0.75) +
                          (squad_rawdata['w_secondary'] * 0.25))
    squad_rawdata.w = squad_rawdata.w.round(1)
    return squad_rawdata
