def calculate_central_midfielder_support(squad_rawdata):
    # calculates Central_midfielder_Support score
    squad_rawdata['cms_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['cms_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['cms_blue'] = ( squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] )
    squad_rawdata['cms'] =( ( ( squad_rawdata['cms_key'] * 5) + (squad_rawdata['cms_green'] * 3) + (squad_rawdata['cms_blue'] * 1) ) / 41)
    squad_rawdata.cms= squad_rawdata.cms.round(1)
    return(squad_rawdata)
