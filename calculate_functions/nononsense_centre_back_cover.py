def calculate_nononsense_centre_back_cover(squad_rawdata):
    # calculates No-nonsense_centre_back_Cover score
    squad_rawdata['ncbc_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['ncbc_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] )
    squad_rawdata['ncbc_blue'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['Str'] )
    squad_rawdata['ncbc'] =( ( ( squad_rawdata['ncbc_key'] * 5) + (squad_rawdata['ncbc_green'] * 3) + (squad_rawdata['ncbc_blue'] * 1) ) / 38)
    squad_rawdata.ncbc= squad_rawdata.ncbc.round(1)
    return(squad_rawdata)
