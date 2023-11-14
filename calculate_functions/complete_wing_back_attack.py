def calculate_complete_wing_back_attack(squad_rawdata):
    # calculates Complete_wing_back_Attack score
    squad_rawdata['cwba_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['cwba_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Tec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['cwba_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['cwba'] =( ( ( squad_rawdata['cwba_key'] * 5) + (squad_rawdata['cwba_green'] * 3) + (squad_rawdata['cwba_blue'] * 1) ) / 47)
    squad_rawdata.cwba= squad_rawdata.cwba.round(1)
    return(squad_rawdata)
