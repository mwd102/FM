def calculate_pressing_forward_support(squad_rawdata):
    # calculates Pressing_forward_Support score
    squad_rawdata['pfs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['pfs_green'] = ( squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Wor'] + squad_rawdata['Sta'] )
    squad_rawdata['pfs_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['pfs'] =( ( ( squad_rawdata['pfs_key'] * 5) + (squad_rawdata['pfs_green'] * 3) + (squad_rawdata['pfs_blue'] * 1) ) / 44)
    squad_rawdata.pfs= squad_rawdata.pfs.round(1)
    return(squad_rawdata)
