def calculate_wide_midfielder_attack(squad_rawdata):
    # calculates Wide_midfielder_Attack score
    squad_rawdata['wma_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wma_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['wma_blue'] = ( squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] )
    squad_rawdata['wma'] =( ( ( squad_rawdata['wma_key'] * 5) + (squad_rawdata['wma_green'] * 3) + (squad_rawdata['wma_blue'] * 1) ) / 41)
    squad_rawdata.wma= squad_rawdata.wma.round(1)
    return(squad_rawdata)
