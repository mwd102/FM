def calculate_defensive_midfielder_support(squad_rawdata):
    # calculates Defensive_midfielder_Support score
    squad_rawdata['dms_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['dms_green'] = ( squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['dms_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Agg'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Str'] )
    squad_rawdata['dms'] =( ( ( squad_rawdata['dms_key'] * 5) + (squad_rawdata['dms_green'] * 3) + (squad_rawdata['dms_blue'] * 1) ) / 42)
    squad_rawdata.dms= squad_rawdata.dms.round(1)
    return(squad_rawdata)
