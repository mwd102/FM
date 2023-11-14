def calculate_wing_back_attack(squad_rawdata):
    # calculates Wing_back_Attack score
    squad_rawdata['wba_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wba_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['wba_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['wba'] =( ( ( squad_rawdata['wba_key'] * 5) + (squad_rawdata['wba_green'] * 3) + (squad_rawdata['wba_blue'] * 1) ) / 48)
    squad_rawdata.wba= squad_rawdata.wba.round(1)
    return(squad_rawdata)
