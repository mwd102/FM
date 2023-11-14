def calculate_segundo_volante_attack(squad_rawdata):
    # calculates Segundo_volante_Attack score
    squad_rawdata['sva_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['sva_green'] = ( squad_rawdata['Fin'] + squad_rawdata['Lon'] + squad_rawdata['Pas'] + squad_rawdata['Tck'] + squad_rawdata['Ant'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] )
    squad_rawdata['sva_blue'] = ( squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Cmp'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] + squad_rawdata['Bal'] )
    squad_rawdata['sva'] =( ( ( squad_rawdata['sva_key'] * 5) + (squad_rawdata['sva_green'] * 3) + (squad_rawdata['sva_blue'] * 1) ) / 47)
    squad_rawdata.sva= squad_rawdata.sva.round(1)
    return(squad_rawdata)
