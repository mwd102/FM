def calculate_carrilero_support(squad_rawdata):
    # calculates Carrilero_Support score
    squad_rawdata['cars_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['cars_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['cars_blue'] = ( squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] )
    squad_rawdata['cars'] =( ( ( squad_rawdata['cars_key'] * 5) + (squad_rawdata['cars_green'] * 3) + (squad_rawdata['cars_blue'] * 1) ) / 44)
    squad_rawdata.cars= squad_rawdata.cars.round(1)
    return(squad_rawdata)
