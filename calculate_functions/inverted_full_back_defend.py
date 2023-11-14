def calculate_inverted_full_back_defend(squad_rawdata):
    # calculates Inverted_full_back_Defend score
    squad_rawdata['ifbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['ifbd_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['ifbd_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Agi'] + squad_rawdata['Jum'] )
    squad_rawdata['ifbd'] =( ( ( squad_rawdata['ifbd_key'] * 5) + (squad_rawdata['ifbd_green'] * 3) + (squad_rawdata['ifbd_blue'] * 1) ) / 47)
    squad_rawdata.ifbd= squad_rawdata.ifbd.round(1)
    return(squad_rawdata)
