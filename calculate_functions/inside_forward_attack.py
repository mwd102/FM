def calculate_inside_forward_attack(squad_rawdata):
    # calculates Inside_forward_Attack score
    squad_rawdata['ifa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ifa_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] )
    squad_rawdata['ifa_blue'] = ( squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Cmp'] + squad_rawdata['Fla'] + squad_rawdata['Bal'] )
    squad_rawdata['ifa'] =( ( ( squad_rawdata['ifa_key'] * 5) + (squad_rawdata['ifa_green'] * 3) + (squad_rawdata['ifa_blue'] * 1) ) / 46)
    squad_rawdata.ifa= squad_rawdata.ifa.round(1)
    return(squad_rawdata)
