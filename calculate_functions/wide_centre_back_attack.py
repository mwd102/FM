def calculate_wide_centre_back_attack(squad_rawdata):
    # calculates Wide_centre_back_Attack score
    squad_rawdata['wcba_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Jum'] + squad_rawdata['Cmp'] )
    squad_rawdata['wcba_green'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Hea'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['OtB'] + squad_rawdata['Sta'] + squad_rawdata['Str'] )
    squad_rawdata['wcba_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Agg'] + squad_rawdata['Ant'] + squad_rawdata['Bra'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Pos'] + squad_rawdata['Wor'] + squad_rawdata['Agi'] )
    squad_rawdata['wcba'] =( ( ( squad_rawdata['wcba_key'] * 5) + (squad_rawdata['wcba_green'] * 3) + (squad_rawdata['wcba_blue'] * 1) ) / 55)
    squad_rawdata.wcba= squad_rawdata.wcba.round(1)
    return(squad_rawdata)
