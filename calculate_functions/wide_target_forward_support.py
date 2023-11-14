def calculate_wide_target_forward_support(squad_rawdata):
    # calculates Wide_target_forward_Support score
    squad_rawdata['wtfs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wtfs_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['Tea'] + squad_rawdata['Jum'] + squad_rawdata['Str'] )
    squad_rawdata['wtfs_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Fir'] + squad_rawdata['Ant'] + squad_rawdata['OtB'] + squad_rawdata['Bal'] )
    squad_rawdata['wtfs'] =( ( ( squad_rawdata['wtfs_key'] * 5) + (squad_rawdata['wtfs_green'] * 3) + (squad_rawdata['wtfs_blue'] * 1) ) / 40)
    squad_rawdata.wtfs= squad_rawdata.wtfs.round(1)
    return(squad_rawdata)
