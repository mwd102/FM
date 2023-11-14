def calculate_attacking_midfielder_attack(squad_rawdata):
    # calculates Attacking_midfielder_Attack score
    squad_rawdata['ama_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ama_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] )
    squad_rawdata['ama_blue'] = ( squad_rawdata['Fin'] + squad_rawdata['Cmp'] + squad_rawdata['Vis'] + squad_rawdata['Agi'] )
    squad_rawdata['ama'] =( ( ( squad_rawdata['ama_key'] * 5) + (squad_rawdata['ama_green'] * 3) + (squad_rawdata['ama_blue'] * 1) ) / 51)
    squad_rawdata.ama= squad_rawdata.ama.round(1)
    return(squad_rawdata)
