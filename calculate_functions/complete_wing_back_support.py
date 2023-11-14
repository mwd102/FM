def calculate_complete_wing_back_support(squad_rawdata):
    # calculates Complete_wing_back_Support score
    squad_rawdata['cwbs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['cwbs_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Tec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['cwbs_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['Pos'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['cwbs'] =( ( ( squad_rawdata['cwbs_key'] * 5) + (squad_rawdata['cwbs_green'] * 3) + (squad_rawdata['cwbs_blue'] * 1) ) / 45)
    squad_rawdata.cwbs= squad_rawdata.cwbs.round(1)
    return(squad_rawdata)
