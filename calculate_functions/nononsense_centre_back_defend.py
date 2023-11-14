def calculate_nononsense_centre_back_defend(squad_rawdata):
    # calculates No-nonsense_centre_back_Defend score
    squad_rawdata['ncbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['ncbd_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['ncbd_blue'] = ( squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] )
    squad_rawdata['ncbd'] =( ( ( squad_rawdata['ncbd_key'] * 5) + (squad_rawdata['ncbd_green'] * 3) + (squad_rawdata['ncbd_blue'] * 1) ) / 39)
    squad_rawdata.ncbd= squad_rawdata.ncbd.round(1)
    return(squad_rawdata)
