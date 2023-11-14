def calculate_advanced_playmaker_support(squad_rawdata):
    # calculates Advanced_playmaker_Support score
    squad_rawdata['aps_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['aps_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['aps_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['Agi'] )
    squad_rawdata['aps'] =( ( ( squad_rawdata['aps_key'] * 5) + (squad_rawdata['aps_green'] * 3) + (squad_rawdata['aps_blue'] * 1) ) / 48)
    squad_rawdata.aps= squad_rawdata.aps.round(1)
    return(squad_rawdata)
