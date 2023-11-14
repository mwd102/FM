def calculate_inside_forward_support(squad_rawdata):
    # calculates Inside_forward_Support score
    squad_rawdata['ifs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ifs_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] )
    squad_rawdata['ifs_blue'] = ( squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Fla'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] )
    squad_rawdata['ifs'] =( ( ( squad_rawdata['ifs_key'] * 5) + (squad_rawdata['ifs_green'] * 3) + (squad_rawdata['ifs_blue'] * 1) ) / 45)
    squad_rawdata.ifs= squad_rawdata.ifs.round(1)
    return(squad_rawdata)
