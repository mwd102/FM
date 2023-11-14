def calculate_mezzala_support(squad_rawdata):
    # calculates Mezzala_Support score
    squad_rawdata['mezs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['mezs_green'] = ( squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] )
    squad_rawdata['mezs_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] )
    squad_rawdata['mezs'] =( ( ( squad_rawdata['mezs_key'] * 5) + (squad_rawdata['mezs_green'] * 3) + (squad_rawdata['mezs_blue'] * 1) ) / 40)
    squad_rawdata.mezs= squad_rawdata.mezs.round(1)
    return(squad_rawdata)
