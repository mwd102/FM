def calculate_segundo_volante_score(squad_rawdata):
    squad_rawdata['vol'] = ((
        (squad_rawdata['Wor'] * 5) +
        (squad_rawdata['Pac'] * 5) +
        (squad_rawdata['Sta'] * 3) +
        (squad_rawdata['Pas'] * 3) +
        (squad_rawdata['Tck'] * 2) +
        (squad_rawdata['Ant'] * 2) +
        (squad_rawdata['Cnt'] * 2) +
        (squad_rawdata['Pos'] * 2) +
        (squad_rawdata['Tea'] * 2) +
        (squad_rawdata['Fir'] * 1) +
        (squad_rawdata['Mar'] * 1) +
        (squad_rawdata['Agg'] * 1) +
        (squad_rawdata['Cmp'] * 1) +
        (squad_rawdata['Dec'] * 1) +
        (squad_rawdata['Str'] * 1))
        / 32)
    squad_rawdata.vol = squad_rawdata.vol.round(1)
    return squad_rawdata
