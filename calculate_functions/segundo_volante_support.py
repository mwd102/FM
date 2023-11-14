def calculate_segundo_volante_support(squad_rawdata):
    # calculates Segundo_volante_Support score
    squad_rawdata['svs_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['svs_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] )
    squad_rawdata['svs_blue'] = ( squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['svs'] =( ( ( squad_rawdata['svs_key'] * 5) + (squad_rawdata['svs_green'] * 3) + (squad_rawdata['svs_blue'] * 1) ) / 44)
    squad_rawdata.svs= squad_rawdata.svs.round(1)
    return(squad_rawdata)
