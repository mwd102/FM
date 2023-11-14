def calculate_poacher_attack(squad_rawdata):
    # calculates Poacher_Attack score
    squad_rawdata['pa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['pa_green'] = ( squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['OtB'] )
    squad_rawdata['pa_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Hea'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] )
    squad_rawdata['pa'] =( ( ( squad_rawdata['pa_key'] * 5) + (squad_rawdata['pa_green'] * 3) + (squad_rawdata['pa_blue'] * 1) ) / 28)
    squad_rawdata.pa= squad_rawdata.pa.round(1)
    return(squad_rawdata)
