def calculate_cb_score(squad_rawdata, cb_core, cb_secondary):
    #Default: 9
    squad_rawdata['cb_core'] = (
        squad_rawdata['Cmp'] + squad_rawdata['Hea'] + squad_rawdata['Jum'] +
        squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Pos'] +
        squad_rawdata['Str'] + squad_rawdata['Tck'] + squad_rawdata['Pac']) / cb_core
    #Default: 8
    squad_rawdata['cb_secondary'] = (
        squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] +
        squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Fir'] +
        squad_rawdata['Tec'] + squad_rawdata['Vis']) / cb_secondary
    squad_rawdata['cb'] = (
        (squad_rawdata['cb_core'] * 0.75) +
        (squad_rawdata['cb_secondary'] * 0.25)
        )
    squad_rawdata.cb = squad_rawdata.cb.round(1)
    return squad_rawdata
