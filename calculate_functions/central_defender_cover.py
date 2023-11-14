def calculate_central_defender_cover(squad_rawdata):
    # calculates Central_defender_Cover score
    squad_rawdata['cdc_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['cdc_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] )
    squad_rawdata['cdc_blue'] = ( squad_rawdata['Hea'] + squad_rawdata['Bra'] + squad_rawdata['Str'] )
    squad_rawdata['cdc'] =( ( ( squad_rawdata['cdc_key'] * 5) + (squad_rawdata['cdc_green'] * 3) + (squad_rawdata['cdc_blue'] * 1) ) / 41)
    squad_rawdata.cdc= squad_rawdata.cdc.round(1)
    return(squad_rawdata)
