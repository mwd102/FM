def calculate_box_to_box_midfielder_support(squad_rawdata):
    # calculates Box_to_box_midfielder_Support score
    squad_rawdata['b2bs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['b2bs_green'] = ( squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['b2bs_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['b2bs'] =( ( ( squad_rawdata['b2bs_key'] * 5) + (squad_rawdata['b2bs_green'] * 3) + (squad_rawdata['b2bs_blue'] * 1) ) / 44)
    squad_rawdata.b2bs= squad_rawdata.b2bs.round(1)
    return(squad_rawdata)
