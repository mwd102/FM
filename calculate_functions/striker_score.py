def calculate_striker_score(squad_rawdata, str_core, str_secondary ):
    #Default: 4
    squad_rawdata['str_core'] = (
        squad_rawdata['Cmp'] + squad_rawdata['Fin'] +
        squad_rawdata['OtB'] + squad_rawdata['Pac']) / str_core
    #Default: 11
    squad_rawdata['str_secondary'] = (
        squad_rawdata['Acc'] + squad_rawdata['Agi'] +
        squad_rawdata['Ant'] + squad_rawdata['Bal'] +
        squad_rawdata['Dec'] + squad_rawdata['Dri'] +
        squad_rawdata['Fir'] + squad_rawdata['Pas'] +
        squad_rawdata['Sta'] + squad_rawdata['Tec'] +
        squad_rawdata['Wor']) / str_secondary
    squad_rawdata['str'] = ((squad_rawdata['str_core'] * 0.5) +
                            (squad_rawdata['str_secondary'] * 0.5))
    squad_rawdata.str = squad_rawdata.str.round(1)
    return squad_rawdata
