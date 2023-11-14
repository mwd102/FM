def calculate_pressing_forward_attack(squad_rawdata):
    # calculates Pressing_forward_Attack score
    squad_rawdata['pfa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['pfa_green'] = ( squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Wor'] + squad_rawdata['Sta'] )
    squad_rawdata['pfa_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['pfa'] =( ( ( squad_rawdata['pfa_key'] * 5) + (squad_rawdata['pfa_green'] * 3) + (squad_rawdata['pfa_blue'] * 1) ) / 43)
    squad_rawdata.pfa= squad_rawdata.pfa.round(1)
    return(squad_rawdata)
