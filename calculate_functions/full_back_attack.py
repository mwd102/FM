def calculate_full_back_attack(squad_rawdata):
    # calculates Full_back_Attack score
    squad_rawdata['fba_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['fba_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['fba_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] )
    squad_rawdata['fba'] =( ( ( squad_rawdata['fba_key'] * 5) + (squad_rawdata['fba_green'] * 3) + (squad_rawdata['fba_blue'] * 1) ) / 46)
    squad_rawdata.fba= squad_rawdata.fba.round(1)
    return(squad_rawdata)
