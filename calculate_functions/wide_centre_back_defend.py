def calculate_wide_centre_back_defend(squad_rawdata):
    # calculates Wide_centre_back_Defend score
    squad_rawdata['wcbd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['wcbd_green'] = ( squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Pos'] + squad_rawdata['Str'] )
    squad_rawdata['wcbd_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Wor'] + squad_rawdata['Agi'] )
    squad_rawdata['wcbd'] =( ( ( squad_rawdata['wcbd_key'] * 5) + (squad_rawdata['wcbd_green'] * 3) + (squad_rawdata['wcbd_blue'] * 1) ) / 46)
    squad_rawdata.wcbd= squad_rawdata.wcbd.round(1)
    return(squad_rawdata)
