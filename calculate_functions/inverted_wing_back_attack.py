def calculate_inverted_wing_back_attack(squad_rawdata):
    # calculates Inverted_wing_back_Attack score
    squad_rawdata['iwba_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['iwba_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['iwba_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Lon'] + squad_rawdata['Mar'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Fla'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] )
    squad_rawdata['iwba'] =( ( ( squad_rawdata['iwba_key'] * 5) + (squad_rawdata['iwba_green'] * 3) + (squad_rawdata['iwba_blue'] * 1) ) / 56)
    squad_rawdata.iwba= squad_rawdata.iwba.round(1)
    return(squad_rawdata)
