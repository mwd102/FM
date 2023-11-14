def calculate_wide_midfielder_support(squad_rawdata):
    # calculates Wide_midfielder_Support score
    squad_rawdata['wms_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['wms_green'] = ( squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] )
    squad_rawdata['wms_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Fir'] + squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] + squad_rawdata['Vis'] )
    squad_rawdata['wms'] =( ( ( squad_rawdata['wms_key'] * 5) + (squad_rawdata['wms_green'] * 3) + (squad_rawdata['wms_blue'] * 1) ) / 41)
    squad_rawdata.wms= squad_rawdata.wms.round(1)
    return(squad_rawdata)
