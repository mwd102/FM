def calculate_roaming_playmaker_support(squad_rawdata):
    # calculates Roaming_playmaker_Support score
    squad_rawdata['rps_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['rps_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['rps_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Lon'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['rps'] =( ( ( squad_rawdata['rps_key'] * 5) + (squad_rawdata['rps_green'] * 3) + (squad_rawdata['rps_blue'] * 1) ) / 53)
    squad_rawdata.rps= squad_rawdata.rps.round(1)
    return(squad_rawdata)
