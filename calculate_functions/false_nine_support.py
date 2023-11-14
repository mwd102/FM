def calculate_false_nine_support(squad_rawdata):
    # calculates False_nine_Support score
    squad_rawdata['f9s_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['f9s_green'] = ( squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['OtB'] + squad_rawdata['Vis'] + squad_rawdata['Agi'] )
    squad_rawdata['f9s_blue'] = ( squad_rawdata['Ant'] + squad_rawdata['Fla'] + squad_rawdata['Tea'] + squad_rawdata['Bal'] )
    squad_rawdata['f9s'] =( ( ( squad_rawdata['f9s_key'] * 5) + (squad_rawdata['f9s_green'] * 3) + (squad_rawdata['f9s_blue'] * 1) ) / 46)
    squad_rawdata.f9s= squad_rawdata.f9s.round(1)
    return(squad_rawdata)
