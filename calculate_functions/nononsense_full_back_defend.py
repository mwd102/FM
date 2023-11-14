def calculate_nononsense_full_back_defend(squad_rawdata):
    # calculates No-nonsense_full_back_Defend score
    squad_rawdata['nfbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['nfbd_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['nfbd_blue'] = ( squad_rawdata['Hea'] + squad_rawdata['Agg'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Tea'] )
    squad_rawdata['nfbd'] =( ( ( squad_rawdata['nfbd_key'] * 5) + (squad_rawdata['nfbd_green'] * 3) + (squad_rawdata['nfbd_blue'] * 1) ) / 40)
    squad_rawdata.nfbd= squad_rawdata.nfbd.round(1)
    return(squad_rawdata)
