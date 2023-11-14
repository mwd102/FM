def calculate_ball_playing_defender_cover(squad_rawdata):
    # calculates Ball_playing_defender_Cover score
    squad_rawdata['bpdc_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['bpdc_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] )
    squad_rawdata['bpdc_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Bra'] + squad_rawdata['Vis'] + squad_rawdata['Str'] + squad_rawdata['Hea'] )
    squad_rawdata['bpdc'] =( ( ( squad_rawdata['bpdc_key'] * 5) + (squad_rawdata['bpdc_green'] * 3) + (squad_rawdata['bpdc_blue'] * 1) ) / 47)
    squad_rawdata.bpdc= squad_rawdata.bpdc.round(1)
    return(squad_rawdata)
