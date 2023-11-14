def calculate_enganche_support(squad_rawdata):
    # calculates Enganche_Support score
    squad_rawdata['engs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['engs_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Vis'] )
    squad_rawdata['engs_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Agi'] )
    squad_rawdata['engs'] =( ( ( squad_rawdata['engs_key'] * 5) + (squad_rawdata['engs_green'] * 3) + (squad_rawdata['engs_blue'] * 1) ) / 44)
    squad_rawdata.engs= squad_rawdata.engs.round(1)
    return(squad_rawdata)
