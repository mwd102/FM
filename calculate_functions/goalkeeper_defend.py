def calculate_goalkeeper_defend(squad_rawdata):
    # calculates Goalkeeper_Defend score
    squad_rawdata['gkd_key'] = ( squad_rawdata['Agi'] + squad_rawdata['Ref'] )
    squad_rawdata['gkd_green'] = ( squad_rawdata['Aer'] + squad_rawdata['Cmd'] + squad_rawdata['Han'] + squad_rawdata['Kic'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] )
    squad_rawdata['gkd_blue'] = ( squad_rawdata['1v1'] + squad_rawdata['Thr'] + squad_rawdata['Ant'] + squad_rawdata['Dec'] )
    squad_rawdata['gkd'] =( ( ( squad_rawdata['gkd_key'] * 5) + (squad_rawdata['gkd_green'] * 3) + (squad_rawdata['gkd_blue'] * 1) ) / 32)
    squad_rawdata.gkd= squad_rawdata.gkd.round(1)
    return(squad_rawdata)
