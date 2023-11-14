def calculate_attacking_midfielder_support(squad_rawdata):
    # calculates Attacking_midfielder_Support score
    squad_rawdata['ams_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ams_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] )
    squad_rawdata['ams_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Cmp'] + squad_rawdata['Vis'] + squad_rawdata['Agi'] )
    squad_rawdata['ams'] =( ( ( squad_rawdata['ams_key'] * 5) + (squad_rawdata['ams_green'] * 3) + (squad_rawdata['ams_blue'] * 1) ) / 48)
    squad_rawdata.ams= squad_rawdata.ams.round(1)
    return(squad_rawdata)
