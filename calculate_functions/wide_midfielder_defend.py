def calculate_wide_midfielder_defend(squad_rawdata):
    # calculates Wide_midfielder_Defend score
    squad_rawdata['wmd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wmd_green'] = ( squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['wmd_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] )
    squad_rawdata['wmd'] =( ( ( squad_rawdata['wmd_key'] * 5) + (squad_rawdata['wmd_green'] * 3) + (squad_rawdata['wmd_blue'] * 1) ) / 44)
    squad_rawdata.wmd= squad_rawdata.wmd.round(1)
    return(squad_rawdata)
