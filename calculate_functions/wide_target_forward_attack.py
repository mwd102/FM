def calculate_wide_target_forward_attack(squad_rawdata):
    # calculates Wide_target_forward_Attack score
    squad_rawdata['wtfa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wtfa_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['OtB'] + squad_rawdata['Jum'] + squad_rawdata['Str'] )
    squad_rawdata['wtfa_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Ant'] + squad_rawdata['Tea'] + squad_rawdata['Bal'] )
    squad_rawdata['wtfa'] =( ( ( squad_rawdata['wtfa_key'] * 5) + (squad_rawdata['wtfa_green'] * 3) + (squad_rawdata['wtfa_blue'] * 1) ) / 41)
    squad_rawdata.wtfa= squad_rawdata.wtfa.round(1)
    return(squad_rawdata)
