def calculate_deep_lying_forward_attack(squad_rawdata):
    # calculates Deep_lying_forward_Attack score
    squad_rawdata['dlfa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['dlfa_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['dlfa_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['dlfa'] =( ( ( squad_rawdata['dlfa_key'] * 5) + (squad_rawdata['dlfa_green'] * 3) + (squad_rawdata['dlfa_blue'] * 1) ) / 42)
    squad_rawdata.dlfa= squad_rawdata.dlfa.round(1)
    return(squad_rawdata)
