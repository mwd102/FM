def calculate_nononsense_centre_back_stopper(squad_rawdata):
    # calculates No-nonsense_centre_back_Stopper score
    squad_rawdata['ncbs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['ncbs_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Bra'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['ncbs_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] )
    squad_rawdata['ncbs'] =( ( ( squad_rawdata['ncbs_key'] * 5) + (squad_rawdata['ncbs_green'] * 3) + (squad_rawdata['ncbs_blue'] * 1) ) / 41)
    squad_rawdata.ncbs= squad_rawdata.ncbs.round(1)
    return(squad_rawdata)
