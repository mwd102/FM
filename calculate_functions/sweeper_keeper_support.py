def calculate_sweeper_keeper_support(squad_rawdata):
    # calculates Sweeper_keeper_Support score
    squad_rawdata['sks_key'] = ( squad_rawdata['Agi'] + squad_rawdata['Ref'] )
    squad_rawdata['sks_green'] = ( squad_rawdata['Cmd'] + squad_rawdata['Kic'] + squad_rawdata['1v1'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] )
    squad_rawdata['sks_blue'] = ( squad_rawdata['Aer'] + squad_rawdata['Fir'] + squad_rawdata['Han'] + squad_rawdata['Pas'] + squad_rawdata['TRO'] + squad_rawdata['Dec'] + squad_rawdata['Vis'] + squad_rawdata['Acc'] )
    squad_rawdata['sks'] =( ( ( squad_rawdata['sks_key'] * 5) + (squad_rawdata['sks_green'] * 3) + (squad_rawdata['sks_blue'] * 1) ) / 36)
    squad_rawdata.sks= squad_rawdata.sks.round(1)
    return(squad_rawdata)
