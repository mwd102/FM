def calculate_target_forward_attack(squad_rawdata):
    # calculates Target_forward_Attack score
    squad_rawdata['tfa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['tfa_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] + squad_rawdata['Bal'] + squad_rawdata['Jum'] + squad_rawdata['Str'] )
    squad_rawdata['tfa_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['tfa'] =( ( ( squad_rawdata['tfa_key'] * 5) + (squad_rawdata['tfa_green'] * 3) + (squad_rawdata['tfa_blue'] * 1) ) / 41)
    squad_rawdata.tfa= squad_rawdata.tfa.round(1)
    return(squad_rawdata)
