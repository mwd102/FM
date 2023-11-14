def calculate_target_forward_support(squad_rawdata):
    # calculates Target_forward_Support score
    squad_rawdata['tfs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['tfs_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['Tea'] + squad_rawdata['Bal'] + squad_rawdata['Jum'] + squad_rawdata['Str'] )
    squad_rawdata['tfs_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] )
    squad_rawdata['tfs'] =( ( ( squad_rawdata['tfs_key'] * 5) + (squad_rawdata['tfs_green'] * 3) + (squad_rawdata['tfs_blue'] * 1) ) / 39)
    squad_rawdata.tfs= squad_rawdata.tfs.round(1)
    return(squad_rawdata)
