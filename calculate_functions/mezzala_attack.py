def calculate_mezzala_attack(squad_rawdata):
    # calculates Mezzala_Attack score
    squad_rawdata['meza_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['meza_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] )
    squad_rawdata['meza_blue'] = ( squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Fla'] + squad_rawdata['Bal'] )
    squad_rawdata['meza'] =( ( ( squad_rawdata['meza_key'] * 5) + (squad_rawdata['meza_green'] * 3) + (squad_rawdata['meza_blue'] * 1) ) / 45)
    squad_rawdata.meza= squad_rawdata.meza.round(1)
    return(squad_rawdata)
