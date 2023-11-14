def calculate_wing_back_defend(squad_rawdata):
    # calculates Wing_back_Defend score
    squad_rawdata['wbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wbd_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['wbd_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] )
    squad_rawdata['wbd'] =( ( ( squad_rawdata['wbd_key'] * 5) + (squad_rawdata['wbd_green'] * 3) + (squad_rawdata['wbd_blue'] * 1) ) / 45)
    squad_rawdata.wbd= squad_rawdata.wbd.round(1)
    return(squad_rawdata)
