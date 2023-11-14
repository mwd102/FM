def calculate_wide_playmaker_attack(squad_rawdata):
    # calculates Wide_playmaker_Attack score
    squad_rawdata['wpa_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wpa_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['wpa_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['Agi'] )
    squad_rawdata['wpa'] =( ( ( squad_rawdata['wpa_key'] * 5) + (squad_rawdata['wpa_green'] * 3) + (squad_rawdata['wpa_blue'] * 1) ) / 50)
    squad_rawdata.wpa= squad_rawdata.wpa.round(1)
    return(squad_rawdata)
