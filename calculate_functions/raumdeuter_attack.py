def calculate_raumdeuter_attack(squad_rawdata):
    # calculates Raumdeuter_Attack score
    squad_rawdata['raua_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['raua_green'] = ( squad_rawdata['Fin'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Bal'] )
    squad_rawdata['raua_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Tec'] )
    squad_rawdata['raua'] =( ( ( squad_rawdata['raua_key'] * 5) + (squad_rawdata['raua_green'] * 3) + (squad_rawdata['raua_blue'] * 1) ) / 43)
    squad_rawdata.raua= squad_rawdata.raua.round(1)
    return(squad_rawdata)
