def calculate_full_back_support(squad_rawdata):
    # calculates Full_back_Support score
    squad_rawdata['fbs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['fbs_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['fbs_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] )
    squad_rawdata['fbs'] =( ( ( squad_rawdata['fbs_key'] * 5) + (squad_rawdata['fbs_green'] * 3) + (squad_rawdata['fbs_blue'] * 1) ) / 43)
    squad_rawdata.fbs= squad_rawdata.fbs.round(1)
    return(squad_rawdata)
