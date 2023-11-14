def calculate_sweeper_keeper_attack(squad_rawdata):
    # calculates Sweeper_keeper_Attack score
    squad_rawdata['ska_key'] = ( squad_rawdata['Agi'] + squad_rawdata['Ref'] )
    squad_rawdata['ska_green'] = ( squad_rawdata['Cmd'] + squad_rawdata['Kic'] + squad_rawdata['1v1'] + squad_rawdata['Ant'] + squad_rawdata['Cnt'] + squad_rawdata['Pos'] )
    squad_rawdata['ska_blue'] = ( squad_rawdata['Aer'] + squad_rawdata['Fir'] + squad_rawdata['Han'] + squad_rawdata['Pas'] + squad_rawdata['TRO'] + squad_rawdata['Dec'] + squad_rawdata['Vis'] + squad_rawdata['Acc'] )
    squad_rawdata['ska'] =( ( ( squad_rawdata['ska_key'] * 5) + (squad_rawdata['ska_green'] * 3) + (squad_rawdata['ska_blue'] * 1) ) / 36)
    squad_rawdata.ska= squad_rawdata.ska.round(1)
    return(squad_rawdata)
