def calculate_inverted_wing_back_support(squad_rawdata):
    # calculates Inverted_wing_back_Support score
    squad_rawdata['iwbs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['iwbs_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['iwbs_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] + squad_rawdata['Vis'] + squad_rawdata['Agi'] )
    squad_rawdata['iwbs'] =( ( ( squad_rawdata['iwbs_key'] * 5) + (squad_rawdata['iwbs_green'] * 3) + (squad_rawdata['iwbs_blue'] * 1) ) / 46)
    squad_rawdata.iwbs= squad_rawdata.iwbs.round(1)
    return(squad_rawdata)
