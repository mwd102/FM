def calculate_shadow_striker_attack(squad_rawdata):
    # calculates Shadow_striker_Attack score
    squad_rawdata['ssa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ssa_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fin'] + squad_rawdata['Fir'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] )
    squad_rawdata['ssa_blue'] = ( squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['ssa'] =( ( ( squad_rawdata['ssa_key'] * 5) + (squad_rawdata['ssa_green'] * 3) + (squad_rawdata['ssa_blue'] * 1) ) / 44)
    squad_rawdata.ssa= squad_rawdata.ssa.round(1)
    return(squad_rawdata)
