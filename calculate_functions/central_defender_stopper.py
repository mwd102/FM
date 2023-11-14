def calculate_central_defender_stopper(squad_rawdata):
    # calculates Central_defender_Stopper score
    squad_rawdata['cds_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['cds_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Bra'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['cds_blue'] = ( squad_rawdata['Mar'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] )
    squad_rawdata['cds'] =( ( ( squad_rawdata['cds_key'] * 5) + (squad_rawdata['cds_green'] * 3) + (squad_rawdata['cds_blue'] * 1) ) / 44)
    squad_rawdata.cds= squad_rawdata.cds.round(1)
    return(squad_rawdata)
