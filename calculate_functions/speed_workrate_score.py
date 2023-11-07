def calculate_speed_workrate_score(squad_rawdata, speed, workrate, setp):
    #Default: 2
    squad_rawdata['Spd'] = (
        squad_rawdata['Pac'] + squad_rawdata['Acc']) / speed
    #Default: 2
    squad_rawdata['Work'] = (
        squad_rawdata['Wor'] + squad_rawdata['Sta']) / workrate
    #Default: 2
    squad_rawdata['SetP'] = (
        squad_rawdata['Jum'] + squad_rawdata['Bra']) / setp
    return squad_rawdata
