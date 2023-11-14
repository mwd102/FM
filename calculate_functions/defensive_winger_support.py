def calculate_defensive_winger_support(squad_rawdata):
    # calculates Defensive_winger_Support score
    squad_rawdata['dws_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['dws_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['dws_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] )
    squad_rawdata['dws'] =( ( ( squad_rawdata['dws_key'] * 5) + (squad_rawdata['dws_green'] * 3) + (squad_rawdata['dws_blue'] * 1) ) / 46)
    squad_rawdata.dws= squad_rawdata.dws.round(1)
    return(squad_rawdata)
