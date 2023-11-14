def calculate_regista_support(squad_rawdata):
    # calculates Regista_Support score
    squad_rawdata['regs_key'] = ( squad_rawdata['Wor'] + squad_rawdata['Sta'] + squad_rawdata['Acc'] + squad_rawdata['Pac'] )
    squad_rawdata['regs_green'] = ( squad_rawdata['Fir'] + squad_rawdata['Pas'] + squad_rawdata['Tec'] + squad_rawdata['Cmp'] + squad_rawdata['Dec'] + squad_rawdata['Fla'] + squad_rawdata['OtB'] + squad_rawdata['Tea'] + squad_rawdata['Vis'] )
    squad_rawdata['regs_blue'] = ( squad_rawdata['Dri'] + squad_rawdata['Lon'] + squad_rawdata['Ant'] + squad_rawdata['Bal'] )
    squad_rawdata['regs'] =( ( ( squad_rawdata['regs_key'] * 5) + (squad_rawdata['regs_green'] * 3) + (squad_rawdata['regs_blue'] * 1) ) / 51)
    squad_rawdata.regs= squad_rawdata.regs.round(1)
    return(squad_rawdata)
