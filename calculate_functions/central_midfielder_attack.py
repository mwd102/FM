def calculate_central_midfielder_attack(squad_rawdata):
    # calculates Central_midfielder_Attack score
    squad_rawdata['cma_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['cma_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] )
    squad_rawdata['cma_blue'] = ( squad_rawdata['Lon'] + squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['cma'] =( ( ( squad_rawdata['cma_key'] * 5) + (squad_rawdata['cma_green'] * 3) + (squad_rawdata['cma_blue'] * 1) ) / 39)
    squad_rawdata.cma= squad_rawdata.cma.round(1)
    return(squad_rawdata)
