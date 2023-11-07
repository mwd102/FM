def calculate_fb_score(squad_rawdata):
    squad_rawdata['fb_essential'] = (
        squad_rawdata['Wor'] +
        squad_rawdata['Acc'] +
        squad_rawdata['Pac'] +
        squad_rawdata['Sta'])
    squad_rawdata['fb_core'] = ( 
        squad_rawdata['Cro'] +
        squad_rawdata['Dri'] +
        squad_rawdata['Mar'] +
        squad_rawdata['OtB'] +
        squad_rawdata['Tck'] +
        squad_rawdata['Tea'])
    squad_rawdata['fb_secondary'] = ( 
        squad_rawdata['Agi'] +
        squad_rawdata['Ant'] +
        squad_rawdata['Cnt'] +
        squad_rawdata['Dec'] +
        squad_rawdata['Fir'] +
        squad_rawdata['Pas'] +
        squad_rawdata['Pos'] +
        squad_rawdata['Tec'])
    squad_rawdata['fb'] =(
        (
            (squad_rawdata['fb_essential'] * 5) + 
            ( squad_rawdata['fb_core'] * 3) + 
            (squad_rawdata['fb_secondary'] * 1)
        ) / 46 )
    squad_rawdata.fb = squad_rawdata.fb.round(1)
    return squad_rawdata
