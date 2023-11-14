def calculate_trequartista_attack(squad_rawdata):
    # calculates Trequartista_Attack score
    squad_rawdata['trea_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['trea_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] )
    squad_rawdata['trea_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['trea'] =( ( ( squad_rawdata['trea_key'] * 5) + (squad_rawdata['trea_green'] * 3) + (squad_rawdata['trea_blue'] * 1) ) / 45)
    squad_rawdata.trea= squad_rawdata.trea.round(1)
    return(squad_rawdata)
