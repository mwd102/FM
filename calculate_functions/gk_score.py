def calculate_gk_score(squad_rawdata):
    # calculates gk score
    squad_rawdata['gk_essential'] = (
        (squad_rawdata['Agi'] +
         squad_rawdata['Ref']) * 5)
    squad_rawdata['gk_core'] = (
        (squad_rawdata['1v1'] +
         squad_rawdata['Ant'] +
         squad_rawdata['Cmd'] +
         squad_rawdata['Cnt'] +
         squad_rawdata['Kic'] +
         squad_rawdata['Pos']) * 3)
    squad_rawdata['gk_secondary'] = (
        ( squad_rawdata['Acc'] +
         squad_rawdata['Aer'] +
         squad_rawdata['Cmp'] +
         squad_rawdata['Dec'] +
         squad_rawdata['Fir'] +
         squad_rawdata['Han'] +
         squad_rawdata['Pas'] +
         squad_rawdata['Thr'] +
         squad_rawdata['Vis']) * 1)
    squad_rawdata['gk'] = ( ((squad_rawdata['gk_essential']) + (squad_rawdata['gk_core']) + (squad_rawdata['gk_secondary'])) / 37 )
    squad_rawdata.gk = squad_rawdata.gk.round(1)
        # # for others: squad_rawdata['gk_core'] = ( squad_rawdata[''] +squad_rawdata[''] +squad_rawdata['']+squad_rawdata['']+squad_rawdata['']+squad_rawdata['']+squad_rawdata['']) / 2
    return squad_rawdata
