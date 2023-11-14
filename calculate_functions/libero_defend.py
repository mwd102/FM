def calculate_libero_defend(squad_rawdata):
    # calculates Libero_Defend score
    squad_rawdata['ld_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['ld_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] + squad_rawdata['Str'] )
    squad_rawdata['ld_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Sta'] )
    squad_rawdata['ld'] =( ( ( squad_rawdata['ld_key'] * 5) + (squad_rawdata['ld_green'] * 3) + (squad_rawdata['ld_blue'] * 1) ) / 54)
    squad_rawdata.ld= squad_rawdata.ld.round(1)
    return(squad_rawdata)
