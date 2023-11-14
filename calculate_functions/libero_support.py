def calculate_libero_support(squad_rawdata):
    # calculates Libero_Support score
    squad_rawdata['ls_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['ls_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Tec'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] + squad_rawdata['Str'] )
    squad_rawdata['ls_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Vis'] + squad_rawdata['Sta'] )
    squad_rawdata['ls'] =( ( ( squad_rawdata['ls_key'] * 5) + (squad_rawdata['ls_green'] * 3) + (squad_rawdata['ls_blue'] * 1) ) / 56)
    squad_rawdata.ls= squad_rawdata.ls.round(1)
    return(squad_rawdata)
