def calculate_full_back_defend(squad_rawdata):
    # calculates Full_back_Defend score
    squad_rawdata['fbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['fbd_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] + squad_rawdata['Pos'] )
    squad_rawdata['fbd_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Pas'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['fbd'] =( ( ( squad_rawdata['fbd_key'] * 5) + (squad_rawdata['fbd_green'] * 3) + (squad_rawdata['fbd_blue'] * 1) ) / 42)
    squad_rawdata.fbd= squad_rawdata.fbd.round(1)
    return(squad_rawdata)
