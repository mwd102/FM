def calculate_ball_playing_defender_defend(squad_rawdata):
    # calculates Ball_playing_defender_Defend score
    squad_rawdata['bpdd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['bpdd_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['bpdd_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Vis'] )
    squad_rawdata['bpdd'] =( ( ( squad_rawdata['bpdd_key'] * 5) + (squad_rawdata['bpdd_green'] * 3) + (squad_rawdata['bpdd_blue'] * 1) ) / 46)
    squad_rawdata.bpdd= squad_rawdata.bpdd.round(1)
    return(squad_rawdata)
