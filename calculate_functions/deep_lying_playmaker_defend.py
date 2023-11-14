def calculate_deep_lying_playmaker_defend(squad_rawdata):
    # calculates Deep_lying_playmaker_Defend score
    squad_rawdata['dlpd_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['dlpd_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['dlpd_blue'] = ( squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Pos'] + squad_rawdata['Bal'] )
    squad_rawdata['dlpd'] =( ( ( squad_rawdata['dlpd_key'] * 5) + (squad_rawdata['dlpd_green'] * 3) + (squad_rawdata['dlpd_blue'] * 1) ) / 45)
    squad_rawdata.dlpd= squad_rawdata.dlpd.round(1)
    return(squad_rawdata)
