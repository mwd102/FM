def calculate_inverted_wing_back_defend(squad_rawdata):
    # calculates Inverted_wing_back_Defend score
    squad_rawdata['iwbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['iwbd_green'] = ( squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['iwbd_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] )
    squad_rawdata['iwbd'] =( ( ( squad_rawdata['iwbd_key'] * 5) + (squad_rawdata['iwbd_green'] * 3) + (squad_rawdata['iwbd_blue'] * 1) ) / 45)
    squad_rawdata.iwbd= squad_rawdata.iwbd.round(1)
    return(squad_rawdata)
