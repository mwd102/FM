def calculate_deep_lying_forward_support(squad_rawdata):
    # calculates Deep_lying_forward_Support score
    squad_rawdata['dlfs_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['dlfs_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] )
    squad_rawdata['dlfs_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['Vis'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['dlfs'] =( ( ( squad_rawdata['dlfs_key'] * 5) + (squad_rawdata['dlfs_green'] * 3) + (squad_rawdata['dlfs_blue'] * 1) ) / 41)
    squad_rawdata.dlfs= squad_rawdata.dlfs.round(1)
    return(squad_rawdata)
