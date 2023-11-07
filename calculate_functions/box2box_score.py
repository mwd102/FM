def calculate_box2box_score(squad_rawdata):
    squad_rawdata['box2'] = (
        (squad_rawdata['Pas'] * 5) +
        (squad_rawdata['Wor'] * 5) +
        (squad_rawdata['Sta'] * 4) +
        (squad_rawdata['Tck'] * 3) +
        (squad_rawdata['OtB'] * 3) +
        (squad_rawdata['Tea'] * 3) +
        (squad_rawdata['Vis'] * 2) +
        (squad_rawdata['Str'] * 2) +
        (squad_rawdata['Dec'] * 2) +
        (squad_rawdata['Pos'] * 2) +
        (squad_rawdata['Pac'] * 2) +
        (squad_rawdata['Agg'] * 1) +
        (squad_rawdata['Ant'] * 1) +
        (squad_rawdata['Fin'] * 1) +
        (squad_rawdata['Lon'] * 1) +
        (squad_rawdata['Cmp'] * 1) +
        (squad_rawdata['Acc'] * 1) +
        (squad_rawdata['Bal'] * 1) +
        (squad_rawdata['Fir'] * 1) +
        (squad_rawdata['Dri'] * 1) +
        (squad_rawdata['Tec'] * 1))
    squad_rawdata.box2 = squad_rawdata.box2.round(0)
    return squad_rawdata
