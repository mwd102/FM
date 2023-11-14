def calculate_pressing_forward_defend(squad_rawdata):
    # calculates Pressing_forward_Defend score
    squad_rawdata['pfd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Fin'] )
    squad_rawdata['pfd_green'] = ( squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Dec'] + squad_rawdata['Tea'] + squad_rawdata['Wor'] + squad_rawdata['Sta'] )
    squad_rawdata['pfd_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Agi'] + squad_rawdata['Bal'] + squad_rawdata['Str'] )
    squad_rawdata['pfd'] =( ( ( squad_rawdata['pfd_key'] * 5) + (squad_rawdata['pfd_green'] * 3) + (squad_rawdata['pfd_blue'] * 1) ) / 42)
    squad_rawdata.pfd= squad_rawdata.pfd.round(1)
    return(squad_rawdata)
