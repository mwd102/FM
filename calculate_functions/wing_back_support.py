def calculate_wing_back_support(squad_rawdata):
    # calculates Wing_back_Support score
    squad_rawdata['wbs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wbs_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['wbs_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['wbs'] =( ( ( squad_rawdata['wbs_key'] * 5) + (squad_rawdata['wbs_green'] * 3) + (squad_rawdata['wbs_blue'] * 1) ) / 47)
    squad_rawdata.wbs= squad_rawdata.wbs.round(1)
    return(squad_rawdata)
