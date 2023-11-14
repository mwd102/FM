def calculate_ball_winning_midfielder_defend(squad_rawdata):
    # calculates Ball_winning_midfielder_Defend score
    squad_rawdata['bwmd_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['bwmd_green'] = ( squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Tea'] )
    squad_rawdata['bwmd_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Str'] )
    squad_rawdata['bwmd'] =( ( ( squad_rawdata['bwmd_key'] * 5) + (squad_rawdata['bwmd_green'] * 3) + (squad_rawdata['bwmd_blue'] * 1) ) / 38)
    squad_rawdata.bwmd= squad_rawdata.bwmd.round(1)
    return(squad_rawdata)
