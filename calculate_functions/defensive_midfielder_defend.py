def calculate_defensive_midfielder_defend(squad_rawdata):
    # calculates Defensive_midfielder_Defend score
    squad_rawdata['dmd_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['dmd_green'] = ( squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['dmd_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Agg'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] )
    squad_rawdata['dmd'] =( ( ( squad_rawdata['dmd_key'] * 5) + (squad_rawdata['dmd_green'] * 3) + (squad_rawdata['dmd_blue'] * 1) ) / 40)
    squad_rawdata.dmd= squad_rawdata.dmd.round(1)
    return(squad_rawdata)
