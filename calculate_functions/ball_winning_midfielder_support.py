def calculate_ball_winning_midfielder_support(squad_rawdata):
    # calculates Ball_winning_midfielder_Support score
    squad_rawdata['bwms_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['bwms_green'] = ( squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Tea'] )
    squad_rawdata['bwms_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Agi'] + squad_rawdata['Str'] )
    squad_rawdata['bwms'] =( ( ( squad_rawdata['bwms_key'] * 5) + (squad_rawdata['bwms_green'] * 3) + (squad_rawdata['bwms_blue'] * 1) ) / 38)
    squad_rawdata.bwms= squad_rawdata.bwms.round(1)
    return(squad_rawdata)
