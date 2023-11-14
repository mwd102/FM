def calculate_complete_forward_support(squad_rawdata):
    # calculates Complete_forward_Support score
    squad_rawdata['cfs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['cfs_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Hea'] + squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] + squad_rawdata['Agi'] + squad_rawdata['Str'] )
    squad_rawdata['cfs_blue'] = ( squad_rawdata['Tea'] + squad_rawdata['Wor'] + squad_rawdata['Bal'] + squad_rawdata['Jum'] + squad_rawdata['Sta'] )
    squad_rawdata['cfs'] =( ( ( squad_rawdata['cfs_key'] * 5) + (squad_rawdata['cfs_green'] * 3) + (squad_rawdata['cfs_blue'] * 1) ) / 59)
    squad_rawdata.cfs= squad_rawdata.cfs.round(1)
    return(squad_rawdata)
