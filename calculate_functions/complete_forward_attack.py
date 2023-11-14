def calculate_complete_forward_attack(squad_rawdata):
    # calculates Complete_forward_Attack score
    squad_rawdata['cfa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['cfa_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Hea'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] + squad_rawdata['Str'] )
    squad_rawdata['cfa_blue'] = ( squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] + squad_rawdata['Wor'] + squad_rawdata['Bal'] + squad_rawdata['Jum'] + squad_rawdata['Sta'] )
    squad_rawdata['cfa'] =( ( ( squad_rawdata['cfa_key'] * 5) + (squad_rawdata['cfa_green'] * 3) + (squad_rawdata['cfa_blue'] * 1) ) / 51)
    squad_rawdata.cfa= squad_rawdata.cfa.round(1)
    return(squad_rawdata)
