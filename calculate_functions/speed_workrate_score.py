def calculate_speed_workrate_score(squad_rawdata):
    squad_rawdata['Spd'] = (
        squad_rawdata['Pac'] + squad_rawdata['Acc']) / 2
    squad_rawdata['Work'] =
    (squad_rawdata['Wor'] + squad_rawdata['Sta']) / 2
    squad_rawdata['SetP'] = (
        squad_rawdata['Jum'] + squad_rawdata['Bra']) / 2
    return squad_rawdata
