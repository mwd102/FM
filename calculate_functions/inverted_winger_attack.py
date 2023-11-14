def calculate_inverted_winger_attack(squad_rawdata):
    # calculates Inverted_winger_Attack score
    squad_rawdata['iwa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['iwa_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agi'] )
    squad_rawdata['iwa_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] )
    squad_rawdata['iwa'] =( ( ( squad_rawdata['iwa_key'] * 5) + (squad_rawdata['iwa_green'] * 3) + (squad_rawdata['iwa_blue'] * 1) ) / 44)
    squad_rawdata.iwa= squad_rawdata.iwa.round(1)
    return(squad_rawdata)
