def calculate_advanced_forward_attack(squad_rawdata):
    # calculates Advanced_forward_Attack score
    squad_rawdata['afa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['afa_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] )
    squad_rawdata['afa_blue'] = ( squad_rawdata['Pas'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Wor'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] + squad_rawdata['Sta'] )
    squad_rawdata['afa'] =( ( ( squad_rawdata['afa_key'] * 5) + (squad_rawdata['afa_green'] * 3) + (squad_rawdata['afa_blue'] * 1) ) / 37)
    squad_rawdata.afa= squad_rawdata.afa.round(1)
    return(squad_rawdata)
