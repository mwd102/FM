def calculate_central_defender_defend(squad_rawdata):
    # calculates Central_defender_Defend score
    squad_rawdata['cdd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['cdd_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['cdd_blue'] = ( squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] )
    squad_rawdata['cdd'] =( ( ( squad_rawdata['cdd_key'] * 5) + (squad_rawdata['cdd_green'] * 3) + (squad_rawdata['cdd_blue'] * 1) ) / 40)
    squad_rawdata.cdd= squad_rawdata.cdd.round(1)
    return(squad_rawdata)
