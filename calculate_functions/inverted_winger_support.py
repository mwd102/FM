def calculate_inverted_winger_support(squad_rawdata):
    # calculates Inverted_winger_Support score
    squad_rawdata['iws_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['iws_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agi'] )
    squad_rawdata['iws_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] )
    squad_rawdata['iws'] =( ( ( squad_rawdata['iws_key'] * 5) + (squad_rawdata['iws_green'] * 3) + (squad_rawdata['iws_blue'] * 1) ) / 42)
    squad_rawdata.iws= squad_rawdata.iws.round(1)
    return(squad_rawdata)
