def calculate_deep_lying_playmaker_support(squad_rawdata):
    # calculates Deep_lying_playmaker_Support score
    squad_rawdata['dlps_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['dlps_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['dlps_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] + squad_rawdata['Bal'] )
    squad_rawdata['dlps'] =( ( ( squad_rawdata['dlps_key'] * 5) + (squad_rawdata['dlps_green'] * 3) + (squad_rawdata['dlps_blue'] * 1) ) / 45)
    squad_rawdata.dlps= squad_rawdata.dlps.round(1)
    return(squad_rawdata)
