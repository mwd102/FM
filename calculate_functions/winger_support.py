def calculate_winger_support(squad_rawdata):
    # calculates Winger_Support score
    squad_rawdata['ws_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ws_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Tec'] + squad_rawdata['Agi'] )
    squad_rawdata['ws_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['OtB'] + squad_rawdata['Bal'] )
    squad_rawdata['ws'] =( ( ( squad_rawdata['ws_key'] * 5) + (squad_rawdata['ws_green'] * 3) + (squad_rawdata['ws_blue'] * 1) ) / 36)
    squad_rawdata.ws= squad_rawdata.ws.round(1)
    return(squad_rawdata)
