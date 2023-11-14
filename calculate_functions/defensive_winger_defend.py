def calculate_defensive_winger_defend(squad_rawdata):
    # calculates Defensive_winger_Defend score
    squad_rawdata['dwd_key'] = ( squad_rawdata['Acc'] + squad_rawdata['Pac'] + squad_rawdata['Sta'] + squad_rawdata['Wor'] )
    squad_rawdata['dwd_green'] = ( squad_rawdata['Tec'] + squad_rawdata['Ant'] + squad_rawdata['OtB'] + squad_rawdata['Pos'] + squad_rawdata['Tea'] )
    squad_rawdata['dwd_blue'] = ( squad_rawdata['Cro'] + squad_rawdata['Dri'] + squad_rawdata['Fir'] + squad_rawdata['Mar'] + squad_rawdata['Tck'] + squad_rawdata['Agg'] + squad_rawdata['Cnt'] + squad_rawdata['Dec'] )
    squad_rawdata['dwd'] =( ( ( squad_rawdata['dwd_key'] * 5) + (squad_rawdata['dwd_green'] * 3) + (squad_rawdata['dwd_blue'] * 1) ) / 43)
    squad_rawdata.dwd= squad_rawdata.dwd.round(1)
    return(squad_rawdata)
