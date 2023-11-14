def calculate_wide_playmaker_support(squad_rawdata):
    # calculates Wide_playmaker_Support score
    squad_rawdata['wps_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wps_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['wps_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] )
    squad_rawdata['wps'] =( ( ( squad_rawdata['wps_key'] * 5) + (squad_rawdata['wps_green'] * 3) + (squad_rawdata['wps_blue'] * 1) ) / 44)
    squad_rawdata.wps= squad_rawdata.wps.round(1)
    return(squad_rawdata)
