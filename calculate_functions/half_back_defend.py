def calculate_half_back_defend(squad_rawdata):
    # calculates Half_back_Defend score
    squad_rawdata['hbd_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['hbd_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['hbd_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Agg'] + squad_rawdata['Bra'] + squad_rawdata['Jum'] + squad_rawdata['Str'] )
    squad_rawdata['hbd'] =( ( ( squad_rawdata['hbd_key'] * 5) + (squad_rawdata['hbd_green'] * 3) + (squad_rawdata['hbd_blue'] * 1) ) / 50)
    squad_rawdata.hbd= squad_rawdata.hbd.round(1)
    return(squad_rawdata)
