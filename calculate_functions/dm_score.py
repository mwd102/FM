def calculate_dm_score(squad_rawdata):
    squad_rawdata['dm'] = ((
        (squad_rawdata['Wor'] * 5) +
        (squad_rawdata['Pac'] * 5) +
        (squad_rawdata['Sta'] * 3) +
        (squad_rawdata['Pas'] * 3) +
        (squad_rawdata['Tck'] * 2) +
        (squad_rawdata['Ant'] * 2) +
        (squad_rawdata['Cnt'] * 2) +
        (squad_rawdata['Pos'] * 2) +
        (squad_rawdata['Bal'] * 2) +
        (squad_rawdata['Agi'] * 2) +
        (squad_rawdata['Tea'] * 1) +
        (squad_rawdata['Fir'] * 1) +
        (squad_rawdata['Mar'] * 1) +
        (squad_rawdata['Agg'] * 1) +
        (squad_rawdata['Cmp'] * 1) +
        (squad_rawdata['Dec'] * 1) +
        (squad_rawdata['Str'] * 1)) / 35)
    squad_rawdata.dm = squad_rawdata.dm.round(1)
    return squad_rawdata
