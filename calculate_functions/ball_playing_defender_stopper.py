def calculate_ball_playing_defender_stopper(squad_rawdata):
    # calculates Ball_playing_defender_Stopper score
    squad_rawdata['bpds_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['bpds_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] + squad_rawdata['Agg'] + squad_rawdata['Bra'] + squad_rawdata['Dec'] )
    squad_rawdata['bpds_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Vis'] + squad_rawdata['Mar'] )
    squad_rawdata['bpds'] =( ( ( squad_rawdata['bpds_key'] * 5) + (squad_rawdata['bpds_green'] * 3) + (squad_rawdata['bpds_blue'] * 1) ) / 50)
    squad_rawdata.bpds= squad_rawdata.bpds.round(1)
    return(squad_rawdata)
