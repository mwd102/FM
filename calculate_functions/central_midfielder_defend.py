def calculate_central_midfielder_defend(squad_rawdata):
    # calculates Central_midfielder_Defend score
    squad_rawdata['cmd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['cmd_green'] = ( squad_rawdata['Tck'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['cmd_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Cmp'] )
    squad_rawdata['cmd'] =( ( ( squad_rawdata['cmd_key'] * 5) + (squad_rawdata['cmd_green'] * 3) + (squad_rawdata['cmd_blue'] * 1) ) / 42)
    squad_rawdata.cmd= squad_rawdata.cmd.round(1)
    return(squad_rawdata)
