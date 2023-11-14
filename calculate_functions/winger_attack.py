def calculate_winger_attack(squad_rawdata):
    # calculates Winger_Attack score
    squad_rawdata['wa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wa_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Tec'] + squad_rawdata['Agi'] )
    squad_rawdata['wa_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Bal'] )
    squad_rawdata['wa'] =( ( ( squad_rawdata['wa_key'] * 5) + (squad_rawdata['wa_green'] * 3) + (squad_rawdata['wa_blue'] * 1) ) / 38)
    squad_rawdata.wa= squad_rawdata.wa.round(1)
    return(squad_rawdata)
