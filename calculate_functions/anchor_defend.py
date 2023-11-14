def calculate_anchor_defend(squad_rawdata):
    # calculates Anchor_Defend score
    squad_rawdata['ad_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['ad_green'] = ( squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] )
    squad_rawdata['ad_blue'] = ( squad_rawdata['Cmp'] + squad_rawdata['Tea'] + squad_rawdata['Str'] )
    squad_rawdata['ad'] =( ( ( squad_rawdata['ad_key'] * 5) + (squad_rawdata['ad_green'] * 3) + (squad_rawdata['ad_blue'] * 1) ) / 41)
    squad_rawdata.ad= squad_rawdata.ad.round(1)
    return(squad_rawdata)
