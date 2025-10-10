# Created by Giseldah

import math
import struct

# Floating point numbers bring errors into the calculation, both inside the Lotro-client and in this function collection. This is why a 100% match with the stats in Lotro is impossible.
# Anyway, to compensate for some errors, we use a calculation deviation correction value. This makes for instance 24.49999999 round to 25, as it's assumed that 24.5 was intended as outcome of a formula.

DblCalcDev = 0.00000001

def CalcStat(SName, SLvl, SParam = 1):

    SN = SName.strip().upper()
    L = SLvl
    Lm = L - DblCalcDev
    Lp = L + DblCalcDev
    N = 1
    C = ''
    match SParam:
        case str():
            C = SParam
        case float() | int():
            N = SParam

    Result = 0

    if SN < 'MINSTRELCDARMOURTOCOMPHYMIT':
	    if SN < 'CPTSHIELDPHYMAS':
		    if SN < 'BRAWLERCDVITALITYTONCMR':
			    if SN < 'BEORNINGCDARMOURTYPE':
				    if SN < 'AWARDILVLDB':
					    if SN < 'ARMOURPROGB':
						    if SN < 'AGILITYC':
							    if SN < 'ADJITEMMAS':
								    if SN < 'ADJCREEPITEM':
									    if SN < 'ACIDMIT':
										    if SN == '-VERSION':
										        Result = "2.4.14f"
									    elif SN > 'ACIDMIT':
										    if SN == 'ACIDMITT':
										        Result = CalcStat("DmgTypeMitT",L,N)
									    else:
									        Result = CalcStat("DmgTypeMit",L,N)
								    elif SN > 'ADJCREEPITEM':
									    if SN < 'ADJCREEPITEMPOWER':
										    if SN == 'ADJCREEPITEMMIT':
										        if 450 <= Lp and Lm <= 499:
										            Result = 0.9235
										        elif 500 <= Lp and Lm <= 500:
										            Result = 0.9215
										        elif 549 <= Lp and Lm <= 549:
										            Result = 0.9913
										        else:
										            Result = 1
									    elif SN > 'ADJCREEPITEMPOWER':
										    if SN == 'ADJITEM':
										        if 499 <= Lp and Lm <= 550:
										            Result = 0.9
										        else:
										            Result = 1
									    else:
									        if 450 <= Lp and Lm <= 499:
									            Result = 0.9
									        elif 500 <= Lp and Lm <= 500:
									            Result = 0.9
									        elif 549 <= Lp and Lm <= 549:
									            Result = 0.9775
									        else:
									            Result = 1
								    else:
								        if 450 <= Lp and Lm <= 499:
								            Result = 0.92253
								        elif 500 <= Lp and Lm <= 500:
								            Result = 0.923
								        elif 549 <= Lp and Lm <= 549:
								            Result = 0.9902
								        else:
								            Result = 1
							    elif SN > 'ADJITEMMAS':
								    if SN < 'ADJTRAITMIT':
									    if SN < 'ADJTRAIT':
										    if SN == 'ADJITEMMIT':
										        if 499 <= Lp and Lm <= 499:
										            Result = 0.78
										        elif 500 <= Lp and Lm <= 550:
										            Result = 0.7
										        else:
										            Result = 1
									    elif SN > 'ADJTRAIT':
										    if SN == 'ADJTRAITMAS':
										        if 141 <= Lp and Lm <= 141:
										            Result = 0.9
										        elif 150 <= Lp and Lm <= 160:
										            Result = 0.8235
										        else:
										            Result = 1
									    else:
									        if 141 <= Lp and Lm <= 150:
									            Result = 0.9
									        else:
									            Result = 1
								    elif SN > 'ADJTRAITMIT':
									    if SN < 'ADJVIRTUEMORALE':
										    if SN == 'ADJVIRTUEMAS':
										        if Lm <= 0:
										            Result = 0
										        elif 399 <= Lp and Lm <= 399:
										            Result = 1.098
										        elif 499 <= Lp and Lm <= 499:
										            Result = 0.9
										        elif 500 <= Lp and Lm <= 550:
										            Result = 0.8235
										        else:
										            Result = 1
									    elif SN > 'ADJVIRTUEMORALE':
										    if SN == 'AGILITY':
										        Result = CalcStat("Main",L,N)
									    else:
									        if Lm <= 0:
									            Result = 0
									        elif 50 <= Lp and Lm <= 50:
									            Result = 2
									        elif 60 <= Lp and Lm <= 80:
									            Result = 1.5
									        elif 499 <= Lp and Lm <= 499:
									            Result = 0.9475
									        else:
									            Result = 1
								    else:
								        if 141 <= Lp and Lm <= 141:
								            Result = 0.78
								        elif 150 <= Lp and Lm <= 160:
								            Result = 0.7
								        else:
								            Result = 1
							    else:
							        if 499 <= Lp and Lm <= 499:
							            Result = 0.9
							        elif 500 <= Lp and Lm <= 550:
							            Result = 0.8235
							        else:
							            Result = 1
						    elif SN > 'AGILITYC':
							    if SN < 'ARMOURCI':
								    if SN < 'ARMCATMP':
									    if SN < 'AGILITYT':
										    if SN == 'AGILITYCI':
										        Result = CalcStat("MainCI",L,N)
									    elif SN > 'AGILITYT':
										    if SN == 'ALIGNMENTNAME':
										        if 1 <= Lp and Lm <= 1:
										            Result = "Good"
										        elif 2 <= Lp and Lm <= 2:
										            Result = "Neutral"
										        elif 3 <= Lp and Lm <= 3:
										            Result = "Evil"
										        else:
										            Result = ""
									    else:
									        Result = CalcStat("MainT",L,N)
								    elif SN > 'ARMCATMP':
									    if SN < 'ARMOUR':
										    if SN == 'ARMCATPROGB':
										        if 1 <= Lp and Lm <= 1:
										            Result = CalcStat("ProgBArmourHeavy",N)
										        elif 2 <= Lp and Lm <= 2:
										            Result = CalcStat("ProgBArmourMedium",N)
										        elif 3 <= Lp and Lm <= 3:
										            Result = CalcStat("ProgBArmourLight",N)
									    elif SN > 'ARMOUR':
										    if SN == 'ARMOURC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ArmourCI",CalcStat("ArmourCILvlFilter",N),N),0)
									    else:
									        Result = RoundDblDown(StatLinInter("ArmourPntMP","ItemPntS","ArmourProgB","AdjItemMit",L,C,0))
								    else:
								        Result = CalcStat("PntMPArmour",L)
							    elif SN > 'ARMOURCI':
								    if SN < 'ARMOURLOW':
									    if SN < 'ARMOURCIRAW':
										    if SN == 'ARMOURCILVLFILTER':
										        if 5.6 <= Lp and Lm <= 5.6:
										            Result = 515
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    elif SN > 'ARMOURCIRAW':
										    if SN == 'ARMOURCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ArmourCIRaw",CalcStat("ArmourCILvlFilter",N),N),99)
									    else:
									        Result = StatLinInter("PntMPArmourC","ItemPntS","ProgBArmour","AdjCreepItemMit",L,N,4)
								    elif SN > 'ARMOURLOW':
									    if SN < 'ARMOURPENT':
										    if SN == 'ARMOURLOWPNTMP':
										        Result = CalcStat("ArmTypeMP",ArmCodeIndex(C,2))*CalcStat("ArmQtyLowMP",ArmCodeIndex(C,2))*CalcStat("ArmCatMP",ArmCodeIndex(C,1))
									    elif SN > 'ARMOURPENT':
										    if SN == 'ARMOURPNTMP':
										        Result = CalcStat("ArmTypeMP",ArmCodeIndex(C,2))*CalcStat("ArmQtyMP",ArmCodeIndex(C,3),ArmCodeIndex(C,2))*CalcStat("ArmCatMP",ArmCodeIndex(C,1))
									    else:
									        Result = EquSng(StatLinInter("PntMPArmourPenT","TraitPntS","ProgBArmour","",L,N,0))
								    else:
								        Result = RoundDblDown(StatLinInter("ArmourLowPntMP","ItemPntS","ArmourProgB","AdjItemMit",L,C,0))
							    else:
							        Result = RoundDblLotro(CalcStat("ArmourCIRaw",L,N))
						    else:
						        Result = CalcStat("MainC",L,N)
					    elif SN > 'ARMOURPROGB':
						    if SN < 'AWARDILVLB':
							    if SN < 'ARMQTYUNCOMMP':
								    if SN < 'ARMQTYINCOMPMP':
									    if SN < 'ARMQTYCOMMMP':
										    if SN == 'ARMOURT':
										        Result = EquSng(StatLinInter("PntMPArmourT","TraitPntS","ProgBArmour","AdjTraitMit",L,N,0))
									    elif SN > 'ARMQTYCOMMMP':
										    if SN == 'ARMQTYEPICMP':
										        if 1 <= Lp and Lm <= 8:
										            Result = DataTableValue((1,1,1,1,1,1.002,1,1),L)
									    else:
									        if 1 <= Lp and Lm <= 8:
									            Result = DataTableValue((22/30,22/30,0.8,0.8,0.76,0.804,0.8,0.7),L)
								    elif SN > 'ARMQTYINCOMPMP':
									    if SN < 'ARMQTYMP':
										    if SN == 'ARMQTYLOWMP':
										        if 1 <= Lp and Lm <= 8:
										            Result = DataTableValue((12/33,12/33,12/33,12/33,12/33,0.996*12/33,12/33,12/33),L)
									    elif SN > 'ARMQTYMP':
										    if SN == 'ARMQTYRAREMP':
										        if 1 <= Lp and Lm <= 8:
										            Result = DataTableValue((26/30,26/30,0.9,0.9,0.88,0.9,0.9,0.8),L)
									    else:
									        if 1 <= Lp and Lm <= 1:
									            Result = CalcStat("ArmQtyCommMP",N)
									        elif 2 <= Lp and Lm <= 2:
									            Result = CalcStat("ArmQtyUncomMP",N)
									        elif 3 <= Lp and Lm <= 3:
									            Result = CalcStat("ArmQtyRareMP",N)
									        elif 4 <= Lp and Lm <= 4:
									            Result = CalcStat("ArmQtyIncompMP",N)
									        elif 5 <= Lp and Lm <= 5:
									            Result = CalcStat("ArmQtyEpicMP",N)
								    else:
								        if 1 <= Lp and Lm <= 8:
								            Result = DataTableValue((28/30,28/30,0.95,0.95,0.94,0.948,0.95,0.95),L)
							    elif SN > 'ARMQTYUNCOMMP':
								    if SN < 'AWARDILVLAA':
									    if SN < 'AUTOLVLTOILVL':
										    if SN == 'ARMTYPEMP':
										        if 1 <= Lp and Lm <= 8:
										            Result = DataTableValue((9,9,20,30,15,25,12,32.726),L)
									    elif SN > 'AUTOLVLTOILVL':
										    if SN == 'AWARDILVLA':
										        if Lm <= 75:
										            Result = L
										        elif Lm <= 94:
										            Result = 5*L-304
										        elif Lm <= 95:
										            Result = 173
										        elif Lm <= 100:
										            Result = 5*L-304
										        elif Lm <= 101:
										            Result = 197
										        elif Lm <= 104:
										            Result = 4*L-206
										        elif Lm <= 105:
										            Result = 218
										        elif Lm <= 110:
										            Result = RoundDbl(LinFmod(1,295,303.8,106,110,L))
										        elif Lm <= 115:
										            Result = 304
										        elif Lm <= 119:
										            Result = RoundDbl(LinFmod(1,345,357,116,119,L))
										        elif Lm <= 120:
										            Result = 359
										        elif Lm <= 130:
										            Result = 395
										        elif Lm <= 140:
										            Result = RoundDbl(LinFmod(1,445.4,455.4,131,140,L))
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,479.4,491.4,141,150,L))
										        else:
										            Result = CalcStat("AwardILvlA",150)
									    else:
									        Result = CalcStat("AwardILvlCC",L)
								    elif SN > 'AWARDILVLAA':
									    if SN < 'AWARDILVLAC':
										    if SN == 'AWARDILVLAB':
										        if 75 <= Lp and Lm <= 75:
										            Result = CalcStat("AwardILvlA",L)+1
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    elif SN > 'AWARDILVLAC':
										    if SN == 'AWARDILVLAOLD':
										        Result = CalcStat("AwardILvlA",L)
									    else:
									        if 75 <= Lp and Lm <= 75:
									            Result = CalcStat("AwardILvlA",L)+2
									        else:
									            Result = CalcStat("AwardILvlA",L)
								    else:
								        if 75 <= Lp and Lm <= 75:
								            Result = CalcStat("AwardILvlA",L)+3
								        else:
								            Result = CalcStat("AwardILvlA",L)
							    else:
							        if 1 <= Lp and Lm <= 8:
							            Result = DataTableValue((22/30,22/30,0.85,0.85,0.82,0.852,0.85,0.75),L)
						    elif SN > 'AWARDILVLB':
							    if SN < 'AWARDILVLCE':
								    if SN < 'AWARDILVLCA':
									    if SN < 'AWARDILVLBOLD':
										    if SN == 'AWARDILVLBA':
										        Result = CalcStat("AwardILvlB",L)
									    elif SN > 'AWARDILVLBOLD':
										    if SN == 'AWARDILVLC':
										        if Lm <= 75:
										            Result = CalcStat("AwardILvlB",L)
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    else:
									        Result = CalcStat("AwardILvlB",L)
								    elif SN > 'AWARDILVLCA':
									    if SN < 'AWARDILVLCC':
										    if SN == 'AWARDILVLCB':
										        if Lm <= 10:
										            Result = CalcStat("AwardILvlA",1)
										        elif Lm <= 85:
										            Result = CalcStat("AwardILvlA",L)-10
										        elif 96 <= Lp and Lm <= 99:
										            Result = CalcStat("AwardILvlA",L)+4
										        elif 100 <= Lp and Lm <= 100:
										            Result = CalcStat("AwardILvlA",L)+6
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    elif SN > 'AWARDILVLCC':
										    if SN == 'AWARDILVLCD':
										        if Lm <= 8:
										            Result = CalcStat("AwardILvlA",1)
										        elif Lm <= 85:
										            Result = CalcStat("AwardILvlA",L)-8
										        elif Lm <= 100:
										            Result = CalcStat("AwardILvlA",L)-4
										        elif Lm <= 105:
										            Result = CalcStat("AwardILvlA",L)+4
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    else:
									        Result = CalcStat("AwardILvlC",L)
								    else:
								        if Lm <= 8:
								            Result = CalcStat("AwardILvlA",1)
								        elif Lm <= 85:
								            Result = CalcStat("AwardILvlA",L)-8
								        elif 96 <= Lp and Lm <= 100:
								            Result = CalcStat("AwardILvlA",L)+4
								        else:
								            Result = CalcStat("AwardILvlA",L)
							    elif SN > 'AWARDILVLCE':
								    if SN < 'AWARDILVLCI':
									    if SN < 'AWARDILVLCG':
										    if SN == 'AWARDILVLCF':
										        if Lm <= 140:
										            Result = CalcStat("AwardILvlC",L)
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,500.4,517.4,141,150,L))
										        else:
										            Result = CalcStat("AwardILvlCF",150)
									    elif SN > 'AWARDILVLCG':
										    if SN == 'AWARDILVLCH':
										        if Lm <= 140:
										            Result = CalcStat("AwardILvlC",L)
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,500.4,525.4,141,150,L))
										        else:
										            Result = CalcStat("AwardILvlCH",150)
									    else:
									        if Lm <= 140:
									            Result = CalcStat("AwardILvlC",L)
									        elif Lm <= 150:
									            Result = RoundDbl(LinFmod(1,500.4,520.4,141,150,L))
									        else:
									            Result = CalcStat("AwardILvlCG",150)
								    elif SN > 'AWARDILVLCI':
									    if SN < 'AWARDILVLD':
										    if SN == 'AWARDILVLCJ':
										        if Lm <= 140:
										            Result = CalcStat("AwardILvlC",L)
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,500.4,535.4,141,150,L))
										        else:
										            Result = CalcStat("AwardILvlCJ",150)
									    elif SN > 'AWARDILVLD':
										    if SN == 'AWARDILVLDA':
										        if 106 <= Lp and Lm <= 115:
										            Result = RoundDbl(LinFmod(1,300,336.5,106,115,L))
										        else:
										            Result = CalcStat("AwardILvlD",L)
									    else:
									        if Lm <= 105:
									            Result = CalcStat("AwardILvlC",L)
									        elif Lm <= 115:
									            Result = 300
									        else:
									            Result = CalcStat("AwardILvlA",L)
								    else:
								        if Lm <= 140:
								            Result = CalcStat("AwardILvlC",L)
								        elif Lm <= 150:
								            Result = RoundDbl(LinFmod(1,500.4,530.4,141,150,L))
								        else:
								            Result = CalcStat("AwardILvlCI",150)
							    else:
							        if Lm <= 140:
							            Result = CalcStat("AwardILvlC",L)
							        elif Lm <= 150:
							            Result = RoundDbl(LinFmod(1,500.4,512.4,141,150,L))
							        else:
							            Result = CalcStat("AwardILvlCE",150)
						    else:
						        if Lm <= 4:
						            Result = CalcStat("AwardILvlA",1)
						        elif Lm <= 50:
						            Result = CalcStat("AwardILvlA",L-4)
						        elif Lm <= 54:
						            Result = CalcStat("AwardILvlA",51)
						        elif Lm <= 75:
						            Result = CalcStat("AwardILvlA",L-4)
						        elif Lm <= 95:
						            Result = CalcStat("AwardILvlA",L)+4
						        else:
						            Result = CalcStat("AwardILvlA",L)
					    else:
					        Result = CalcStat("ArmCatProgB",ArmCodeIndex(C,1),L)
				    elif SN > 'AWARDILVLDB':
					    if SN < 'AWARDLVLCAP':
						    if SN < 'AWARDILVLGA':
							    if SN < 'AWARDILVLEB':
								    if SN < 'AWARDILVLDF':
									    if SN < 'AWARDILVLDD':
										    if SN == 'AWARDILVLDC':
										        if 106 <= Lp and Lm <= 110:
										            Result = RoundDbl(LinFmod(1,300,320,106,115,L))
										        elif 111 <= Lp and Lm <= 115:
										            Result = CalcStat("AwardILvlDC",110)
										        else:
										            Result = CalcStat("AwardILvlD",L)
									    elif SN > 'AWARDILVLDD':
										    if SN == 'AWARDILVLDE':
										        if 106 <= Lp and Lm <= 115:
										            Result = RoundDbl(LinFmod(1,300.4,326.4,106,115,L))
										        else:
										            Result = CalcStat("AwardILvlD",L)
									    else:
									        if 106 <= Lp and Lm <= 114:
									            Result = RoundDbl(LinFmod(1,300,327,106,115,L))
									        elif 115 <= Lp and Lm <= 115:
									            Result = CalcStat("AwardILvlD",115)+30
									        else:
									            Result = CalcStat("AwardILvlD",L)
								    elif SN > 'AWARDILVLDF':
									    if SN < 'AWARDILVLE':
										    if SN == 'AWARDILVLDG':
										        if 106 <= Lp and Lm <= 114:
										            Result = RoundDbl(LinFmod(1,300,336,106,115,L))
										        elif 115 <= Lp and Lm <= 115:
										            Result = CalcStat("AwardILvlD",115)+40
										        else:
										            Result = CalcStat("AwardILvlD",L)
									    elif SN > 'AWARDILVLE':
										    if SN == 'AWARDILVLEA':
										        if 116 <= Lp and Lm <= 119:
										            Result = RoundDbl(LinFmod(1,350,378,116,120,L))
										        elif 120 <= Lp and Lm <= 120:
										            Result = CalcStat("AwardILvlE",120)+26
										        else:
										            Result = CalcStat("AwardILvlE",L)
									    else:
									        if Lm <= 115:
									            Result = CalcStat("AwardILvlC",L)
									        elif Lm <= 120:
									            Result = 350
									        else:
									            Result = CalcStat("AwardILvlA",L)
								    else:
								        if 106 <= Lp and Lm <= 110:
								            Result = CalcStat("AwardILvlDF",111)
								        elif 111 <= Lp and Lm <= 115:
								            Result = RoundDbl(LinFmod(1,299.5,320.5,106,115,L))
								        else:
								            Result = CalcStat("AwardILvlD",L)
							    elif SN > 'AWARDILVLEB':
								    if SN < 'AWARDILVLF':
									    if SN < 'AWARDILVLED':
										    if SN == 'AWARDILVLEC':
										        if 116 <= Lp and Lm <= 120:
										            Result = RoundDbl(LinFmod(1,350,382,116,120,L))
										        else:
										            Result = CalcStat("AwardILvlE",L)
									    elif SN > 'AWARDILVLED':
										    if SN == 'AWARDILVLEE':
										        if 116 <= Lp and Lm <= 119:
										            Result = RoundDbl(LinFmod(1,350,366,116,120,L))
										        elif 120 <= Lp and Lm <= 120:
										            Result = CalcStat("AwardILvlE",120)+14
										        else:
										            Result = CalcStat("AwardILvlE",L)
									    else:
									        if 116 <= Lp and Lm <= 120:
									            Result = RoundDbl(LinFmod(1,350,370,116,120,L))
									        else:
									            Result = CalcStat("AwardILvlE",L)
								    elif SN > 'AWARDILVLF':
									    if SN < 'AWARDILVLFB':
										    if SN == 'AWARDILVLFA':
										        if Lm <= 9:
										            Result = RoundDbl(LinFmod(1,0.5,4.5,1,9,L))
										        elif Lm <= 19:
										            Result = LinFmod(1,6,15,10,19,L)
										        elif Lm <= 23:
										            Result = RoundDbl(LinFmod(1,15.5,17,20,23,L))
										        elif Lm <= 49:
										            Result = LinFmod(1,18,43,24,49,L)
										        elif Lm <= 65:
										            Result = LinFmod(1,43,58,50,65,L)
										        elif Lm <= 75:
										            Result = LinFmod(1,60,69,66,75,L)
										        elif Lm <= 84:
										            Result = CalcStat("AwardILvlF",L)
										        elif Lm <= 85:
										            Result = 120
										        elif Lm <= 93:
										            Result = CalcStat("AwardILvlF",L)
										        elif Lm <= 95:
										            Result = LinFmod(1,166,172,94,95,L)
										        elif Lm <= 119:
										            Result = CalcStat("AwardILvlF",L)
										        elif Lm <= 120:
										            Result = 368
										        elif Lm <= 129:
										            Result = RoundDbl(LinFmod(1,400,423,121,129,L))
										        elif Lm <= 130:
										            Result = 424
										        elif Lm <= 135:
										            Result = LinFmod(1,450,462,131,135,L)
										        elif Lm <= 139:
										            Result = LinFmod(1,463,472,136,139,L)
										        elif Lm <= 140:
										            Result = 473
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,500.4,504.4,141,150,L))
										        else:
										            Result = CalcStat("AwardILvlFA",150)
									    elif SN > 'AWARDILVLFB':
										    if SN == 'AWARDILVLG':
										        if Lm <= 120:
										            Result = CalcStat("AwardILvlC",L)
										        elif Lm <= 130:
										            Result = 400
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    else:
									        if Lm <= 40:
									            Result = LinFmod(1,1,40,1,40,L)
									        elif Lm <= 45:
									            Result = LinFmod(1,40,44,41,45,L)
									        elif Lm <= 50:
									            Result = RoundDbl(LinFmod(1,45.4,47,46,50,L))
									        elif Lm <= 55:
									            Result = RoundDbl(LinFmod(1,51,54.4,51,55,L))
									        elif Lm <= 60:
									            Result = RoundDbl(LinFmod(1,54,57.4,56,60,L))
									        elif Lm <= 75:
									            Result = LinFmod(1,58,72,61,75,L)
									        elif Lm <= 84:
									            Result = CalcStat("AwardILvlF",L)
									        elif Lm <= 85:
									            Result = 122
									        elif Lm <= 93:
									            Result = CalcStat("AwardILvlF",L)
									        elif Lm <= 95:
									            Result = LinFmod(1,168,174,94,95,L)
									        elif Lm <= 119:
									            Result = CalcStat("AwardILvlF",L)
									        elif Lm <= 120:
									            Result = 380
									        elif Lm <= 125:
									            Result = LinFmod(1,400,416,121,125,L)
									        elif Lm <= 129:
									            Result = LinFmod(1,418,430,126,129,L)
									        elif Lm <= 130:
									            Result = 432
									        elif Lm <= 135:
									            Result = RoundDbl(LinFmod(1,450.4,463.8,131,135,L))
									        elif Lm <= 138:
									            Result = RoundDbl(LinFmod(1,465.8,472.8,136,138,L))
									        elif Lm <= 140:
									            Result = 475
									        elif Lm <= 150:
									            Result = RoundDbl(LinFmod(1,500.4,526.4,141,150,L))
									        else:
									            Result = CalcStat("AwardILvlFB",150)
								    else:
								        if Lm <= 75:
								            Result = 0
								        elif Lm <= 84:
								            Result = LinFmod(1,78,118,76,84,L)
								        elif Lm <= 85:
								            Result = 0
								        elif Lm <= 93:
								            Result = RoundDbl(LinFmod(1,129.4,163,86,93,L))
								        elif Lm <= 95:
								            Result = 0
								        elif Lm <= 100:
								            Result = RoundDbl(LinFmod(1,175,198.4,95,100,L))
								        elif Lm <= 104:
								            Result = LinFmod(1,201,213,101,104,L)
								        elif Lm <= 105:
								            Result = 220
								        elif Lm <= 114:
								            Result = RoundDbl(LinFmod(1,300,323,106,114,L))
								        elif Lm <= 115:
								            Result = 324
								        elif Lm <= 119:
								            Result = RoundDbl(LinFmod(1,349.6,368.4,116,120,L))
							    else:
							        if 116 <= Lp and Lm <= 119:
							            Result = RoundDbl(LinFmod(1,350,390,116,120,L))
							        elif 120 <= Lp and Lm <= 120:
							            Result = CalcStat("AwardILvlE",120)+38
							        else:
							            Result = CalcStat("AwardILvlE",L)
						    elif SN > 'AWARDILVLGA':
							    if SN < 'AWARDILVLIA':
								    if SN < 'AWARDILVLGE':
									    if SN < 'AWARDILVLGC':
										    if SN == 'AWARDILVLGB':
										        if 121 <= Lp and Lm <= 130:
										            Result = RoundDbl(LinFmod(1,400.4,418.4,121,130,L))
										        else:
										            Result = CalcStat("AwardILvlG",L)
									    elif SN > 'AWARDILVLGC':
										    if SN == 'AWARDILVLGD':
										        if 121 <= Lp and Lm <= 130:
										            Result = RoundDbl(LinFmod(1,400.4,426.4,121,130,L))
										        else:
										            Result = CalcStat("AwardILvlG",L)
									    else:
									        if 121 <= Lp and Lm <= 130:
									            Result = RoundDbl(LinFmod(1,400.4,408.3,121,130,L))
									        else:
									            Result = CalcStat("AwardILvlG",L)
								    elif SN > 'AWARDILVLGE':
									    if SN < 'AWARDILVLH':
										    if SN == 'AWARDILVLGF':
										        if 121 <= Lp and Lm <= 130:
										            Result = RoundDbl(LinFmod(1,400.4,440.4,121,130,L))
										        else:
										            Result = CalcStat("AwardILvlG",L)
									    elif SN > 'AWARDILVLH':
										    if SN == 'AWARDILVLI':
										        if Lm <= 44:
										            Result = 1
										        elif Lm <= 55:
										            Result = 52
										        elif Lm <= 75:
										            Result = RoundDblDown((L-56)/5)*5+60
										        elif Lm <= 85:
										            Result = RoundDblDown((L-76)/5)*29+100
										        elif Lm <= 95:
										            Result = RoundDblDown((L-86)/5)*20+155
										        elif Lm <= 100:
										            Result = RoundDblDown((L-96)/4)*10+190
										        elif Lm <= 105:
										            Result = RoundDblDown((L-101)/4)*35+215
										        elif Lm <= 110:
										            Result = CalcStat("LvlToILvl",106)+15
										        elif Lm <= 115:
										            Result = CalcStat("LvlToILvl",115)
										        elif Lm <= 119:
										            Result = CalcStat("LvlToILvl",116)+15
										        elif Lm <= 120:
										            Result = CalcStat("LvlToILvl",120)
										        elif Lm <= 125:
										            Result = CalcStat("LvlToILvl",121)+15
										        elif Lm <= 130:
										            Result = CalcStat("LvlToILvl",130)
										        elif Lm <= 135:
										            Result = CalcStat("LvlToILvl",131)+15
										        elif Lm <= 140:
										            Result = CalcStat("LvlToILvl",140)
										        elif Lm <= 145:
										            Result = CalcStat("LvlToILvl",141)+15
										        elif Lm <= 150:
										            Result = CalcStat("LvlToILvl",150)
										        else:
										            Result = CalcStat("AwardILvlI",150)
									    else:
									        if Lm <= 4:
									            Result = CalcStat("AwardILvlA",1)
									        elif Lm <= 50:
									            Result = CalcStat("AwardILvlA",L-4)
									        elif Lm <= 54:
									            Result = CalcStat("AwardILvlA",51)
									        elif Lm <= 75:
									            Result = CalcStat("AwardILvlA",L-4)
									        else:
									            Result = L-4
								    else:
								        if 121 <= Lp and Lm <= 130:
								            Result = RoundDbl(LinFmod(1,400.4,434.4,121,130,L))
								        else:
								            Result = CalcStat("AwardILvlG",L)
							    elif SN > 'AWARDILVLIA':
								    if SN < 'AWARDILVLJC':
									    if SN < 'AWARDILVLJA':
										    if SN == 'AWARDILVLJ':
										        if Lm <= 130:
										            Result = CalcStat("AwardILvlC",L)
										        elif Lm <= 140:
										            Result = RoundDbl(LinFmod(1,450.4,460.4,131,140,L))
										        else:
										            Result = CalcStat("AwardILvlA",L)
									    elif SN > 'AWARDILVLJA':
										    if SN == 'AWARDILVLJB':
										        if 131 <= Lp and Lm <= 140:
										            Result = RoundDbl(LinFmod(1,450.4,470.4,131,140,L))
										        else:
										            Result = CalcStat("AwardILvlJ",L)
									    else:
									        if 131 <= Lp and Lm <= 140:
									            Result = RoundDbl(LinFmod(1,450.4,465.4,131,140,L))
									        else:
									            Result = CalcStat("AwardILvlJ",L)
								    elif SN > 'AWARDILVLJC':
									    if SN < 'AWARDILVLK':
										    if SN == 'AWARDILVLJD':
										        if 131 <= Lp and Lm <= 140:
										            Result = RoundDbl(LinFmod(1,450.4,480.4,131,140,L))
										        else:
										            Result = CalcStat("AwardILvlJ",L)
									    elif SN > 'AWARDILVLK':
										    if SN == 'AWARDILVLL':
										        if Lm <= 50:
										            Result = CalcStat("AwardILvlB",L)
										        elif Lm <= 54:
										            Result = CalcStat("AwardILvlA",L)-3
										        elif Lm <= 74:
										            Result = CalcStat("AwardILvlA",L)-4
										        elif Lm <= 75:
										            Result = CalcStat("AwardILvlA",L)-5
										        elif Lm <= 95:
										            Result = CalcStat("AwardILvlA",L)-1
										        elif Lm <= 115:
										            Result = CalcStat("AwardILvlA",L)-2
										        elif Lm <= 120:
										            Result = CalcStat("AwardILvlA",L)
										        elif Lm <= 130:
										            Result = RoundDbl(LinFmod(1,397,400,121,130,L))
										        elif Lm <= 134:
										            Result = CalcStat("AwardILvlA",L)
										        elif Lm <= 137:
										            Result = DataTableValue((449,450,450),L-134)
										        elif Lm <= 140:
										            Result = CalcStat("AwardILvlL",L-3)
										        elif Lm <= 145:
										            Result = RoundDbl(LinFmod(1,495.4,500.4,141,145,L))
										        elif Lm <= 150:
										            Result = RoundDbl(LinFmod(1,500.5,502,146,150,L))
										        else:
										            Result = CalcStat("AwardILvlL",150)
									    else:
									        Result = CalcStat("CombatBaseTacHPSLvlToILvl",L)
								    else:
								        if 131 <= Lp and Lm <= 140:
								            Result = RoundDbl(LinFmod(1,450.4,475.4,131,140,L))
								        else:
								            Result = CalcStat("AwardILvlJ",L)
							    else:
							        if Lm <= 44:
							            Result = CalcStat("AwardILvlI",L)
							        elif Lm <= 55:
							            Result = RoundDblDown((L-45)/6)+51
							        elif Lm <= 90:
							            Result = CalcStat("AwardILvlI",L)
							        elif Lm <= 104:
							            Result = RoundDblDown((L-91)/5)*25+165
							        elif Lm <= 105:
							            Result = CalcStat("LvlToILvl",L)
							        elif Lm <= 110:
							            Result = CalcStat("LvlToILvl",106)+15
							        elif Lm <= 115:
							            Result = CalcStat("LvlToILvl",115)-20
							        elif Lm <= 120:
							            Result = CalcStat("LvlToILvl",116)+15
							        elif Lm <= 125:
							            Result = CalcStat("LvlToILvl",121)+15
							        elif Lm <= 130:
							            Result = CalcStat("LvlToILvl",130)-20
							        elif Lm <= 135:
							            Result = CalcStat("LvlToILvl",131)+15
							        elif Lm <= 140:
							            Result = CalcStat("LvlToILvl",140)-4
							        elif Lm <= 150:
							            Result = CalcStat("LvlToILvl",141)+15
							        else:
							            Result = CalcStat("AwardILvlIA",150)
						    else:
						        if 121 <= Lp and Lm <= 130:
						            Result = RoundDbl(LinFmod(1,400.4,412.4,121,130,L))
						        else:
						            Result = CalcStat("AwardILvlG",L)
					    elif SN > 'AWARDLVLCAP':
						    if SN < 'BATTLELOREPHYMAS':
							    if SN < 'BASEFATE':
								    if SN < 'BALANCEOFMANBLOCK':
									    if SN < 'AXEARMOURREND':
										    if SN == 'AWARDLVLTOILVL':
										        Result = CalcStat("AwardILvlC",L)
									    elif SN > 'AXEARMOURREND':
										    if SN == 'AXEARMRENDPOS':
										        if Lm <= 7:
										            Result = RoundDbl(LinFmod(1,0.5,3.25,1,7,L))
										        elif Lm <= 14:
										            Result = RoundDbl(LinFmod(1,3.75,8.5,8,14,L))
										        elif Lm <= 30:
										            Result = RoundDbl(LinFmod(1,9,24.7,15,30,L))
										        elif Lm <= 39:
										            Result = RoundDbl(LinFmod(1,26.5,37,31,39,L))
										        elif Lm <= 50:
										            Result = RoundDbl(LinFmod(1,38.5,53,40,50,L))
										        elif Lm <= 52:
										            Result = 53
										        elif Lm <= 60:
										            Result = RoundDbl(LinFmod(1,53.2,64.8,53,60,L))
										        elif Lm <= 77:
										            Result = RoundDbl(LinFmod(1,66.15,94.8,61,77,L))
										        elif Lm <= 113:
										            Result = RoundDbl(RoundDbl(L/3-0.5)*1.95+44.1)
										        elif Lm <= 141:
										            Result = 116
										        elif Lm <= 181:
										            Result = RoundDbl(RoundDbl(L/4)*2+46)
										        elif Lm <= 217:
										            Result = RoundDbl(RoundDbl(L/4)*2+45)
										        elif Lm <= 221:
										            Result = 153
										        elif Lm <= 299:
										            Result = 155
										        elif Lm <= 308:
										            Result = RoundDbl(RoundDbl(L/2.6-0.4)*2-73)
										        elif Lm <= 317:
										            Result = RoundDbl(RoundDbl(L/2.74-0.75)*2-60)
										        elif Lm <= 325:
										            Result = 172
										        elif Lm <= 326:
										            Result = 174
										        elif 327 <= Lp and Lm <= 599:
										            Result = EquSng(ExpFmod(CalcStat("AxeArmRendPos",326),327,1,L,1))
										        else:
										            Result = CalcStat("AxeArmRendPos",599)
									    else:
									        Result = -CalcStat("AxeArmRendPos",L)
								    elif SN > 'BALANCEOFMANBLOCK':
									    if SN < 'BALANCEOFMANPARRY':
										    if SN == 'BALANCEOFMANEVADE':
										        Result = CalcStat("EvadeT",L,1.0)
									    elif SN > 'BALANCEOFMANPARRY':
										    if SN == 'BASEAGILITY':
										        Result = CalcStat("BaseMain",L,N)
									    else:
									        Result = CalcStat("ParryT",L,0.8)
								    else:
								        Result = CalcStat("BlockT",L,0.8)
							    elif SN > 'BASEFATE':
								    if SN < 'BASEPOWER':
									    if SN < 'BASEMIGHT':
										    if SN == 'BASEMAIN':
										        if Lm <= 95:
										            Result = RoundDbl(CalcStat("ProgBMainBase",L)*N)
										        else:
										            Result = RoundDbl(RoundDbl(CalcStat("ProgBMainBase",L))*N)
									    elif SN > 'BASEMIGHT':
										    if SN == 'BASEMORALE':
										        if Lm <= 95:
										            Result = RoundDblDown(CalcStat("ProgBMorale",L)*10)
										        else:
										            Result = RoundDbl(RoundDbl(CalcStat("ProgBMorale",L))*10)
									    else:
									        Result = CalcStat("BaseMain",L,N)
								    elif SN > 'BASEPOWER':
									    if SN < 'BASEWILL':
										    if SN == 'BASEVITALITY':
										        if Lm <= 95:
										            Result = RoundDbl(CalcStat("ProgBVitality",L)*1.5)
										        else:
										            Result = RoundDbl(RoundDbl(CalcStat("ProgBVitality",L))*1.5)
									    elif SN > 'BASEWILL':
										    if SN == 'BATTLELOREMAS':
										        if Lm <= 105:
										            Result = CalcStat("Mastery",L,2.5)
										        elif 120 <= Lp and Lm <= 120 or 130 <= Lp and Lm <= 130:
										            Result = CalcStat("MasteryT",L,1.6)
										        else:
										            Result = CalcStat("MasteryT",L,1.2)
									    else:
									        Result = CalcStat("BaseMain",L,N)
								    else:
								        if Lm <= 95:
								            Result = RoundDblDown(CalcStat("ProgBPower",L)*10)
								        else:
								            Result = RoundDbl(CalcStat("ProgBPower",L)*10)
							    else:
							        if Lm <= 95:
							            Result = RoundDbl(CalcStat("ProgBFate",L)*7.0)
							        else:
							            Result = RoundDbl(RoundDbl(CalcStat("ProgBFate",L),1)*7.0)
						    elif SN > 'BATTLELOREPHYMAS':
							    if SN < 'BEORNINGCDAGILITYTOCRITHIT':
								    if SN < 'BEOFATE':
									    if SN < 'BEOBEARFORMCRITDEF':
										    if SN == 'BATTLELORETACMAS':
										        Result = CalcStat("BattleLoreMas",L)
									    elif SN > 'BEOBEARFORMCRITDEF':
										    if SN == 'BEOEMISSARYFATE':
										        Result = CalcStat("FateT",L,1.0)
									    else:
									        Result = CalcStat("CritDefT",L,0.4)
								    elif SN > 'BEOFATE':
									    if SN < 'BEOFEWINNUMBERFATE':
										    if SN == 'BEOFERALPRESFATE':
										        Result = CalcStat("FateT",L,1.0)
									    elif SN > 'BEOFEWINNUMBERFATE':
										    if SN == 'BEOMIGHTOFTHEWILDMIGHT':
										        Result = CalcStat("MightT",L,1.0)
									    else:
									        Result = -CalcStat("FateT",L,0.4)
								    else:
								        Result = CalcStat("FateT",L,CalcStat("Trait567810Choice",N)*0.4)
							    elif SN > 'BEORNINGCDAGILITYTOCRITHIT':
								    if SN < 'BEORNINGCDAGILITYTOPHYMAS':
									    if SN < 'BEORNINGCDAGILITYTOFINESSE':
										    if SN == 'BEORNINGCDAGILITYTOEVADE':
										        Result = 1
									    elif SN > 'BEORNINGCDAGILITYTOFINESSE':
										    if SN == 'BEORNINGCDAGILITYTOOUTHEAL':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'BEORNINGCDAGILITYTOPHYMAS':
									    if SN < 'BEORNINGCDARMOURTONONPHYMIT':
										    if SN == 'BEORNINGCDARMOURTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'BEORNINGCDARMOURTONONPHYMIT':
										    if SN == 'BEORNINGCDARMOURTOTACMIT':
										        Result = 0.2
									    else:
									        Result = 0.2
								    else:
								        Result = 2
							    else:
							        Result = 2
						    else:
						        Result = CalcStat("BattleLoreMas",L)
					    else:
					        Result = 150
				    else:
				        if 106 <= Lp and Lm <= 115:
				            Result = RoundDbl(LinFmod(1,300,345,106,115,L))
				        else:
				            Result = CalcStat("AwardILvlD",L)
			    elif SN > 'BEORNINGCDARMOURTYPE':
				    if SN < 'BLOCKT':
					    if SN < 'BEORNINGCDWILLTOFINESSE':
						    if SN < 'BEORNINGCDFATETOICMR':
							    if SN < 'BEORNINGCDBASENCPR':
								    if SN < 'BEORNINGCDBASEICPR':
									    if SN < 'BEORNINGCDBASEFATE':
										    if SN == 'BEORNINGCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityM",L)
									    elif SN > 'BEORNINGCDBASEFATE':
										    if SN == 'BEORNINGCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRM",L)
									    else:
									        Result = CalcStat("ClassBaseFate",L)
								    elif SN > 'BEORNINGCDBASEICPR':
									    if SN < 'BEORNINGCDBASEMORALE':
										    if SN == 'BEORNINGCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightM",L)
									    elif SN > 'BEORNINGCDBASEMORALE':
										    if SN == 'BEORNINGCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRM",L)
									    else:
									        Result = CalcStat("ClassBaseMorale",L)
								    else:
								        Result = CalcStat("ClassBaseICPR",L)
							    elif SN > 'BEORNINGCDBASENCPR':
								    if SN < 'BEORNINGCDCALCTYPECOMPHYMIT':
									    if SN < 'BEORNINGCDBASEVITALITY':
										    if SN == 'BEORNINGCDBASEPOWER':
										        Result = 10
									    elif SN > 'BEORNINGCDBASEVITALITY':
										    if SN == 'BEORNINGCDBASEWILL':
										        Result = CalcStat("ClassBaseWillM",L)
									    else:
									        Result = CalcStat("ClassBaseVitality",L)
								    elif SN > 'BEORNINGCDCALCTYPECOMPHYMIT':
									    if SN < 'BEORNINGCDCALCTYPETACMIT':
										    if SN == 'BEORNINGCDCALCTYPENONPHYMIT':
										        Result = 14
									    elif SN > 'BEORNINGCDCALCTYPETACMIT':
										    if SN == 'BEORNINGCDCANBLOCK':
										        if 6 <= Lp:
										            Result = 1
									    else:
									        Result = 27
								    else:
								        Result = 14
							    else:
							        Result = CalcStat("ClassBaseNCPR",L)
						    elif SN > 'BEORNINGCDFATETOICMR':
							    if SN < 'BEORNINGCDMIGHTTOPHYMIT':
								    if SN < 'BEORNINGCDMIGHTTOEVADE':
									    if SN < 'BEORNINGCDFATETONCMR':
										    if SN == 'BEORNINGCDFATETOMORALE':
										        Result = 2.5
									    elif SN > 'BEORNINGCDFATETONCMR':
										    if SN == 'BEORNINGCDMIGHTTOCRITHIT':
										        Result = 1
									    else:
									        Result = 0.12
								    elif SN > 'BEORNINGCDMIGHTTOEVADE':
									    if SN < 'BEORNINGCDMIGHTTOPARRY':
										    if SN == 'BEORNINGCDMIGHTTOOUTHEAL':
										        Result = 3
									    elif SN > 'BEORNINGCDMIGHTTOPARRY':
										    if SN == 'BEORNINGCDMIGHTTOPHYMAS':
										        Result = 3
									    else:
									        Result = 1
								    else:
								        Result = 2
							    elif SN > 'BEORNINGCDMIGHTTOPHYMIT':
								    if SN < 'BEORNINGCDTACMASTOOUTHEAL':
									    if SN < 'BEORNINGCDPHYMITTOCOMPHYMIT':
										    if SN == 'BEORNINGCDMIGHTTOTACMIT':
										        Result = 1
									    elif SN > 'BEORNINGCDPHYMITTOCOMPHYMIT':
										    if SN == 'BEORNINGCDPHYMITTONONPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'BEORNINGCDTACMASTOOUTHEAL':
									    if SN < 'BEORNINGCDVITALITYTOMORALE':
										    if SN == 'BEORNINGCDVITALITYTOICMR':
										        Result = 0.012
									    elif SN > 'BEORNINGCDVITALITYTOMORALE':
										    if SN == 'BEORNINGCDVITALITYTONCMR':
										        Result = 0.12
									    else:
									        Result = 4.5
								    else:
								        Result = 1
							    else:
							        Result = 1
						    else:
						        Result = 0.04
					    elif SN > 'BEORNINGCDWILLTOFINESSE':
						    if SN < 'BLACKARROWCDCALCTYPENONPHYMIT':
							    if SN < 'BEORNINGRDPSVTWONAME':
								    if SN < 'BEORNINGCDWILLTORESIST':
									    if SN < 'BEORNINGCDWILLTOPHYMAS':
										    if SN == 'BEORNINGCDWILLTOOUTHEAL':
										        Result = 1
									    elif SN > 'BEORNINGCDWILLTOPHYMAS':
										    if SN == 'BEORNINGCDWILLTOPHYMIT':
										        Result = 1.5
									    else:
									        Result = 1
								    elif SN > 'BEORNINGCDWILLTORESIST':
									    if SN < 'BEORNINGRDPSVONEFATE':
										    if SN == 'BEORNINGCDWILLTOTACMIT':
										        Result = 1.5
									    elif SN > 'BEORNINGRDPSVONEFATE':
										    if SN == 'BEORNINGRDPSVONENAME':
										        Result = "Emissary"
									    else:
									        Result = CalcStat("BeoEmissaryFate",L)
								    else:
								        Result = 1
							    elif SN > 'BEORNINGRDPSVTWONAME':
								    if SN < 'BEOTHICKHIDEVITALITY':
									    if SN < 'BEORNINGRDTRAITMIGHT':
										    if SN == 'BEORNINGRDTRAITFATE':
										        Result = CalcStat("BeoFewinNumberFate",L)
									    elif SN > 'BEORNINGRDTRAITMIGHT':
										    if SN == 'BEORNINGRDTRAITVITALITY':
										        Result = CalcStat("BeoThickHideVitality",L)
									    else:
									        Result = CalcStat("BeoMightoftheWildMight",L)
								    elif SN > 'BEOTHICKHIDEVITALITY':
									    if SN < 'BLACKARROWCANBLOCK':
										    if SN == 'BEOVITALITYINCREASE':
										        Result = CalcStat("VitalityT",L,CalcStat("Trait567810Choice",N)*0.4)
									    elif SN > 'BLACKARROWCANBLOCK':
										    if SN == 'BLACKARROWCDCALCTYPECOMPHYMIT':
										        Result = 13
									    else:
									        Result = 1
								    else:
								        Result = CalcStat("VitalityT",L,1.0)
							    else:
							        Result = ""
						    elif SN > 'BLACKARROWCDCALCTYPENONPHYMIT':
							    if SN < 'BLOCKPBONUS':
								    if SN < 'BLOCKC':
									    if SN < 'BLACKARROWCDHASPOWER':
										    if SN == 'BLACKARROWCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'BLACKARROWCDHASPOWER':
										    if SN == 'BLOCK':
										        Result = CalcStat("BPE",L,N)
									    else:
									        Result = 1
								    elif SN > 'BLOCKC':
									    if SN < 'BLOCKCIRAW':
										    if SN == 'BLOCKCI':
										        Result = CalcStat("BPECI",L,N)
									    elif SN > 'BLOCKCIRAW':
										    if SN == 'BLOCKCRAW':
										        Result = CalcStat("BPECRAW",L,N)
									    else:
									        Result = CalcStat("BPECIRAW",L,N)
								    else:
								        Result = CalcStat("BPEC",L,N)
							    elif SN > 'BLOCKPBONUS':
								    if SN < 'BLOCKPRATPB':
									    if SN < 'BLOCKPRATP':
										    if SN == 'BLOCKPPRAT':
										        Result = CalcStat("BPEPPRat",L,N)
									    elif SN > 'BLOCKPRATP':
										    if SN == 'BLOCKPRATPA':
										        Result = CalcStat("BPEPRatPA",L)
									    else:
									        Result = CalcStat("BPEPRatP",L,N)
								    elif SN > 'BLOCKPRATPB':
									    if SN < 'BLOCKPRATPCAP':
										    if SN == 'BLOCKPRATPC':
										        Result = CalcStat("BPEPRatPC",L)
									    elif SN > 'BLOCKPRATPCAP':
										    if SN == 'BLOCKPRATPCAPR':
										        Result = CalcStat("BPEPRatPCapR",L)
									    else:
									        Result = CalcStat("BPEPRatPCap",L)
								    else:
								        Result = CalcStat("BPEPRatPB",L)
							    else:
							        Result = CalcStat("BPEPBonus",L)
						    else:
						        Result = 14
					    else:
					        Result = 1
				    elif SN > 'BLOCKT':
					    if SN < 'BRAWLERCDARMOURTOCOMPHYMIT':
						    if SN < 'BRATDEVHIT':
							    if SN < 'BPEPRATP':
								    if SN < 'BPECILVLFILTER':
									    if SN < 'BPEC':
										    if SN == 'BPE':
										        Result = EquSng(StatLinInter("PntMPBPE","ItemPntS","ProgBBPE","AdjItem",L,N,0))
									    elif SN > 'BPEC':
										    if SN == 'BPECI':
										        Result = RoundDblLotro(CalcStat("BPECIRaw",L,N))
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("BPECI",CalcStat("BPECILvlFilter",N),N),0)
								    elif SN > 'BPECILVLFILTER':
									    if SN < 'BPECRAW':
										    if SN == 'BPECIRAW':
										        Result = StatLinInter("PntMPBPEC","ItemPntS","ProgBBPE","AdjCreepItem",L,N,4)
									    elif SN > 'BPECRAW':
										    if SN == 'BPEPPRAT':
										        Result = CalcRatAB(CalcStat("BPEPRatPA",L),CalcStat("BPEPRatPB",L),CalcStat("BPEPRatPCapR",L),N)
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("BPECIRaw",CalcStat("BPECILvlFilter",N),N),99)
								    else:
								        if 3.8 <= Lp and Lm <= 3.8 or 4 <= Lp and Lm <= 4 or 4.6 <= Lp and Lm <= 4.6 or 6.2 <= Lp and Lm <= 6.2 or 8 <= Lp and Lm <= 8 or 12 <= Lp and Lm <= 12:
								            Result = 515
								        else:
								            Result = CalcStat("CreepILvlCurr",L)
							    elif SN > 'BPEPRATP':
								    if SN < 'BPEPRATPCAP':
									    if SN < 'BPEPRATPB':
										    if SN == 'BPEPRATPA':
										        Result = 39
									    elif SN > 'BPEPRATPB':
										    if SN == 'BPEPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatStandard")
								    elif SN > 'BPEPRATPCAP':
									    if SN < 'BPET':
										    if SN == 'BPEPRATPCAPR':
										        Result = CalcStat("BPEPRatPB",L)*CalcStat("BPEPRatPC",L)
									    elif SN > 'BPET':
										    if SN == 'BRATCRITMAGN':
										        Result = CalcStat("StdProgRatings",L,600)
									    else:
									        Result = EquSng(StatLinInter("PntMPBPE","TraitPntS","ProgBBPE","AdjTrait",L,N,0))
								    else:
								        Result = 13
							    else:
							        Result = CalcPercAB(CalcStat("BPEPRatPA",L),CalcStat("BPEPRatPB",L),CalcStat("BPEPRatPCap",L),N)
						    elif SN > 'BRATDEVHIT':
							    if SN < 'BRATPROGB':
								    if SN < 'BRATMITLIGHT':
									    if SN < 'BRATMITHEAVY':
										    if SN == 'BRATEXTRA':
										        Result = CalcStat("StdProgRatings",L,300)
									    elif SN > 'BRATMITHEAVY':
										    if SN == 'BRATMITIGATIONS':
										        if Lm <= 50:
										            Result = LinFmod(1,(N*CalcStat("BRatStandard",1))*7/6-50.4,N*CalcStat("BRatStandard",50),1,50,L,"P")
										        else:
										            Result = StatLinInter("","StdPntS","BRatStandard","",L,N,3)
									    else:
									        Result = CalcStat("BRatStandard",L)
								    elif SN > 'BRATMITLIGHT':
									    if SN < 'BRATOUTHEAL':
										    if SN == 'BRATMITMEDIUM':
										        Result = CalcStat("BRatMitigations",L,0.833)
									    elif SN > 'BRATOUTHEAL':
										    if SN == 'BRATPARTBPE':
										        Result = CalcStat("StdProgRatings",L,350)
									    else:
									        Result = CalcStat("StdProgRatings",L,450)
								    else:
								        Result = CalcStat("BRatMitigations",L,0.666)
							    elif SN > 'BRATPROGB':
								    if SN < 'BRAWLERCDAGILITYTOEVADE':
									    if SN < 'BRATSTANDARD':
										    if SN == 'BRATROUNDED':
										        if Lm <= 50:
										            Result = RoundDbl(CalcStat(C,L))
										        elif Lm <= 105:
										            Result = RoundDbl(CalcStat(C,L),-1)
										        elif Lm <= 115:
										            Result = RoundDbl(CalcStat(C,L),-2)
										        elif Lm <= 130:
										            Result = RoundDbl(CalcStat(C,L),-1)
										        elif Lm <= 150:
										            Result = RoundDbl(CalcStat(C,L),-2)
										        else:
										            Result = RoundDbl(CalcStat(C,L))
									    elif SN > 'BRATSTANDARD':
										    if SN == 'BRAWLERCDAGILITYTOCRITHIT':
										        Result = 2
									    else:
									        Result = CalcStat("StdProgRatings",L,200)
								    elif SN > 'BRAWLERCDAGILITYTOEVADE':
									    if SN < 'BRAWLERCDAGILITYTOOUTHEAL':
										    if SN == 'BRAWLERCDAGILITYTOFINESSE':
										        Result = 1
									    elif SN > 'BRAWLERCDAGILITYTOOUTHEAL':
										    if SN == 'BRAWLERCDAGILITYTOPHYMAS':
										        Result = 2
									    else:
									        Result = 2
								    else:
								        Result = 2
							    else:
							        if Lm <= 50:
							            Result = RoundDbl(CalcStat(C,L))
							        else:
							            Result = CalcStat(C,L)
						    else:
						        Result = CalcStat("StdProgRatings",L,400)
					    elif SN > 'BRAWLERCDARMOURTOCOMPHYMIT':
						    if SN < 'BRAWLERCDCALCTYPENONPHYMIT':
							    if SN < 'BRAWLERCDBASEMIGHT':
								    if SN < 'BRAWLERCDBASEAGILITY':
									    if SN < 'BRAWLERCDARMOURTOTACMIT':
										    if SN == 'BRAWLERCDARMOURTONONPHYMIT':
										        Result = 0.2
									    elif SN > 'BRAWLERCDARMOURTOTACMIT':
										    if SN == 'BRAWLERCDARMOURTYPE':
										        Result = 3
									    else:
									        Result = 0.2
								    elif SN > 'BRAWLERCDBASEAGILITY':
									    if SN < 'BRAWLERCDBASEICMR':
										    if SN == 'BRAWLERCDBASEFATE':
										        Result = CalcStat("ClassBaseFate",L)
									    elif SN > 'BRAWLERCDBASEICMR':
										    if SN == 'BRAWLERCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    else:
									        Result = CalcStat("ClassBaseICMRL",L)
								    else:
								        Result = CalcStat("ClassBaseAgilityM",L)
							    elif SN > 'BRAWLERCDBASEMIGHT':
								    if SN < 'BRAWLERCDBASEPOWER':
									    if SN < 'BRAWLERCDBASENCMR':
										    if SN == 'BRAWLERCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    elif SN > 'BRAWLERCDBASENCMR':
										    if SN == 'BRAWLERCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    else:
									        Result = CalcStat("ClassBaseNCMRL",L)
								    elif SN > 'BRAWLERCDBASEPOWER':
									    if SN < 'BRAWLERCDBASEWILL':
										    if SN == 'BRAWLERCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    elif SN > 'BRAWLERCDBASEWILL':
										    if SN == 'BRAWLERCDCALCTYPECOMPHYMIT':
										        Result = 14
									    else:
									        Result = CalcStat("ClassBaseWillL",L)
								    else:
								        Result = CalcStat("ClassBasePower",L)
							    else:
							        Result = CalcStat("ClassBaseMightH",L)
						    elif SN > 'BRAWLERCDCALCTYPENONPHYMIT':
							    if SN < 'BRAWLERCDMIGHTTOPARRY':
								    if SN < 'BRAWLERCDHASPOWER':
									    if SN < 'BRAWLERCDFATETONCPR':
										    if SN == 'BRAWLERCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'BRAWLERCDFATETONCPR':
										    if SN == 'BRAWLERCDFATETOPOWER':
										        Result = 1
									    else:
									        Result = 0.07
								    elif SN > 'BRAWLERCDHASPOWER':
									    if SN < 'BRAWLERCDMIGHTTOEVADE':
										    if SN == 'BRAWLERCDMIGHTTOCRITHIT':
										        Result = 1
									    elif SN > 'BRAWLERCDMIGHTTOEVADE':
										    if SN == 'BRAWLERCDMIGHTTOOUTHEAL':
										        Result = 3
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'BRAWLERCDMIGHTTOPARRY':
								    if SN < 'BRAWLERCDPHYMITTOCOMPHYMIT':
									    if SN < 'BRAWLERCDMIGHTTOPHYMIT':
										    if SN == 'BRAWLERCDMIGHTTOPHYMAS':
										        Result = 3
									    elif SN > 'BRAWLERCDMIGHTTOPHYMIT':
										    if SN == 'BRAWLERCDMIGHTTOTACMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'BRAWLERCDPHYMITTOCOMPHYMIT':
									    if SN < 'BRAWLERCDTACMASTOOUTHEAL':
										    if SN == 'BRAWLERCDPHYMITTONONPHYMIT':
										        Result = 1
									    elif SN > 'BRAWLERCDTACMASTOOUTHEAL':
										    if SN > 'BRAWLERCDVITALITYTOICMR':
											    if SN == 'BRAWLERCDVITALITYTOMORALE':
											        Result = 4.5
										    elif SN == 'BRAWLERCDVITALITYTOICMR':
										        Result = 0.012
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = 1
						    else:
						        Result = 14
					    else:
					        Result = 1
				    else:
				        Result = CalcStat("BPET",L,N)
			    else:
			        Result = 3
		    elif SN > 'BRAWLERCDVITALITYTONCMR':
			    if SN < 'CHAMPIONCDBASEICMR':
				    if SN < 'BURGLARCDVITALITYTONCMR':
					    if SN < 'BURGLARCDAGILITYTOTACMIT':
						    if SN < 'BRWINNSTRCLEVTECHFINESSE':
							    if SN < 'BRGALLINONEXPFINESSE':
								    if SN < 'BRAWLERCDWILLTOPHYMIT':
									    if SN < 'BRAWLERCDWILLTOOUTHEAL':
										    if SN == 'BRAWLERCDWILLTOFINESSE':
										        Result = 1
									    elif SN > 'BRAWLERCDWILLTOOUTHEAL':
										    if SN == 'BRAWLERCDWILLTOPHYMAS':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'BRAWLERCDWILLTOPHYMIT':
									    if SN < 'BRAWLERCDWILLTOTACMIT':
										    if SN == 'BRAWLERCDWILLTORESIST':
										        Result = 1
									    elif SN > 'BRAWLERCDWILLTOTACMIT':
										    if SN == 'BRGALLINFINESSE':
										        Result = CalcStat("Finesse",L,2)
									    else:
									        Result = 1.5
								    else:
								        Result = 1.5
							    elif SN > 'BRGALLINONEXPFINESSE':
								    if SN < 'BRGTRICKCNTDEFBPE':
									    if SN < 'BRGREVWEAKNFINESSE':
										    if SN == 'BRGREVWEAKNCRITDEF':
										        Result = -CalcStat("CritDefT",L,0.4)
									    elif SN > 'BRGREVWEAKNFINESSE':
										    if SN == 'BRGREVWEAKNRESIST':
										        Result = -CalcStat("ResistT",L,0.4)
									    else:
									        Result = -CalcStat("FinesseT",L,0.4)
								    elif SN > 'BRGTRICKCNTDEFBPE':
									    if SN < 'BRWAGGPOSTUREPHYMIT':
										    if SN == 'BRGTRICKCNTDEFCRITDEF':
										        Result = -CalcStat("CritDefT",L,0.8)
									    elif SN > 'BRWAGGPOSTUREPHYMIT':
										    if SN == 'BRWDEFPOSTUREPHYMAS':
										        Result = -CalcStat("PhyMasT",L,4)
									    else:
									        Result = -CalcStat("PhyMitT",L,3)
								    else:
								        Result = -CalcStat("BPET",L,1.2)
							    else:
							        Result = -CalcStat("Finesse",L,2)
						    elif SN > 'BRWINNSTRCLEVTECHFINESSE':
							    if SN < 'BRWTACMIT':
								    if SN < 'BRWRETINTENSITYCRITHIT':
									    if SN < 'BRWMAELSTROMMIGHT':
										    if SN == 'BRWINNSTRPRECISIONCRITHIT':
										        Result = CalcStat("CritHitT",L,CalcStat("Trait13510Choice",N)*0.2)
									    elif SN > 'BRWMAELSTROMMIGHT':
										    if SN == 'BRWMIGHTINCREASE':
										        Result = CalcStat("MightT",L,CalcStat("Trait567810Choice",N)*0.4)
									    else:
									        Result = CalcStat("MightT",L,2)
								    elif SN > 'BRWRETINTENSITYCRITHIT':
									    if SN < 'BRWSHAREISBALANCEFINESSE':
										    if SN == 'BRWRETPRECISIONFINESSE':
										        Result = CalcStat("FinesseT",L,CalcStat("Trait234Choice",N))
									    elif SN > 'BRWSHAREISBALANCEFINESSE':
										    if SN == 'BRWSHAREISHEAVYCRITHIT':
										        Result = CalcStat("BrwInnStrPrecisionCritHit",L,3)
									    else:
									        Result = CalcStat("BrwInnStrClevTechFinesse",L,3)
								    else:
								        Result = CalcStat("CritHitT",L,CalcStat("Trait234Choice",N))
							    elif SN > 'BRWTACMIT':
								    if SN < 'BURGLARCDAGILITYTOOUTHEAL':
									    if SN < 'BURGLARCDAGILITYTOCRITHIT':
										    if SN == 'BRWVITALITYINCREASE':
										        Result = CalcStat("VitalityT",L,CalcStat("Trait567810Choice",N)*0.4)
									    elif SN > 'BURGLARCDAGILITYTOCRITHIT':
										    if SN == 'BURGLARCDAGILITYTOEVADE':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'BURGLARCDAGILITYTOOUTHEAL':
									    if SN < 'BURGLARCDAGILITYTOPHYMAS':
										    if SN == 'BURGLARCDAGILITYTOPARRY':
										        Result = 1
									    elif SN > 'BURGLARCDAGILITYTOPHYMAS':
										    if SN == 'BURGLARCDAGILITYTOPHYMIT':
										        Result = 1
									    else:
									        Result = 3
								    else:
								        Result = 3
							    else:
							        Result = CalcStat("TacMitT",L,CalcStat("Trait12345Choice",N)*0.4)
						    else:
						        Result = CalcStat("FinesseT",L,CalcStat("Trait13510Choice",N)*0.2)
					    elif SN > 'BURGLARCDAGILITYTOTACMIT':
						    if SN < 'BURGLARCDCALCTYPECOMPHYMIT':
							    if SN < 'BURGLARCDBASEICPR':
								    if SN < 'BURGLARCDARMOURTYPE':
									    if SN < 'BURGLARCDARMOURTONONPHYMIT':
										    if SN == 'BURGLARCDARMOURTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'BURGLARCDARMOURTONONPHYMIT':
										    if SN == 'BURGLARCDARMOURTOTACMIT':
										        Result = 0.2
									    else:
									        Result = 0.2
								    elif SN > 'BURGLARCDARMOURTYPE':
									    if SN < 'BURGLARCDBASEFATE':
										    if SN == 'BURGLARCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityH",L)
									    elif SN > 'BURGLARCDBASEFATE':
										    if SN == 'BURGLARCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRL",L)
									    else:
									        Result = CalcStat("ClassBaseFate",L)
								    else:
								        Result = 2
							    elif SN > 'BURGLARCDBASEICPR':
								    if SN < 'BURGLARCDBASENCPR':
									    if SN < 'BURGLARCDBASEMORALE':
										    if SN == 'BURGLARCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightM",L)
									    elif SN > 'BURGLARCDBASEMORALE':
										    if SN == 'BURGLARCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRL",L)
									    else:
									        Result = CalcStat("ClassBaseMorale",L)
								    elif SN > 'BURGLARCDBASENCPR':
									    if SN < 'BURGLARCDBASEVITALITY':
										    if SN == 'BURGLARCDBASEPOWER':
										        Result = CalcStat("ClassBasePower",L)
									    elif SN > 'BURGLARCDBASEVITALITY':
										    if SN == 'BURGLARCDBASEWILL':
										        Result = CalcStat("ClassBaseWillL",L)
									    else:
									        Result = CalcStat("ClassBaseVitality",L)
								    else:
								        Result = CalcStat("ClassBaseNCPR",L)
							    else:
							        Result = CalcStat("ClassBaseICPR",L)
						    elif SN > 'BURGLARCDCALCTYPECOMPHYMIT':
							    if SN < 'BURGLARCDMIGHTTOFINESSE':
								    if SN < 'BURGLARCDFATETOPOWER':
									    if SN < 'BURGLARCDCALCTYPETACMIT':
										    if SN == 'BURGLARCDCALCTYPENONPHYMIT':
										        Result = 13
									    elif SN > 'BURGLARCDCALCTYPETACMIT':
										    if SN == 'BURGLARCDFATETONCPR':
										        Result = 0.07
									    else:
									        Result = 26
								    elif SN > 'BURGLARCDFATETOPOWER':
									    if SN < 'BURGLARCDMIGHTTOCRITHIT':
										    if SN == 'BURGLARCDHASPOWER':
										        Result = 1
									    elif SN > 'BURGLARCDMIGHTTOCRITHIT':
										    if SN == 'BURGLARCDMIGHTTOEVADE':
										        Result = 1
									    else:
									        Result = 1.5
								    else:
								        Result = 1
							    elif SN > 'BURGLARCDMIGHTTOFINESSE':
								    if SN < 'BURGLARCDPHYMITTONONPHYMIT':
									    if SN < 'BURGLARCDMIGHTTOPHYMAS':
										    if SN == 'BURGLARCDMIGHTTOOUTHEAL':
										        Result = 2
									    elif SN > 'BURGLARCDMIGHTTOPHYMAS':
										    if SN == 'BURGLARCDPHYMITTOCOMPHYMIT':
										        Result = 1
									    else:
									        Result = 2
								    elif SN > 'BURGLARCDPHYMITTONONPHYMIT':
									    if SN < 'BURGLARCDVITALITYTOICMR':
										    if SN == 'BURGLARCDTACMASTOOUTHEAL':
										        Result = 1
									    elif SN > 'BURGLARCDVITALITYTOICMR':
										    if SN == 'BURGLARCDVITALITYTOMORALE':
										        Result = 4.5
									    else:
									        Result = 0.012
								    else:
								        Result = 1
							    else:
							        Result = 1.5
						    else:
						        Result = 13
					    else:
					        Result = 1
				    elif SN > 'BURGLARCDVITALITYTONCMR':
					    if SN < 'CAPTAINCDFATETONCPR':
						    if SN < 'CAPTAINCDARMOURTYPE':
							    if SN < 'CAPTAINCDAGILITYTOCRITHIT':
								    if SN < 'BURGLARCDWILLTOPHYMAS':
									    if SN < 'BURGLARCDWILLTOFINESSE':
										    if SN == 'BURGLARCDWILLTOCRITHIT':
										        Result = 0.5
									    elif SN > 'BURGLARCDWILLTOFINESSE':
										    if SN == 'BURGLARCDWILLTOOUTHEAL':
										        Result = 2
									    else:
									        Result = 1.5
								    elif SN > 'BURGLARCDWILLTOPHYMAS':
									    if SN < 'BURGLARCDWILLTORESIST':
										    if SN == 'BURGLARCDWILLTOPHYMIT':
										        Result = 1
									    elif SN > 'BURGLARCDWILLTORESIST':
										    if SN == 'C':
										        Result = C
									    else:
									        Result = 1
								    else:
								        Result = 2
							    elif SN > 'CAPTAINCDAGILITYTOCRITHIT':
								    if SN < 'CAPTAINCDAGILITYTOTACMAS':
									    if SN < 'CAPTAINCDAGILITYTOPARRY':
										    if SN == 'CAPTAINCDAGILITYTOFINESSE':
										        Result = 1
									    elif SN > 'CAPTAINCDAGILITYTOPARRY':
										    if SN == 'CAPTAINCDAGILITYTOPHYMAS':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'CAPTAINCDAGILITYTOTACMAS':
									    if SN < 'CAPTAINCDARMOURTONONPHYMIT':
										    if SN == 'CAPTAINCDARMOURTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'CAPTAINCDARMOURTONONPHYMIT':
										    if SN == 'CAPTAINCDARMOURTOTACMIT':
										        Result = 0.2
									    else:
									        Result = 0.2
								    else:
								        Result = 2
							    else:
							        Result = 2
						    elif SN > 'CAPTAINCDARMOURTYPE':
							    if SN < 'CAPTAINCDBASENCPR':
								    if SN < 'CAPTAINCDBASEICPR':
									    if SN < 'CAPTAINCDBASEFATE':
										    if SN == 'CAPTAINCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityL",L)
									    elif SN > 'CAPTAINCDBASEFATE':
										    if SN == 'CAPTAINCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRM",L)
									    else:
									        Result = CalcStat("ClassBaseFate",L)
								    elif SN > 'CAPTAINCDBASEICPR':
									    if SN < 'CAPTAINCDBASEMORALE':
										    if SN == 'CAPTAINCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightH",L)
									    elif SN > 'CAPTAINCDBASEMORALE':
										    if SN == 'CAPTAINCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRM",L)
									    else:
									        Result = CalcStat("ClassBaseMorale",L)
								    else:
								        Result = CalcStat("ClassBaseICPR",L)
							    elif SN > 'CAPTAINCDBASENCPR':
								    if SN < 'CAPTAINCDCALCTYPECOMPHYMIT':
									    if SN < 'CAPTAINCDBASEVITALITY':
										    if SN == 'CAPTAINCDBASEPOWER':
										        Result = CalcStat("ClassBasePower",L)
									    elif SN > 'CAPTAINCDBASEVITALITY':
										    if SN == 'CAPTAINCDBASEWILL':
										        Result = CalcStat("ClassBaseWillM",L)
									    else:
									        Result = CalcStat("ClassBaseVitality",L)
								    elif SN > 'CAPTAINCDCALCTYPECOMPHYMIT':
									    if SN < 'CAPTAINCDCALCTYPETACMIT':
										    if SN == 'CAPTAINCDCALCTYPENONPHYMIT':
										        Result = 14
									    elif SN > 'CAPTAINCDCALCTYPETACMIT':
										    if SN == 'CAPTAINCDCANBLOCK':
										        if 15 <= Lp:
										            Result = 1
									    else:
									        Result = 27
								    else:
								        Result = 14
							    else:
							        Result = CalcStat("ClassBaseNCPR",L)
						    else:
						        Result = 3
					    elif SN > 'CAPTAINCDFATETONCPR':
						    if SN < 'CAPTAINCDWILLTOFINESSE':
							    if SN < 'CAPTAINCDMIGHTTOTACMAS':
								    if SN < 'CAPTAINCDMIGHTTOCRITHIT':
									    if SN < 'CAPTAINCDHASPOWER':
										    if SN == 'CAPTAINCDFATETOPOWER':
										        Result = 1
									    elif SN > 'CAPTAINCDHASPOWER':
										    if SN == 'CAPTAINCDMIGHTTOBLOCK':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'CAPTAINCDMIGHTTOCRITHIT':
									    if SN < 'CAPTAINCDMIGHTTOPHYMAS':
										    if SN == 'CAPTAINCDMIGHTTOPARRY':
										        Result = 1
									    elif SN > 'CAPTAINCDMIGHTTOPHYMAS':
										    if SN == 'CAPTAINCDMIGHTTOPHYMIT':
										        Result = 1
									    else:
									        Result = 3
								    else:
								        Result = 1
							    elif SN > 'CAPTAINCDMIGHTTOTACMAS':
								    if SN < 'CAPTAINCDTACMASTOOUTHEAL':
									    if SN < 'CAPTAINCDPHYMITTOCOMPHYMIT':
										    if SN == 'CAPTAINCDMIGHTTOTACMIT':
										        Result = 1
									    elif SN > 'CAPTAINCDPHYMITTOCOMPHYMIT':
										    if SN == 'CAPTAINCDPHYMITTONONPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'CAPTAINCDTACMASTOOUTHEAL':
									    if SN < 'CAPTAINCDVITALITYTOMORALE':
										    if SN == 'CAPTAINCDVITALITYTOICMR':
										        Result = 0.012
									    elif SN > 'CAPTAINCDVITALITYTOMORALE':
										    if SN == 'CAPTAINCDVITALITYTONCMR':
										        Result = 0.12
									    else:
									        Result = 4.5
								    else:
								        Result = 1
							    else:
							        Result = 3
						    elif SN > 'CAPTAINCDWILLTOFINESSE':
							    if SN < 'CHAMPIONCDAGILITYTOOUTHEAL':
								    if SN < 'CAPTAINCDWILLTOTACMAS':
									    if SN < 'CAPTAINCDWILLTOPHYMIT':
										    if SN == 'CAPTAINCDWILLTOPHYMAS':
										        Result = 1
									    elif SN > 'CAPTAINCDWILLTOPHYMIT':
										    if SN == 'CAPTAINCDWILLTORESIST':
										        Result = 1
									    else:
									        Result = 1.5
								    elif SN > 'CAPTAINCDWILLTOTACMAS':
									    if SN < 'CHAMPIONCDAGILITYTOCRITHIT':
										    if SN == 'CAPTAINCDWILLTOTACMIT':
										        Result = 1.5
									    elif SN > 'CHAMPIONCDAGILITYTOCRITHIT':
										    if SN == 'CHAMPIONCDAGILITYTOFINESSE':
										        Result = 1
									    else:
									        Result = 2
								    else:
								        Result = 1
							    elif SN > 'CHAMPIONCDAGILITYTOOUTHEAL':
								    if SN < 'CHAMPIONCDARMOURTONONPHYMIT':
									    if SN < 'CHAMPIONCDAGILITYTOPHYMAS':
										    if SN == 'CHAMPIONCDAGILITYTOPARRY':
										        Result = 1
									    elif SN > 'CHAMPIONCDAGILITYTOPHYMAS':
										    if SN == 'CHAMPIONCDARMOURTOCOMPHYMIT':
										        Result = 1
									    else:
									        Result = 2
								    elif SN > 'CHAMPIONCDARMOURTONONPHYMIT':
									    if SN < 'CHAMPIONCDARMOURTYPE':
										    if SN == 'CHAMPIONCDARMOURTOTACMIT':
										        Result = 0.2
									    elif SN > 'CHAMPIONCDARMOURTYPE':
										    if SN > 'CHAMPIONCDBASEAGILITY':
											    if SN == 'CHAMPIONCDBASEFATE':
											        Result = CalcStat("ClassBaseFate",L)
										    elif SN == 'CHAMPIONCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityM",L)
									    else:
									        Result = 3
								    else:
								        Result = 0.2
							    else:
							        Result = 2
						    else:
						        Result = 1
					    else:
					        Result = 0.07
				    else:
				        Result = 0.12
			    elif SN > 'CHAMPIONCDBASEICMR':
				    if SN < 'CLASSBASENCMRH':
					    if SN < 'CHAMPIONCDWILLTORESIST':
						    if SN < 'CHAMPIONCDMIGHTTOCRITHIT':
							    if SN < 'CHAMPIONCDBASEWILL':
								    if SN < 'CHAMPIONCDBASENCMR':
									    if SN < 'CHAMPIONCDBASEMIGHT':
										    if SN == 'CHAMPIONCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    elif SN > 'CHAMPIONCDBASEMIGHT':
										    if SN == 'CHAMPIONCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    else:
									        Result = CalcStat("ClassBaseMightH",L)
								    elif SN > 'CHAMPIONCDBASENCMR':
									    if SN < 'CHAMPIONCDBASEPOWER':
										    if SN == 'CHAMPIONCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    elif SN > 'CHAMPIONCDBASEPOWER':
										    if SN == 'CHAMPIONCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    else:
									        Result = CalcStat("ClassBasePower",L)
								    else:
								        Result = CalcStat("ClassBaseNCMRH",L)
							    elif SN > 'CHAMPIONCDBASEWILL':
								    if SN < 'CHAMPIONCDCANBLOCK':
									    if SN < 'CHAMPIONCDCALCTYPENONPHYMIT':
										    if SN == 'CHAMPIONCDCALCTYPECOMPHYMIT':
										        Result = 14
									    elif SN > 'CHAMPIONCDCALCTYPENONPHYMIT':
										    if SN == 'CHAMPIONCDCALCTYPETACMIT':
										        Result = 27
									    else:
									        Result = 14
								    elif SN > 'CHAMPIONCDCANBLOCK':
									    if SN < 'CHAMPIONCDFATETOPOWER':
										    if SN == 'CHAMPIONCDFATETONCPR':
										        Result = 0.07
									    elif SN > 'CHAMPIONCDFATETOPOWER':
										    if SN == 'CHAMPIONCDHASPOWER':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        if 6 <= Lp:
								            Result = 1
							    else:
							        Result = CalcStat("ClassBaseWillL",L)
						    elif SN > 'CHAMPIONCDMIGHTTOCRITHIT':
							    if SN < 'CHAMPIONCDTACMASTOOUTHEAL':
								    if SN < 'CHAMPIONCDMIGHTTOPHYMIT':
									    if SN < 'CHAMPIONCDMIGHTTOPARRY':
										    if SN == 'CHAMPIONCDMIGHTTOOUTHEAL':
										        Result = 3
									    elif SN > 'CHAMPIONCDMIGHTTOPARRY':
										    if SN == 'CHAMPIONCDMIGHTTOPHYMAS':
										        Result = 3
									    else:
									        Result = 3
								    elif SN > 'CHAMPIONCDMIGHTTOPHYMIT':
									    if SN < 'CHAMPIONCDPHYMITTOCOMPHYMIT':
										    if SN == 'CHAMPIONCDMIGHTTOTACMIT':
										        Result = 1
									    elif SN > 'CHAMPIONCDPHYMITTOCOMPHYMIT':
										    if SN == 'CHAMPIONCDPHYMITTONONPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'CHAMPIONCDTACMASTOOUTHEAL':
								    if SN < 'CHAMPIONCDWILLTOFINESSE':
									    if SN < 'CHAMPIONCDVITALITYTOMORALE':
										    if SN == 'CHAMPIONCDVITALITYTOICMR':
										        Result = 0.012
									    elif SN > 'CHAMPIONCDVITALITYTOMORALE':
										    if SN == 'CHAMPIONCDVITALITYTONCMR':
										        Result = 0.12
									    else:
									        Result = 4.5
								    elif SN > 'CHAMPIONCDWILLTOFINESSE':
									    if SN < 'CHAMPIONCDWILLTOPHYMAS':
										    if SN == 'CHAMPIONCDWILLTOOUTHEAL':
										        Result = 1
									    elif SN > 'CHAMPIONCDWILLTOPHYMAS':
										    if SN == 'CHAMPIONCDWILLTOPHYMIT':
										        Result = 1.5
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = 1
						    else:
						        Result = 1
					    elif SN > 'CHAMPIONCDWILLTORESIST':
						    if SN < 'CHPSTALWBLADEVITALITY':
							    if SN < 'CHISELCRITHITHOLD':
								    if SN < 'CHICKENCDCALCTYPENONPHYMIT':
									    if SN < 'CHICKENCANBLOCK':
										    if SN == 'CHAMPIONCDWILLTOTACMIT':
										        Result = 1.5
									    elif SN > 'CHICKENCANBLOCK':
										    if SN == 'CHICKENCDCALCTYPECOMPHYMIT':
										        Result = 14
									    else:
									        Result = 1
								    elif SN > 'CHICKENCDCALCTYPENONPHYMIT':
									    if SN < 'CHICKENCDHASPOWER':
										    if SN == 'CHICKENCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'CHICKENCDHASPOWER':
										    if SN == 'CHISELCRITHITH':
										        if Lm <= 140:
										            Result = CalcStat("U371LegacyStatFix",L,"ChiselCritHitHOld")
										        else:
										            Result = CalcStat("ChiselCritHitH",140)
									    else:
									        Result = 1
								    else:
								        Result = 14
							    elif SN > 'CHISELCRITHITHOLD':
								    if SN < 'CHPCONTRBURNICPR':
									    if SN < 'CHISELCRITHITLOLD':
										    if SN == 'CHISELCRITHITL':
										        if Lm <= 140:
										            Result = CalcStat("U371LegacyStatFix",L,"ChiselCritHitLOld")
										        else:
										            Result = CalcStat("ChiselCritHitL",140)
									    elif SN > 'CHISELCRITHITLOLD':
										    if SN == 'CHP2HWPNBLOCK':
										        Result = CalcStat("BlockT",L,4)
									    else:
									        if Lm <= 105:
									            Result = RoundDbl(16.16*L)
									        else:
									            Result = CalcStat("ProgExtHighLinExpRnd",L,CalcStat("ChiselCritHitLOld",105))
								    elif SN > 'CHPCONTRBURNICPR':
									    if SN < 'CHPFLURRYINCRCRITHIT':
										    if SN == 'CHPFINESSEINCREASE':
										        Result = CalcStat("FinesseT",L,CalcStat("Trait12345Choice",N)*0.4)
									    elif SN > 'CHPFLURRYINCRCRITHIT':
										    if SN == 'CHPMIGHTINCREASE':
										        Result = CalcStat("MightT",L,CalcStat("Trait567810Choice",N)*0.4)
									    else:
									        Result = CalcStat("CritHitT",L,2.4)
								    else:
								        Result = CalcStat("ICPRT",L,0.4)
							    else:
							        if Lm <= 105:
							            Result = RoundDbl(24.24*L)
							        else:
							            Result = CalcStat("ProgExtHighLinExpRnd",L,CalcStat("ChiselCritHitHOld",105))
						    elif SN > 'CHPSTALWBLADEVITALITY':
							    if SN < 'CLASSBASEICMRL':
								    if SN < 'CLASSBASEAGILITYL':
									    if SN < 'CHPUNBREAKTIERPTS':
										    if SN == 'CHPUNBREAKTACMIT':
										        Result = CalcStat("TacMitT",L,CalcStat("ChpUnbreakTierPts",N))
									    elif SN > 'CHPUNBREAKTIERPTS':
										    if SN == 'CLASSBASEAGILITYH':
										        Result = CalcStat("BaseAgility",L,1.5)
									    else:
									        if 1 <= Lp and Lm <= 10:
									            Result = 0.4*L
								    elif SN > 'CLASSBASEAGILITYL':
									    if SN < 'CLASSBASEFATE':
										    if SN == 'CLASSBASEAGILITYM':
										        Result = CalcStat("BaseAgility",L,1.0)
									    elif SN > 'CLASSBASEFATE':
										    if SN == 'CLASSBASEICMRH':
										        Result = EquSng(0.2)
									    else:
									        Result = CalcStat("BaseFate",L)
								    else:
								        Result = CalcStat("BaseAgility",L,0.5)
							    elif SN > 'CLASSBASEICMRL':
								    if SN < 'CLASSBASEMIGHTH':
									    if SN < 'CLASSBASEICPR':
										    if SN == 'CLASSBASEICMRM':
										        Result = EquSng(0.175)
									    elif SN > 'CLASSBASEICPR':
										    if SN == 'CLASSBASEICPRADJ':
										        if Lm <= 1:
										            Result = 1.5
										        elif Lm <= 20:
										            Result = 1.1
										        else:
										            Result = 1
									    else:
									        Result = EquSng(StatLinInter("PntMPClassBaseICPR","ClassBasePowerRegenPntS","ProgBICPR","ClassBaseICPRAdj",L,N,99))
								    elif SN > 'CLASSBASEMIGHTH':
									    if SN < 'CLASSBASEMIGHTM':
										    if SN == 'CLASSBASEMIGHTL':
										        Result = CalcStat("BaseMight",L,0.5)
									    elif SN > 'CLASSBASEMIGHTM':
										    if SN == 'CLASSBASEMORALE':
										        Result = CalcStat("BaseMorale",L)
									    else:
									        Result = CalcStat("BaseMight",L,1.0)
								    else:
								        Result = CalcStat("BaseMight",L,1.5)
							    else:
							        Result = EquSng(0.15)
						    else:
						        Result = CalcStat("VitalityT",L,CalcStat("Trait567810Choice",N)*0.4)
					    else:
					        Result = 1
				    elif SN > 'CLASSBASENCMRH':
					    if SN < 'COMBATDAMAGEMOD':
						    if SN < 'COMBATBASETACDPS':
							    if SN < 'CLASSBASEWILLH':
								    if SN < 'CLASSBASENCPRADJ':
									    if SN < 'CLASSBASENCMRM':
										    if SN == 'CLASSBASENCMRL':
										        Result = 1
									    elif SN > 'CLASSBASENCMRM':
										    if SN == 'CLASSBASENCPR':
										        Result = EquSng(StatLinInter("PntMPClassBaseNCPR","ClassBasePowerRegenPntS","ProgBNCPR","ClassBaseNCPRAdj",L,N,99))
									    else:
									        Result = 1
								    elif SN > 'CLASSBASENCPRADJ':
									    if SN < 'CLASSBASEPOWERREGENPNTS':
										    if SN == 'CLASSBASEPOWER':
										        Result = CalcStat("BasePower",L)
									    elif SN > 'CLASSBASEPOWERREGENPNTS':
										    if SN == 'CLASSBASEVITALITY':
										        Result = CalcStat("BaseVitality",L)
									    else:
									        Result = ((1,20,50,60,65,75,85,95,100,105,115,120,130,140,141,150),(1,20,50,60,65,75,85,95,100,105,115,120,130,140,141,150))
								    else:
								        if Lm <= 1:
								            Result = 1.5
								        elif Lm <= 20:
								            Result = 1.1
								        else:
								            Result = 1
							    elif SN > 'CLASSBASEWILLH':
								    if SN < 'CLOTHARMOUR':
									    if SN < 'CLASSBASEWILLM':
										    if SN == 'CLASSBASEWILLL':
										        Result = CalcStat("BaseWill",L,0.5)
									    elif SN > 'CLASSBASEWILLM':
										    if SN == 'CLASSNAME':
										        if 23 <= Lp and Lm <= 23:
										            Result = "Guardian"
										        elif 24 <= Lp and Lm <= 24:
										            Result = "Captain"
										        elif 31 <= Lp and Lm <= 31:
										            Result = "Minstrel"
										        elif 40 <= Lp and Lm <= 40:
										            Result = "Burglar"
										        elif 52 <= Lp and Lm <= 52:
										            Result = "Warleader"
										        elif 71 <= Lp and Lm <= 71:
										            Result = "Reaver"
										        elif 126 <= Lp and Lm <= 126:
										            Result = "Stalker"
										        elif 127 <= Lp and Lm <= 127:
										            Result = "Weaver"
										        elif 128 <= Lp and Lm <= 128:
										            Result = "Defiler"
										        elif 162 <= Lp and Lm <= 162:
										            Result = "Hunter"
										        elif 172 <= Lp and Lm <= 172:
										            Result = "Champion"
										        elif 179 <= Lp and Lm <= 179:
										            Result = "Blackarrow"
										        elif 185 <= Lp and Lm <= 185:
										            Result = "LoreMaster"
										        elif 192 <= Lp and Lm <= 192:
										            Result = "Chicken"
										        elif 193 <= Lp and Lm <= 193:
										            Result = "RuneKeeper"
										        elif 194 <= Lp and Lm <= 194:
										            Result = "Warden"
										        elif 214 <= Lp and Lm <= 214:
										            Result = "Beorning"
										        elif 215 <= Lp and Lm <= 215:
										            Result = "Brawler"
										        elif 216 <= Lp and Lm <= 216:
										            Result = "Mariner"
										        else:
										            Result = ""
									    else:
									        Result = CalcStat("BaseWill",L,1.0)
								    elif SN > 'CLOTHARMOUR':
									    if SN < 'COMBATBASEPHYDPS':
										    if SN == 'COMBATBASEDPSMINUSLOW':
										        Result = CalcStat("ProgBDamage",L)-CalcStat("ProgBDamage",50)
									    elif SN > 'COMBATBASEPHYDPS':
										    if SN == 'COMBATBASEPHYDPSITEMPNTS':
										        Result = ((1,50,60,65,75,125,175,200,222,300,301,350,351,400,401,450,451,500,501,550,551,600),(1,50,60,65,75,85,95,100,105,105,106,115,116,120,121,130,131,140,141,150,151,160))
									    else:
									        if Lm <= 600:
									            Result = StatLinInter("","CombatBasePhyDPSItemPntS","ProgBDamage","",L,N,99)
									        elif Lm <= 650:
									            Result = RoundDblDown(RoundDblUp((L-50)/5.5)*36.7-2811,-1)
									        else:
									            Result = CalcStat("CombatBasePhyDPS",650)
								    else:
								        if Lm <= 50:
								            Result = L
								        else:
								            Result = 50
							    else:
							        Result = CalcStat("BaseWill",L,1.5)
						    elif SN > 'COMBATBASETACDPS':
							    if SN < 'COMBATBASETACHPSCURVES':
								    if SN < 'COMBATBASETACDPSRAWITEMPNTS':
									    if SN < 'COMBATBASETACDPSNOCLASS':
										    if SN == 'COMBATBASETACDPSBYLEVEL':
										        if Lm <= 50:
										            Result = EquSng(CalcStat("ProgBDamage",L))
										        else:
										            Result = CalcStat("CombatBaseTacDPSByLevel",50)
									    elif SN > 'COMBATBASETACDPSNOCLASS':
										    if SN == 'COMBATBASETACDPSRAW':
										        if Lm <= 46:
										            Result = 0.5
										        elif Lm <= 50:
										            Result = LinFmod(1,0.5,0.8,47,50,L)
										        elif Lm <= 51:
										            Result = 1
										        elif Lm <= 599:
										            Result = StatLinInter("","CombatBaseTacDPSRawItemPntS","CombatBaseDPSMinusLow","",L,N,99)
										        elif Lm <= 649:
										            Result = RoundDblDown(RoundDblUp((L-49)/5.5)*36.7-2831,-1)
										        else:
										            Result = CalcStat("CombatBaseTacDPSRaw",649)
									    else:
									        if Lm <= 50:
									            Result = L
									        else:
									            Result = CalcStat("CombatBaseTacDPSNoClass",50)
								    elif SN > 'COMBATBASETACDPSRAWITEMPNTS':
									    if SN < 'COMBATBASETACHPSBYLEVEL':
										    if SN == 'COMBATBASETACHPS':
										        if Lm <= 56:
										            Result = EquSng(CalcStat("CombatBaseTacHPSRaw",L))
										        else:
										            Result = EquSng(DecSng(CalcStat("CombatBaseTacHPSRaw",L)))
									    elif SN > 'COMBATBASETACHPSBYLEVEL':
										    if SN == 'COMBATBASETACHPSBYLEVELRAW':
										        if Lm <= 46:
										            Result = CalcStat("CombatBaseTacHPSCurves",L)
										        else:
										            Result = CalcStat("CombatBaseTacHPSByLevelRaw",46)
									    else:
									        Result = EquSng(CalcStat("CombatBaseTacHPSByLevelRaw",L))
								    else:
								        Result = ((1,50,60,65,75,125,175,200,222,299,300,349,350,399,400,449,450,499,500,549,550,599),(1,50,60,65,75,85,95,100,105,105,106,115,116,120,121,130,131,140,141,150,151,160))
							    elif SN > 'COMBATBASETACHPSCURVES':
								    if SN < 'COMBATBASEWPNDPS':
									    if SN < 'COMBATBASETACHPSNOCLASS':
										    if SN == 'COMBATBASETACHPSLVLTOILVL':
										        if Lm <= 75:
										            Result = LinFmod(1,1,75,1,75,L)
										        elif Lm <= 100:
										            Result = LinFmod(1,75,200,75,100,L)
										        elif Lm <= 104:
										            Result = RoundDbl(LinFmod(1,201.3,214.3,101,104,L))
										        elif Lm <= 105:
										            Result = 222
										        else:
										            Result = RoundDbl(CalcStat("LvlToILvl",L))
									    elif SN > 'COMBATBASETACHPSNOCLASS':
										    if SN == 'COMBATBASETACHPSRAW':
										        if Lm <= 49:
										            Result = CalcStat("CombatBaseTacHPSCurves",L)-CalcStat("CombatBaseTacHPSByLevelRaw",L)
										        elif Lm <= 55:
										            Result = 0.5
										        elif Lm <= 599:
										            Result = CalcStat("CommonTacHPS",L)-CalcStat("CombatBaseTacHPSByLevelRaw",L)
										        elif Lm <= 649:
										            Result = (RoundDblUp((4*L+2)/22)*678-RoundDblUp((L+1)/22))*0.175-11734.1-CalcStat("CombatBaseTacHPSByLevelRaw",L)
										        else:
										            Result = CalcStat("CombatBaseTacHPSRaw",649)
									    else:
									        Result = EquSng(CalcStat("CombatBaseTacHPSByLevelRaw",L)+CalcStat("CombatBaseTacHPSRaw",CalcStat("CombatBaseTacHPSLvlToILvl",L)))
								    elif SN > 'COMBATBASEWPNDPS':
									    if SN < 'COMBATBASEWPNDPSCATTYPEMP':
										    if SN == 'COMBATBASEWPNDPSBASE':
										        Result = EquSng(DecSng(CalcStat("CombatBaseWpnDPSCatTypeMP",WpnCodeIndex(C,1)*4+WpnCodeIndex(C,2))*CalcStat("CombatBasePhyDPS",L)*1.08))
									    elif SN > 'COMBATBASEWPNDPSCATTYPEMP':
										    if SN == 'COMBATBASEWPNDPSQTYMP':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,1.02,1.04,1.08,1.12),L))
									    else:
									        if 9 <= Lp and Lm <= 9:
									            Result = 0.9
									        elif 5 <= Lp and Lm <= 5:
									            Result = 1
									        elif 10 <= Lp and Lm <= 11:
									            Result = 1.2
									        elif 6 <= Lp and Lm <= 7:
									            Result = 1.4
									        else:
									            Result = 1
								    else:
								        Result = EquSng(CalcStat("CombatBaseWpnDPSBase",L,C)*CalcStat("CombatBaseWpnDPSQtyMP",WpnCodeIndex(C,3)))
							    else:
							        if Lm <= 25:
							            Result = (13*L+85)*(81-L)/3920
							        else:
							            Result = (13*L+85)*(75-L)/3500
						    else:
						        Result = EquSng(DecSng(CalcStat("CombatBaseTacDPSRaw",L)))
					    elif SN > 'COMBATDAMAGEMOD':
						    if SN < 'COMBATDAMAGEMODPLAYERSADJ':
							    if SN < 'COMBATDAMAGEMODMPDMGADJ':
								    if SN < 'COMBATDAMAGEMODHEALTHLOWADJ':
									    if SN < 'COMBATDAMAGEMODHEALTHITEM':
										    if SN == 'COMBATDAMAGEMODENERGY':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBEnergy","",L,N,2))
									    elif SN > 'COMBATDAMAGEMODHEALTHITEM':
										    if SN == 'COMBATDAMAGEMODHEALTHLOW':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBHealth","CombatDamageModHealthLowAdj",L,N,99))
									    else:
									        Result = EquSng(StatLinInter("PntMPCombatDamageMod","ItemPntSClassic","ProgBHealth","",L,N,0))
								    elif SN > 'COMBATDAMAGEMODHEALTHLOWADJ':
									    if SN < 'COMBATDAMAGEMODHEALTHMEDIUMADJ':
										    if SN == 'COMBATDAMAGEMODHEALTHMEDIUM':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBHealth","CombatDamageModHealthMediumAdj",L,N,99))
									    elif SN > 'COMBATDAMAGEMODHEALTHMEDIUMADJ':
										    if SN == 'COMBATDAMAGEMODMPDMG':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","CombatDamageModMPDmgAdj",L,N,2))
									    else:
									        if Lm <= 1:
									            Result = 0.36
									        elif Lm <= 25:
									            Result = 0.54
									        elif Lm <= 50:
									            Result = 0.72
									        else:
									            Result = 0.9
								    else:
								        if Lm <= 1:
								            Result = 0.144
								        elif Lm <= 25:
								            Result = 0.324
								        elif Lm <= 50:
								            Result = 0.576
								        else:
								            Result = 0.9
							    elif SN > 'COMBATDAMAGEMODMPDMGADJ':
								    if SN < 'COMBATDAMAGEMODPETS':
									    if SN < 'COMBATDAMAGEMODMPHEALADJ':
										    if SN == 'COMBATDAMAGEMODMPHEAL':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBHealth","CombatDamageModMPHealAdj",L,N,2))
									    elif SN > 'COMBATDAMAGEMODMPHEALADJ':
										    if SN == 'COMBATDAMAGEMODNPCS':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","",L,N,99))
									    else:
									        if Lm <= 141:
									            Result = 1
									        else:
									            Result = 0.71
								    elif SN > 'COMBATDAMAGEMODPETS':
									    if SN < 'COMBATDAMAGEMODPETSRND':
										    if SN == 'COMBATDAMAGEMODPETSADJ':
										        if Lm <= 1:
										            Result = 1
										        elif Lm <= 25:
										            Result = 0.4
										        elif Lm <= 50:
										            Result = 0.5
										        elif Lm <= 60:
										            Result = 0.6
										        elif Lm <= 65:
										            Result = 0.7
										        elif Lm <= 75:
										            Result = 0.8
										        elif Lm <= 85:
										            Result = 0.85
										        elif Lm <= 95:
										            Result = 0.9
										        elif Lm <= 100:
										            Result = 0.95
										        else:
										            Result = 1
									    elif SN > 'COMBATDAMAGEMODPETSRND':
										    if SN == 'COMBATDAMAGEMODPLAYERS':
										        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","CombatDamageModPlayersAdj",L,N,99))
									    else:
									        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","CombatDamageModPetsAdj",L,N,2))
								    else:
								        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","CombatDamageModPetsAdj",L,N,99))
							    else:
							        if Lm <= 141:
							            Result = 1
							        else:
							            Result = 0.875
						    elif SN > 'COMBATDAMAGEMODPLAYERSADJ':
							    if SN < 'CPTCOVFATE':
								    if SN < 'CONSTSTATC':
									    if SN < 'COMMONTACHPS':
										    if SN == 'COMBATINHEAL':
										        Result = CalcStat("InHeal",L,2.0)
									    elif SN > 'COMMONTACHPS':
										    if SN == 'COMMONTACHPSITEMPNTS':
										        Result = ((1,50,60,65,75,125,175,200,222,299,300,349,350,399,400,449,450,499,500,549,550,599),(1,50,60,65,75,85,95,100,105,105,106,115,116,120,121,130,131,140,141,150,151,160))
									    else:
									        Result = StatLinInter("PntMPTacHPS","CommonTacHPSItemPntS","ProgBTacHPS","",L,N,99)
								    elif SN > 'CONSTSTATC':
									    if SN < 'CPTBLADEPHYMAS':
										    if SN == 'CPTBLADECRITDEF':
										        Result = CalcStat("CritDefT",L,0.8)
									    elif SN > 'CPTBLADEPHYMAS':
										    if SN == 'CPTBLADETACMAS':
										        Result = CalcStat("TacMasT",L,0.8)
									    else:
									        Result = CalcStat("PhyMasT",L,1.2)
								    else:
								        Result = CalcStat(C,1,L)
							    elif SN > 'CPTCOVFATE':
								    if SN < 'CPTCRITDEF':
									    if SN < 'CPTCOVPHYMIT':
										    if SN == 'CPTCOVMAIN':
										        Result = CalcStat("MainT",L,0.4)
									    elif SN > 'CPTCOVPHYMIT':
										    if SN == 'CPTCOVVITALITY':
										        Result = CalcStat("VitalityT",L,0.4)
									    else:
									        Result = CalcStat("PhyMitT",L,2.4)
								    elif SN > 'CPTCRITDEF':
									    if SN < 'CPTIDOMEMAIN':
										    if SN == 'CPTIDOMEFATE':
										        Result = CalcStat("FateT",L,0.4)
									    elif SN > 'CPTIDOMEMAIN':
										    if SN > 'CPTIDOMEVITALITY':
											    if SN == 'CPTSHIELDCRITDEF':
											        Result = CalcStat("CritDefT",L,1.2)
										    elif SN == 'CPTIDOMEVITALITY':
										        Result = CalcStat("VitalityT",L,0.4)
									    else:
									        Result = CalcStat("MainT",L,0.4)
								    else:
								        Result = CalcStat("CritDef",L,0.6)
							    else:
							        Result = CalcStat("FateT",L,0.4)
						    else:
						        if Lm <= 1:
						            Result = 0.8
						        elif Lm <= 25:
						            Result = 0.9
						        else:
						            Result = 1
					    else:
					        Result = EquSng(StatLinInter("PntMPCombatDamageMod","TraitPntSVital","ProgBDamageNoImp","",L,N,2))
				    else:
				        Result = 2
			    else:
			        Result = CalcStat("ClassBaseICMRH",L)
		    else:
		        Result = 0.12
	    elif SN > 'CPTSHIELDPHYMAS':
		    if SN < 'HNTCAMPFIRENCMR':
			    if SN < 'EVADEPRATP':
				    if SN < 'CRITMAGNPRATPCAP':
					    if SN < 'CRITDEFCI':
						    if SN < 'CREEPAUDACITYTACDMGP':
							    if SN < 'CREEPAUDACITYCOST':
								    if SN < 'CPTSONGTACMAS':
									    if SN < 'CPTSONGCRITDEF':
										    if SN == 'CPTSHIELDTACMAS':
										        Result = CalcStat("TacMasT",L,0.8)
									    elif SN > 'CPTSONGCRITDEF':
										    if SN == 'CPTSONGPHYMAS':
										        Result = CalcStat("PhyMasT",L,0.8)
									    else:
									        Result = CalcStat("CritDefT",L,0.8)
								    elif SN > 'CPTSONGTACMAS':
									    if SN < 'CPTSTANDALONETACMAS':
										    if SN == 'CPTSTANDALONEPHYMAS':
										        Result = CalcStat("PhyMasT",L,1.2)
									    elif SN > 'CPTSTANDALONETACMAS':
										    if SN == 'CREEPAUDACITYCCDP':
										        if 1 <= Lp and Lm <= 16:
										            Result = 0.5
										        elif 17 <= Lp and Lm <= 60:
										            Result = 0.4
									    else:
									        Result = CalcStat("TacMasT",L,0.8)
								    else:
								        Result = CalcStat("TacMasT",L,1.2)
							    elif SN > 'CREEPAUDACITYCOST':
								    if SN < 'CREEPAUDACITYMELREDP':
									    if SN < 'CREEPAUDACITYDMGP':
										    if SN == 'CREEPAUDACITYCOSTBASE':
										        if 1 <= Lp and Lm <= 2:
										            Result = 2*L
										        elif 3 <= Lp and Lm <= 9:
										            Result = 2*L-1
										        elif 10 <= Lp and Lm <= 15:
										            Result = 3*L
										        elif 16 <= Lp and Lm <= 25:
										            Result = 6*L
										        elif 26 <= Lp and Lm <= 29:
										            Result = 9*L
										        elif 30 <= Lp and Lm <= 36:
										            Result = 300
									    elif SN > 'CREEPAUDACITYDMGP':
										    if SN == 'CREEPAUDACITYMELDMGP':
										        Result = CalcStat("CreepAudacityDmgP",L)
									    else:
									        if 1 <= Lp and Lm <= 10:
									            Result = LinFmod(1,1,1.2,1,10,L)
									        elif 11 <= Lp and Lm <= 36:
									            Result = LinFmod(1,1.2,1.25,10,36,L)
									        elif 37 <= Lp and Lm <= 41:
									            Result = LinFmod(1,1.25,1.3,36,41,L)
									        elif 42 <= Lp and Lm <= 60:
									            Result = LinFmod(1,1.3,1.25,41,60,L)
								    elif SN > 'CREEPAUDACITYMELREDP':
									    if SN < 'CREEPAUDACITYRNGDMGP':
										    if SN == 'CREEPAUDACITYREDP':
										        if 1 <= Lp and Lm <= 10:
										            Result = LinFmod(1,0.5,0.5,1,10,L)
										        elif 11 <= Lp and Lm <= 36:
										            Result = LinFmod(1,0.5,0.5,10,36,L)
										        elif 37 <= Lp and Lm <= 41:
										            Result = LinFmod(1,0.5,0.5,36,41,L)
										        elif 42 <= Lp and Lm <= 60:
										            Result = LinFmod(1,0.5,0.5,41,60,L)
									    elif SN > 'CREEPAUDACITYRNGDMGP':
										    if SN == 'CREEPAUDACITYRNGREDP':
										        Result = CalcStat("CreepAudacityRedP",L)
									    else:
									        Result = CalcStat("CreepAudacityDmgP",L)
								    else:
								        Result = CalcStat("CreepAudacityRedP",L)
							    else:
							        Result = CalcStat("CreepAudacityCostBase",L)*25
						    elif SN > 'CREEPAUDACITYTACDMGP':
							    if SN < 'CREEPBATPROMTACDMGP':
								    if SN < 'CREEPBATPROMMELDMGP':
									    if SN < 'CREEPBATPROMDMGP':
										    if SN == 'CREEPAUDACITYTACREDP':
										        Result = CalcStat("CreepAudacityRedP",L)
									    elif SN > 'CREEPBATPROMDMGP':
										    if SN == 'CREEPBATPROMHEALTHP':
										        Result = CalcStat("CreepBatPromVitalP",L)
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = LinFmod(1,0.005,0.02,1,5,L)
									        elif 6 <= Lp and Lm <= 10:
									            Result = LinFmod(1,0.02,0.045,5,10,L)
									        elif 11 <= Lp and Lm <= 15:
									            Result = LinFmod(1,0.045,0.075,10,15,L)
								    elif SN > 'CREEPBATPROMMELDMGP':
									    if SN < 'CREEPBATPROMPOWERP':
										    if SN == 'CREEPBATPROMOUTHEALP':
										        if 1 <= Lp and Lm <= 5:
										            Result = LinFmod(1,0.02,0.1,1,5,L)
										        elif 6 <= Lp and Lm <= 10:
										            Result = LinFmod(1,0.1,0.15,5,10,L)
										        elif 11 <= Lp and Lm <= 15:
										            Result = LinFmod(1,0.15,0.2,10,15,L)
									    elif SN > 'CREEPBATPROMPOWERP':
										    if SN == 'CREEPBATPROMRNGDMGP':
										        Result = CalcStat("CreepBatPromDmgP",L)
									    else:
									        Result = CalcStat("CreepBatPromVitalP",L)
								    else:
								        Result = CalcStat("CreepBatPromDmgP",L)
							    elif SN > 'CREEPBATPROMTACDMGP':
								    if SN < 'CREEPTRAITPNTS':
									    if SN < 'CREEPILVLCURR':
										    if SN == 'CREEPBATPROMVITALP':
										        if 1 <= Lp and Lm <= 5:
										            Result = LinFmod(1,1.02,1.1,1,5,L)
										        elif 6 <= Lp and Lm <= 10:
										            Result = LinFmod(1,1.1,1.15,5,10,L)
										        elif 11 <= Lp and Lm <= 15:
										            Result = LinFmod(1,1.15,1.2,10,15,L)
									    elif SN > 'CREEPILVLCURR':
										    if SN == 'CREEPITEMPNTS':
										        Result = ((500,549),(141,150))
									    else:
									        Result = 525
								    elif SN > 'CREEPTRAITPNTS':
									    if SN < 'CRITDEF':
										    if SN == 'CREEPTRAITPROGB':
										        Result = LinFmod(1,0.01,1,1,CalcStat("LevelCap",L),L)
									    elif SN > 'CRITDEF':
										    if SN == 'CRITDEFC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("CritDefCI",CalcStat("CritDefCILvlFilter",N),N),0)
									    else:
									        Result = EquSng(StatLinInter("PntMPCritDef","ItemPntS","ProgBCritDef","AdjItem",L,N,0))
								    else:
								        Result = ((1,150),(1,150))
							    else:
							        Result = CalcStat("CreepBatPromDmgP",L)
						    else:
						        Result = CalcStat("CreepAudacityDmgP",L)
					    elif SN > 'CRITDEFCI':
						    if SN < 'CRITHITCIRAW':
							    if SN < 'CRITDEFPRATPC':
								    if SN < 'CRITDEFPPRAT':
									    if SN < 'CRITDEFCIRAW':
										    if SN == 'CRITDEFCILVLFILTER':
										        if 4 <= Lp and Lm <= 4 or 4.6 <= Lp and Lm <= 4.6 or 5.6 <= Lp and Lm <= 5.6 or 6.2 <= Lp and Lm <= 6.2 or 8.4 <= Lp and Lm <= 8.4 or 11.2 <= Lp and Lm <= 11.2 or 14 <= Lp and Lm <= 14:
										            Result = 515
										        elif 2.8 <= Lp and Lm <= 2.8:
										            Result = 520
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    elif SN > 'CRITDEFCIRAW':
										    if SN == 'CRITDEFCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("CritDefCIRaw",CalcStat("CritDefCILvlFilter",N),N),99)
									    else:
									        Result = StatLinInter("PntMPCritDefC","ItemPntS","ProgBCritDef","AdjCreepItem",L,N,4)
								    elif SN > 'CRITDEFPPRAT':
									    if SN < 'CRITDEFPRATPA':
										    if SN == 'CRITDEFPRATP':
										        Result = CalcPercAB(CalcStat("CritDefPRatPA",L),CalcStat("CritDefPRatPB",L),CalcStat("CritDefPRatPCap",L),N)
									    elif SN > 'CRITDEFPRATPA':
										    if SN == 'CRITDEFPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatStandard")
									    else:
									        Result = 240
								    else:
								        Result = CalcRatAB(CalcStat("CritDefPRatPA",L),CalcStat("CritDefPRatPB",L),CalcStat("CritDefPRatPCapR",L),N)
							    elif SN > 'CRITDEFPRATPC':
								    if SN < 'CRITHIT':
									    if SN < 'CRITDEFPRATPCAPR':
										    if SN == 'CRITDEFPRATPCAP':
										        Result = 80
									    elif SN > 'CRITDEFPRATPCAPR':
										    if SN == 'CRITDEFT':
										        Result = EquSng(StatLinInter("PntMPCritDef","TraitPntS","ProgBCritDef","AdjTrait",L,N,0))
									    else:
									        Result = CalcStat("CritDefPRatPB",L)*CalcStat("CritDefPRatPC",L)
								    elif SN > 'CRITHIT':
									    if SN < 'CRITHITCI':
										    if SN == 'CRITHITC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("CritHitCI",CalcStat("CritHitCILvlFilter",N),N),0)
									    elif SN > 'CRITHITCI':
										    if SN == 'CRITHITCILVLFILTER':
										        if 2.2 <= Lp and Lm <= 2.2 or 3.8 <= Lp and Lm <= 3.8 or 4.6 <= Lp and Lm <= 4.6 or 5.2 <= Lp and Lm <= 5.2 or 10.4 <= Lp and Lm <= 10.4 or 15.6 <= Lp and Lm <= 15.6:
										            Result = 515
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    else:
									        Result = RoundDblLotro(CalcStat("CritHitCIRaw",L,N))
								    else:
								        Result = EquSng(StatLinInter("PntMPCritHit","ItemPntS","ProgBCritHit","AdjItem",L,N,0))
							    else:
							        Result = 0.5
						    elif SN > 'CRITHITCIRAW':
							    if SN < 'CRITHITPRATPCAP':
								    if SN < 'CRITHITPRATP':
									    if SN < 'CRITHITOLD':
										    if SN == 'CRITHITCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("CritHitCIRaw",CalcStat("CritHitCILvlFilter",N),N),99)
									    elif SN > 'CRITHITOLD':
										    if SN == 'CRITHITPPRAT':
										        Result = CalcRatAB(CalcStat("CritHitPRatPA",L),CalcStat("CritHitPRatPB",L),CalcStat("CritHitPRatPCapR",L),N)
									    else:
									        Result = CalcStat("CritHit",L,N)
								    elif SN > 'CRITHITPRATP':
									    if SN < 'CRITHITPRATPB':
										    if SN == 'CRITHITPRATPA':
										        Result = 75
									    elif SN > 'CRITHITPRATPB':
										    if SN == 'CRITHITPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatExtra")
								    else:
								        Result = CalcPercAB(CalcStat("CritHitPRatPA",L),CalcStat("CritHitPRatPB",L),CalcStat("CritHitPRatPCap",L),N)
							    elif SN > 'CRITHITPRATPCAP':
								    if SN < 'CRITMAGNPRATP':
									    if SN < 'CRITHITT':
										    if SN == 'CRITHITPRATPCAPR':
										        Result = CalcStat("CritHitPRatPB",L)*CalcStat("CritHitPRatPC",L)
									    elif SN > 'CRITHITT':
										    if SN == 'CRITMAGNPPRAT':
										        Result = CalcRatAB(CalcStat("CritMagnPRatPA",L),CalcStat("CritMagnPRatPB",L),CalcStat("CritMagnPRatPCapR",L),N)
									    else:
									        Result = EquSng(StatLinInter("PntMPCritHit","TraitPntS","ProgBCritHit","AdjTrait",L,N,0))
								    elif SN > 'CRITMAGNPRATP':
									    if SN < 'CRITMAGNPRATPB':
										    if SN == 'CRITMAGNPRATPA':
										        Result = 225
									    elif SN > 'CRITMAGNPRATPB':
										    if SN == 'CRITMAGNPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatCritMagn")
								    else:
								        Result = CalcPercAB(CalcStat("CritMagnPRatPA",L),CalcStat("CritMagnPRatPB",L),CalcStat("CritMagnPRatPCap",L),N)
							    else:
							        Result = 25
						    else:
						        Result = StatLinInter("PntMPCritHitC","ItemPntS","ProgBCritHit","AdjCreepItem",L,N,4)
					    else:
					        Result = RoundDblLotro(CalcStat("CritDefCIRaw",L,N))
				    elif SN > 'CRITMAGNPRATPCAP':
					    if SN < 'DWARFRDTRAITNCMR':
						    if SN < 'DISEASERESIST':
							    if SN < 'DEFILERCDHASPOWER':
								    if SN < 'DEFILERCANBLOCK':
									    if SN < 'CRYRESIST':
										    if SN == 'CRITMAGNPRATPCAPR':
										        Result = CalcStat("CritMagnPRatPB",L)*CalcStat("CritMagnPRatPC",L)
									    elif SN > 'CRYRESIST':
										    if SN == 'CRYRESISTT':
										        Result = CalcStat("ResistAddT",L,N)
									    else:
									        Result = CalcStat("ResistAdd",L,N)
								    elif SN > 'DEFILERCANBLOCK':
									    if SN < 'DEFILERCDCALCTYPENONPHYMIT':
										    if SN == 'DEFILERCDCALCTYPECOMPHYMIT':
										        Result = 13
									    elif SN > 'DEFILERCDCALCTYPENONPHYMIT':
										    if SN == 'DEFILERCDCALCTYPETACMIT':
										        Result = 27
									    else:
									        Result = 14
								    else:
								        Result = 1
							    elif SN > 'DEFILERCDHASPOWER':
								    if SN < 'DEVHITPRATPB':
									    if SN < 'DEVHITPRATP':
										    if SN == 'DEVHITPPRAT':
										        Result = CalcRatAB(CalcStat("DevHitPRatPA",L),CalcStat("DevHitPRatPB",L),CalcStat("DevHitPRatPCapR",L),N)
									    elif SN > 'DEVHITPRATP':
										    if SN == 'DEVHITPRATPA':
										        Result = 30
									    else:
									        Result = CalcPercAB(CalcStat("DevHitPRatPA",L),CalcStat("DevHitPRatPB",L),CalcStat("DevHitPRatPCap",L),N)
								    elif SN > 'DEVHITPRATPB':
									    if SN < 'DEVHITPRATPCAP':
										    if SN == 'DEVHITPRATPC':
										        Result = 0.5
									    elif SN > 'DEVHITPRATPCAP':
										    if SN == 'DEVHITPRATPCAPR':
										        Result = CalcStat("DevHitPRatPB",L)*CalcStat("DevHitPRatPC",L)
									    else:
									        Result = 10
								    else:
								        Result = CalcStat("BRatRounded",L,"BRatDevHit")
							    else:
							        Result = 1
						    elif SN > 'DISEASERESIST':
							    if SN < 'DWARFRDPSVONENAME':
								    if SN < 'DWARFENDURVITALITY':
									    if SN < 'DMGTYPEMIT':
										    if SN == 'DISEASERESISTT':
										        Result = CalcStat("ResistAddT",L,N)
									    elif SN > 'DMGTYPEMIT':
										    if SN == 'DMGTYPEMITT':
										        Result = EquSng(StatLinInter("PntMPDmgTypeMitT","TraitPntS","ProgBMitigation","AdjTraitMit",L,N,0))
									    else:
									        Result = EquSng(StatLinInter("PntMPDmgTypeMit","ItemPntS","ProgBMitigation","AdjItemMit",L,N,0))
								    elif SN > 'DWARFENDURVITALITY':
									    if SN < 'DWARFLOSTDWARFKDSFATE':
										    if SN == 'DWARFFATEFULDWARFFATE':
										        Result = CalcStat("FateT",L,1.0)
									    elif SN > 'DWARFLOSTDWARFKDSFATE':
										    if SN == 'DWARFRDPSVONEFATE':
										        Result = CalcStat("DwarfFatefulDwarfFate",L)
									    else:
									        Result = -CalcStat("FateT",L,0.4)
								    else:
								        Result = CalcStat("VitalityT",L,1.0)
							    elif SN > 'DWARFRDPSVONENAME':
								    if SN < 'DWARFRDTRAITFATE':
									    if SN < 'DWARFRDPSVTWONAME':
										    if SN == 'DWARFRDPSVTWOBLOCK':
										        Result = CalcStat("DwarfShieldBrwlBlock",L)
									    elif SN > 'DWARFRDPSVTWONAME':
										    if SN == 'DWARFRDTRAITAGILITY':
										        Result = CalcStat("DwarfStockyAgility",L)
									    else:
									        Result = "Shield Brawler"
								    elif SN > 'DWARFRDTRAITFATE':
									    if SN < 'DWARFRDTRAITICPR':
										    if SN == 'DWARFRDTRAITICMR':
										        Result = CalcStat("DwarfUnwearBattleICMR",L)
									    elif SN > 'DWARFRDTRAITICPR':
										    if SN == 'DWARFRDTRAITMIGHT':
										        Result = CalcStat("DwarfSturdinessMight",L)
									    else:
									        Result = CalcStat("DwarfUnwearBattleICPR",L)
								    else:
								        Result = CalcStat("DwarfLostDwarfKdsFate",L)
							    else:
							        Result = "Fateful Dwarf"
						    else:
						        Result = CalcStat("ResistAdd",L,N)
					    elif SN > 'DWARFRDTRAITNCMR':
						    if SN < 'ELFRDPSVONEFATE':
							    if SN < 'DWARFSTURDINESSVITALITY':
								    if SN < 'DWARFSHIELDBRWLBLOCK':
									    if SN < 'DWARFRDTRAITPHYMITP':
										    if SN == 'DWARFRDTRAITNCPR':
										        Result = CalcStat("DwarfUnwearBattleNCPR",L)
									    elif SN > 'DWARFRDTRAITPHYMITP':
										    if SN == 'DWARFRDTRAITVITALITY':
										        Result = CalcStat("DwarfSturdinessVitality",L)
									    else:
									        Result = CalcStat("DwarfSturdinessPhyMitP",L)
								    elif SN > 'DWARFSHIELDBRWLBLOCK':
									    if SN < 'DWARFSTURDINESSMIGHT':
										    if SN == 'DWARFSTOCKYAGILITY':
										        Result = -CalcStat("AgilityT",L,0.4)
									    elif SN > 'DWARFSTURDINESSMIGHT':
										    if SN == 'DWARFSTURDINESSPHYMITP':
										        Result = 1
									    else:
									        Result = CalcStat("MightT",L,1.0)
								    else:
								        Result = CalcStat("BlockT",L,0.8)
							    elif SN > 'DWARFSTURDINESSVITALITY':
								    if SN < 'DWARFUNWEARBATTLENCPR':
									    if SN < 'DWARFUNWEARBATTLEICPR':
										    if SN == 'DWARFUNWEARBATTLEICMR':
										        Result = CalcStat("ICMRT",L,0.6)
									    elif SN > 'DWARFUNWEARBATTLEICPR':
										    if SN == 'DWARFUNWEARBATTLENCMR':
										        Result = -CalcStat("NCMRT",L,0.4)
									    else:
									        Result = CalcStat("ICPRT",L,0.6)
								    elif SN > 'DWARFUNWEARBATTLENCPR':
									    if SN < 'ELFFADINGFIRSTBORNFATE':
										    if SN == 'ELFAGILITYWOODSAGILITY':
										        Result = CalcStat("AgilityT",L,1.0)
									    elif SN > 'ELFFADINGFIRSTBORNFATE':
										    if SN == 'ELFFRIENDOFMANFATE':
										        Result = CalcStat("FateT",L,1.0)
									    else:
									        Result = -CalcStat("FateT",L,0.4)
								    else:
								        Result = -CalcStat("NCPRT",L,0.4)
							    else:
							        Result = CalcStat("VitalityT",L,1.0)
						    elif SN > 'ELFRDPSVONEFATE':
							    if SN < 'ELFSORROWFIRSTBORNNCMR':
								    if SN < 'ELFRDTRAITFATE':
									    if SN < 'ELFRDPSVTWONAME':
										    if SN == 'ELFRDPSVONENAME':
										        Result = "Friend Of Man"
									    elif SN > 'ELFRDPSVTWONAME':
										    if SN == 'ELFRDTRAITAGILITY':
										        Result = CalcStat("ElfAgilityWoodsAgility",L)
									    else:
									        Result = ""
								    elif SN > 'ELFRDTRAITFATE':
									    if SN < 'ELFRDTRAITNCMR':
										    if SN == 'ELFRDTRAITMORALE':
										        Result = CalcStat("ElfSorrowFirstbornMorale",L)
									    elif SN > 'ELFRDTRAITNCMR':
										    if SN == 'ELFSORROWFIRSTBORNMORALE':
										        Result = -CalcStat("MoraleT",L,0.4)
									    else:
									        Result = CalcStat("ElfSorrowFirstbornNCMR",L)
								    else:
								        Result = CalcStat("ElfFadingFirstbornFate",L)
							    elif SN > 'ELFSORROWFIRSTBORNNCMR':
								    if SN < 'EVADECIRAW':
									    if SN < 'EVADEC':
										    if SN == 'EVADE':
										        Result = CalcStat("BPE",L,N)
									    elif SN > 'EVADEC':
										    if SN == 'EVADECI':
										        Result = CalcStat("BPECI",L,N)
									    else:
									        Result = CalcStat("BPEC",L,N)
								    elif SN > 'EVADECIRAW':
									    if SN < 'EVADEPBONUS':
										    if SN == 'EVADECRAW':
										        Result = CalcStat("BPECRAW",L,N)
									    elif SN > 'EVADEPBONUS':
										    if SN == 'EVADEPPRAT':
										        Result = CalcStat("BPEPPRat",L,N)
									    else:
									        Result = CalcStat("BPEPBonus",L)
								    else:
								        Result = CalcStat("BPECIRAW",L,N)
							    else:
							        Result = -CalcStat("NCMRT",L,0.4)
						    else:
						        Result = CalcStat("ElfFriendOfManFate",L)
					    else:
					        Result = CalcStat("DwarfUnwearBattleNCMR",L)
				    else:
				        Result = 75
			    elif SN > 'EVADEPRATP':
				    if SN < 'GRDTENDERIZET4CRITHIT':
					    if SN < 'FOODNCMRM':
						    if SN < 'FINESSECILVLFILTER':
							    if SN < 'FATEC':
								    if SN < 'EVADEPRATPCAP':
									    if SN < 'EVADEPRATPB':
										    if SN == 'EVADEPRATPA':
										        Result = CalcStat("BPEPRatPA",L)
									    elif SN > 'EVADEPRATPB':
										    if SN == 'EVADEPRATPC':
										        Result = CalcStat("BPEPRatPC",L)
									    else:
									        Result = CalcStat("BPEPRatPB",L)
								    elif SN > 'EVADEPRATPCAP':
									    if SN < 'EVADET':
										    if SN == 'EVADEPRATPCAPR':
										        Result = CalcStat("BPEPRatPCapR",L)
									    elif SN > 'EVADET':
										    if SN == 'FATE':
										        Result = RoundDblDown(StatLinInter("PntMPFate","ItemPntSVital","ProgBFate","",L,N,0))
									    else:
									        Result = CalcStat("BPET",L,N)
								    else:
								        Result = CalcStat("BPEPRatPCap",L)
							    elif SN > 'FATEC':
								    if SN < 'FEARRESISTT':
									    if SN < 'FATET':
										    if SN == 'FATECI':
										        Result = CalcStat("MainCI",L,N)
									    elif SN > 'FATET':
										    if SN == 'FEARRESIST':
										        Result = CalcStat("ResistAdd",L,N)
									    else:
									        Result = RoundDblDown(StatLinInter("PntMPFate","TraitPntSVital","ProgBFate","",L,N,0))
								    elif SN > 'FEARRESISTT':
									    if SN < 'FINESSEC':
										    if SN == 'FINESSE':
										        Result = EquSng(StatLinInter("PntMPFinesse","ItemPntS","ProgBFinesse","AdjItem",L,N,0))
									    elif SN > 'FINESSEC':
										    if SN == 'FINESSECI':
										        Result = RoundDblLotro(CalcStat("FinesseCIRaw",L,N))
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("FinesseCI",CalcStat("FinesseCILvlFilter",N),N),0)
								    else:
								        Result = CalcStat("ResistAddT",L,N)
							    else:
							        Result = CalcStat("MainC",L,N)
						    elif SN > 'FINESSECILVLFILTER':
							    if SN < 'FINESSEPRATPCAP':
								    if SN < 'FINESSEPRATP':
									    if SN < 'FINESSECRAW':
										    if SN == 'FINESSECIRAW':
										        Result = StatLinInter("PntMPFinesseC","ItemPntS","ProgBFinesse","AdjCreepItem",L,N,4)
									    elif SN > 'FINESSECRAW':
										    if SN == 'FINESSEPPRAT':
										        Result = CalcRatAB(CalcStat("FinessePRatPA",L),CalcStat("FinessePRatPB",L),CalcStat("FinessePRatPCapR",L),N)
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("FinesseCIRaw",CalcStat("FinesseCILvlFilter",N),N),99)
								    elif SN > 'FINESSEPRATP':
									    if SN < 'FINESSEPRATPB':
										    if SN == 'FINESSEPRATPA':
										        Result = 150
									    elif SN > 'FINESSEPRATPB':
										    if SN == 'FINESSEPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatStandard")
								    else:
								        Result = CalcPercAB(CalcStat("FinessePRatPA",L),CalcStat("FinessePRatPB",L),CalcStat("FinessePRatPCap",L),N)
							    elif SN > 'FINESSEPRATPCAP':
								    if SN < 'FIREMITT':
									    if SN < 'FINESSET':
										    if SN == 'FINESSEPRATPCAPR':
										        Result = CalcStat("FinessePRatPB",L)*CalcStat("FinessePRatPC",L)
									    elif SN > 'FINESSET':
										    if SN == 'FIREMIT':
										        Result = CalcStat("DmgTypeMit",L,N)
									    else:
									        Result = EquSng(StatLinInter("PntMPFinesseT","TraitPntS","ProgBFinesse","AdjTrait",L,N,0))
								    elif SN > 'FIREMITT':
									    if SN < 'FOODNCMRH':
										    if SN == 'FOODNCMRBASEPROG':
										        if Lm <= 1:
										            Result = (N*70.2+210)/60
										        elif Lm <= 2:
										            Result = (N*84+216)/120
										        else:
										            Result = (N*83.7+270)/90
									    elif SN > 'FOODNCMRH':
										    if SN == 'FOODNCMRL':
										        Result = EquSng(CalcStat("FoodNCMRProg",L,2)*N)
									    else:
									        Result = EquSng(CalcStat("FoodNCMRProg",L,1)*N)
								    else:
								        Result = CalcStat("DmgTypeMitT",L,N)
							    else:
							        Result = 50
						    else:
						        if 3 <= Lp and Lm <= 3 or 3.6 <= Lp and Lm <= 3.6 or 6.2 <= Lp and Lm <= 6.2 or 7.2 <= Lp and Lm <= 7.2 or 10.8 <= Lp and Lm <= 10.8 or 14.4 <= Lp and Lm <= 14.4:
						            Result = 515
						        else:
						            Result = CalcStat("CreepILvlCurr",L)
					    elif SN > 'FOODNCMRM':
						    if SN < 'FREEPAUDACITYTACDMGP':
							    if SN < 'FREEPAUDACITYCCDP':
								    if SN < 'FOODNCPRL':
									    if SN < 'FOODNCPRBASEPROG':
										    if SN == 'FOODNCMRPROG':
										        if Lm <= 50:
										            Result = CalcStat("FoodNCMRBaseProg",N,L)
										        elif Lm <= 52:
										            Result = CalcStat("FoodNCMRBaseProg",N,50)
										        elif Lm <= 77:
										            Result = CalcStat("FoodNCMRBaseProg",N,L-3)
										        elif Lm <= 111:
										            Result = CalcStat("FoodNCMRBaseProg",N,RoundDbl((L+143)/3))
										        elif Lm <= 140:
										            Result = CalcStat("FoodNCMRBaseProg",N,85)
										        elif Lm <= 217:
										            Result = CalcStat("FoodNCMRBaseProg",N,RoundDbl((L+200)/4))
										        elif Lm <= 221:
										            Result = CalcStat("FoodNCMRBaseProg",N,104)
										        elif Lm <= 299:
										            Result = CalcStat("FoodNCMRBaseProg",N,105)
										        elif Lm <= 320:
										            Result = CalcStat("FoodNCMRBaseProg",N,RoundDbl((L-53)/(7/3)))
										        elif Lm <= 325:
										            Result = CalcStat("FoodNCMRBaseProg",N,114)
										        elif Lm <= 326:
										            Result = CalcStat("FoodNCMRBaseProg",N,115)
										        elif 327 <= Lp:
										            Result = ExpFmod(CalcStat("FoodNCMRProg",326,N),327,1,L,1)
									    elif SN > 'FOODNCPRBASEPROG':
										    if SN == 'FOODNCPRH':
										        Result = EquSng(CalcStat("FoodNCPRProg",L,1)*N)
									    else:
									        if Lm <= 1:
									            Result = (N*75+300)/60
									        elif Lm <= 2:
									            Result = (N*100+350)/120
									        else:
									            Result = (N*90+337.5)/90
								    elif SN > 'FOODNCPRL':
									    if SN < 'FOODNCPRPROG':
										    if SN == 'FOODNCPRM':
										        Result = EquSng(CalcStat("FoodNCPRProg",L,3)*N)
									    elif SN > 'FOODNCPRPROG':
										    if SN == 'FOODRESIST':
										        Result = EquSng(StatLinInter("PntMPFoodResist","ItemPntS","ProgBResist","AdjItem",L,N,0))
									    else:
									        if Lm <= 1:
									            Result = CalcStat("FoodNCPRBaseProg",N,L)
									        elif Lm <= 6:
									            Result = CalcStat("FoodNCPRBaseProg",N,L)-0.25
									        elif Lm <= 24:
									            Result = CalcStat("FoodNCPRBaseProg",N,L)-0.5
									        elif Lm <= 48:
									            Result = CalcStat("FoodNCPRBaseProg",N,L)-0.75
									        elif Lm <= 61:
									            Result = RoundDblDown(CalcStat("FoodNCPRProg",48,N))+1
									        elif Lm <= 66:
									            Result = RoundDblDown(CalcStat("FoodNCPRProg",48,N))+2
									        elif Lm <= 72:
									            Result = RoundDblDown(CalcStat("FoodNCPRProg",48,N))+3
									        elif Lm <= 326:
									            Result = RoundDblDown(CalcStat("FoodNCPRProg",48,N))+4
									        elif 327 <= Lp:
									            Result = ExpFmod(CalcStat("FoodNCPRProg",326,N),327,1,L,1)
								    else:
								        Result = EquSng(CalcStat("FoodNCPRProg",L,2)*N)
							    elif SN > 'FREEPAUDACITYCCDP':
								    if SN < 'FREEPAUDACITYMORALEP':
									    if SN < 'FREEPAUDACITYMELDMGP':
										    if SN == 'FREEPAUDACITYDMGP':
										        if 1 <= Lp and Lm <= 16:
										            Result = 0.75
										        elif 17 <= Lp and Lm <= 36:
										            Result = LinFmod(1,1.15,1.25,17,36,L)
										        elif 37 <= Lp and Lm <= 60:
										            Result = CalcStat("FreepAudacityDmgP",36)
									    elif SN > 'FREEPAUDACITYMELDMGP':
										    if SN == 'FREEPAUDACITYMELREDP':
										        Result = CalcStat("FreepAudacityRedP",L)
									    else:
									        Result = CalcStat("FreepAudacityDmgP",L)
								    elif SN > 'FREEPAUDACITYMORALEP':
									    if SN < 'FREEPAUDACITYRNGDMGP':
										    if SN == 'FREEPAUDACITYREDP':
										        if 1 <= Lp and Lm <= 16:
										            Result = 1.5
										        elif 17 <= Lp and Lm <= 36:
										            Result = 0.5
										        elif 37 <= Lp and Lm <= 60:
										            Result = CalcStat("FreepAudacityRedP",36)
									    elif SN > 'FREEPAUDACITYRNGDMGP':
										    if SN == 'FREEPAUDACITYRNGREDP':
										        Result = CalcStat("FreepAudacityRedP",L)
									    else:
									        Result = CalcStat("FreepAudacityDmgP",L)
								    else:
								        if 1 <= Lp and Lm <= 16:
								            Result = LinFmod(1,0.5,1.3,1,16,L)
								        elif 17 <= Lp and Lm <= 36:
								            Result = 1.4
								        elif 37 <= Lp and Lm <= 60:
								            Result = CalcStat("FreepAudacityMoraleP",36)
							    else:
							        if 1 <= Lp and Lm <= 16:
							            Result = 0.5
							        elif 17 <= Lp and Lm <= 36:
							            Result = 0.4
							        elif 37 <= Lp and Lm <= 60:
							            Result = CalcStat("FreepAudacityCCDP",36)
						    elif SN > 'FREEPAUDACITYTACDMGP':
							    if SN < 'FREEPBATPROMVITALP':
								    if SN < 'FREEPBATPROMMELDMGP':
									    if SN < 'FREEPBATPROMDMGP':
										    if SN == 'FREEPAUDACITYTACREDP':
										        Result = CalcStat("FreepAudacityRedP",L)
									    elif SN > 'FREEPBATPROMDMGP':
										    if SN == 'FREEPBATPROMHEALTHP':
										        Result = CalcStat("FreepBatPromVitalP",L)
									    else:
									        if 1 <= Lp and Lm <= 1:
									            Result = 0.005
									        elif 2 <= Lp and Lm <= 14:
									            Result = LinFmod(1,0.005,0.065,2,14,L)
									        elif 15 <= Lp and Lm <= 15:
									            Result = 0.075
								    elif SN > 'FREEPBATPROMMELDMGP':
									    if SN < 'FREEPBATPROMRNGDMGP':
										    if SN == 'FREEPBATPROMPOWERP':
										        Result = CalcStat("FreepBatPromVitalP",L)
									    elif SN > 'FREEPBATPROMRNGDMGP':
										    if SN == 'FREEPBATPROMTACDMGP':
										        Result = CalcStat("FreepBatPromDmgP",L)
									    else:
									        Result = CalcStat("FreepBatPromDmgP",L)
								    else:
								        Result = CalcStat("FreepBatPromDmgP",L)
							    elif SN > 'FREEPBATPROMVITALP':
								    if SN < 'GRDRELENTLASSFINESSE':
									    if SN < 'FROSTMITT':
										    if SN == 'FROSTMIT':
										        Result = CalcStat("DmgTypeMit",L,N)
									    elif SN > 'FROSTMITT':
										    if SN == 'GRDCRITDEF':
										        Result = CalcStat("CritDef",L)
									    else:
									        Result = CalcStat("DmgTypeMitT",L,N)
								    elif SN > 'GRDRELENTLASSFINESSE':
									    if SN < 'GRDTENDERIZET2CRITHIT':
										    if SN == 'GRDTENDERIZECRITHIT':
										        Result = CalcStat("CritHitT",L,CalcStat("Trait12345Choice",N)*0.2)
									    elif SN > 'GRDTENDERIZET2CRITHIT':
										    if SN == 'GRDTENDERIZET3CRITHIT':
										        Result = CalcStat("CritHitT",L,CalcStat("Trait357912Choice",N)*0.2)
									    else:
									        Result = CalcStat("CritHitT",L,CalcStat("Trait12345Choice",N)*0.4)
								    else:
								        Result = CalcStat("FinesseT",L,CalcStat("Trait12345Choice",N)*0.2)
							    else:
							        if 1 <= Lp and Lm <= 5:
							            Result = LinFmod(1,1.02,1.1,1,5,L)
							        elif 6 <= Lp and Lm <= 10:
							            Result = LinFmod(1,1.1,1.15,5,10,L)
							        elif 11 <= Lp and Lm <= 15:
							            Result = LinFmod(1,1.15,1.2,10,15,L)
						    else:
						        Result = CalcStat("FreepAudacityDmgP",L)
					    else:
					        Result = EquSng(CalcStat("FoodNCMRProg",L,3)*N)
				    elif SN > 'GRDTENDERIZET4CRITHIT':
					    if SN < 'GUARDIANCDMIGHTTOOUTHEAL':
						    if SN < 'GUARDIANCDBASEMIGHT':
							    if SN < 'GUARDIANCDARMOURTOCOMPHYMIT':
								    if SN < 'GUARDIANCDAGILITYTOFINESSE':
									    if SN < 'GRDWARDTACTTACMIT':
										    if SN == 'GRDTENDERIZET5CRITHIT':
										        Result = CalcStat("CritHitT",L,CalcStat("Trait58121620Choice",N)*0.2)
									    elif SN > 'GRDWARDTACTTACMIT':
										    if SN == 'GUARDIANCDAGILITYTOCRITHIT':
										        Result = 2
									    else:
									        Result = CalcStat("TacMitT",L,CalcStat("Trait12345Choice",N)*0.2)
								    elif SN > 'GUARDIANCDAGILITYTOFINESSE':
									    if SN < 'GUARDIANCDAGILITYTOPARRY':
										    if SN == 'GUARDIANCDAGILITYTOOUTHEAL':
										        Result = 2
									    elif SN > 'GUARDIANCDAGILITYTOPARRY':
										    if SN == 'GUARDIANCDAGILITYTOPHYMAS':
										        Result = 2
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'GUARDIANCDARMOURTOCOMPHYMIT':
								    if SN < 'GUARDIANCDBASEAGILITY':
									    if SN < 'GUARDIANCDARMOURTOTACMIT':
										    if SN == 'GUARDIANCDARMOURTONONPHYMIT':
										        Result = 0.2
									    elif SN > 'GUARDIANCDARMOURTOTACMIT':
										    if SN == 'GUARDIANCDARMOURTYPE':
										        Result = 3
									    else:
									        Result = 0.2
								    elif SN > 'GUARDIANCDBASEAGILITY':
									    if SN < 'GUARDIANCDBASEICMR':
										    if SN == 'GUARDIANCDBASEFATE':
										        Result = CalcStat("ClassBaseFate",L)
									    elif SN > 'GUARDIANCDBASEICMR':
										    if SN == 'GUARDIANCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    else:
									        Result = CalcStat("ClassBaseICMRH",L)
								    else:
								        Result = CalcStat("ClassBaseAgilityM",L)
							    else:
							        Result = 1
						    elif SN > 'GUARDIANCDBASEMIGHT':
							    if SN < 'GUARDIANCDCALCTYPENONPHYMIT':
								    if SN < 'GUARDIANCDBASEPOWER':
									    if SN < 'GUARDIANCDBASENCMR':
										    if SN == 'GUARDIANCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    elif SN > 'GUARDIANCDBASENCMR':
										    if SN == 'GUARDIANCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    else:
									        Result = CalcStat("ClassBaseNCMRH",L)
								    elif SN > 'GUARDIANCDBASEPOWER':
									    if SN < 'GUARDIANCDBASEWILL':
										    if SN == 'GUARDIANCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    elif SN > 'GUARDIANCDBASEWILL':
										    if SN == 'GUARDIANCDCALCTYPECOMPHYMIT':
										        Result = 14
									    else:
									        Result = CalcStat("ClassBaseWillL",L)
								    else:
								        Result = CalcStat("ClassBasePower",L)
							    elif SN > 'GUARDIANCDCALCTYPENONPHYMIT':
								    if SN < 'GUARDIANCDFATETOPOWER':
									    if SN < 'GUARDIANCDCANBLOCK':
										    if SN == 'GUARDIANCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'GUARDIANCDCANBLOCK':
										    if SN == 'GUARDIANCDFATETONCPR':
										        Result = 0.07
									    else:
									        Result = 1
								    elif SN > 'GUARDIANCDFATETOPOWER':
									    if SN < 'GUARDIANCDMIGHTTOBLOCK':
										    if SN == 'GUARDIANCDHASPOWER':
										        Result = 1
									    elif SN > 'GUARDIANCDMIGHTTOBLOCK':
										    if SN == 'GUARDIANCDMIGHTTOCRITHIT':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = 14
						    else:
						        Result = CalcStat("ClassBaseMightH",L)
					    elif SN > 'GUARDIANCDMIGHTTOOUTHEAL':
						    if SN < 'GUARDIANCDWILLTOTACMIT':
							    if SN < 'GUARDIANCDVITALITYTOICMR':
								    if SN < 'GUARDIANCDMIGHTTOTACMIT':
									    if SN < 'GUARDIANCDMIGHTTOPHYMAS':
										    if SN == 'GUARDIANCDMIGHTTOPARRY':
										        Result = 2
									    elif SN > 'GUARDIANCDMIGHTTOPHYMAS':
										    if SN == 'GUARDIANCDMIGHTTOPHYMIT':
										        Result = 1
									    else:
									        Result = 3
								    elif SN > 'GUARDIANCDMIGHTTOTACMIT':
									    if SN < 'GUARDIANCDPHYMITTONONPHYMIT':
										    if SN == 'GUARDIANCDPHYMITTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'GUARDIANCDPHYMITTONONPHYMIT':
										    if SN == 'GUARDIANCDTACMASTOOUTHEAL':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'GUARDIANCDVITALITYTOICMR':
								    if SN < 'GUARDIANCDWILLTOOUTHEAL':
									    if SN < 'GUARDIANCDVITALITYTONCMR':
										    if SN == 'GUARDIANCDVITALITYTOMORALE':
										        Result = 4.5
									    elif SN > 'GUARDIANCDVITALITYTONCMR':
										    if SN == 'GUARDIANCDWILLTOFINESSE':
										        Result = 1
									    else:
									        Result = 0.12
								    elif SN > 'GUARDIANCDWILLTOOUTHEAL':
									    if SN < 'GUARDIANCDWILLTOPHYMIT':
										    if SN == 'GUARDIANCDWILLTOPHYMAS':
										        Result = 1
									    elif SN > 'GUARDIANCDWILLTOPHYMIT':
										    if SN == 'GUARDIANCDWILLTORESIST':
										        Result = 1
									    else:
									        Result = 1.5
								    else:
								        Result = 1
							    else:
							        Result = 0.012
						    elif SN > 'GUARDIANCDWILLTOTACMIT':
							    if SN < 'HIGHELFRDPSVTWONAME':
								    if SN < 'HELFSORROWUNDYINGWILL':
									    if SN < 'HELFPEACEELDARMORALE':
										    if SN == 'HELFFADINGFIRSTBORNFATE':
										        Result = -CalcStat("FateT",L,0.4)
									    elif SN > 'HELFPEACEELDARMORALE':
										    if SN == 'HELFPEACEELDARNCMR':
										        Result = CalcStat("NCMRT",L,0.6)
									    else:
									        Result = CalcStat("MoraleT",L,1.0)
								    elif SN > 'HELFSORROWUNDYINGWILL':
									    if SN < 'HIGHELFRDPSVONENAME':
										    if SN == 'HELFTHOSEWHOREMAINWILL':
										        Result = CalcStat("WillT",L,1.0)
									    elif SN > 'HIGHELFRDPSVONENAME':
										    if SN == 'HIGHELFRDPSVONEWILL':
										        Result = CalcStat("HElfThoseWhoRemainWill",L)
									    else:
									        Result = "Those Who Remain"
								    else:
								        Result = -CalcStat("WillT",L,0.4)
							    elif SN > 'HIGHELFRDPSVTWONAME':
								    if SN < 'HIGHELFRDTRAITWILL':
									    if SN < 'HIGHELFRDTRAITMORALE':
										    if SN == 'HIGHELFRDTRAITFATE':
										        Result = CalcStat("HElfFadingFirstbornFate",L)
									    elif SN > 'HIGHELFRDTRAITMORALE':
										    if SN == 'HIGHELFRDTRAITNCMR':
										        Result = CalcStat("HElfPeaceEldarNCMR",L)
									    else:
									        Result = CalcStat("HElfPeaceEldarMorale",L)
								    elif SN > 'HIGHELFRDTRAITWILL':
									    if SN < 'HNTARMOURRENDEVADE':
										    if SN == 'HNTARMOURRENDBLOCK':
										        Result = -CalcStat("ShieldBlock",L,CalcStat("Trait23456Choice",N)*0.4)
									    elif SN > 'HNTARMOURRENDEVADE':
										    if SN > 'HNTARMOURRENDPARRY':
											    if SN == 'HNTBREACHFINDERRNGMIT':
											        Result = (-20)*L
										    elif SN == 'HNTARMOURRENDPARRY':
										        Result = -CalcStat("ParryT",L,CalcStat("Trait23456Choice",N)*0.4)
									    else:
									        Result = -CalcStat("EvadeT",L,CalcStat("Trait23456Choice",N)*0.4)
								    else:
								        Result = CalcStat("HElfSorrowUndyingWill",L)
							    else:
							        Result = ""
						    else:
						        Result = 1.5
					    else:
					        Result = 3
				    else:
				        Result = CalcStat("CritHitT",L,CalcStat("Trait47101316Choice",N)*0.2)
			    else:
			        Result = CalcStat("BPEPRatP",L,N)
		    elif SN > 'HNTCAMPFIRENCMR':
			    if SN < 'LOREMASTERCDBASEFATE':
				    if SN < 'ICMRC':
					    if SN < 'HUNTERCDBASEICPR':
						    if SN < 'HOBSMALLSIZEMIGHT':
							    if SN < 'HOBBITRDPSVONENAME':
								    if SN < 'HNTRAPIDFIREPHYMAS':
									    if SN < 'HNTPRECISIONSTANCEFINESSE':
										    if SN == 'HNTCAMPFIRENCPR':
										        Result = CalcStat("NCPRT",L,1.2)
									    elif SN > 'HNTPRECISIONSTANCEFINESSE':
										    if SN == 'HNTPURGEPOISONRESIST':
										        Result = CalcStat("PoisonResistT",L,4)
									    else:
									        Result = CalcStat("FinesseT",L,1.6)
								    elif SN > 'HNTRAPIDFIREPHYMAS':
									    if SN < 'HNTSTRENGTHSTANCECRITHIT':
										    if SN == 'HNTRAPIDFIRESEL':
										        if 1 <= Lp and Lm <= 8:
										            Result = L+2
										        elif 9 <= Lp and Lm <= 10:
										            Result = 2*L-6
									    elif SN > 'HNTSTRENGTHSTANCECRITHIT':
										    if SN == 'HOBBITRDPSVONEMIGHT':
										        Result = CalcStat("HobHobbitStatureMight",L)
									    else:
									        Result = CalcStat("CritHitT",L,4)
								    else:
								        Result = CalcStat("PhyMasT",L,CalcStat("HntRapidFireSel",N)*0.2)
							    elif SN > 'HOBBITRDPSVONENAME':
								    if SN < 'HOBBITRDTRAITVITALITY':
									    if SN < 'HOBBITRDTRAITMIGHT':
										    if SN == 'HOBBITRDPSVTWONAME':
										        Result = ""
									    elif SN > 'HOBBITRDTRAITMIGHT':
										    if SN == 'HOBBITRDTRAITNCMR':
										        Result = CalcStat("HobRapidRecoveryNCMR",L)
									    else:
									        Result = CalcStat("HobSmallSizeMight",L)
								    elif SN > 'HOBBITRDTRAITVITALITY':
									    if SN < 'HOBHOBBITTOUGHNVITALITY':
										    if SN == 'HOBHOBBITSTATUREMIGHT':
										        Result = CalcStat("MightT",L,1.0)
									    elif SN > 'HOBHOBBITTOUGHNVITALITY':
										    if SN == 'HOBRAPIDRECOVERYNCMR':
										        Result = CalcStat("NCMRT",L,0.6)
									    else:
									        Result = CalcStat("VitalityT",L,1.0)
								    else:
								        Result = CalcStat("HobHobbitToughnVitality",L)
							    else:
							        Result = "Hobbit-stature"
						    elif SN > 'HOBSMALLSIZEMIGHT':
							    if SN < 'HUNTERCDAGILITYTOTACMIT':
								    if SN < 'HUNTERCDAGILITYTOOUTHEAL':
									    if SN < 'HUNTERCDAGILITYTOCRITHIT':
										    if SN == 'HOPEMORALEP':
										        if Lm <= 5:
										            Result = DataTableValue((-0.99,-0.97,-0.95,-0.9,-0.85,-0.8,-0.65,-0.6,-0.5,-0.4,-0.3,-0.2,-0.15,-0.1,-0.05,0,0.01,0.02,0.03,0.04,0.05),L+16)
										        else:
										            Result = CalcStat("HopeMoraleP",5)
									    elif SN > 'HUNTERCDAGILITYTOCRITHIT':
										    if SN == 'HUNTERCDAGILITYTOEVADE':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'HUNTERCDAGILITYTOOUTHEAL':
									    if SN < 'HUNTERCDAGILITYTOPHYMAS':
										    if SN == 'HUNTERCDAGILITYTOPARRY':
										        Result = 1
									    elif SN > 'HUNTERCDAGILITYTOPHYMAS':
										    if SN == 'HUNTERCDAGILITYTOPHYMIT':
										        Result = 1
									    else:
									        Result = 3
								    else:
								        Result = 3
							    elif SN > 'HUNTERCDAGILITYTOTACMIT':
								    if SN < 'HUNTERCDARMOURTYPE':
									    if SN < 'HUNTERCDARMOURTONONPHYMIT':
										    if SN == 'HUNTERCDARMOURTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'HUNTERCDARMOURTONONPHYMIT':
										    if SN == 'HUNTERCDARMOURTOTACMIT':
										        Result = 0.2
									    else:
									        Result = 0.2
								    elif SN > 'HUNTERCDARMOURTYPE':
									    if SN < 'HUNTERCDBASEFATE':
										    if SN == 'HUNTERCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityH",L)
									    elif SN > 'HUNTERCDBASEFATE':
										    if SN == 'HUNTERCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRM",L)
									    else:
									        Result = CalcStat("ClassBaseFate",L)
								    else:
								        Result = 2
							    else:
							        Result = 1
						    else:
						        Result = -CalcStat("MightT",L,0.4)
					    elif SN > 'HUNTERCDBASEICPR':
						    if SN < 'HUNTERCDMIGHTTOFINESSE':
							    if SN < 'HUNTERCDCALCTYPECOMPHYMIT':
								    if SN < 'HUNTERCDBASENCPR':
									    if SN < 'HUNTERCDBASEMORALE':
										    if SN == 'HUNTERCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightM",L)
									    elif SN > 'HUNTERCDBASEMORALE':
										    if SN == 'HUNTERCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRM",L)
									    else:
									        Result = CalcStat("ClassBaseMorale",L)
								    elif SN > 'HUNTERCDBASENCPR':
									    if SN < 'HUNTERCDBASEVITALITY':
										    if SN == 'HUNTERCDBASEPOWER':
										        Result = CalcStat("ClassBasePower",L)
									    elif SN > 'HUNTERCDBASEVITALITY':
										    if SN == 'HUNTERCDBASEWILL':
										        Result = CalcStat("ClassBaseWillL",L)
									    else:
									        Result = CalcStat("ClassBaseVitality",L)
								    else:
								        Result = CalcStat("ClassBaseNCPR",L)
							    elif SN > 'HUNTERCDCALCTYPECOMPHYMIT':
								    if SN < 'HUNTERCDFATETOPOWER':
									    if SN < 'HUNTERCDCALCTYPETACMIT':
										    if SN == 'HUNTERCDCALCTYPENONPHYMIT':
										        Result = 13
									    elif SN > 'HUNTERCDCALCTYPETACMIT':
										    if SN == 'HUNTERCDFATETONCPR':
										        Result = 0.07
									    else:
									        Result = 26
								    elif SN > 'HUNTERCDFATETOPOWER':
									    if SN < 'HUNTERCDMIGHTTOCRITHIT':
										    if SN == 'HUNTERCDHASPOWER':
										        Result = 1
									    elif SN > 'HUNTERCDMIGHTTOCRITHIT':
										    if SN == 'HUNTERCDMIGHTTOEVADE':
										        Result = 1
									    else:
									        Result = 1.5
								    else:
								        Result = 1
							    else:
							        Result = 13
						    elif SN > 'HUNTERCDMIGHTTOFINESSE':
							    if SN < 'HUNTERCDVITALITYTONCMR':
								    if SN < 'HUNTERCDPHYMITTONONPHYMIT':
									    if SN < 'HUNTERCDMIGHTTOPHYMAS':
										    if SN == 'HUNTERCDMIGHTTOOUTHEAL':
										        Result = 2
									    elif SN > 'HUNTERCDMIGHTTOPHYMAS':
										    if SN == 'HUNTERCDPHYMITTOCOMPHYMIT':
										        Result = 1
									    else:
									        Result = 2
								    elif SN > 'HUNTERCDPHYMITTONONPHYMIT':
									    if SN < 'HUNTERCDVITALITYTOICMR':
										    if SN == 'HUNTERCDTACMASTOOUTHEAL':
										        Result = 1
									    elif SN > 'HUNTERCDVITALITYTOICMR':
										    if SN == 'HUNTERCDVITALITYTOMORALE':
										        Result = 4.5
									    else:
									        Result = 0.012
								    else:
								        Result = 1
							    elif SN > 'HUNTERCDVITALITYTONCMR':
								    if SN < 'HUNTERCDWILLTOPHYMAS':
									    if SN < 'HUNTERCDWILLTOFINESSE':
										    if SN == 'HUNTERCDWILLTOCRITHIT':
										        Result = 0.5
									    elif SN > 'HUNTERCDWILLTOFINESSE':
										    if SN == 'HUNTERCDWILLTOOUTHEAL':
										        Result = 2
									    else:
									        Result = 1.5
								    elif SN > 'HUNTERCDWILLTOPHYMAS':
									    if SN < 'HUNTERCDWILLTORESIST':
										    if SN == 'HUNTERCDWILLTOPHYMIT':
										        Result = 1
									    elif SN > 'HUNTERCDWILLTORESIST':
										    if SN == 'ICMR':
										        Result = EquSng(StatLinInter("PntMPICMR","ItemPntSVital","ProgBICMR","",L,N,1))
									    else:
									        Result = 1
								    else:
								        Result = 2
							    else:
							        Result = 0.12
						    else:
						        Result = 1.5
					    else:
					        Result = CalcStat("ClassBaseICPR",L)
				    elif SN > 'ICMRC':
					    if SN < 'ITEMPNTS':
						    if SN < 'INDMGPRATPA':
							    if SN < 'ICPRC':
								    if SN < 'ICMRCRAW':
									    if SN < 'ICMRCILVLFILTER':
										    if SN == 'ICMRCI':
										        Result = RoundDblLotro(CalcStat("ICMRCIRaw",L,N))
									    elif SN > 'ICMRCILVLFILTER':
										    if SN == 'ICMRCIRAW':
										        Result = StatLinInter("PntMPICMRC","ItemPntS","ProgBICMR","AdjCreepItem",L,N,4)
									    else:
									        if 0 <= Lp and Lm <= 0:
									            Result = 515
									        else:
									            Result = CalcStat("CreepILvlCurr",L)
								    elif SN > 'ICMRCRAW':
									    if SN < 'ICMRT':
										    if SN == 'ICMRDEBUFFT':
										        Result = EquSng(StatLinInter("PntMPICMRDebuffT","TraitPntSVital","ProgBICMR","",L,N,99))
									    elif SN > 'ICMRT':
										    if SN == 'ICPR':
										        Result = EquSng(StatLinInter("PntMPICPR","ItemPntSVital","ProgBICPR","",L,N,99))
									    else:
									        Result = EquSng(StatLinInter("PntMPICMR","TraitPntSVital","ProgBICMR","",L,N,1))
								    else:
								        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ICMRCIRaw",CalcStat("ICMRCILvlFilter",N),N),99)
							    elif SN > 'ICPRC':
								    if SN < 'ICPRCRAW':
									    if SN < 'ICPRCILVLFILTER':
										    if SN == 'ICPRCI':
										        Result = RoundDblLotro(CalcStat("ICPRCIRaw",L,N))
									    elif SN > 'ICPRCILVLFILTER':
										    if SN == 'ICPRCIRAW':
										        Result = StatLinInter("PntMPICPRC","ItemPntS","ProgBICPR","AdjCreepItemPower",L,N,4)
									    else:
									        if 0 <= Lp and Lm <= 0:
									            Result = 515
									        else:
									            Result = CalcStat("CreepILvlCurr",L)
								    elif SN > 'ICPRCRAW':
									    if SN < 'INDMGPPRAT':
										    if SN == 'ICPRT':
										        Result = EquSng(StatLinInter("PntMPICPR","TraitPntSVital","ProgBICPR","",L,N,99))
									    elif SN > 'INDMGPPRAT':
										    if SN == 'INDMGPRATP':
										        Result = CalcPercAB(CalcStat("InDmgPRatPA",L),CalcStat("InDmgPRatPB",L),CalcStat("InDmgPRatPCap",L),N)
									    else:
									        Result = CalcRatAB(CalcStat("InDmgPRatPA",L),CalcStat("InDmgPRatPB",L),CalcStat("InDmgPRatPCapR",L),N)
								    else:
								        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ICPRCIRaw",CalcStat("ICPRCILvlFilter",N),N),99)
							    else:
							        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ICPRCI",CalcStat("ICPRCILvlFilter",N),N),0)
						    elif SN > 'INDMGPRATPA':
							    if SN < 'INHEALPRATPA':
								    if SN < 'INDMGPRATPCAPR':
									    if SN < 'INDMGPRATPC':
										    if SN == 'INDMGPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatStandard")
									    elif SN > 'INDMGPRATPC':
										    if SN == 'INDMGPRATPCAP':
										        Result = 400
									    else:
									        Result = 0.5
								    elif SN > 'INDMGPRATPCAPR':
									    if SN < 'INHEALPPRAT':
										    if SN == 'INHEAL':
										        Result = EquSng(StatLinInter("PntMPInHeal","ItemPntS","ProgBInHeal","AdjItem",L,N,0))
									    elif SN > 'INHEALPPRAT':
										    if SN == 'INHEALPRATP':
										        Result = CalcPercAB(CalcStat("InHealPRatPA",L),CalcStat("InHealPRatPB",L),CalcStat("InHealPRatPCap",L),N)
									    else:
									        Result = CalcRatAB(CalcStat("InHealPRatPA",L),CalcStat("InHealPRatPB",L),CalcStat("InHealPRatPCapR",L),N)
								    else:
								        Result = CalcStat("InDmgPRatPB",L)*CalcStat("InDmgPRatPC",L)
							    elif SN > 'INHEALPRATPA':
								    if SN < 'INHEALPRATPCAPR':
									    if SN < 'INHEALPRATPC':
										    if SN == 'INHEALPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatStandard")
									    elif SN > 'INHEALPRATPC':
										    if SN == 'INHEALPRATPCAP':
										        Result = 25
									    else:
									        Result = 0.5
								    elif SN > 'INHEALPRATPCAPR':
									    if SN < 'INSTRMORALE':
										    if SN == 'INHEALT':
										        Result = EquSng(StatLinInter("PntMPInHeal","TraitPntS","ProgBInHeal","AdjTrait",L,N,0))
									    elif SN > 'INSTRMORALE':
										    if SN == 'INSTRPOWER':
										        if Lm <= 9:
										            Result = RoundDbl(0.95*L+12.6)
										        elif Lm <= 18:
										            Result = RoundDbl(1.95*L+3)
										        elif Lm <= 26:
										            Result = RoundDbl(2.95*L-15.55)
										        elif Lm <= 35:
										            Result = RoundDbl(3.95*L-42.15)
										        elif Lm <= 42:
										            Result = RoundDbl(4.95*L-77.7)
										        elif Lm <= 45:
										            Result = RoundDbl(5.95*L-120.35)
										        elif Lm <= 105:
										            Result = RoundDbl(6*L-124)
										        else:
										            Result = CalcStat("ProgExtMpExpRnd",L,CalcStat("InstrPower",105))
									    else:
									        if Lm <= 105:
									            Result = RoundDbl(4.04*L)
									        else:
									            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("InstrMorale",105))
								    else:
								        Result = CalcStat("InHealPRatPB",L)*CalcStat("InHealPRatPC",L)
							    else:
							        Result = 75
						    else:
						        Result = 1200
					    elif SN > 'ITEMPNTS':
						    if SN < 'LMHEARTYDIETMORALE':
							    if SN < 'LI2REFORGECOST':
								    if SN < 'ITEMPNTSVITAL':
									    if SN < 'ITEMPNTSVIRTUEMASTERY':
										    if SN == 'ITEMPNTSCLASSIC':
										        Result = ((1,25,50,60,79,80,200,225,300,349,350,399,400,449,450,499,500,549,550,599),(1,25,50,60,75,76,100,105,106,115,116,120,121,130,131,140,141,150,151,160))
									    elif SN > 'ITEMPNTSVIRTUEMASTERY':
										    if SN == 'ITEMPNTSVIRTUEMORALE':
										        Result = ((0,1,2,50,80,200,225,300,349,350,399,400,449,450,499,500,549,550,599),(0,1,2,50,76,100,105,106,115,116,120,121,130,131,140,141,150,151,160))
									    else:
									        Result = ((0,1,25,50,79,80,200,225,300,349,399,400,449,450,499,500,549,550,599),(0,1,25,50,75,76,100,105,106,115,116,121,130,131,140,141,150,151,160))
								    elif SN > 'ITEMPNTSVITAL':
									    if SN < 'LEVELCAP':
										    if SN == 'L':
										        Result = L
									    elif SN > 'LEVELCAP':
										    if SN == 'LI2ILVLCAP':
										        Result = 530
									    else:
									        Result = 150
								    else:
								        Result = ((1,25,50,60,79,80,200,225,300,349,350,399,400,449,450,499,500,549,550,599),(1,25,50,60,75,76,100,105,106,115,116,120,121,130,131,140,141,150,151,160))
							    elif SN > 'LI2REFORGECOST':
								    if SN < 'LIGHTMITT':
									    if SN < 'LI2REFORGEILVL':
										    if SN == 'LI2REFORGECOSTSEG':
										        if Lm <= 0:
										            Result = 0
										        elif 1 <= Lp and Lm <= 12:
										            Result = DataTableValue((1,1.2,1.4,1.7,2.1,2.5,3,3.6,4.3,5.1,6.4,7.5),L)
										        elif Lm <= 22:
										            Result = LinFmod(1,8,35,13,22,L)
										        elif Lm <= 41:
										            Result = LinFmod(1,35.7,48.3,23,41,L)
										        elif Lm <= 43:
										            Result = LinFmod(1,50,60,42,43,L)
										        elif Lm <= 48:
										            Result = RoundDbl(LinFmod(1,62.6,77,44,48,L))
										        elif Lm <= 53:
										            Result = RoundDbl(LinFmod(1,80,99,49,53,L))
										        elif Lm <= 55:
										            Result = LinFmod(1,103.5,109,54,55,L)
										        elif Lm <= 61:
										            Result = RoundDbl(LinFmod(1,113.6,145,56,61,L))
										        elif Lm <= 120:
										            Result = LinFmod(1,153,849,62,120,L)
										        elif Lm <= 130:
										            Result = LinFmod(1,855,909,121,130,L)
										        else:
										            Result = LinFmod(1,914,1009,131,150,L)
									    elif SN > 'LI2REFORGEILVL':
										    if SN == 'LIGHTMIT':
										        Result = CalcStat("DmgTypeMit",L,N)
									    else:
									        if Lm <= 145:
									            Result = CalcStat("AwardILvlI",L)
									        else:
									            Result = N
								    elif SN > 'LIGHTMITT':
									    if SN < 'LIGHTNINGMITT':
										    if SN == 'LIGHTNINGMIT':
										        Result = CalcStat("DmgTypeMit",L,N)
									    elif SN > 'LIGHTNINGMITT':
										    if SN == 'LMANCIENTWISDOMWILL':
										        if Lm <= 105:
										            Result = RoundDbl(1.1*L)
										        else:
										            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("LmAncientWisdomWill",105))
									    else:
									        Result = CalcStat("DmgTypeMitT",L,N)
								    else:
								        Result = CalcStat("DmgTypeMitT",L,N)
							    else:
							        Result = RoundDbl(CalcStat("Li2ReforgeCostSeg",L)*(L+9)*12.5)
						    elif SN > 'LMHEARTYDIETMORALE':
							    if SN < 'LOREMASTERCDAGILITYTOCRITHIT':
								    if SN < 'LMSWSTAFFBUGPARRY':
									    if SN < 'LMPREPFORWARTACMAS':
										    if SN == 'LMHEARTYDIETMORALECHOICE':
										        if 1 <= Lp and Lm <= 6:
										            Result = DataTableValue((0.4,1,1.6,2.4,3.2,3.2),L)
									    elif SN > 'LMPREPFORWARTACMAS':
										    if SN == 'LMSWSTAFFBUGMORALE':
										        if Lm <= 105:
										            Result = RoundDbl(LinFmod(1,16.2,696.9,1,105,L))
										        else:
										            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("LmSwStaffBugMorale",105))
									    else:
									        Result = CalcStat("TacMasT",L,CalcStat("Trait12345Choice",N)*0.4)
								    elif SN > 'LMSWSTAFFBUGPARRY':
									    if SN < 'LOE':
										    if SN == 'LMSWSTAFFBUGPARRYOLD':
										        if Lm <= 105:
										            Result = RoundDbl(44.44*L)
										        else:
										            Result = CalcStat("ProgExtHighLinExpRnd",L,CalcStat("LmSwStaffBugParryOld",105))
									    elif SN > 'LOE':
										    if SN == 'LOEPASSIVE':
										        if 116 <= Lp and Lm <= 119:
										            Result = 20*L-2300
										        elif 120 <= Lp:
										            Result = CalcStat("LoEPassive",119)
									    else:
									        Result = 2*N
								    else:
								        if Lm <= 140:
								            Result = CalcStat("U371LegacyStatFix",L,"LmSwStaffBugParryOld")
								        else:
								            Result = CalcStat("LMSwStaffBugParry",140)
							    elif SN > 'LOREMASTERCDAGILITYTOCRITHIT':
								    if SN < 'LOREMASTERCDARMOURTOCOMPHYMIT':
									    if SN < 'LOREMASTERCDAGILITYTOFINESSE':
										    if SN == 'LOREMASTERCDAGILITYTOEVADE':
										        Result = 1
									    elif SN > 'LOREMASTERCDAGILITYTOFINESSE':
										    if SN == 'LOREMASTERCDAGILITYTOTACMAS':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'LOREMASTERCDARMOURTOCOMPHYMIT':
									    if SN < 'LOREMASTERCDARMOURTOTACMIT':
										    if SN == 'LOREMASTERCDARMOURTONONPHYMIT':
										        Result = 0.2
									    elif SN > 'LOREMASTERCDARMOURTOTACMIT':
										    if SN > 'LOREMASTERCDARMOURTYPE':
											    if SN == 'LOREMASTERCDBASEAGILITY':
											        Result = CalcStat("ClassBaseAgilityL",L)
										    elif SN == 'LOREMASTERCDARMOURTYPE':
										        Result = 1
									    else:
									        Result = 0.2
								    else:
								        Result = 1
							    else:
							        Result = 2
						    else:
						        Result = CalcStat("Morale",L,CalcStat("LmHeartyDietMoraleChoice",N))
					    else:
					        Result = ((1,25,50,79,80,200,225,300,349,350,399,400,449,450,499,500,549,550,599),(1,25,50,75,76,100,105,106,115,116,120,121,130,131,140,141,150,151,160))
				    else:
				        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ICMRCI",CalcStat("ICMRCILvlFilter",N),N),0)
			    elif SN > 'LOREMASTERCDBASEFATE':
				    if SN < 'MARINERCDAGILITYTOPHYMAS':
					    if SN < 'LVLBONUSMORRES':
						    if SN < 'LOREMASTERCDMIGHTTOCRITHIT':
							    if SN < 'LOREMASTERCDBASEVITALITY':
								    if SN < 'LOREMASTERCDBASEMORALE':
									    if SN < 'LOREMASTERCDBASEICPR':
										    if SN == 'LOREMASTERCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRL",L)
									    elif SN > 'LOREMASTERCDBASEICPR':
										    if SN == 'LOREMASTERCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightM",L)
									    else:
									        Result = CalcStat("ClassBaseICPR",L)
								    elif SN > 'LOREMASTERCDBASEMORALE':
									    if SN < 'LOREMASTERCDBASENCPR':
										    if SN == 'LOREMASTERCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRL",L)
									    elif SN > 'LOREMASTERCDBASENCPR':
										    if SN == 'LOREMASTERCDBASEPOWER':
										        Result = CalcStat("ClassBasePower",L)
									    else:
									        Result = CalcStat("ClassBaseNCPR",L)
								    else:
								        Result = CalcStat("ClassBaseMorale",L)
							    elif SN > 'LOREMASTERCDBASEVITALITY':
								    if SN < 'LOREMASTERCDCALCTYPETACMIT':
									    if SN < 'LOREMASTERCDCALCTYPECOMPHYMIT':
										    if SN == 'LOREMASTERCDBASEWILL':
										        Result = CalcStat("ClassBaseWillH",L)
									    elif SN > 'LOREMASTERCDCALCTYPECOMPHYMIT':
										    if SN == 'LOREMASTERCDCALCTYPENONPHYMIT':
										        Result = 12
									    else:
									        Result = 12
								    elif SN > 'LOREMASTERCDCALCTYPETACMIT':
									    if SN < 'LOREMASTERCDFATETOPOWER':
										    if SN == 'LOREMASTERCDFATETONCPR':
										        Result = 0.07
									    elif SN > 'LOREMASTERCDFATETOPOWER':
										    if SN == 'LOREMASTERCDHASPOWER':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 25
							    else:
							        Result = CalcStat("ClassBaseVitality",L)
						    elif SN > 'LOREMASTERCDMIGHTTOCRITHIT':
							    if SN < 'LOREMASTERCDVITALITYTOMORALE':
								    if SN < 'LOREMASTERCDPHYMITTOCOMPHYMIT':
									    if SN < 'LOREMASTERCDMIGHTTOPARRY':
										    if SN == 'LOREMASTERCDMIGHTTOFINESSE':
										        Result = 1.5
									    elif SN > 'LOREMASTERCDMIGHTTOPARRY':
										    if SN == 'LOREMASTERCDMIGHTTOTACMAS':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'LOREMASTERCDPHYMITTOCOMPHYMIT':
									    if SN < 'LOREMASTERCDTACMASTOOUTHEAL':
										    if SN == 'LOREMASTERCDPHYMITTONONPHYMIT':
										        Result = 1
									    elif SN > 'LOREMASTERCDTACMASTOOUTHEAL':
										    if SN == 'LOREMASTERCDVITALITYTOICMR':
										        Result = 0.012
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'LOREMASTERCDVITALITYTOMORALE':
								    if SN < 'LOREMASTERCDWILLTOPHYMIT':
									    if SN < 'LOREMASTERCDWILLTOCRITHIT':
										    if SN == 'LOREMASTERCDVITALITYTONCMR':
										        Result = 0.12
									    elif SN > 'LOREMASTERCDWILLTOCRITHIT':
										    if SN == 'LOREMASTERCDWILLTOEVADE':
										        Result = 2
									    else:
									        Result = 1
								    elif SN > 'LOREMASTERCDWILLTOPHYMIT':
									    if SN < 'LOREMASTERCDWILLTOTACMAS':
										    if SN == 'LOREMASTERCDWILLTORESIST':
										        Result = 1
									    elif SN > 'LOREMASTERCDWILLTOTACMAS':
										    if SN == 'LOREMASTERCDWILLTOTACMIT':
										        Result = 1
									    else:
									        Result = 3
								    else:
								        Result = 1
							    else:
							        Result = 4.5
						    else:
						        Result = 1.5
					    elif SN > 'LVLBONUSMORRES':
						    if SN < 'MANFOURTHAGEWILL':
							    if SN < 'MAINC':
								    if SN < 'LVLEXPCOST':
									    if SN < 'LVLBONUSPOWRES':
										    if SN == 'LVLBONUSPHYDMG':
										        Result = EquSng(0.1)
									    elif SN > 'LVLBONUSPOWRES':
										    if SN == 'LVLBONUSTACDMG':
										        Result = EquSng(0.1)
									    else:
									        Result = CalcStat("SkillPowerCost",L,N)
								    elif SN > 'LVLEXPCOST':
									    if SN < 'LVLTOILVL':
										    if SN == 'LVLEXPCOSTTOT':
										        if 1 <= Lp:
										            Result = CalcStat("LvlExpCostTot",L-1)+CalcStat("LvlExpCost",L)
									    elif SN > 'LVLTOILVL':
										    if SN == 'MAIN':
										        Result = RoundDblDown(StatLinInter("PntMPMain","ItemPntS","ProgBMain","AdjItem",L,N,0))
									    else:
									        if Lm <= 106:
									            Result = LinFmod(1,225,300,105,106,L)
									        elif Lm <= 115:
									            Result = LinFmod(1,300,349,106,115,L)
									        elif Lm <= 116:
									            Result = LinFmod(1,349,350,115,116,L)
									        elif Lm <= 120:
									            Result = LinFmod(1,350,399,116,120,L)
									        elif Lm <= 121:
									            Result = LinFmod(1,399,400,120,121,L)
									        elif Lm <= 130:
									            Result = LinFmod(1,400,449,121,130,L)
									        elif Lm <= 131:
									            Result = LinFmod(1,449,450,130,131,L)
									        elif Lm <= 140:
									            Result = LinFmod(1,450,499,131,140,L)
									        elif Lm <= 141:
									            Result = LinFmod(1,499,500,140,141,L)
									        else:
									            Result = LinFmod(1,500,549,141,150,L)
								    else:
								        if Lm <= 1:
								            Result = 0
								        elif Lm <= 5:
								            Result = RoundDbl(12.5*L*L+12.5666666666667*L+24.8666666666667)
								        elif Lm <= 10:
								            Result = RoundDbl(33.8*L*L-179.48*L+452.6)
								        elif Lm <= 15:
								            Result = RoundDbl(55.05*L*L-583.77*L+2370.5)
								        elif Lm <= 20:
								            Result = RoundDbl(76.2*L*L-1196.96*L+6809)
								        elif Lm <= 25:
								            Result = RoundDbl(97.4*L*L-2023*L+14849.8)
								        elif Lm <= 30:
								            Result = RoundDbl(118.7*L*L-3066.02 *L+27612.8)
								        elif Lm <= 35:
								            Result = RoundDbl(139.95*L*L-4319.23*L+46084.1)
								        elif Lm <= 40:
								            Result = RoundDbl(161.2*L*L-5785.04*L+71356.2)
								        elif Lm <= 45:
								            Result = RoundDbl(182.5*L*L-7467.38*L+104569.8)
								        elif Lm <= 50:
								            Result = RoundDbl(203.8*L*L-9363.48*L+146761.8)
								        elif Lm <= 55:
								            Result = RoundDbl(225.05*L*L-11467.77*L+198851.3)
								        elif Lm <= 60:
								            Result = RoundDbl(246.3*L*L-13784.46*L+261988)
								        elif 61 <= Lp and Lm <= 70:
								            Result = RoundDbl(ExpFmod(CalcStat("LvlExpCost",60),61,5.071,L,None,3.485))
								        elif 71 <= Lp and Lm <= 75:
								            Result = RoundDbl(ExpFmod(CalcStat("LvlExpCost",70),71,5.072,L,None,-0.95))
								        elif 76 <= Lp:
								            Result = ExpFmod(CalcStat("LvlExpCost",75),76,5,L,0,-0.5)
							    elif SN > 'MAINC':
								    if SN < 'MAINCRAW':
									    if SN < 'MAINCILVLFILTER':
										    if SN == 'MAINCI':
										        Result = RoundDblLotro(CalcStat("MainCIRaw",L,N))
									    elif SN > 'MAINCILVLFILTER':
										    if SN == 'MAINCIRAW':
										        Result = StatLinInter("PntMPMainC","ItemPntS","ProgBMain","AdjCreepItem",L,N,4)
									    else:
									        if -19.5 <= Lp and Lm <= -19.5 or 19.5 <= Lp and Lm <= 19.5:
									            Result = 520
									        else:
									            Result = CalcStat("CreepILvlCurr",L)
								    elif SN > 'MAINCRAW':
									    if SN < 'MANDIMMANKINDWILL':
										    if SN == 'MAINT':
										        Result = RoundDblDown(StatLinInter("PntMPMain","TraitPntS","ProgBMain","AdjTrait",L,N,0))
									    elif SN > 'MANDIMMANKINDWILL':
										    if SN == 'MANEASILYINSPINHEALP':
										        Result = 5
									    else:
									        Result = -CalcStat("WillT",L,0.4)
								    else:
								        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("MainCIRaw",CalcStat("MainCILvlFilter",N),N),99)
							    else:
							        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("MainCI",CalcStat("MainCILvlFilter",N),N),0)
						    elif SN > 'MANFOURTHAGEWILL':
							    if SN < 'MANRDTRAITFATE':
								    if SN < 'MANRDPSVTWOBLOCK':
									    if SN < 'MANRDPSVONENAME':
										    if SN == 'MANGIFTOFMENFATE':
										        Result = CalcStat("FateT",L,1.0)
									    elif SN > 'MANRDPSVONENAME':
										    if SN == 'MANRDPSVONEWILL':
										        Result = CalcStat("ManFourthAgeWill",L)
									    else:
									        Result = "Man of the Fourth Age"
								    elif SN > 'MANRDPSVTWOBLOCK':
									    if SN < 'MANRDPSVTWONAME':
										    if SN == 'MANRDPSVTWOEVADE':
										        Result = CalcStat("BalanceOfManEvade",L)
									    elif SN > 'MANRDPSVTWONAME':
										    if SN == 'MANRDPSVTWOPARRY':
										        Result = CalcStat("BalanceOfManParry",L)
									    else:
									        Result = "Balance of Man"
								    else:
								        Result = CalcStat("BalanceOfManBlock",L)
							    elif SN > 'MANRDTRAITFATE':
								    if SN < 'MANSTRONGMENMIGHT':
									    if SN < 'MANRDTRAITMIGHT':
										    if SN == 'MANRDTRAITINHEALP':
										        Result = CalcStat("ManEasilyInspInHealP",L)
									    elif SN > 'MANRDTRAITMIGHT':
										    if SN == 'MANRDTRAITWILL':
										        Result = CalcStat("ManDimMankindWill",L)
									    else:
									        Result = CalcStat("ManStrongMenMight",L)
								    elif SN > 'MANSTRONGMENMIGHT':
									    if SN < 'MARINERCDAGILITYTOOUTHEAL':
										    if SN == 'MARINERCDAGILITYTOCRITHIT':
										        Result = 1
									    elif SN > 'MARINERCDAGILITYTOOUTHEAL':
										    if SN == 'MARINERCDAGILITYTOPARRY':
										        Result = 3
									    else:
									        Result = 3
								    else:
								        Result = CalcStat("MightT",L,1.0)
							    else:
							        Result = CalcStat("ManGiftOfMenFate",L)
						    else:
						        Result = CalcStat("WillT",L,1.0)
					    else:
					        Result = EquSng(0.1)
				    elif SN > 'MARINERCDAGILITYTOPHYMAS':
					    if SN < 'MARINERCDVITALITYTOICMR':
						    if SN < 'MARINERCDBASEVITALITY':
							    if SN < 'MARINERCDBASEFATE':
								    if SN < 'MARINERCDARMOURTONONPHYMIT':
									    if SN < 'MARINERCDAGILITYTOTACMIT':
										    if SN == 'MARINERCDAGILITYTOPHYMIT':
										        Result = 1
									    elif SN > 'MARINERCDAGILITYTOTACMIT':
										    if SN == 'MARINERCDARMOURTOCOMPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'MARINERCDARMOURTONONPHYMIT':
									    if SN < 'MARINERCDARMOURTYPE':
										    if SN == 'MARINERCDARMOURTOTACMIT':
										        Result = 0.2
									    elif SN > 'MARINERCDARMOURTYPE':
										    if SN == 'MARINERCDBASEAGILITY':
										        Result = CalcStat("ClassBaseAgilityM",L)
									    else:
									        Result = 2
								    else:
								        Result = 0.2
							    elif SN > 'MARINERCDBASEFATE':
								    if SN < 'MARINERCDBASEMORALE':
									    if SN < 'MARINERCDBASEICPR':
										    if SN == 'MARINERCDBASEICMR':
										        Result = CalcStat("ClassBaseICMRL",L)
									    elif SN > 'MARINERCDBASEICPR':
										    if SN == 'MARINERCDBASEMIGHT':
										        Result = CalcStat("ClassBaseMightM",L)
									    else:
									        Result = CalcStat("ClassBaseICPR",L)
								    elif SN > 'MARINERCDBASEMORALE':
									    if SN < 'MARINERCDBASENCPR':
										    if SN == 'MARINERCDBASENCMR':
										        Result = CalcStat("ClassBaseNCMRL",L)
									    elif SN > 'MARINERCDBASENCPR':
										    if SN == 'MARINERCDBASEPOWER':
										        Result = CalcStat("ClassBasePower",L)
									    else:
									        Result = CalcStat("ClassBaseNCPR",L)
								    else:
								        Result = CalcStat("ClassBaseMorale",L)
							    else:
							        Result = CalcStat("ClassBaseFate",L)
						    elif SN > 'MARINERCDBASEVITALITY':
							    if SN < 'MARINERCDMIGHTTOCRITHIT':
								    if SN < 'MARINERCDCALCTYPETACMIT':
									    if SN < 'MARINERCDCALCTYPECOMPHYMIT':
										    if SN == 'MARINERCDBASEWILL':
										        Result = CalcStat("ClassBaseWillM",L)
									    elif SN > 'MARINERCDCALCTYPECOMPHYMIT':
										    if SN == 'MARINERCDCALCTYPENONPHYMIT':
										        Result = 13
									    else:
									        Result = 13
								    elif SN > 'MARINERCDCALCTYPETACMIT':
									    if SN < 'MARINERCDFATETOPOWER':
										    if SN == 'MARINERCDFATETONCPR':
										        Result = 0.07
									    elif SN > 'MARINERCDFATETOPOWER':
										    if SN == 'MARINERCDHASPOWER':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 26
							    elif SN > 'MARINERCDMIGHTTOCRITHIT':
								    if SN < 'MARINERCDMIGHTTOPHYMAS':
									    if SN < 'MARINERCDMIGHTTOOUTHEAL':
										    if SN == 'MARINERCDMIGHTTOFINESSE':
										        Result = 1.5
									    elif SN > 'MARINERCDMIGHTTOOUTHEAL':
										    if SN == 'MARINERCDMIGHTTOPARRY':
										        Result = 1
									    else:
									        Result = 2
								    elif SN > 'MARINERCDMIGHTTOPHYMAS':
									    if SN < 'MARINERCDPHYMITTONONPHYMIT':
										    if SN == 'MARINERCDPHYMITTOCOMPHYMIT':
										        Result = 1
									    elif SN > 'MARINERCDPHYMITTONONPHYMIT':
										    if SN == 'MARINERCDTACMASTOOUTHEAL':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 2
							    else:
							        Result = 1.5
						    else:
						        Result = CalcStat("ClassBaseVitality",L)
					    elif SN > 'MARINERCDVITALITYTOICMR':
						    if SN < 'MASTERYT':
							    if SN < 'MARINERCDWILLTORESIST':
								    if SN < 'MARINERCDWILLTOFINESSE':
									    if SN < 'MARINERCDVITALITYTONCMR':
										    if SN == 'MARINERCDVITALITYTOMORALE':
										        Result = 4.5
									    elif SN > 'MARINERCDVITALITYTONCMR':
										    if SN == 'MARINERCDWILLTOCRITHIT':
										        Result = 0.5
									    else:
									        Result = 0.12
								    elif SN > 'MARINERCDWILLTOFINESSE':
									    if SN < 'MARINERCDWILLTOPHYMAS':
										    if SN == 'MARINERCDWILLTOOUTHEAL':
										        Result = 2
									    elif SN > 'MARINERCDWILLTOPHYMAS':
										    if SN == 'MARINERCDWILLTOPHYMIT':
										        Result = 1
									    else:
									        Result = 2
								    else:
								        Result = 1.5
							    elif SN > 'MARINERCDWILLTORESIST':
								    if SN < 'MASTERYCILVLFILTER':
									    if SN < 'MASTERYC':
										    if SN == 'MASTERY':
										        Result = EquSng(StatLinInter("PntMPMastery","ItemPntS","ProgBMastery","AdjItemMas",L,N,0))
									    elif SN > 'MASTERYC':
										    if SN == 'MASTERYCI':
										        Result = RoundDblLotro(CalcStat("MasteryCIRaw",L,N))
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("MasteryCI",CalcStat("MasteryCILvlFilter",N),N),0)
								    elif SN > 'MASTERYCILVLFILTER':
									    if SN < 'MASTERYCRAW':
										    if SN == 'MASTERYCIRAW':
										        Result = StatLinInter("PntMPMasteryC","ItemPntS","ProgBMastery","AdjCreepItem",L,N,4)
									    elif SN > 'MASTERYCRAW':
										    if SN == 'MASTERYOLD':
										        Result = CalcStat("Mastery",L,N)
									    else:
									        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("MasteryCIRaw",CalcStat("MasteryCILvlFilter",N),N),99)
								    else:
								        if 4.6 <= Lp and Lm <= 4.6 or 4.8 <= Lp and Lm <= 4.8 or 7 <= Lp and Lm <= 7 or 9.6 <= Lp and Lm <= 9.6 or 14.4 <= Lp and Lm <= 14.4:
								            Result = 515
								        else:
								            Result = CalcStat("CreepILvlCurr",L)
							    else:
							        Result = 1
						    elif SN > 'MASTERYT':
							    if SN < 'MINCOURAGERESIST':
								    if SN < 'MIGHTCI':
									    if SN < 'MIGHT':
										    if SN == 'MATHOMLVLTOILVL':
										        Result = CalcStat("AwardLvlToILvl",L)
									    elif SN > 'MIGHT':
										    if SN == 'MIGHTC':
										        Result = CalcStat("MainC",L,N)
									    else:
									        Result = CalcStat("Main",L,N)
								    elif SN > 'MIGHTCI':
									    if SN < 'MINCOMPOSURERESIST':
										    if SN == 'MIGHTT':
										        Result = CalcStat("MainT",L,N)
									    elif SN > 'MINCOMPOSURERESIST':
										    if SN == 'MINCOMPOSURETACMIT':
										        Result = CalcStat("TacMitT",L,1.0)
									    else:
									        Result = CalcStat("ResistT",L,1.6)
								    else:
								        Result = CalcStat("MainCI",L,N)
							    elif SN > 'MINCOURAGERESIST':
								    if SN < 'MINPIERCINGBALFINESSE':
									    if SN < 'MINECHOESBATTLERESIST':
										    if SN == 'MINECHOESBATTLECRITDEF':
										        Result = -CalcStat("CritDefT",L,2.0)
									    elif SN > 'MINECHOESBATTLERESIST':
										    if SN == 'MINENDMORALE':
										        Result = CalcStat("MoraleT",L,CalcStat("Trait12345Choice",N)*0.8)
									    else:
									        Result = -CalcStat("SongResistT",L,1.0)
								    elif SN > 'MINPIERCINGBALFINESSE':
									    if SN < 'MINSTRELCDAGILITYTOEVADE':
										    if SN == 'MINSTRELCDAGILITYTOCRITHIT':
										        Result = 2
									    elif SN > 'MINSTRELCDAGILITYTOEVADE':
										    if SN > 'MINSTRELCDAGILITYTOFINESSE':
											    if SN == 'MINSTRELCDAGILITYTOTACMAS':
											        Result = 2
										    elif SN == 'MINSTRELCDAGILITYTOFINESSE':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = CalcStat("FinesseT",L,CalcStat("Trait12345Choice",N)*0.4)
							    else:
							        Result = CalcStat("FearResistT",L,1.0)
						    else:
						        Result = EquSng(StatLinInter("PntMPMastery","TraitPntS","ProgBMastery","AdjTraitMas",L,N,0))
					    else:
					        Result = 0.012
				    else:
				        Result = 3
			    else:
			        Result = CalcStat("ClassBaseFate",L)
		    else:
		        Result = CalcStat("NCMRT",L,1.2)
	    else:
	        Result = CalcStat("PhyMasT",L,0.8)
    elif SN > 'MINSTRELCDARMOURTOCOMPHYMIT':
	    if SN < 'TACMITHPRATPCAPR':
		    if SN < 'PNTMPCLASSBASEICPR':
			    if SN < 'PARTBLOCKPRATPCAP':
				    if SN < 'MITLIGHTPRATPCAP':
					    if SN < 'MINSTRELCDWILLTOBLOCK':
						    if SN < 'MINSTRELCDCALCTYPENONPHYMIT':
							    if SN < 'MINSTRELCDBASEMIGHT':
								    if SN < 'MINSTRELCDBASEAGILITY':
									    if SN < 'MINSTRELCDARMOURTOTACMIT':
										    if SN == 'MINSTRELCDARMOURTONONPHYMIT':
										        Result = 0.2
									    elif SN > 'MINSTRELCDARMOURTOTACMIT':
										    if SN == 'MINSTRELCDARMOURTYPE':
										        Result = 1
									    else:
									        Result = 0.2
								    elif SN > 'MINSTRELCDBASEAGILITY':
									    if SN < 'MINSTRELCDBASEICMR':
										    if SN == 'MINSTRELCDBASEFATE':
										        Result = CalcStat("ClassBaseFate",L)
									    elif SN > 'MINSTRELCDBASEICMR':
										    if SN == 'MINSTRELCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    else:
									        Result = CalcStat("ClassBaseICMRL",L)
								    else:
								        Result = CalcStat("ClassBaseAgilityM",L)
							    elif SN > 'MINSTRELCDBASEMIGHT':
								    if SN < 'MINSTRELCDBASEPOWER':
									    if SN < 'MINSTRELCDBASENCMR':
										    if SN == 'MINSTRELCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    elif SN > 'MINSTRELCDBASENCMR':
										    if SN == 'MINSTRELCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    else:
									        Result = CalcStat("ClassBaseNCMRL",L)
								    elif SN > 'MINSTRELCDBASEPOWER':
									    if SN < 'MINSTRELCDBASEWILL':
										    if SN == 'MINSTRELCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    elif SN > 'MINSTRELCDBASEWILL':
										    if SN == 'MINSTRELCDCALCTYPECOMPHYMIT':
										        Result = 12
									    else:
									        Result = CalcStat("ClassBaseWillH",L)
								    else:
								        Result = CalcStat("ClassBasePower",L)
							    else:
							        Result = CalcStat("ClassBaseMightL",L)
						    elif SN > 'MINSTRELCDCALCTYPENONPHYMIT':
							    if SN < 'MINSTRELCDMIGHTTOTACMAS':
								    if SN < 'MINSTRELCDFATETOPOWER':
									    if SN < 'MINSTRELCDCANBLOCK':
										    if SN == 'MINSTRELCDCALCTYPETACMIT':
										        Result = 25
									    elif SN > 'MINSTRELCDCANBLOCK':
										    if SN == 'MINSTRELCDFATETONCPR':
										        Result = 0.07
									    else:
									        if 20 <= Lp:
									            Result = 1
								    elif SN > 'MINSTRELCDFATETOPOWER':
									    if SN < 'MINSTRELCDMIGHTTOCRITHIT':
										    if SN == 'MINSTRELCDHASPOWER':
										        Result = 1
									    elif SN > 'MINSTRELCDMIGHTTOCRITHIT':
										    if SN == 'MINSTRELCDMIGHTTOOUTHEAL':
										        Result = 2
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'MINSTRELCDMIGHTTOTACMAS':
								    if SN < 'MINSTRELCDTACMASTOOUTHEAL':
									    if SN < 'MINSTRELCDPHYMITTOCOMPHYMIT':
										    if SN == 'MINSTRELCDMIGHTTOTACMIT':
										        Result = 1
									    elif SN > 'MINSTRELCDPHYMITTOCOMPHYMIT':
										    if SN == 'MINSTRELCDPHYMITTONONPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'MINSTRELCDTACMASTOOUTHEAL':
									    if SN < 'MINSTRELCDVITALITYTOMORALE':
										    if SN == 'MINSTRELCDVITALITYTOICMR':
										        Result = 0.012
									    elif SN > 'MINSTRELCDVITALITYTOMORALE':
										    if SN == 'MINSTRELCDVITALITYTONCMR':
										        Result = 0.12
									    else:
									        Result = 4.5
								    else:
								        Result = 1
							    else:
							        Result = 2
						    else:
						        Result = 12
					    elif SN > 'MINSTRELCDWILLTOBLOCK':
						    if SN < 'MINTOTRESISTSEL':
							    if SN < 'MINTIMEECHOESBATTLERESIST':
								    if SN < 'MINSTRELCDWILLTORESIST':
									    if SN < 'MINSTRELCDWILLTOEVADE':
										    if SN == 'MINSTRELCDWILLTOCRITHIT':
										        Result = 1
									    elif SN > 'MINSTRELCDWILLTOEVADE':
										    if SN == 'MINSTRELCDWILLTOPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'MINSTRELCDWILLTORESIST':
									    if SN < 'MINSTRELCDWILLTOTACMIT':
										    if SN == 'MINSTRELCDWILLTOTACMAS':
										        Result = 3
									    elif SN > 'MINSTRELCDWILLTOTACMIT':
										    if SN == 'MINTACMAS':
										        Result = CalcStat("TacMasT",L,CalcStat("Trait123455Choice",N)*0.4)
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'MINTIMEECHOESBATTLERESIST':
								    if SN < 'MINTOTFATESEL':
									    if SN < 'MINTOTCRITHITSEL':
										    if SN == 'MINTOTCRITHIT':
										        Result = CalcStat("CritHitT",L,CalcStat("MinToTCritHitSel",N))
									    elif SN > 'MINTOTCRITHITSEL':
										    if SN == 'MINTOTFATE':
										        Result = CalcStat("FateT",L,CalcStat("MinToTFateSel",N))
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = DataTableValue((0,0,0,0.4,0.6),L)
								    elif SN > 'MINTOTFATESEL':
									    if SN < 'MINTOTFINESSESEL':
										    if SN == 'MINTOTFINESSE':
										        Result = CalcStat("FinesseT",L,CalcStat("MinToTFinesseSel",N))
									    elif SN > 'MINTOTFINESSESEL':
										    if SN == 'MINTOTRESIST':
										        Result = CalcStat("ResistT",L,CalcStat("MinToTResistSel",N))
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = DataTableValue((0,0,0.2,0.4,0.6),L)
								    else:
								        if 1 <= Lp and Lm <= 5:
								            Result = DataTableValue((0.2,0.3,0.4,0.5,0.6),L)
							    else:
							        Result = -CalcStat("SongResistT",L,0.6)
						    elif SN > 'MINTOTRESISTSEL':
							    if SN < 'MITHEAVYPRATPCAP':
								    if SN < 'MITHEAVYPRATP':
									    if SN < 'MINTOTVITALITYSEL':
										    if SN == 'MINTOTVITALITY':
										        Result = CalcStat("VitalityT",L,CalcStat("MinToTVitalitySel",N))
									    elif SN > 'MINTOTVITALITYSEL':
										    if SN == 'MITHEAVYPPRAT':
										        Result = CalcRatAB(CalcStat("MitHeavyPRatPA",L),CalcStat("MitHeavyPRatPB",L),CalcStat("MitHeavyPRatPCapR",L),N)
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = DataTableValue((0,0,0,0,0.4),L)
								    elif SN > 'MITHEAVYPRATP':
									    if SN < 'MITHEAVYPRATPB':
										    if SN == 'MITHEAVYPRATPA':
										        Result = 180
									    elif SN > 'MITHEAVYPRATPB':
										    if SN == 'MITHEAVYPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatMitHeavy")
								    else:
								        Result = CalcPercAB(CalcStat("MitHeavyPRatPA",L),CalcStat("MitHeavyPRatPB",L),CalcStat("MitHeavyPRatPCap",L),N)
							    elif SN > 'MITHEAVYPRATPCAP':
								    if SN < 'MITLIGHTPRATP':
									    if SN < 'MITIGATION':
										    if SN == 'MITHEAVYPRATPCAPR':
										        Result = CalcStat("MitHeavyPRatPB",L)*CalcStat("MitHeavyPRatPC",L)
									    elif SN > 'MITIGATION':
										    if SN == 'MITLIGHTPPRAT':
										        Result = CalcRatAB(CalcStat("MitLightPRatPA",L),CalcStat("MitLightPRatPB",L),CalcStat("MitLightPRatPCapR",L),N)
									    else:
									        Result = EquSng(StatLinInter("PntMPMitigation","ItemPntS","ProgBMitigation","AdjItemMit",L,N,0))
								    elif SN > 'MITLIGHTPRATP':
									    if SN < 'MITLIGHTPRATPB':
										    if SN == 'MITLIGHTPRATPA':
										        Result = 120
									    elif SN > 'MITLIGHTPRATPB':
										    if SN == 'MITLIGHTPRATPC':
										        Result = 0.5
									    else:
									        Result = CalcStat("BRatRounded",L,"BRatMitLight")
								    else:
								        Result = CalcPercAB(CalcStat("MitLightPRatPA",L),CalcStat("MitLightPRatPB",L),CalcStat("MitLightPRatPCap",L),N)
							    else:
							        Result = 60
						    else:
						        if 1 <= Lp and Lm <= 5:
						            Result = DataTableValue((0,0.2,0.3,0.4,0.5),L)
					    else:
					        Result = 1
				    elif SN > 'MITLIGHTPRATPCAP':
					    if SN < 'OUTHEALPRATPC':
						    if SN < 'NCPR':
							    if SN < 'MITMEDIUMPRATPCAPR':
								    if SN < 'MITMEDIUMPRATPA':
									    if SN < 'MITMEDIUMPPRAT':
										    if SN == 'MITLIGHTPRATPCAPR':
										        Result = CalcStat("MitLightPRatPB",L)*CalcStat("MitLightPRatPC",L)
									    elif SN > 'MITMEDIUMPPRAT':
										    if SN == 'MITMEDIUMPRATP':
										        Result = CalcPercAB(CalcStat("MitMediumPRatPA",L),CalcStat("MitMediumPRatPB",L),CalcStat("MitMediumPRatPCap",L),N)
									    else:
									        Result = CalcRatAB(CalcStat("MitMediumPRatPA",L),CalcStat("MitMediumPRatPB",L),CalcStat("MitMediumPRatPCapR",L),N)
								    elif SN > 'MITMEDIUMPRATPA':
									    if SN < 'MITMEDIUMPRATPC':
										    if SN == 'MITMEDIUMPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatMitMedium")
									    elif SN > 'MITMEDIUMPRATPC':
										    if SN == 'MITMEDIUMPRATPCAP':
										        Result = 50
									    else:
									        Result = 0.5
								    else:
								        Result = 150
							    elif SN > 'MITMEDIUMPRATPCAPR':
								    if SN < 'MORALETADJ':
									    if SN < 'MORALEADJ':
										    if SN == 'MORALE':
										        Result = EquSng(StatLinInter("PntMPMorale","ItemPntSVital","ProgBMorale","MoraleAdj",L,N,0))
									    elif SN > 'MORALEADJ':
										    if SN == 'MORALET':
										        Result = EquSng(StatLinInter("PntMPMorale","TraitPntSVital","ProgBMorale","MoraleTAdj",L,N,0))
									    else:
									        if Lm <= 25:
									            Result = 0.5
									        elif Lm <= 50:
									            Result = 0.6
									        elif Lm <= 60:
									            Result = 0.7
									        elif Lm <= 79:
									            Result = 0.8
									        elif Lm <= 80:
									            Result = 0.9
									        else:
									            Result = 1
								    elif SN > 'MORALETADJ':
									    if SN < 'NCMR':
										    if SN == 'N':
										        Result = N
									    elif SN > 'NCMR':
										    if SN == 'NCMRT':
										        Result = EquSng(StatLinInter("PntMPNCMR","TraitPntSVital","ProgBNCMR","",L,N,1))
									    else:
									        Result = EquSng(StatLinInter("PntMPNCMR","ItemPntSVital","ProgBNCMR","",L,N,1))
								    else:
								        if Lm <= 25:
								            Result = 0.5
								        elif Lm <= 50:
								            Result = 0.6
								        elif Lm <= 60:
								            Result = 0.7
								        elif Lm <= 65:
								            Result = 0.8
								        elif Lm <= 75:
								            Result = 0.9
								        else:
								            Result = 1
							    else:
							        Result = CalcStat("MitMediumPRatPB",L)*CalcStat("MitMediumPRatPC",L)
						    elif SN > 'NCPR':
							    if SN < 'OUTDMGPRATPC':
								    if SN < 'OUTDMGPPRAT':
									    if SN < 'OFFSET':
										    if SN == 'NCPRT':
										        Result = EquSng(StatLinInter("PntMPNCPR","TraitPntSVital","ProgBNCPR","",L,N,99))
									    elif SN > 'OFFSET':
										    if SN == 'ORCMIT':
										        Result = EquSng(StatLinInter("PntMPOrcMit","ItemPntS","ProgBMitigation","AdjItemMit",L,N,0))
									    else:
									        Result = L+N
								    elif SN > 'OUTDMGPPRAT':
									    if SN < 'OUTDMGPRATPA':
										    if SN == 'OUTDMGPRATP':
										        Result = CalcPercAB(CalcStat("OutDmgPRatPA",L),CalcStat("OutDmgPRatPB",L),CalcStat("OutDmgPRatPCap",L),N)
									    elif SN > 'OUTDMGPRATPA':
										    if SN == 'OUTDMGPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatExtra")
									    else:
									        Result = 600
								    else:
								        Result = CalcRatAB(CalcStat("OutDmgPRatPA",L),CalcStat("OutDmgPRatPB",L),CalcStat("OutDmgPRatPCapR",L),N)
							    elif SN > 'OUTDMGPRATPC':
								    if SN < 'OUTHEALPPRAT':
									    if SN < 'OUTDMGPRATPCAPR':
										    if SN == 'OUTDMGPRATPCAP':
										        Result = 200
									    elif SN > 'OUTDMGPRATPCAPR':
										    if SN == 'OUTHEAL':
										        Result = EquSng(StatLinInter("PntMPOutHeal","ItemPntS","ProgBOutHeal","AdjItem",L,N,0))
									    else:
									        Result = CalcStat("OutDmgPRatPB",L)*CalcStat("OutDmgPRatPC",L)
								    elif SN > 'OUTHEALPPRAT':
									    if SN < 'OUTHEALPRATPA':
										    if SN == 'OUTHEALPRATP':
										        Result = CalcPercAB(CalcStat("OutHealPRatPA",L),CalcStat("OutHealPRatPB",L),CalcStat("OutHealPRatPCap",L),N)
									    elif SN > 'OUTHEALPRATPA':
										    if SN == 'OUTHEALPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatOutHeal")
									    else:
									        Result = 210
								    else:
								        Result = CalcRatAB(CalcStat("OutHealPRatPA",L),CalcStat("OutHealPRatPB",L),CalcStat("OutHealPRatPCapR",L),N)
							    else:
							        Result = 0.5
						    else:
						        Result = EquSng(StatLinInter("PntMPNCPR","ItemPntSClassic","ProgBNCPR","",L,N,99))
					    elif SN > 'OUTHEALPRATPC':
						    if SN < 'PARRYPRATPCAPR':
							    if SN < 'PARRYCRAW':
								    if SN < 'PARRY':
									    if SN < 'OUTHEALPRATPCAPR':
										    if SN == 'OUTHEALPRATPCAP':
										        Result = 70
									    elif SN > 'OUTHEALPRATPCAPR':
										    if SN == 'OUTHEALT':
										        Result = EquSng(StatLinInter("PntMPOutHeal","TraitPntS","ProgBOutHeal","AdjTrait",L,N,0))
									    else:
									        Result = CalcStat("OutHealPRatPB",L)*CalcStat("OutHealPRatPC",L)
								    elif SN > 'PARRY':
									    if SN < 'PARRYCI':
										    if SN == 'PARRYC':
										        Result = CalcStat("BPEC",L,N)
									    elif SN > 'PARRYCI':
										    if SN == 'PARRYCIRAW':
										        Result = CalcStat("BPECIRAW",L,N)
									    else:
									        Result = CalcStat("BPECI",L,N)
								    else:
								        Result = CalcStat("BPE",L,N)
							    elif SN > 'PARRYCRAW':
								    if SN < 'PARRYPRATPA':
									    if SN < 'PARRYPPRAT':
										    if SN == 'PARRYPBONUS':
										        Result = CalcStat("BPEPBonus",L)
									    elif SN > 'PARRYPPRAT':
										    if SN == 'PARRYPRATP':
										        Result = CalcStat("BPEPRatP",L,N)
									    else:
									        Result = CalcStat("BPEPPRat",L,N)
								    elif SN > 'PARRYPRATPA':
									    if SN < 'PARRYPRATPC':
										    if SN == 'PARRYPRATPB':
										        Result = CalcStat("BPEPRatPB",L)
									    elif SN > 'PARRYPRATPC':
										    if SN == 'PARRYPRATPCAP':
										        Result = CalcStat("BPEPRatPCap",L)
									    else:
									        Result = CalcStat("BPEPRatPC",L)
								    else:
								        Result = CalcStat("BPEPRatPA",L)
							    else:
							        Result = CalcStat("BPECRAW",L,N)
						    elif SN > 'PARRYPRATPCAPR':
							    if SN < 'PARTBLOCKMITPRATPCAP':
								    if SN < 'PARTBLOCKMITPRATP':
									    if SN < 'PARTBLOCKMITPBONUS':
										    if SN == 'PARRYT':
										        Result = CalcStat("BPET",L,N)
									    elif SN > 'PARTBLOCKMITPBONUS':
										    if SN == 'PARTBLOCKMITPPRAT':
										        Result = CalcStat("PartMitPPRat",L,N)
									    else:
									        Result = CalcStat("PartMitPBonus",L)
								    elif SN > 'PARTBLOCKMITPRATP':
									    if SN < 'PARTBLOCKMITPRATPB':
										    if SN == 'PARTBLOCKMITPRATPA':
										        Result = CalcStat("PartMitPRatPA",L)
									    elif SN > 'PARTBLOCKMITPRATPB':
										    if SN == 'PARTBLOCKMITPRATPC':
										        Result = CalcStat("PartMitPRatPC",L)
									    else:
									        Result = CalcStat("PartMitPRatPB",L)
								    else:
								        Result = CalcStat("PartMitPRatP",L,N)
							    elif SN > 'PARTBLOCKMITPRATPCAP':
								    if SN < 'PARTBLOCKPRATP':
									    if SN < 'PARTBLOCKPBONUS':
										    if SN == 'PARTBLOCKMITPRATPCAPR':
										        Result = CalcStat("PartMitPRatPCapR",L)
									    elif SN > 'PARTBLOCKPBONUS':
										    if SN == 'PARTBLOCKPPRAT':
										        Result = CalcStat("PartBPEPPRat",L,N)
									    else:
									        Result = CalcStat("PartBPEPBonus",L)
								    elif SN > 'PARTBLOCKPRATP':
									    if SN < 'PARTBLOCKPRATPB':
										    if SN == 'PARTBLOCKPRATPA':
										        Result = CalcStat("PartBPEPRatPA",L)
									    elif SN > 'PARTBLOCKPRATPB':
										    if SN == 'PARTBLOCKPRATPC':
										        Result = CalcStat("PartBPEPRatPC",L)
									    else:
									        Result = CalcStat("PartBPEPRatPB",L)
								    else:
								        Result = CalcStat("PartBPEPRatP",L,N)
							    else:
							        Result = CalcStat("PartMitPRatPCap",L)
						    else:
						        Result = CalcStat("BPEPRatPCapR",L)
					    else:
					        Result = 0.5
				    else:
				        Result = 40
			    elif SN > 'PARTBLOCKPRATPCAP':
				    if SN < 'PERKNCMR':
					    if SN < 'PARTFINESSEPPRAT':
						    if SN < 'PARTEVADEMITPRATPCAPR':
							    if SN < 'PARTBPEPRATPCAPR':
								    if SN < 'PARTBPEPRATPA':
									    if SN < 'PARTBPEPPRAT':
										    if SN == 'PARTBLOCKPRATPCAPR':
										        Result = CalcStat("PartBPEPRatPCapR",L)
									    elif SN > 'PARTBPEPPRAT':
										    if SN == 'PARTBPEPRATP':
										        Result = CalcPercAB(CalcStat("PartBPEPRatPA",L),CalcStat("PartBPEPRatPB",L),CalcStat("PartBPEPRatPCap",L),N)
									    else:
									        Result = CalcRatAB(CalcStat("PartBPEPRatPA",L),CalcStat("PartBPEPRatPB",L),CalcStat("PartBPEPRatPCapR",L),N)
								    elif SN > 'PARTBPEPRATPA':
									    if SN < 'PARTBPEPRATPC':
										    if SN == 'PARTBPEPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatPartBPE")
									    elif SN > 'PARTBPEPRATPC':
										    if SN == 'PARTBPEPRATPCAP':
										        Result = 25
									    else:
									        Result = 0.5
								    else:
								        Result = 75
							    elif SN > 'PARTBPEPRATPCAPR':
								    if SN < 'PARTEVADEMITPRATPA':
									    if SN < 'PARTEVADEMITPPRAT':
										    if SN == 'PARTEVADEMITPBONUS':
										        Result = CalcStat("PartMitPBonus",L)
									    elif SN > 'PARTEVADEMITPPRAT':
										    if SN == 'PARTEVADEMITPRATP':
										        Result = CalcStat("PartMitPRatP",L,N)
									    else:
									        Result = CalcStat("PartMitPPRat",L,N)
								    elif SN > 'PARTEVADEMITPRATPA':
									    if SN < 'PARTEVADEMITPRATPC':
										    if SN == 'PARTEVADEMITPRATPB':
										        Result = CalcStat("PartMitPRatPB",L)
									    elif SN > 'PARTEVADEMITPRATPC':
										    if SN == 'PARTEVADEMITPRATPCAP':
										        Result = CalcStat("PartMitPRatPCap",L)
									    else:
									        Result = CalcStat("PartMitPRatPC",L)
								    else:
								        Result = CalcStat("PartMitPRatPA",L)
							    else:
							        Result = CalcStat("PartBPEPRatPB",L)*CalcStat("PartBPEPRatPC",L)
						    elif SN > 'PARTEVADEMITPRATPCAPR':
							    if SN < 'PARTEVADEPRATPCAPR':
								    if SN < 'PARTEVADEPRATPA':
									    if SN < 'PARTEVADEPPRAT':
										    if SN == 'PARTEVADEPBONUS':
										        Result = CalcStat("PartBPEPBonus",L)
									    elif SN > 'PARTEVADEPPRAT':
										    if SN == 'PARTEVADEPRATP':
										        Result = CalcStat("PartBPEPRatP",L,N)
									    else:
									        Result = CalcStat("PartBPEPPRat",L,N)
								    elif SN > 'PARTEVADEPRATPA':
									    if SN < 'PARTEVADEPRATPC':
										    if SN == 'PARTEVADEPRATPB':
										        Result = CalcStat("PartBPEPRatPB",L)
									    elif SN > 'PARTEVADEPRATPC':
										    if SN == 'PARTEVADEPRATPCAP':
										        Result = CalcStat("PartBPEPRatPCap",L)
									    else:
									        Result = CalcStat("PartBPEPRatPC",L)
								    else:
								        Result = CalcStat("PartBPEPRatPA",L)
							    elif SN > 'PARTEVADEPRATPCAPR':
								    if SN < 'PARTFINESSEDMGPRATPB':
									    if SN < 'PARTFINESSEDMGPRATP':
										    if SN == 'PARTFINESSEDMGPPRAT':
										        Result = CalcRatAB(CalcStat("PartFinesseDmgPRatPA",L),CalcStat("PartFinesseDmgPRatPB",L),CalcStat("PartFinesseDmgPRatPCapR",L),N)
									    elif SN > 'PARTFINESSEDMGPRATP':
										    if SN == 'PARTFINESSEDMGPRATPA':
										        Result = 150
									    else:
									        Result = CalcPercAB(CalcStat("PartFinesseDmgPRatPA",L),CalcStat("PartFinesseDmgPRatPB",L),CalcStat("PartFinesseDmgPRatPCap",L),N)
								    elif SN > 'PARTFINESSEDMGPRATPB':
									    if SN < 'PARTFINESSEDMGPRATPCAP':
										    if SN == 'PARTFINESSEDMGPRATPC':
										        Result = 0.5
									    elif SN > 'PARTFINESSEDMGPRATPCAP':
										    if SN == 'PARTFINESSEDMGPRATPCAPR':
										        Result = CalcStat("PartFinesseDmgPRatPB",L)*CalcStat("PartFinesseDmgPRatPC",L)
									    else:
									        Result = 50
								    else:
								        Result = CalcStat("BRatRounded",L,"BRatStandard")
							    else:
							        Result = CalcStat("PartBPEPRatPCapR",L)
						    else:
						        Result = CalcStat("PartMitPRatPCapR",L)
					    elif SN > 'PARTFINESSEPPRAT':
						    if SN < 'PARTPARRYMITPPRAT':
							    if SN < 'PARTMITPPRAT':
								    if SN < 'PARTFINESSEPRATPC':
									    if SN < 'PARTFINESSEPRATPA':
										    if SN == 'PARTFINESSEPRATP':
										        Result = CalcPercAB(CalcStat("PartFinessePRatPA",L),CalcStat("PartFinessePRatPB",L),CalcStat("PartFinessePRatPCap",L),N)
									    elif SN > 'PARTFINESSEPRATPA':
										    if SN == 'PARTFINESSEPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatStandard")
									    else:
									        Result = 150
								    elif SN > 'PARTFINESSEPRATPC':
									    if SN < 'PARTFINESSEPRATPCAPR':
										    if SN == 'PARTFINESSEPRATPCAP':
										        Result = 50
									    elif SN > 'PARTFINESSEPRATPCAPR':
										    if SN == 'PARTMITPBONUS':
										        Result = 0.1
									    else:
									        Result = CalcStat("PartFinessePRatPB",L)*CalcStat("PartFinessePRatPC",L)
								    else:
								        Result = 0.5
							    elif SN > 'PARTMITPPRAT':
								    if SN < 'PARTMITPRATPC':
									    if SN < 'PARTMITPRATPA':
										    if SN == 'PARTMITPRATP':
										        Result = CalcPercAB(CalcStat("PartMitPRatPA",L),CalcStat("PartMitPRatPB",L),CalcStat("PartMitPRatPCap",L),N)
									    elif SN > 'PARTMITPRATPA':
										    if SN == 'PARTMITPRATPB':
										        Result = CalcStat("BRatRounded",L,"BRatPartBPE")
									    else:
									        Result = 105
								    elif SN > 'PARTMITPRATPC':
									    if SN < 'PARTMITPRATPCAPR':
										    if SN == 'PARTMITPRATPCAP':
										        Result = 35
									    elif SN > 'PARTMITPRATPCAPR':
										    if SN == 'PARTPARRYMITPBONUS':
										        Result = CalcStat("PartMitPBonus",L)
									    else:
									        Result = CalcStat("PartMitPRatPB",L)*CalcStat("PartMitPRatPC",L)
								    else:
								        Result = 0.5
							    else:
							        Result = CalcRatAB(CalcStat("PartMitPRatPA",L),CalcStat("PartMitPRatPB",L),CalcStat("PartMitPRatPCapR",L),N)
						    elif SN > 'PARTPARRYMITPPRAT':
							    if SN < 'PARTPARRYPPRAT':
								    if SN < 'PARTPARRYMITPRATPC':
									    if SN < 'PARTPARRYMITPRATPA':
										    if SN == 'PARTPARRYMITPRATP':
										        Result = CalcStat("PartMitPRatP",L,N)
									    elif SN > 'PARTPARRYMITPRATPA':
										    if SN == 'PARTPARRYMITPRATPB':
										        Result = CalcStat("PartMitPRatPB",L)
									    else:
									        Result = CalcStat("PartMitPRatPA",L)
								    elif SN > 'PARTPARRYMITPRATPC':
									    if SN < 'PARTPARRYMITPRATPCAPR':
										    if SN == 'PARTPARRYMITPRATPCAP':
										        Result = CalcStat("PartMitPRatPCap",L)
									    elif SN > 'PARTPARRYMITPRATPCAPR':
										    if SN == 'PARTPARRYPBONUS':
										        Result = CalcStat("PartBPEPBonus",L)
									    else:
									        Result = CalcStat("PartMitPRatPCapR",L)
								    else:
								        Result = CalcStat("PartMitPRatPC",L)
							    elif SN > 'PARTPARRYPPRAT':
								    if SN < 'PARTPARRYPRATPC':
									    if SN < 'PARTPARRYPRATPA':
										    if SN == 'PARTPARRYPRATP':
										        Result = CalcStat("PartBPEPRatP",L,N)
									    elif SN > 'PARTPARRYPRATPA':
										    if SN == 'PARTPARRYPRATPB':
										        Result = CalcStat("PartBPEPRatPB",L)
									    else:
									        Result = CalcStat("PartBPEPRatPA",L)
								    elif SN > 'PARTPARRYPRATPC':
									    if SN < 'PARTPARRYPRATPCAPR':
										    if SN == 'PARTPARRYPRATPCAP':
										        Result = CalcStat("PartBPEPRatPCap",L)
									    elif SN > 'PARTPARRYPRATPCAPR':
										    if SN == 'PERKMORALE':
										        if 1 <= Lp and Lm <= 4:
										            Result = DataTableValue((10,20,30,40),L)
									    else:
									        Result = CalcStat("PartBPEPRatPCapR",L)
								    else:
								        Result = CalcStat("PartBPEPRatPC",L)
							    else:
							        Result = CalcStat("PartBPEPPRat",L,N)
						    else:
						        Result = CalcStat("PartMitPPRat",L,N)
					    else:
					        Result = CalcRatAB(CalcStat("PartFinessePRatPA",L),CalcStat("PartFinessePRatPB",L),CalcStat("PartFinessePRatPCapR",L),N)
				    elif SN > 'PERKNCMR':
					    if SN < 'PHYMITHPRATPCAP':
						    if SN < 'PHYMASCIRAW':
							    if SN < 'PHYDMGPRATPA':
								    if SN < 'PERKTACMIT':
									    if SN < 'PERKPHYMIT':
										    if SN == 'PERKNCPR':
										        Result = CalcStat("FoodNCPRL",L)
									    elif SN > 'PERKPHYMIT':
										    if SN == 'PERKPOWER':
										        if 1 <= Lp and Lm <= 4:
										            Result = DataTableValue((10,20,30,40),L)
									    else:
									        Result = CalcStat("PhyMitT",L,0.2*N)
								    elif SN > 'PERKTACMIT':
									    if SN < 'PHYDMGPPRAT':
										    if SN == 'PHYDMGPBONUS':
										        Result = CalcStat("OutDmgPBonus",L)
									    elif SN > 'PHYDMGPPRAT':
										    if SN == 'PHYDMGPRATP':
										        Result = CalcStat("OutDmgPRatP",L,N)
									    else:
									        Result = CalcStat("OutDmgPPRat",L,N)
								    else:
								        Result = CalcStat("TacMitT",L,0.2*N)
							    elif SN > 'PHYDMGPRATPA':
								    if SN < 'PHYDMGPRATPCAPR':
									    if SN < 'PHYDMGPRATPC':
										    if SN == 'PHYDMGPRATPB':
										        Result = CalcStat("OutDmgPRatPB",L)
									    elif SN > 'PHYDMGPRATPC':
										    if SN == 'PHYDMGPRATPCAP':
										        Result = CalcStat("OutDmgPRatPCap",L)
									    else:
									        Result = CalcStat("OutDmgPRatPC",L)
								    elif SN > 'PHYDMGPRATPCAPR':
									    if SN < 'PHYMASC':
										    if SN == 'PHYMAS':
										        Result = CalcStat("Mastery",L,N)
									    elif SN > 'PHYMASC':
										    if SN == 'PHYMASCI':
										        Result = CalcStat("MasteryCI",L,N)
									    else:
									        Result = CalcStat("MasteryC",L,N)
								    else:
								        Result = CalcStat("OutDmgPRatPCapR",L)
							    else:
							        Result = CalcStat("OutDmgPRatPA",L)
						    elif SN > 'PHYMASCIRAW':
							    if SN < 'PHYMITCIRAW':
								    if SN < 'PHYMIT':
									    if SN < 'PHYMASOLD':
										    if SN == 'PHYMASCRAW':
										        Result = CalcStat("MasteryCRaw",L,N)
									    elif SN > 'PHYMASOLD':
										    if SN == 'PHYMAST':
										        Result = CalcStat("MasteryT",L,N)
									    else:
									        Result = CalcStat("Mastery",L,N)
								    elif SN > 'PHYMIT':
									    if SN < 'PHYMITCI':
										    if SN == 'PHYMITC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("PhyMitCI",CalcStat("PhyMitCILvlFilter",N),N),0)
									    elif SN > 'PHYMITCI':
										    if SN == 'PHYMITCILVLFILTER':
										        if 3.8 <= Lp and Lm <= 3.8 or 8.2 <= Lp and Lm <= 8.2 or 14.4 <= Lp and Lm <= 14.4 or 19.1 <= Lp and Lm <= 19.1 or 23.125 <= Lp and Lm <= 23.125 or 26.5 <= Lp and Lm <= 26.5:
										            Result = 515
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    else:
									        Result = RoundDblLotro(CalcStat("PhyMitCIRaw",L,N))
								    else:
								        Result = EquSng(StatLinInter("PntMPPhyMit","ItemPntS","ProgBMitigation","AdjItemMit",L,N,0))
							    elif SN > 'PHYMITCIRAW':
								    if SN < 'PHYMITHPRATP':
									    if SN < 'PHYMITHPBONUS':
										    if SN == 'PHYMITCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("PhyMitCIRaw",CalcStat("PhyMitCILvlFilter",N),N),99)
									    elif SN > 'PHYMITHPBONUS':
										    if SN == 'PHYMITHPPRAT':
										        Result = CalcStat("MitHeavyPPRat",L,N)
									    else:
									        Result = CalcStat("MitHeavyPBonus",L)
								    elif SN > 'PHYMITHPRATP':
									    if SN < 'PHYMITHPRATPB':
										    if SN == 'PHYMITHPRATPA':
										        Result = CalcStat("MitHeavyPRatPA",L)
									    elif SN > 'PHYMITHPRATPB':
										    if SN == 'PHYMITHPRATPC':
										        Result = CalcStat("MitHeavyPRatPC",L)
									    else:
									        Result = CalcStat("MitHeavyPRatPB",L)
								    else:
								        Result = CalcStat("MitHeavyPRatP",L,N)
							    else:
							        Result = StatLinInter("PntMPPhyMitC","ItemPntS","ProgBMitigation","AdjCreepItemMit",L,N,4)
						    else:
						        Result = CalcStat("MasteryCIRaw",L,N)
					    elif SN > 'PHYMITHPRATPCAP':
						    if SN < 'PHYMITMPRATPCAP':
							    if SN < 'PHYMITLPRATPCAP':
								    if SN < 'PHYMITLPRATP':
									    if SN < 'PHYMITLPBONUS':
										    if SN == 'PHYMITHPRATPCAPR':
										        Result = CalcStat("MitHeavyPRatPCapR",L)
									    elif SN > 'PHYMITLPBONUS':
										    if SN == 'PHYMITLPPRAT':
										        Result = CalcStat("MitLightPPRat",L,N)
									    else:
									        Result = CalcStat("MitLightPBonus",L)
								    elif SN > 'PHYMITLPRATP':
									    if SN < 'PHYMITLPRATPB':
										    if SN == 'PHYMITLPRATPA':
										        Result = CalcStat("MitLightPRatPA",L)
									    elif SN > 'PHYMITLPRATPB':
										    if SN == 'PHYMITLPRATPC':
										        Result = CalcStat("MitLightPRatPC",L)
									    else:
									        Result = CalcStat("MitLightPRatPB",L)
								    else:
								        Result = CalcStat("MitLightPRatP",L,N)
							    elif SN > 'PHYMITLPRATPCAP':
								    if SN < 'PHYMITMPRATP':
									    if SN < 'PHYMITMPBONUS':
										    if SN == 'PHYMITLPRATPCAPR':
										        Result = CalcStat("MitLightPRatPCapR",L)
									    elif SN > 'PHYMITMPBONUS':
										    if SN == 'PHYMITMPPRAT':
										        Result = CalcStat("MitMediumPPRat",L,N)
									    else:
									        Result = CalcStat("MitMediumPBonus",L)
								    elif SN > 'PHYMITMPRATP':
									    if SN < 'PHYMITMPRATPB':
										    if SN == 'PHYMITMPRATPA':
										        Result = CalcStat("MitMediumPRatPA",L)
									    elif SN > 'PHYMITMPRATPB':
										    if SN == 'PHYMITMPRATPC':
										        Result = CalcStat("MitMediumPRatPC",L)
									    else:
									        Result = CalcStat("MitMediumPRatPB",L)
								    else:
								        Result = CalcStat("MitMediumPRatP",L,N)
							    else:
							        Result = CalcStat("MitLightPRatPCap",L)
						    elif SN > 'PHYMITMPRATPCAP':
							    if SN < 'PLAYERBASEPHYMAS':
								    if SN < 'PHYRESISTT':
									    if SN < 'PHYMITT':
										    if SN == 'PHYMITMPRATPCAPR':
										        Result = CalcStat("MitMediumPRatPCapR",L)
									    elif SN > 'PHYMITT':
										    if SN == 'PHYRESIST':
										        Result = CalcStat("ResistAdd",L,N)
									    else:
									        Result = EquSng(StatLinInter("PntMPPhyMit","TraitPntS","ProgBMitigation","AdjTraitMit",L,N,0))
								    elif SN > 'PHYRESISTT':
									    if SN < 'PLAYERBASEMORALE':
										    if SN == 'PLAYERBASEEVADE':
										        Result = 1
									    elif SN > 'PLAYERBASEMORALE':
										    if SN == 'PLAYERBASEPARRY':
										        Result = 3
									    else:
									        Result = 52.5
								    else:
								        Result = CalcStat("ResistAddT",L,N)
							    elif SN > 'PLAYERBASEPHYMAS':
								    if SN < 'PNTMPARMOURPENT':
									    if SN < 'PNTMPARMOUR':
										    if SN == 'PLAYERBASETACMAS':
										        Result = 11.5
									    elif SN > 'PNTMPARMOUR':
										    if SN == 'PNTMPARMOURC':
										        Result = 20/1200
									    else:
									        Result = 4.4/1200
								    elif SN > 'PNTMPARMOURPENT':
									    if SN < 'PNTMPARMOURVIRTUES':
										    if SN == 'PNTMPARMOURT':
										        Result = 25/1200
									    elif SN > 'PNTMPARMOURVIRTUES':
										    if SN > 'PNTMPBPE':
											    if SN == 'PNTMPBPEC':
											        Result = 20/1200
										    elif SN == 'PNTMPBPE':
										        Result = 42/1200
									    else:
									        Result = 24/1200
								    else:
								        Result = 72/1200
							    else:
							        Result = 11.5
						    else:
						        Result = CalcStat("MitMediumPRatPCap",L)
					    else:
					        Result = CalcStat("MitHeavyPRatPCap",L)
				    else:
				        Result = CalcStat("FoodNCMRL",L)
			    else:
			        Result = CalcStat("PartBPEPRatPCap",L)
		    elif SN > 'PNTMPCLASSBASEICPR':
			    if SN < 'RIVERHOBBITRDTRAITFROSTMITP':
				    if SN < 'PROGBINHEAL':
					    if SN < 'PNTMPPHYMITC':
						    if SN < 'PNTMPICMRDEBUFFT':
							    if SN < 'PNTMPDMGTYPEMITT':
								    if SN < 'PNTMPCRITDEFC':
									    if SN < 'PNTMPCOMBATDAMAGEMOD':
										    if SN == 'PNTMPCLASSBASENCPR':
										        Result = 0.5
									    elif SN > 'PNTMPCOMBATDAMAGEMOD':
										    if SN == 'PNTMPCRITDEF':
										        Result = 40/1200
									    else:
									        Result = 0.5
								    elif SN > 'PNTMPCRITDEFC':
									    if SN < 'PNTMPCRITHITC':
										    if SN == 'PNTMPCRITHIT':
										        Result = 20/1200
									    elif SN > 'PNTMPCRITHITC':
										    if SN == 'PNTMPDMGTYPEMIT':
										        Result = 24/1200
									    else:
									        Result = 20/1200
								    else:
								        Result = 0.01667
							    elif SN > 'PNTMPDMGTYPEMITT':
								    if SN < 'PNTMPFINESSET':
									    if SN < 'PNTMPFINESSE':
										    if SN == 'PNTMPFATE':
										        Result = 2.5
									    elif SN > 'PNTMPFINESSE':
										    if SN == 'PNTMPFINESSEC':
										        Result = 0.01667
									    else:
									        Result = 40/1200
								    elif SN > 'PNTMPFINESSET':
									    if SN < 'PNTMPICMR':
										    if SN == 'PNTMPFOODRESIST':
										        Result = 30/1200
									    elif SN > 'PNTMPICMR':
										    if SN == 'PNTMPICMRC':
										        Result = 23.5/1200
									    else:
									        Result = 0.03
								    else:
								        Result = 36/1200
							    else:
							        Result = 60/1200
						    elif SN > 'PNTMPICMRDEBUFFT':
							    if SN < 'PNTMPMITIGATION':
								    if SN < 'PNTMPMAIN':
									    if SN < 'PNTMPICPRC':
										    if SN == 'PNTMPICPR':
										        Result = 0.125
									    elif SN > 'PNTMPICPRC':
										    if SN == 'PNTMPINHEAL':
										        Result = 40/1200
									    else:
									        Result = 23.5/1200
								    elif SN > 'PNTMPMAIN':
									    if SN < 'PNTMPMASTERY':
										    if SN == 'PNTMPMAINC':
										        Result = 199.75/1200
									    elif SN > 'PNTMPMASTERY':
										    if SN == 'PNTMPMASTERYC':
										        Result = 20/1200
									    else:
									        Result = 17/1200
								    else:
								        Result = 0.5
							    elif SN > 'PNTMPMITIGATION':
								    if SN < 'PNTMPNCPR':
									    if SN < 'PNTMPMORALEVIRTUES':
										    if SN == 'PNTMPMORALE':
										        Result = 2
									    elif SN > 'PNTMPMORALEVIRTUES':
										    if SN == 'PNTMPNCMR':
										        Result = 0.3
									    else:
									        Result = 1.5
								    elif SN > 'PNTMPNCPR':
									    if SN < 'PNTMPOUTHEAL':
										    if SN == 'PNTMPORCMIT':
										        Result = 19.2/1200
									    elif SN > 'PNTMPOUTHEAL':
										    if SN == 'PNTMPPHYMIT':
										        Result = 36/1200
									    else:
									        Result = 30/1200
								    else:
								        Result = 1
							    else:
							        Result = 28/1200
						    else:
						        Result = 0.076
					    elif SN > 'PNTMPPHYMITC':
						    if SN < 'PROGBARMOUR':
							    if SN < 'PNTMPTACMITC':
								    if SN < 'PNTMPRESISTC':
									    if SN < 'PNTMPPOWERT':
										    if SN == 'PNTMPPOWER':
										        Result = 2
									    elif SN > 'PNTMPPOWERT':
										    if SN == 'PNTMPRESIST':
										        Result = 36/1200
									    else:
									        Result = 1.333
								    elif SN > 'PNTMPRESISTC':
									    if SN < 'PNTMPTACHPS':
										    if SN == 'PNTMPSHIELDBLOCK':
										        Result = 80/1200
									    elif SN > 'PNTMPTACHPS':
										    if SN == 'PNTMPTACMIT':
										        Result = 36/1200
									    else:
									        Result = 0.175
								    else:
								        Result = 20/1200
							    elif SN > 'PNTMPTACMITC':
								    if SN < 'POISONRESIST':
									    if SN < 'PNTMPVITALITYC':
										    if SN == 'PNTMPVITALITY':
										        Result = 0.35
									    elif SN > 'PNTMPVITALITYC':
										    if SN == 'PNTMPVITALITYT':
										        Result = 0.45
									    else:
									        Result = 398.6/1200
								    elif SN > 'POISONRESIST':
									    if SN < 'POWER':
										    if SN == 'POISONRESISTT':
										        Result = CalcStat("ResistAddT",L,N)
									    elif SN > 'POWER':
										    if SN == 'POWERT':
										        Result = EquSng(StatLinInter("PntMPPowerT","TraitPntSVital","ProgBPower","",L,N,0))
									    else:
									        Result = EquSng(StatLinInter("PntMPPower","ItemPntSVital","ProgBPower","",L,N,0))
								    else:
								        Result = CalcStat("ResistAdd",L,N)
							    else:
							        Result = 20/1200
						    elif SN > 'PROGBARMOUR':
							    if SN < 'PROGBDAMAGENOIMP':
								    if SN < 'PROGBBPE':
									    if SN < 'PROGBARMOURLIGHT':
										    if SN == 'PROGBARMOURHEAVY':
										        Result = CalcStat("BRatProgB",L,"BRatMitHeavy")
									    elif SN > 'PROGBARMOURLIGHT':
										    if SN == 'PROGBARMOURMEDIUM':
										        Result = CalcStat("BRatProgB",L,"BRatMitMedium")
									    else:
									        Result = CalcStat("BRatProgB",L,"BRatMitLight")
								    elif SN > 'PROGBBPE':
									    if SN < 'PROGBCRITHIT':
										    if SN == 'PROGBCRITDEF':
										        Result = CalcStat("BRatProgB",L,"BRatStandard")
									    elif SN > 'PROGBCRITHIT':
										    if SN == 'PROGBDAMAGE':
										        Result = CalcStat("StdProgDamage",L,2.0)
									    else:
									        Result = CalcStat("BRatProgB",L,"BRatExtra")
								    else:
								        Result = CalcStat("BRatProgB",L,"BRatStandard")
							    elif SN > 'PROGBDAMAGENOIMP':
								    if SN < 'PROGBFINESSE':
									    if SN < 'PROGBENERGY':
										    if SN == 'PROGBDAMAGENOIMPADJ':
										        if Lm <= 50:
										            Result = LinFmod(1,1.25,3,1,50,L)
										        elif Lm <= 100:
										            Result = LinFmod(1,3,4.5,50,100,L)
										        else:
										            Result = LinFmod(1,4.5,5,100,140,L)
									    elif SN > 'PROGBENERGY':
										    if SN == 'PROGBFATE':
										        Result = CalcStat("ProgBEnergy",L)
									    else:
									        Result = CalcStat("StdProgEnergy",L,2.0)
								    elif SN > 'PROGBFINESSE':
									    if SN < 'PROGBICMR':
										    if SN == 'PROGBHEALTH':
										        Result = CalcStat("StdProgHealth",L,4.0)
									    elif SN > 'PROGBICMR':
										    if SN == 'PROGBICPR':
										        Result = CalcStat("ProgBEnergy",L)
									    else:
									        Result = CalcStat("ProgBHealth",L)
								    else:
								        Result = CalcStat("BRatProgB",L,"BRatStandard")
							    else:
							        Result = StatLinInter("","TraitPntSVital","ProgBDamage","ProgBDamageNoImpAdj",L,N,99)
						    else:
						        Result = CalcStat("BRatProgB",L,"BRatMitMedium")
					    else:
					        Result = 20/1200
				    elif SN > 'PROGBINHEAL':
					    if SN < 'REPFATEL':
						    if SN < 'PROGEXTCOMLOWRND':
							    if SN < 'PROGBOUTHEAL':
								    if SN < 'PROGBMITIGATION':
									    if SN < 'PROGBMAINBASE':
										    if SN == 'PROGBMAIN':
										        Result = CalcStat("StdProgRatings",L,1.75)
									    elif SN > 'PROGBMAINBASE':
										    if SN == 'PROGBMASTERY':
										        Result = CalcStat("BRatProgB",L,"BRatExtra")
									    else:
									        if 141 <= Lp and Lm <= 150:
									            Result = LinFmod(CalcStat("StdProgRatings",140,1.0),1.15,2,141,150,L,"P")
									        else:
									            Result = CalcStat("StdProgRatings",L,1.0)
								    elif SN > 'PROGBMITIGATION':
									    if SN < 'PROGBNCMR':
										    if SN == 'PROGBMORALE':
										        Result = CalcStat("ProgBHealth",L)
									    elif SN > 'PROGBNCMR':
										    if SN == 'PROGBNCPR':
										        Result = CalcStat("ProgBEnergy",L)
									    else:
									        Result = CalcStat("ProgBHealth",L)
								    else:
								        Result = CalcStat("BRatProgB",L,"BRatMitMedium")
							    elif SN > 'PROGBOUTHEAL':
								    if SN < 'PROGBVITALITY':
									    if SN < 'PROGBRESIST':
										    if SN == 'PROGBPOWER':
										        Result = CalcStat("ProgBEnergy",L)
									    elif SN > 'PROGBRESIST':
										    if SN == 'PROGBTACHPS':
										        Result = CalcStat("ProgBHealth",L)
									    else:
									        Result = CalcStat("BRatProgB",L,"BRatExtra")
								    elif SN > 'PROGBVITALITY':
									    if SN < 'PROGEXTCOMHIGHRND':
										    if SN == 'PROGEXTCOMHIGHRAW':
										        if 121 <= Lp and Lm <= 121:
										            Result = ExpFmod(N,121,20,L,None)
										        elif 122 <= Lp and Lm <= 125:
										            Result = ExpFmod(CalcStat("ProgExtComHighRaw",121,N),122,5.5,L,None)
										        elif 126 <= Lp and Lm <= 126:
										            Result = ExpFmod(CalcStat("ProgExtComHighRaw",125,N),126,20,L,None)
										        elif 127 <= Lp and Lm <= 130:
										            Result = ExpFmod(CalcStat("ProgExtComHighRaw",126,N),127,5.5,L,None)
										        elif 131 <= Lp and Lm <= 131:
										            Result = ExpFmod(CalcStat("ProgExtComHighRaw",130,N),131,20,L,None)
										        elif 132 <= Lp and Lm <= 150:
										            Result = ExpFmod(CalcStat("ProgExtComHighRaw",131,N),132,5.5,L,None)
										        elif 151 <= Lp:
										            Result = CalcStat("ProgExtComHighRaw",150,N)
									    elif SN > 'PROGEXTCOMHIGHRND':
										    if SN == 'PROGEXTCOMLOWRAW':
										        if 116 <= Lp and Lm <= 116:
										            Result = ExpFmod(N,116,20,L,None)
										        elif 117 <= Lp and Lm <= 120:
										            Result = ExpFmod(CalcStat("ProgExtComLowRaw",116,N),117,5.5,L,None)
										        elif 121 <= Lp:
										            Result = CalcStat("ProgExtComHighRaw",L,CalcStat("ProgExtComLowRaw",120,N))
									    else:
									        if 121 <= Lp and Lm <= 121:
									            Result = ExpFmod(N,121,20,L,0)
									        elif 122 <= Lp and Lm <= 125:
									            Result = ExpFmod(CalcStat("ProgExtComHighRnd",121,N),122,5.5,L,0)
									        elif 126 <= Lp and Lm <= 126:
									            Result = ExpFmod(CalcStat("ProgExtComHighRnd",125,N),126,20,L,0)
									        elif 127 <= Lp and Lm <= 130:
									            Result = ExpFmod(CalcStat("ProgExtComHighRnd",126,N),127,5.5,L,0)
									        elif 131 <= Lp and Lm <= 131:
									            Result = ExpFmod(CalcStat("ProgExtComHighRnd",130,N),131,20,L,0)
									        elif 132 <= Lp and Lm <= 150:
									            Result = ExpFmod(CalcStat("ProgExtComHighRnd",131,N),132,5.5,L,0)
									        elif 151 <= Lp:
									            Result = CalcStat("ProgExtComHighRnd",150,N)
								    else:
								        Result = CalcStat("ProgBHealth",L)
							    else:
							        Result = CalcStat("BRatProgB",L,"BRatOutHeal")
						    elif SN > 'PROGEXTCOMLOWRND':
							    if SN < 'REAVERCDCALCTYPENONPHYMIT':
								    if SN < 'PROGEXTMPEXPRND':
									    if SN < 'PROGEXTLOWEXPRND':
										    if SN == 'PROGEXTHIGHLINEXPRND':
										        if 106 <= Lp and Lm <= 115:
										            Result = LinFmod(N,2,4,106,115,L,-1)
										        elif 116 <= Lp:
										            Result = CalcStat("ProgExtComLowRnd",L,CalcStat("ProgExtHighLinExpRnd",115,N))
									    elif SN > 'PROGEXTLOWEXPRND':
										    if SN == 'PROGEXTMEDEXPRAW':
										        if 106 <= Lp and Lm <= 106:
										            Result = ExpFmod(N,106,10,L,None)
										        elif 107 <= Lp and Lm <= 115:
										            Result = ExpFmod(CalcStat("ProgExtMedExpRaw",106,N),107,5.5,L,None)
										        elif 116 <= Lp:
										            Result = CalcStat("ProgExtComLowRaw",L,CalcStat("ProgExtMedExpRaw",115,N))
									    else:
									        if 106 <= Lp and Lm <= 115:
									            Result = ExpFmod(N,106,5.5,L,0)
									        elif 116 <= Lp:
									            Result = CalcStat("ProgExtComLowRnd",L,CalcStat("ProgExtLowExpRnd",115,N))
								    elif SN > 'PROGEXTMPEXPRND':
									    if SN < 'REAVERCANBLOCK':
										    if SN == 'RACENAME':
										        if 6 <= Lp and Lm <= 6:
										            Result = "Uruk"
										        elif 7 <= Lp and Lm <= 7:
										            Result = "Orc"
										        elif 12 <= Lp and Lm <= 12:
										            Result = "Spider"
										        elif 23 <= Lp and Lm <= 23:
										            Result = "Man"
										        elif 27 <= Lp and Lm <= 27:
										            Result = "Critter"
										        elif 65 <= Lp and Lm <= 65:
										            Result = "Elf"
										        elif 66 <= Lp and Lm <= 66:
										            Result = "Warg"
										        elif 73 <= Lp and Lm <= 73:
										            Result = "Dwarf"
										        elif 81 <= Lp and Lm <= 81:
										            Result = "Hobbit"
										        elif 114 <= Lp and Lm <= 114:
										            Result = "Beorning"
										        elif 117 <= Lp and Lm <= 117:
										            Result = "HighElf"
										        elif 120 <= Lp and Lm <= 120:
										            Result = "StoutAxe"
										        elif 125 <= Lp and Lm <= 125:
										            Result = "RiverHobbit"
										        else:
										            Result = ""
									    elif SN > 'REAVERCANBLOCK':
										    if SN == 'REAVERCDCALCTYPECOMPHYMIT':
										        Result = 13
									    else:
									        Result = 1
								    else:
								        if 106 <= Lp and Lm <= 114:
								            Result = ExpFmod(N,106,7.5,L,0)
								        elif 115 <= Lp and Lm <= 115:
								            Result = 2*N
								        elif 116 <= Lp and Lm <= 119:
								            Result = ExpFmod(CalcStat("ProgExtMpExpRnd",115,N),116,25,L,0)
								        elif 120 <= Lp and Lm <= 120:
								            Result = RoundDbl((16/3)*N)
								        elif 121 <= Lp:
								            Result = CalcStat("ProgExtComHighRnd",L,CalcStat("ProgExtMpExpRnd",120,N))
							    elif SN > 'REAVERCDCALCTYPENONPHYMIT':
								    if SN < 'REPAGILITYL':
									    if SN < 'REAVERCDHASPOWER':
										    if SN == 'REAVERCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'REAVERCDHASPOWER':
										    if SN == 'REPAGILITYH':
										        Result = CalcStat("RepMainH",L)
									    else:
									        Result = 1
								    elif SN > 'REPAGILITYL':
									    if SN < 'REPCRITHIT':
										    if SN == 'REPCRITDEF':
										        if Lm <= 50:
										            Result = LinFmod(1,900,1488,1,50,L)
										        elif Lm <= 85:
										            Result = LinFmod(1,1488,1908,50,85,L)
										        elif Lm <= 105:
										            Result = LinFmod(1,1908,2148,85,105,L)
										        else:
										            Result = LinFmod(1,2148,2328,105,120,L)
									    elif SN > 'REPCRITHIT':
										    if SN == 'REPFATEH':
										        Result = CalcStat("RepMainH",L)
									    else:
									        if Lm <= 50:
									            Result = LinFmod(1,300,496,1,50,L)
									        elif Lm <= 85:
									            Result = LinFmod(1,496,636,50,85,L)
									        elif Lm <= 105:
									            Result = LinFmod(1,636,716,85,105,L)
									        else:
									            Result = LinFmod(1,716,776,105,120,L)
								    else:
								        Result = CalcStat("RepMainL",L)
							    else:
							        Result = 14
						    else:
						        if 116 <= Lp and Lm <= 116:
						            Result = ExpFmod(N,116,20,L,0)
						        elif 117 <= Lp and Lm <= 120:
						            Result = ExpFmod(CalcStat("ProgExtComLowRnd",116,N),117,5.5,L,0)
						        elif 121 <= Lp:
						            Result = CalcStat("ProgExtComHighRnd",L,CalcStat("ProgExtComLowRnd",120,N))
					    elif SN > 'REPFATEL':
						    if SN < 'RESISTC':
							    if SN < 'REPTACMIT':
								    if SN < 'REPMIGHTH':
									    if SN < 'REPMAINH':
										    if SN == 'REPFINESSE':
										        if Lm <= 50:
										            Result = LinFmod(1,322,557,1,50,L)
										        elif Lm <= 85:
										            Result = LinFmod(1,557,749.9477,50,85,L)
										        elif Lm <= 105:
										            Result = LinFmod(1,749.9477,859.1634,85,105,L)
										        else:
										            Result = LinFmod(1,859.1634,939.2549,105,120,L)
									    elif SN > 'REPMAINH':
										    if SN == 'REPMAINL':
										        if Lm <= 50:
										            Result = RoundDblDown(LinFmod(1,53,102,1,50,L))
										        elif Lm <= 85:
										            Result = RoundDblDown(LinFmod(1,102,137,50,85,L))
										        elif Lm <= 105:
										            Result = RoundDblDown(LinFmod(1,137,157,85,105,L))
										        else:
										            Result = RoundDblDown(LinFmod(1,157,172,105,120,L))
									    else:
									        if Lm <= 50:
									            Result = RoundDblDown(LinFmod(1,80,153,1,50,L))
									        elif Lm <= 85:
									            Result = RoundDblDown(LinFmod(1,153,206,50,85,L))
									        elif Lm <= 105:
									            Result = RoundDblDown(LinFmod(1,206,236,85,105,L))
									        else:
									            Result = RoundDblDown(LinFmod(1,236,258,105,120,L))
								    elif SN > 'REPMIGHTH':
									    if SN < 'REPMORALE':
										    if SN == 'REPMIGHTL':
										        Result = CalcStat("RepMainL",L)
									    elif SN > 'REPMORALE':
										    if SN == 'REPPOWER':
										        if Lm <= 50:
										            Result = LinFmod(1,94,212,1,50,L)
										        elif Lm <= 85:
										            Result = LinFmod(1,212,296,50,85,L)
										        elif Lm <= 105:
										            Result = LinFmod(1,296,344,85,105,L)
										        else:
										            Result = LinFmod(1,344,380,105,120,L)
									    else:
									        if Lm <= 50:
									            Result = LinFmod(1,187,427,1,50,L)
									        elif Lm <= 85:
									            Result = LinFmod(1,427,599,50,85,L)
									        elif Lm <= 105:
									            Result = LinFmod(1,599,697,85,105,L)
									        else:
									            Result = LinFmod(1,697,770,105,120,L)
								    else:
								        Result = CalcStat("RepMainH",L)
							    elif SN > 'REPTACMIT':
								    if SN < 'REPWILLL':
									    if SN < 'REPVITALITYL':
										    if SN == 'REPVITALITYH':
										        Result = CalcStat("RepMainH",L)
									    elif SN > 'REPVITALITYL':
										    if SN == 'REPWILLH':
										        Result = CalcStat("RepMainH",L)
									    else:
									        Result = CalcStat("RepMainL",L)
								    elif SN > 'REPWILLL':
									    if SN < 'RESISTADD':
										    if SN == 'RESIST':
										        Result = EquSng(StatLinInter("PntMPResist","ItemPntS","ProgBResist","AdjItem",L,N,0))
									    elif SN > 'RESISTADD':
										    if SN == 'RESISTADDT':
										        Result = CalcStat("ResistT",L,N)
									    else:
									        Result = CalcStat("Resist",L,N)
								    else:
								        Result = CalcStat("RepMainL",L)
							    else:
							        if Lm <= 50:
							            Result = LinFmod(1,675,1116,1,50,L)
							        elif Lm <= 85:
							            Result = LinFmod(1,1116,1431,50,85,L)
							        elif Lm <= 105:
							            Result = LinFmod(1,1431,1611,85,105,L)
							        else:
							            Result = LinFmod(1,1611,1746,105,120,L)
						    elif SN > 'RESISTC':
							    if SN < 'RESISTPRATPB':
								    if SN < 'RESISTCRAW':
									    if SN < 'RESISTCILVLFILTER':
										    if SN == 'RESISTCI':
										        Result = RoundDblLotro(CalcStat("ResistCIRaw",L,N))
									    elif SN > 'RESISTCILVLFILTER':
										    if SN == 'RESISTCIRAW':
										        Result = StatLinInter("PntMPResistC","ItemPntS","ProgBResist","AdjCreepItem",L,N,4)
									    else:
									        if 2.4 <= Lp and Lm <= 2.4 or 3.2 <= Lp and Lm <= 3.2 or 4 <= Lp and Lm <= 4 or 8 <= Lp and Lm <= 8 or 12 <= Lp and Lm <= 12:
									            Result = 515
									        else:
									            Result = CalcStat("CreepILvlCurr",L)
								    elif SN > 'RESISTCRAW':
									    if SN < 'RESISTPRATP':
										    if SN == 'RESISTPPRAT':
										        Result = CalcRatAB(CalcStat("ResistPRatPA",L),CalcStat("ResistPRatPB",L),CalcStat("ResistPRatPCapR",L),N)
									    elif SN > 'RESISTPRATP':
										    if SN == 'RESISTPRATPA':
										        Result = 150
									    else:
									        Result = CalcPercAB(CalcStat("ResistPRatPA",L),CalcStat("ResistPRatPB",L),CalcStat("ResistPRatPCap",L),N)
								    else:
								        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ResistCIRaw",CalcStat("ResistCILvlFilter",N),N),99)
							    elif SN > 'RESISTPRATPB':
								    if SN < 'RESISTT':
									    if SN < 'RESISTPRATPCAP':
										    if SN == 'RESISTPRATPC':
										        Result = 0.5
									    elif SN > 'RESISTPRATPCAP':
										    if SN == 'RESISTPRATPCAPR':
										        Result = CalcStat("ResistPRatPB",L)*CalcStat("ResistPRatPC",L)
									    else:
									        Result = 50
								    elif SN > 'RESISTT':
									    if SN < 'RIVERHOBBITRDPSVONEWILL':
										    if SN == 'RIVERHOBBITRDPSVONENAME':
										        Result = "Seen the World"
									    elif SN > 'RIVERHOBBITRDPSVONEWILL':
										    if SN > 'RIVERHOBBITRDPSVTWONAME':
											    if SN == 'RIVERHOBBITRDTRAITAGILITY':
											        Result = CalcStat("RivHobSlipperyAgility",L)
										    elif SN == 'RIVERHOBBITRDPSVTWONAME':
										        Result = ""
									    else:
									        Result = CalcStat("RivHobSeenWorldWill",L)
								    else:
								        Result = EquSng(StatLinInter("PntMPResist","TraitPntS","ProgBResist","AdjTrait",L,N,0))
							    else:
							        Result = CalcStat("BRatRounded",L,"BRatExtra")
						    else:
						        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("ResistCI",CalcStat("ResistCILvlFilter",N),N),0)
					    else:
					        Result = CalcStat("RepMainL",L)
				    else:
				        Result = CalcStat("BRatProgB",L,"BRatStandard")
			    elif SN > 'RIVERHOBBITRDTRAITFROSTMITP':
				    if SN < 'STATC':
					    if SN < 'RUNEKEEPERCDFATETONCPR':
						    if SN < 'RUNEKEEPERCDARMOURTOTACMIT':
							    if SN < 'RKDETERMINATIONWILL':
								    if SN < 'RIVHOBSECLUSIONWILL':
									    if SN < 'RIVERHOBBITRDTRAITWILL':
										    if SN == 'RIVERHOBBITRDTRAITMORALE':
										        Result = CalcStat("RivHobHardyHolbMorale",L)
									    elif SN > 'RIVERHOBBITRDTRAITWILL':
										    if SN == 'RIVHOBHARDYHOLBMORALE':
										        Result = CalcStat("MoraleT",L,1.0)
									    else:
									        Result = CalcStat("RivHobSeclusionWill",L)
								    elif SN > 'RIVHOBSECLUSIONWILL':
									    if SN < 'RIVHOBSLIPPERYAGILITY':
										    if SN == 'RIVHOBSEENWORLDWILL':
										        Result = CalcStat("WillT",L,1.0)
									    elif SN > 'RIVHOBSLIPPERYAGILITY':
										    if SN == 'RIVHOBSWIMMERFROSTMITP':
										        Result = 1
									    else:
									        Result = CalcStat("AgilityT",L,1.0)
								    else:
								        Result = -CalcStat("WillT",L,0.4)
							    elif SN > 'RKDETERMINATIONWILL':
								    if SN < 'RUNEKEEPERCDAGILITYTOFINESSE':
									    if SN < 'RUNEKEEPERCDAGILITYTOCRITHIT':
										    if SN == 'RKFORTUNESMILESFATE':
										        Result = CalcStat("FateT",L,CalcStat("Trait567810Choice",N)*0.4)
									    elif SN > 'RUNEKEEPERCDAGILITYTOCRITHIT':
										    if SN == 'RUNEKEEPERCDAGILITYTOEVADE':
										        Result = 1
									    else:
									        Result = 2
								    elif SN > 'RUNEKEEPERCDAGILITYTOFINESSE':
									    if SN < 'RUNEKEEPERCDARMOURTOCOMPHYMIT':
										    if SN == 'RUNEKEEPERCDAGILITYTOTACMAS':
										        Result = 2
									    elif SN > 'RUNEKEEPERCDARMOURTOCOMPHYMIT':
										    if SN == 'RUNEKEEPERCDARMOURTONONPHYMIT':
										        Result = 0.2
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = CalcStat("WillT",L,CalcStat("Trait567810Choice",N)*0.4)
						    elif SN > 'RUNEKEEPERCDARMOURTOTACMIT':
							    if SN < 'RUNEKEEPERCDBASENCMR':
								    if SN < 'RUNEKEEPERCDBASEICMR':
									    if SN < 'RUNEKEEPERCDBASEAGILITY':
										    if SN == 'RUNEKEEPERCDARMOURTYPE':
										        Result = 1
									    elif SN > 'RUNEKEEPERCDBASEAGILITY':
										    if SN == 'RUNEKEEPERCDBASEFATE':
										        Result = CalcStat("ClassBaseFate",L)
									    else:
									        Result = CalcStat("ClassBaseAgilityL",L)
								    elif SN > 'RUNEKEEPERCDBASEICMR':
									    if SN < 'RUNEKEEPERCDBASEMIGHT':
										    if SN == 'RUNEKEEPERCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    elif SN > 'RUNEKEEPERCDBASEMIGHT':
										    if SN == 'RUNEKEEPERCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    else:
									        Result = CalcStat("ClassBaseMightM",L)
								    else:
								        Result = CalcStat("ClassBaseICMRL",L)
							    elif SN > 'RUNEKEEPERCDBASENCMR':
								    if SN < 'RUNEKEEPERCDBASEWILL':
									    if SN < 'RUNEKEEPERCDBASEPOWER':
										    if SN == 'RUNEKEEPERCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    elif SN > 'RUNEKEEPERCDBASEPOWER':
										    if SN == 'RUNEKEEPERCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    else:
									        Result = CalcStat("ClassBasePower",L)
								    elif SN > 'RUNEKEEPERCDBASEWILL':
									    if SN < 'RUNEKEEPERCDCALCTYPENONPHYMIT':
										    if SN == 'RUNEKEEPERCDCALCTYPECOMPHYMIT':
										        Result = 12
									    elif SN > 'RUNEKEEPERCDCALCTYPENONPHYMIT':
										    if SN == 'RUNEKEEPERCDCALCTYPETACMIT':
										        Result = 25
									    else:
									        Result = 12
								    else:
								        Result = CalcStat("ClassBaseWillH",L)
							    else:
							        Result = CalcStat("ClassBaseNCMRL",L)
						    else:
						        Result = 0.2
					    elif SN > 'RUNEKEEPERCDFATETONCPR':
						    if SN < 'RUNEKEEPERCDWILLTORESIST':
							    if SN < 'RUNEKEEPERCDPHYMITTONONPHYMIT':
								    if SN < 'RUNEKEEPERCDMIGHTTOOUTHEAL':
									    if SN < 'RUNEKEEPERCDHASPOWER':
										    if SN == 'RUNEKEEPERCDFATETOPOWER':
										        Result = 1
									    elif SN > 'RUNEKEEPERCDHASPOWER':
										    if SN == 'RUNEKEEPERCDMIGHTTOCRITHIT':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'RUNEKEEPERCDMIGHTTOOUTHEAL':
									    if SN < 'RUNEKEEPERCDMIGHTTOTACMIT':
										    if SN == 'RUNEKEEPERCDMIGHTTOTACMAS':
										        Result = 2
									    elif SN > 'RUNEKEEPERCDMIGHTTOTACMIT':
										    if SN == 'RUNEKEEPERCDPHYMITTOCOMPHYMIT':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 2
							    elif SN > 'RUNEKEEPERCDPHYMITTONONPHYMIT':
								    if SN < 'RUNEKEEPERCDVITALITYTONCMR':
									    if SN < 'RUNEKEEPERCDVITALITYTOICMR':
										    if SN == 'RUNEKEEPERCDTACMASTOOUTHEAL':
										        Result = 1
									    elif SN > 'RUNEKEEPERCDVITALITYTOICMR':
										    if SN == 'RUNEKEEPERCDVITALITYTOMORALE':
										        Result = 4.5
									    else:
									        Result = 0.012
								    elif SN > 'RUNEKEEPERCDVITALITYTONCMR':
									    if SN < 'RUNEKEEPERCDWILLTOEVADE':
										    if SN == 'RUNEKEEPERCDWILLTOCRITHIT':
										        Result = 1
									    elif SN > 'RUNEKEEPERCDWILLTOEVADE':
										    if SN == 'RUNEKEEPERCDWILLTOPHYMIT':
										        Result = 1
									    else:
									        Result = 2
								    else:
								        Result = 0.12
							    else:
							        Result = 1
						    elif SN > 'RUNEKEEPERCDWILLTORESIST':
							    if SN < 'SKILLPOWERCOSTMOUNTED':
								    if SN < 'SHADOWMITT':
									    if SN < 'RUNEKEEPERCDWILLTOTACMIT':
										    if SN == 'RUNEKEEPERCDWILLTOTACMAS':
										        Result = 3
									    elif SN > 'RUNEKEEPERCDWILLTOTACMIT':
										    if SN == 'SHADOWMIT':
										        Result = CalcStat("DmgTypeMit",L,N)
									    else:
									        Result = 1
								    elif SN > 'SHADOWMITT':
									    if SN < 'SHIELDBRAWLERBLOCK':
										    if SN == 'SHIELDBLOCK':
										        Result = EquSng(StatLinInter("PntMPShieldBlock","ItemPntS","ProgBBPE","AdjItem",L,N,0))
									    elif SN > 'SHIELDBRAWLERBLOCK':
										    if SN == 'SKILLPOWERCOST':
										        if Lm <= 140:
										            Result = CalcStat("CombatDamageModEnergy",L,0.64*N)
										        else:
										            Result = CalcStat("CombatDamageModEnergy",L,1.05*0.64*N)
									    else:
									        Result = CalcStat("DwarfShieldBrwlBlock",L)
								    else:
								        Result = CalcStat("DmgTypeMitT",L,N)
							    elif SN > 'SKILLPOWERCOSTMOUNTED':
								    if SN < 'STALKERCDCALCTYPECOMPHYMIT':
									    if SN < 'SONGRESISTT':
										    if SN == 'SONGRESIST':
										        Result = CalcStat("ResistAdd",L,N)
									    elif SN > 'SONGRESISTT':
										    if SN == 'STALKERCANBLOCK':
										        Result = 1
									    else:
									        Result = CalcStat("ResistAddT",L,N)
								    elif SN > 'STALKERCDCALCTYPECOMPHYMIT':
									    if SN < 'STALKERCDCALCTYPETACMIT':
										    if SN == 'STALKERCDCALCTYPENONPHYMIT':
										        Result = 14
									    elif SN > 'STALKERCDCALCTYPETACMIT':
										    if SN == 'STALKERCDHASPOWER':
										        Result = 1
									    else:
									        Result = 27
								    else:
								        Result = 13
							    else:
							        Result = CalcStat("CombatDamageModEnergy",L,0.64*N)
						    else:
						        Result = 1
					    else:
					        Result = 0.07
				    elif SN > 'STATC':
					    if SN < 'STOUTWRBLACKLSHADOWMITP':
						    if SN < 'STOUTAXERDTRAITAGILITY':
							    if SN < 'STDPOWERRAW':
								    if SN < 'STDMORALERAW':
									    if SN < 'STDMORALEL':
										    if SN == 'STDMORALEH':
										        if Lm <= 105:
										            Result = RoundDbl(2*CalcStat("StdMoraleRaw",L))
										        else:
										            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("StdMoraleH",105))
									    elif SN > 'STDMORALEL':
										    if SN == 'STDMORALEM':
										        if Lm <= 105:
										            Result = RoundDbl(1.5*CalcStat("StdMoraleRaw",L))
										        else:
										            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("StdMoraleM",105))
									    else:
									        if Lm <= 105:
									            Result = RoundDbl(CalcStat("StdMoraleRaw",L))
									        else:
									            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("StdMoraleL",105))
								    elif SN > 'STDMORALERAW':
									    if SN < 'STDPOWERH':
										    if SN == 'STDPNTS':
										        Result = ((1,50,60,65,75,85,95,100,105,106,115,116,120,121,130,131,140,141,150,151,160),(1,50,60,65,75,85,95,100,105,106,115,116,120,121,130,131,140,141,150,151,160))
									    elif SN > 'STDPOWERH':
										    if SN == 'STDPOWERL':
										        if Lm <= 105:
										            Result = RoundDbl(CalcStat("StdPowerRaw",L))
										        else:
										            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("StdPowerL",105))
									    else:
									        if Lm <= 105:
									            Result = RoundDbl(2*CalcStat("StdPowerRaw",L))
									        else:
									            Result = CalcStat("ProgExtLowExpRnd",L,CalcStat("StdPowerH",105))
								    else:
								        if Lm <= 50:
								            Result = LinFmod(1,7.51,227.59,1,50,L)
								        else:
								            Result = LinFmod(1,227.59,1327.5,50,105,L)
							    elif SN > 'STDPOWERRAW':
								    if SN < 'STDPROGRATINGS':
									    if SN < 'STDPROGENERGY':
										    if SN == 'STDPROGDAMAGE':
										        if Lm <= 50:
										            Result = LinFmod(N,1,10,1,50,L,"P")
										        elif Lm <= 60:
										            Result = LinFmod(CalcStat("StdProgDamage",50,N),1,1.33,50,60,L,"P")
										        elif Lm <= 65:
										            Result = LinFmod(CalcStat("StdProgDamage",60,N),1,1.095,60,65,L,"P")
										        elif Lm <= 75:
										            Result = LinFmod(CalcStat("StdProgDamage",65,N),1,1.33,65,75,L,"P")
										        elif Lm <= 85:
										            Result = LinFmod(CalcStat("StdProgDamage",75,N),1,1.33,75,85,L,"P")
										        elif Lm <= 95:
										            Result = LinFmod(CalcStat("StdProgDamage",85,N),1,1.33,85,95,L,"P")
										        elif Lm <= 100:
										            Result = LinFmod(CalcStat("StdProgDamage",95,N),1,1.25,95,100,L,"P")
										        elif Lm <= 105:
										            Result = LinFmod(CalcStat("StdProgDamage",100,N),1,1.25,100,105,L,"P")
										        elif Lm <= 115:
										            Result = LinFmod(CalcStat("StdProgDamage",105,N),1.1,1.33,106,115,L,"P")
										        elif Lm <= 120:
										            Result = LinFmod(CalcStat("StdProgDamage",115,N),1.1,1.25,116,120,L,"P")
										        elif Lm <= 130:
										            Result = LinFmod(CalcStat("StdProgDamage",120,N),1.1,1.33,121,130,L,"P")
										        elif Lm <= 140:
										            Result = LinFmod(CalcStat("StdProgDamage",130,N),1.1,1.5,131,140,L,"P")
										        elif Lm <= 150:
										            Result = LinFmod(CalcStat("StdProgDamage",140,N),1.1,1.5,141,150,L,"P")
										        else:
										            Result = LinFmod(CalcStat("StdProgDamage",150,N),1.1,1.5,151,160,L,"P")
									    elif SN > 'STDPROGENERGY':
										    if SN == 'STDPROGHEALTH':
										        if Lm <= 50:
										            Result = LinFmod(N,1,7.5,1,50,L,"P")
										        elif Lm <= 60:
										            Result = LinFmod(CalcStat("StdProgHealth",50,N),1,1.33,50,60,L,"P")
										        elif Lm <= 65:
										            Result = LinFmod(CalcStat("StdProgHealth",60,N),1,1.25,60,65,L,"P")
										        elif Lm <= 75:
										            Result = LinFmod(CalcStat("StdProgHealth",65,N),1,1.5,65,75,L,"P")
										        elif Lm <= 85:
										            Result = LinFmod(CalcStat("StdProgHealth",75,N),1,1.5,75,85,L,"P")
										        elif Lm <= 95:
										            Result = LinFmod(CalcStat("StdProgHealth",85,N),1,1.33,85,95,L,"P")
										        elif Lm <= 100:
										            Result = LinFmod(CalcStat("StdProgHealth",95,N),1,1.5,95,100,L,"P")
										        elif Lm <= 105:
										            Result = LinFmod(CalcStat("StdProgHealth",100,N),1,1.333,100,105,L,"P")
										        elif Lm <= 115:
										            Result = LinFmod(CalcStat("StdProgHealth",105,N),1.1,1.5,106,115,L,"P")
										        elif Lm <= 120:
										            Result = LinFmod(CalcStat("StdProgHealth",115,N),1.15,1.25,116,120,L,"P")
										        elif Lm <= 130:
										            Result = LinFmod(CalcStat("StdProgHealth",120,N),1.15,1.5,121,130,L,"P")
										        elif Lm <= 140:
										            Result = LinFmod(CalcStat("StdProgHealth",130,N),1.15,2,131,140,L,"P")
										        elif Lm <= 150:
										            Result = LinFmod(CalcStat("StdProgHealth",140,N),1.15,2,141,150,L,"P")
										        else:
										            Result = LinFmod(CalcStat("StdProgHealth",150,N),1,2,151,160,L,"P")
									    else:
									        if Lm <= 50:
									            Result = LinFmod(N,1,2,1,50,L,"P")
									        elif Lm <= 60:
									            Result = LinFmod(CalcStat("StdProgEnergy",50,N),1,1.33,50,60,L,"P")
									        elif Lm <= 65:
									            Result = LinFmod(CalcStat("StdProgEnergy",60,N),1,1.25,60,65,L,"P")
									        elif Lm <= 75:
									            Result = LinFmod(CalcStat("StdProgEnergy",65,N),1,1.5,65,75,L,"P")
									        elif Lm <= 85:
									            Result = LinFmod(CalcStat("StdProgEnergy",75,N),1,1.5,75,85,L,"P")
									        elif Lm <= 95:
									            Result = LinFmod(CalcStat("StdProgEnergy",85,N),1,1.33,85,95,L,"P")
									        elif Lm <= 100:
									            Result = LinFmod(CalcStat("StdProgEnergy",95,N),1,1.315,95,100,L,"P")
									        elif Lm <= 105:
									            Result = LinFmod(CalcStat("StdProgEnergy",100,N),1,1.333,100,105,L,"P")
									        elif Lm <= 115:
									            Result = LinFmod(CalcStat("StdProgEnergy",105,N),1.1,1.5,106,115,L,"P")
									        elif Lm <= 120:
									            Result = LinFmod(CalcStat("StdProgEnergy",115,N),1.15,1.25,116,120,L,"P")
									        elif Lm <= 130:
									            Result = LinFmod(CalcStat("StdProgEnergy",120,N),1.15,1.5,121,130,L,"P")
									        elif Lm <= 140:
									            Result = LinFmod(CalcStat("StdProgEnergy",130,N),1.15,2,131,140,L,"P")
									        elif Lm <= 150:
									            Result = LinFmod(CalcStat("StdProgEnergy",140,N),1.15,2,141,150,L,"P")
									        else:
									            Result = LinFmod(CalcStat("StdProgEnergy",150,N),1,2,151,160,L,"P")
								    elif SN > 'STDPROGRATINGS':
									    if SN < 'STOUTAXERDPSVONEVITALITY':
										    if SN == 'STOUTAXERDPSVONENAME':
										        Result = "Unwritten Destiny"
									    elif SN > 'STOUTAXERDPSVONEVITALITY':
										    if SN == 'STOUTAXERDPSVTWONAME':
										        Result = ""
									    else:
									        Result = CalcStat("StoutUnwritDestVitality",L)
								    else:
								        if Lm <= 50:
								            Result = LinFmod(N,1,10,1,50,L,"P")
								        elif Lm <= 60:
								            Result = LinFmod(CalcStat("StdProgRatings",50,N),1,1.5,50,60,L,"P")
								        elif Lm <= 65:
								            Result = LinFmod(CalcStat("StdProgRatings",60,N),1,1.335,60,65,L,"P")
								        elif Lm <= 75:
								            Result = LinFmod(CalcStat("StdProgRatings",65,N),1,1.5,65,75,L,"P")
								        elif Lm <= 85:
								            Result = LinFmod(CalcStat("StdProgRatings",75,N),1,1.5,75,85,L,"P")
								        elif Lm <= 95:
								            Result = LinFmod(CalcStat("StdProgRatings",85,N),1,1.445,85,95,L,"P")
								        elif Lm <= 100:
								            Result = LinFmod(CalcStat("StdProgRatings",95,N),1,1.39,95,100,L,"P")
								        elif Lm <= 105:
								            Result = LinFmod(CalcStat("StdProgRatings",100,N),1,1.33,100,105,L,"P")
								        elif Lm <= 115:
								            Result = LinFmod(CalcStat("StdProgRatings",105,N),1.1,1.5,106,115,L,"P")
								        elif Lm <= 120:
								            Result = LinFmod(CalcStat("StdProgRatings",115,N),1.15,1.25,116,120,L,"P")
								        elif Lm <= 130:
								            Result = LinFmod(CalcStat("StdProgRatings",120,N),1.15,1.5,121,130,L,"P")
								        elif Lm <= 140:
								            Result = LinFmod(CalcStat("StdProgRatings",130,N),1.15,2,131,140,L,"P")
								        elif Lm <= 150:
								            Result = LinFmod(CalcStat("StdProgRatings",140,N),1.3,2.205,141,150,L,"P")
								        else:
								            Result = LinFmod(CalcStat("StdProgRatings",150,N),1,2,151,160,L,"P")
							    else:
							        if Lm <= 50:
							            Result = LinFmod(1,3,91.0375,1,50,L)
							        else:
							            Result = LinFmod(1,91.0375,421,50,105,L)
						    elif SN > 'STOUTAXERDTRAITAGILITY':
							    if SN < 'STOUTDOOMDRASAFATE':
								    if SN < 'STOUTAXERDTRAITPHYMITP':
									    if SN < 'STOUTAXERDTRAITFATE':
										    if SN == 'STOUTAXERDTRAITDISEASERESISTP':
										        Result = CalcStat("StoutWrBlackLDiseaseResistP",L)
									    elif SN > 'STOUTAXERDTRAITFATE':
										    if SN == 'STOUTAXERDTRAITMIGHT':
										        Result = CalcStat("StoutWrBlackLMight",L)
									    else:
									        Result = CalcStat("StoutDoomDrasaFate",L)
								    elif SN > 'STOUTAXERDTRAITPHYMITP':
									    if SN < 'STOUTAXERDTRAITVITALITY':
										    if SN == 'STOUTAXERDTRAITSHADOWMITP':
										        Result = CalcStat("StoutWrBlackLShadowMitP",L)
									    elif SN > 'STOUTAXERDTRAITVITALITY':
										    if SN == 'STOUTAXERDTRAITWILL':
										        Result = CalcStat("StoutUnyieldingWill",L)
									    else:
									        Result = CalcStat("StoutShadowEyeVitality",L)
								    else:
								        Result = CalcStat("StoutUnyieldingPhyMitP",L)
							    elif SN > 'STOUTDOOMDRASAFATE':
								    if SN < 'STOUTUNYIELDINGWILL':
									    if SN < 'STOUTUNWRITDESTVITALITY':
										    if SN == 'STOUTSHADOWEYEVITALITY':
										        Result = -CalcStat("VitalityT",L,0.4)
									    elif SN > 'STOUTUNWRITDESTVITALITY':
										    if SN == 'STOUTUNYIELDINGPHYMITP':
										        Result = 1
									    else:
									        Result = CalcStat("VitalityT",L,1.0)
								    elif SN > 'STOUTUNYIELDINGWILL':
									    if SN < 'STOUTWRBLACKLDISEASERESISTP':
										    if SN == 'STOUTWRBLACKLAGILITY':
										        Result = CalcStat("AgilityT",L,1.0)
									    elif SN > 'STOUTWRBLACKLDISEASERESISTP':
										    if SN == 'STOUTWRBLACKLMIGHT':
										        Result = CalcStat("MightT",L,1.0)
									    else:
									        Result = 1
								    else:
								        Result = CalcStat("WillT",L,1.0)
							    else:
							        Result = -CalcStat("FateT",L,0.4)
						    else:
						        Result = CalcStat("StoutWrBlackLAgility",L)
					    elif SN > 'STOUTWRBLACKLSHADOWMITP':
						    if SN < 'TACMASCIRAW':
							    if SN < 'TACDMGPRATPA':
								    if SN < 'T2PENRESIST':
									    if SN < 'T2PENBPE':
										    if SN == 'T2PENARMOUR':
										        Result = CalcStat("T2penMit",L)
									    elif SN > 'T2PENBPE':
										    if SN == 'T2PENMIT':
										        if Lm <= 115:
										            Result = RoundDblDown(L*13.5)*-5
										        else:
										            Result = EquSng(DecSng(CalcStat("ProgExtComLowRaw",L,CalcStat("T2PenMit",115))))
									    else:
									        if Lm <= 115:
									            Result = (-40)*L
									        else:
									            Result = EquSng(DecSng(CalcStat("ProgExtComLowRaw",L,CalcStat("T2PenBPE",115))))
								    elif SN > 'T2PENRESIST':
									    if SN < 'TACDMGPPRAT':
										    if SN == 'TACDMGPBONUS':
										        Result = CalcStat("OutDmgPBonus",L)
									    elif SN > 'TACDMGPPRAT':
										    if SN == 'TACDMGPRATP':
										        Result = CalcStat("OutDmgPRatP",L,N)
									    else:
									        Result = CalcStat("OutDmgPPRat",L,N)
								    else:
								        if Lm <= 115:
								            Result = (-90)*L
								        else:
								            Result = EquSng(DecSng(CalcStat("ProgExtComLowRaw",L,CalcStat("T2PenResist",115))))
							    elif SN > 'TACDMGPRATPA':
								    if SN < 'TACDMGPRATPCAPR':
									    if SN < 'TACDMGPRATPC':
										    if SN == 'TACDMGPRATPB':
										        Result = CalcStat("OutDmgPRatPB",L)
									    elif SN > 'TACDMGPRATPC':
										    if SN == 'TACDMGPRATPCAP':
										        Result = CalcStat("OutDmgPRatPCap",L)
									    else:
									        Result = CalcStat("OutDmgPRatPC",L)
								    elif SN > 'TACDMGPRATPCAPR':
									    if SN < 'TACMASC':
										    if SN == 'TACMAS':
										        Result = CalcStat("Mastery",L,N)
									    elif SN > 'TACMASC':
										    if SN == 'TACMASCI':
										        Result = CalcStat("MasteryCI",L,N)
									    else:
									        Result = CalcStat("MasteryC",L,N)
								    else:
								        Result = CalcStat("OutDmgPRatPCapR",L)
							    else:
							        Result = CalcStat("OutDmgPRatPA",L)
						    elif SN > 'TACMASCIRAW':
							    if SN < 'TACMITCIRAW':
								    if SN < 'TACMIT':
									    if SN < 'TACMASOLD':
										    if SN == 'TACMASCRAW':
										        Result = CalcStat("MasteryCRaw",L,N)
									    elif SN > 'TACMASOLD':
										    if SN == 'TACMAST':
										        Result = CalcStat("MasteryT",L,N)
									    else:
									        Result = CalcStat("Mastery",L,N)
								    elif SN > 'TACMIT':
									    if SN < 'TACMITCI':
										    if SN == 'TACMITC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("TacMitCI",CalcStat("TacMitCILvlFilter",N),N),0)
									    elif SN > 'TACMITCI':
										    if SN == 'TACMITCILVLFILTER':
										        if 3.8 <= Lp and Lm <= 3.8 or 5.6 <= Lp and Lm <= 5.6 or 6.9 <= Lp and Lm <= 6.9 or 12.9 <= Lp and Lm <= 12.9 or 17.3 <= Lp and Lm <= 17.3 or 24.225 <= Lp and Lm <= 24.225:
										            Result = 515
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    else:
									        Result = RoundDblLotro(CalcStat("TacMitCIRaw",L,N))
								    else:
								        Result = EquSng(StatLinInter("PntMPTacMit","ItemPntS","ProgBMitigation","AdjItemMit",L,N,0))
							    elif SN > 'TACMITCIRAW':
								    if SN < 'TACMITHPRATP':
									    if SN < 'TACMITHPBONUS':
										    if SN == 'TACMITCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("TacMitCIRaw",CalcStat("TacMitCILvlFilter",N),N),99)
									    elif SN > 'TACMITHPBONUS':
										    if SN == 'TACMITHPPRAT':
										        Result = CalcStat("MitHeavyPPRat",L,N)
									    else:
									        Result = CalcStat("MitHeavyPBonus",L)
								    elif SN > 'TACMITHPRATP':
									    if SN < 'TACMITHPRATPB':
										    if SN == 'TACMITHPRATPA':
										        Result = CalcStat("MitHeavyPRatPA",L)
									    elif SN > 'TACMITHPRATPB':
										    if SN > 'TACMITHPRATPC':
											    if SN == 'TACMITHPRATPCAP':
											        Result = CalcStat("MitHeavyPRatPCap",L)
										    elif SN == 'TACMITHPRATPC':
										        Result = CalcStat("MitHeavyPRatPC",L)
									    else:
									        Result = CalcStat("MitHeavyPRatPB",L)
								    else:
								        Result = CalcStat("MitHeavyPRatP",L,N)
							    else:
							        Result = StatLinInter("PntMPTacMitC","ItemPntS","ProgBMitigation","AdjCreepItemMit",L,N,4)
						    else:
						        Result = CalcStat("MasteryCIRaw",L,N)
					    else:
					        Result = 1
				    else:
				        Result = CalcStat(C,L)
			    else:
			        Result = CalcStat("RivHobSwimmerFrostMitP",L)
		    else:
		        Result = 0.25
	    elif SN > 'TACMITHPRATPCAPR':
		    if SN < 'WARDENCDMIGHTTOCRITHIT':
			    if SN < 'VIRTVALOURPHYMAS':
				    if SN < 'VIRTCONFIDENCEFINESSE':
					    if SN < 'TOMEVITALITYDEC':
						    if SN < 'TACMITMPRATPCAPR':
							    if SN < 'TACMITLPRATPCAPR':
								    if SN < 'TACMITLPRATPA':
									    if SN < 'TACMITLPPRAT':
										    if SN == 'TACMITLPBONUS':
										        Result = CalcStat("MitLightPBonus",L)
									    elif SN > 'TACMITLPPRAT':
										    if SN == 'TACMITLPRATP':
										        Result = CalcStat("MitLightPRatP",L,N)
									    else:
									        Result = CalcStat("MitLightPPRat",L,N)
								    elif SN > 'TACMITLPRATPA':
									    if SN < 'TACMITLPRATPC':
										    if SN == 'TACMITLPRATPB':
										        Result = CalcStat("MitLightPRatPB",L)
									    elif SN > 'TACMITLPRATPC':
										    if SN == 'TACMITLPRATPCAP':
										        Result = CalcStat("MitLightPRatPCap",L)
									    else:
									        Result = CalcStat("MitLightPRatPC",L)
								    else:
								        Result = CalcStat("MitLightPRatPA",L)
							    elif SN > 'TACMITLPRATPCAPR':
								    if SN < 'TACMITMPRATPA':
									    if SN < 'TACMITMPPRAT':
										    if SN == 'TACMITMPBONUS':
										        Result = CalcStat("MitMediumPBonus",L)
									    elif SN > 'TACMITMPPRAT':
										    if SN == 'TACMITMPRATP':
										        Result = CalcStat("MitMediumPRatP",L,N)
									    else:
									        Result = CalcStat("MitMediumPPRat",L,N)
								    elif SN > 'TACMITMPRATPA':
									    if SN < 'TACMITMPRATPC':
										    if SN == 'TACMITMPRATPB':
										        Result = CalcStat("MitMediumPRatPB",L)
									    elif SN > 'TACMITMPRATPC':
										    if SN == 'TACMITMPRATPCAP':
										        Result = CalcStat("MitMediumPRatPCap",L)
									    else:
									        Result = CalcStat("MitMediumPRatPC",L)
								    else:
								        Result = CalcStat("MitMediumPRatPA",L)
							    else:
							        Result = CalcStat("MitLightPRatPCapR",L)
						    elif SN > 'TACMITMPRATPCAPR':
							    if SN < 'TOMETOTALFATE':
								    if SN < 'TOMEFATE':
									    if SN < 'TACRESIST':
										    if SN == 'TACMITT':
										        Result = EquSng(StatLinInter("PntMPTacMit","TraitPntS","ProgBMitigation","AdjTraitMit",L,N,0))
									    elif SN > 'TACRESIST':
										    if SN == 'TACRESISTT':
										        Result = CalcStat("ResistAddT",L,N)
									    else:
									        Result = CalcStat("ResistAdd",L,N)
								    elif SN > 'TOMEFATE':
									    if SN < 'TOMEMAIN':
										    if SN == 'TOMEFATEDEC':
										        Result = CalcStat("TomeTotalFateDec",L)-CalcStat("TomeTotalFateDec",L-1)
									    elif SN > 'TOMEMAIN':
										    if SN == 'TOMEMAINDEC':
										        Result = CalcStat("TomeTotalMainDec",L)-CalcStat("TomeTotalMainDec",L-1)
									    else:
									        Result = CalcStat("TomeMainDec",RomanRankDecode(C))
								    else:
								        Result = CalcStat("TomeFateDec",RomanRankDecode(C))
							    elif SN > 'TOMETOTALFATE':
								    if SN < 'TOMETOTALMAINDEC':
									    if SN < 'TOMETOTALLEVEL':
										    if SN == 'TOMETOTALFATEDEC':
										        Result = CalcStat("FateT",CalcStat("TomeTotalLevel",L),2.0)
									    elif SN > 'TOMETOTALLEVEL':
										    if SN == 'TOMETOTALMAIN':
										        Result = CalcStat("TomeTotalMainDec",RomanRankDecode(C))
									    else:
									        if 1 <= Lp and Lm <= 23:
									            Result = DataTableValue((4,15,27,38,48,54,60,63,67,71,75,78,85,90,95,98,101,104,106,110,114,116,121),L)
								    elif SN > 'TOMETOTALMAINDEC':
									    if SN < 'TOMETOTALVITALITYDEC':
										    if SN == 'TOMETOTALVITALITY':
										        Result = CalcStat("TomeTotalVitalityDec",RomanRankDecode(C))
									    elif SN > 'TOMETOTALVITALITYDEC':
										    if SN == 'TOMEVITALITY':
										        Result = CalcStat("TomeVitalityDec",RomanRankDecode(C))
									    else:
									        Result = CalcStat("VitalityT",CalcStat("TomeTotalLevel",L),2.0)
								    else:
								        Result = CalcStat("MainT",CalcStat("TomeTotalLevel",L),2.0)
							    else:
							        Result = CalcStat("TomeTotalFateDec",RomanRankDecode(C))
						    else:
						        Result = CalcStat("MitMediumPRatPCapR",L)
					    elif SN > 'TOMEVITALITYDEC':
						    if SN < 'TRAIT56789CHOICE':
							    if SN < 'TRAIT1234CHOICE':
								    if SN < 'TPENRESIST':
									    if SN < 'TPENBPE':
										    if SN == 'TPENARMOUR':
										        Result = -CalcStat("ArmourPenT",L,CalcStat("TpenChoice",N))
									    elif SN > 'TPENBPE':
										    if SN == 'TPENCHOICE':
										        if 1 <= Lp:
										            Result = DataTableValue((0.5,1,2),L)
									    else:
									        Result = -CalcStat("BPET",L,CalcStat("TpenChoice",N))
								    elif SN > 'TPENRESIST':
									    if SN < 'TRAIT12345CHOICE':
										    if SN == 'TRAIT123455CHOICE':
										        if 1 <= Lp and Lm <= 6:
										            Result = DataTableValue((1,2,3,4,5,5),L)
									    elif SN > 'TRAIT12345CHOICE':
										    if SN == 'TRAIT12347CHOICE':
										        if 1 <= Lp and Lm <= 5:
										            Result = DataTableValue((1,2,3,4,7),L)
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = DataTableValue((1,2,3,4,5),L)
								    else:
								        Result = -CalcStat("ResistT",L,CalcStat("TpenChoice",N)*2)
							    elif SN > 'TRAIT1234CHOICE':
								    if SN < 'TRAIT234CHOICE':
									    if SN < 'TRAIT13510CHOICE':
										    if SN == 'TRAIT123CHOICE':
										        if 1 <= Lp and Lm <= 3:
										            Result = DataTableValue((1,2,3),L)
									    elif SN > 'TRAIT13510CHOICE':
										    if SN == 'TRAIT23456CHOICE':
										        if 1 <= Lp and Lm <= 5:
										            Result = DataTableValue((2,3,4,5,6),L)
									    else:
									        if 1 <= Lp and Lm <= 4:
									            Result = DataTableValue((1,3,5,10),L)
								    elif SN > 'TRAIT234CHOICE':
									    if SN < 'TRAIT47101316CHOICE':
										    if SN == 'TRAIT357912CHOICE':
										        if 1 <= Lp and Lm <= 5:
										            Result = DataTableValue((3,5,7,9,12),L)
									    elif SN > 'TRAIT47101316CHOICE':
										    if SN == 'TRAIT567810CHOICE':
										        if 1 <= Lp and Lm <= 5:
										            Result = DataTableValue((5,6,7,8,10),L)
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = DataTableValue((4,7,10,13,16),L)
								    else:
								        if 1 <= Lp and Lm <= 3:
								            Result = DataTableValue((2,3,4),L)
							    else:
							        if 1 <= Lp and Lm <= 4:
							            Result = DataTableValue((1,2,3,4),L)
						    elif SN > 'TRAIT56789CHOICE':
							    if SN < 'VIRTCHARITYVITALITY':
								    if SN < 'U371LEGACYSTATFIX':
									    if SN < 'TRAITPNTS':
										    if SN == 'TRAIT58121620CHOICE':
										        if 1 <= Lp and Lm <= 5:
										            Result = DataTableValue((5,8,12,16,20),L)
									    elif SN > 'TRAITPNTS':
										    if SN == 'TRAITPNTSVITAL':
										        Result = ((1,25,50,60,65,75,85,95,100,105,115,120,130,140,141,150),(1,25,50,60,65,75,85,95,100,105,115,120,130,140,141,150))
									    else:
									        Result = ((1,25,50,60,65,75,85,95,100,105,115,120,130,131,140,141,150),(1,25,50,60,65,75,85,95,100,105,115,120,130,131,140,141,150))
								    elif SN > 'U371LEGACYSTATFIX':
									    if SN < 'VIRTCHARITYPHYMIT':
										    if SN == 'VARMOUR':
										        Result = RoundDbl(StatLinInter("PntMPArmourVirtues","ItemPntS","ProgBArmourLight","AdjItemMit",L,N,0))
									    elif SN > 'VIRTCHARITYPHYMIT':
										    if SN == 'VIRTCHARITYRESIST':
										        Result = CalcStat("VSResistH",L)
									    else:
									        Result = CalcStat("VSPhyMitM",L)
								    else:
								        if Lm <= 2:
								            Result = 0
								        else:
								            Result = RoundDblUp(CalcStat(C,L-2)*0.07)
							    elif SN > 'VIRTCHARITYVITALITY':
								    if SN < 'VIRTCOMPASSIONTACMIT':
									    if SN < 'VIRTCOMPASSIONARMOUR':
										    if SN == 'VIRTCHARITYVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    elif SN > 'VIRTCOMPASSIONARMOUR':
										    if SN == 'VIRTCOMPASSIONPHYMIT':
										        Result = CalcStat("VSPhyMitH",L)
									    else:
									        Result = CalcStat("VSArmourL",L)
								    elif SN > 'VIRTCOMPASSIONTACMIT':
									    if SN < 'VIRTCONFIDENCECRITHIT':
										    if SN == 'VIRTCOMPASSIONVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    elif SN > 'VIRTCONFIDENCECRITHIT':
										    if SN == 'VIRTCONFIDENCEEVADE':
										        Result = CalcStat("VSEvadeL",L)
									    else:
									        Result = CalcStat("VSCritHitH",L)
								    else:
								        Result = CalcStat("VSTacMitM",L)
							    else:
							        Result = CalcStat("VSVitalityL",L)
						    else:
						        if 1 <= Lp and Lm <= 5:
						            Result = DataTableValue((5,6,7,8,9),L)
					    else:
					        Result = CalcStat("TomeTotalVitalityDec",L)-CalcStat("TomeTotalVitalityDec",L-1)
				    elif SN > 'VIRTCONFIDENCEFINESSE':
					    if SN < 'VIRTHONOURVPMORALE':
						    if SN < 'VIRTFIDELITYPHYMIT':
							    if SN < 'VIRTDISCIPLINEINHEAL':
								    if SN < 'VIRTDETERMINATIONCRITHIT':
									    if SN < 'VIRTCONFIDENCEVPTACMAS':
										    if SN == 'VIRTCONFIDENCEVPPHYMAS':
										        Result = CalcStat("VSVPPhyMas",L)
									    elif SN > 'VIRTCONFIDENCEVPTACMAS':
										    if SN == 'VIRTDETERMINATIONAGILITY':
										        Result = CalcStat("VSAgilityH",L)
									    else:
									        Result = CalcStat("VSVPTacMas",L)
								    elif SN > 'VIRTDETERMINATIONCRITHIT':
									    if SN < 'VIRTDETERMINATIONVPPHYMAS':
										    if SN == 'VIRTDETERMINATIONPHYMAS':
										        Result = CalcStat("VSPhyMasM",L)
									    elif SN > 'VIRTDETERMINATIONVPPHYMAS':
										    if SN == 'VIRTDETERMINATIONVPTACMAS':
										        Result = CalcStat("VSVPTacMas",L)
									    else:
									        Result = CalcStat("VSVPPhyMas",L)
								    else:
								        Result = CalcStat("VSCritHitL",L)
							    elif SN > 'VIRTDISCIPLINEINHEAL':
								    if SN < 'VIRTEMPATHYARMOUR':
									    if SN < 'VIRTDISCIPLINERESIST':
										    if SN == 'VIRTDISCIPLINEPHYMIT':
										        Result = CalcStat("VSPhyMitL",L)
									    elif SN > 'VIRTDISCIPLINERESIST':
										    if SN == 'VIRTDISCIPLINEVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    else:
									        Result = CalcStat("VSResistH",L)
								    elif SN > 'VIRTEMPATHYARMOUR':
									    if SN < 'VIRTEMPATHYRESIST':
										    if SN == 'VIRTEMPATHYCRITDEF':
										        Result = CalcStat("VSCritDefM",L)
									    elif SN > 'VIRTEMPATHYRESIST':
										    if SN == 'VIRTEMPATHYVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    else:
									        Result = CalcStat("VSResistL",L)
								    else:
								        Result = CalcStat("VSArmourH",L)
							    else:
							        Result = CalcStat("VSInHealM",L)
						    elif SN > 'VIRTFIDELITYPHYMIT':
							    if SN < 'VIRTHONESTYCRITHIT':
								    if SN < 'VIRTFORTITUDECRITDEF':
									    if SN < 'VIRTFIDELITYVITALITY':
										    if SN == 'VIRTFIDELITYTACMIT':
										        Result = CalcStat("VSTacMitH",L)
									    elif SN > 'VIRTFIDELITYVITALITY':
										    if SN == 'VIRTFIDELITYVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    else:
									        Result = CalcStat("VSVitalityM",L)
								    elif SN > 'VIRTFORTITUDECRITDEF':
									    if SN < 'VIRTFORTITUDERESIST':
										    if SN == 'VIRTFORTITUDEMORALE':
										        Result = CalcStat("VSMoraleH",L)
									    elif SN > 'VIRTFORTITUDERESIST':
										    if SN == 'VIRTFORTITUDEVPMORALE':
										        Result = CalcStat("VSVPMorale",L)
									    else:
									        Result = CalcStat("VSResistL",L)
								    else:
								        Result = CalcStat("VSCritDefM",L)
							    elif SN > 'VIRTHONESTYCRITHIT':
								    if SN < 'VIRTHONESTYWILL':
									    if SN < 'VIRTHONESTYVPPHYMAS':
										    if SN == 'VIRTHONESTYTACMAS':
										        Result = CalcStat("VSTacMasH",L)
									    elif SN > 'VIRTHONESTYVPPHYMAS':
										    if SN == 'VIRTHONESTYVPTACMAS':
										        Result = CalcStat("VSVPTacMas",L)
									    else:
									        Result = CalcStat("VSVPPhyMas",L)
								    elif SN > 'VIRTHONESTYWILL':
									    if SN < 'VIRTHONOURMORALE':
										    if SN == 'VIRTHONOURCRITDEF':
										        Result = CalcStat("VSCritDefL",L)
									    elif SN > 'VIRTHONOURMORALE':
										    if SN == 'VIRTHONOURTACMIT':
										        Result = CalcStat("VSTacMitM",L)
									    else:
									        Result = CalcStat("VSMoraleH",L)
								    else:
								        Result = CalcStat("VSWillM",L)
							    else:
							        Result = CalcStat("VSCritHitL",L)
						    else:
						        Result = CalcStat("VSPhyMitL",L)
					    elif SN > 'VIRTHONOURVPMORALE':
						    if SN < 'VIRTLOYALTYVPMORALE':
							    if SN < 'VIRTINNOCENCEVPMORALE':
								    if SN < 'VIRTIDEALISMVPMORALE':
									    if SN < 'VIRTIDEALISMINHEAL':
										    if SN == 'VIRTIDEALISMFATE':
										        Result = CalcStat("VSFateH",L)
									    elif SN > 'VIRTIDEALISMINHEAL':
										    if SN == 'VIRTIDEALISMMORALE':
										        Result = CalcStat("VSMoraleL",L)
									    else:
									        Result = CalcStat("VSInHealM",L)
								    elif SN > 'VIRTIDEALISMVPMORALE':
									    if SN < 'VIRTINNOCENCERESIST':
										    if SN == 'VIRTINNOCENCEPHYMIT':
										        Result = CalcStat("VSPhyMitH",L)
									    elif SN > 'VIRTINNOCENCERESIST':
										    if SN == 'VIRTINNOCENCETACMIT':
										        Result = CalcStat("VSTacMitL",L)
									    else:
									        Result = CalcStat("VSResistM",L)
								    else:
								        Result = CalcStat("VSVPMorale",L)
							    elif SN > 'VIRTINNOCENCEVPMORALE':
								    if SN < 'VIRTJUSTICEVPMORALE':
									    if SN < 'VIRTJUSTICEMORALE':
										    if SN == 'VIRTJUSTICEICMR':
										        Result = CalcStat("VSICMRH",L)
									    elif SN > 'VIRTJUSTICEMORALE':
										    if SN == 'VIRTJUSTICETACMIT':
										        Result = CalcStat("VSTacMitL",L)
									    else:
									        Result = CalcStat("VSMoraleM",L)
								    elif SN > 'VIRTJUSTICEVPMORALE':
									    if SN < 'VIRTLOYALTYINHEAL':
										    if SN == 'VIRTLOYALTYARMOUR':
										        Result = CalcStat("VSArmourM",L)
									    elif SN > 'VIRTLOYALTYINHEAL':
										    if SN == 'VIRTLOYALTYVITALITY':
										        Result = CalcStat("VSVitalityH",L)
									    else:
									        Result = CalcStat("VSInHealL",L)
								    else:
								        Result = CalcStat("VSVPMorale",L)
							    else:
							        Result = CalcStat("VSVPMorale",L)
						    elif SN > 'VIRTLOYALTYVPMORALE':
							    if SN < 'VIRTPATIENCEVPMORALE':
								    if SN < 'VIRTMERCYVPMORALE':
									    if SN < 'VIRTMERCYFATE':
										    if SN == 'VIRTMERCYEVADE':
										        Result = CalcStat("VSEvadeH",L)
									    elif SN > 'VIRTMERCYFATE':
										    if SN == 'VIRTMERCYVITALITY':
										        Result = CalcStat("VSVitalityL",L)
									    else:
									        Result = CalcStat("VSFateM",L)
								    elif SN > 'VIRTMERCYVPMORALE':
									    if SN < 'VIRTPATIENCEEVADE':
										    if SN == 'VIRTPATIENCECRITHIT':
										        Result = CalcStat("VSCritHitL",L)
									    elif SN > 'VIRTPATIENCEEVADE':
										    if SN == 'VIRTPATIENCEPOWER':
										        Result = CalcStat("VSPowerH",L)
									    else:
									        Result = CalcStat("VSEvadeM",L)
								    else:
								        Result = CalcStat("VSVPMorale",L)
							    elif SN > 'VIRTPATIENCEVPMORALE':
								    if SN < 'VIRTTOLERANCERESIST':
									    if SN < 'VIRTRNKCOSTTOT':
										    if SN == 'VIRTRNKCOST':
										        if Lm <= 0:
										            Result = 0
										        elif Lm <= 10:
										            Result = 1000
										        elif Lm <= 60:
										            Result = RoundDbl(18*L+878,-2)
										        elif Lm <= 73:
										            Result = RoundDbl(18.75*L+878,-2)
										        elif Lm <= 90:
										            Result = RoundDbl(17.45*L+878,-2)
										        else:
										            Result = 2500
									    elif SN > 'VIRTRNKCOSTTOT':
										    if SN == 'VIRTTOLERANCEPHYMIT':
										        Result = CalcStat("VSPhyMitL",L)
									    else:
									        if 1 <= Lp:
									            Result = CalcStat("VirtRnkCostTot",L-1)+CalcStat("VirtRnkCost",L)
								    elif SN > 'VIRTTOLERANCERESIST':
									    if SN < 'VIRTTOLERANCEVPMORALE':
										    if SN == 'VIRTTOLERANCETACMIT':
										        Result = CalcStat("VSTacMitH",L)
									    elif SN > 'VIRTTOLERANCEVPMORALE':
										    if SN > 'VIRTVALOURCRITHIT':
											    if SN == 'VIRTVALOURFINESSE':
											        Result = CalcStat("VSFinesseM",L)
										    elif SN == 'VIRTVALOURCRITHIT':
										        Result = CalcStat("VSCritHitL",L)
									    else:
									        Result = CalcStat("VSVPMorale",L)
								    else:
								        Result = CalcStat("VSResistM",L)
							    else:
							        Result = CalcStat("VSVPMorale",L)
						    else:
						        Result = CalcStat("VSVPMorale",L)
					    else:
					        Result = CalcStat("VSVPMorale",L)
				    else:
				        Result = CalcStat("VSFinesseM",L)
			    elif SN > 'VIRTVALOURPHYMAS':
				    if SN < 'VSINHEALL':
					    if SN < 'VMMASTERYPSV':
						    if SN < 'VIRTZEALPHYMAS':
							    if SN < 'VIRTWITCRITHIT':
								    if SN < 'VIRTWISDOMTACMAS':
									    if SN < 'VIRTVALOURVPTACMAS':
										    if SN == 'VIRTVALOURVPPHYMAS':
										        Result = CalcStat("VSVPPhyMas",L)
									    elif SN > 'VIRTVALOURVPTACMAS':
										    if SN == 'VIRTWISDOMFINESSE':
										        Result = CalcStat("VSFinesseL",L)
									    else:
									        Result = CalcStat("VSVPTacMas",L)
								    elif SN > 'VIRTWISDOMTACMAS':
									    if SN < 'VIRTWISDOMVPTACMAS':
										    if SN == 'VIRTWISDOMVPPHYMAS':
										        Result = CalcStat("VSVPPhyMas",L)
									    elif SN > 'VIRTWISDOMVPTACMAS':
										    if SN == 'VIRTWISDOMWILL':
										        Result = CalcStat("VSWillH",L)
									    else:
									        Result = CalcStat("VSVPTacMas",L)
								    else:
								        Result = CalcStat("VSTacMasM",L)
							    elif SN > 'VIRTWITCRITHIT':
								    if SN < 'VIRTWITVPPHYMAS':
									    if SN < 'VIRTWITPHYMAS':
										    if SN == 'VIRTWITFINESSE':
										        Result = CalcStat("VSFinesseH",L)
									    elif SN > 'VIRTWITPHYMAS':
										    if SN == 'VIRTWITTACMAS':
										        Result = CalcStat("VSTacMasL",L)
									    else:
									        Result = CalcStat("VSPhyMasL",L)
								    elif SN > 'VIRTWITVPPHYMAS':
									    if SN < 'VIRTZEALCRITHIT':
										    if SN == 'VIRTWITVPTACMAS':
										        Result = CalcStat("VSVPTacMas",L)
									    elif SN > 'VIRTZEALCRITHIT':
										    if SN == 'VIRTZEALMIGHT':
										        Result = CalcStat("VSMightH",L)
									    else:
									        Result = CalcStat("VSCritHitL",L)
								    else:
								        Result = CalcStat("VSVPPhyMas",L)
							    else:
							        Result = CalcStat("VSCritHitM",L)
						    elif SN > 'VIRTZEALPHYMAS':
							    if SN < 'VITALITYCIRAW':
								    if SN < 'VITALITYADJ':
									    if SN < 'VIRTZEALVPTACMAS':
										    if SN == 'VIRTZEALVPPHYMAS':
										        Result = CalcStat("VSVPPhyMas",L)
									    elif SN > 'VIRTZEALVPTACMAS':
										    if SN == 'VITALITY':
										        Result = RoundDblDown(StatLinInter("PntMPVitality","ItemPntSVital","ProgBVitality","VitalityAdj",L,N,0))
									    else:
									        Result = CalcStat("VSVPTacMas",L)
								    elif SN > 'VITALITYADJ':
									    if SN < 'VITALITYCI':
										    if SN == 'VITALITYC':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("VitalityCI",CalcStat("VitalityCILvlFilter",N),N),0)
									    elif SN > 'VITALITYCI':
										    if SN == 'VITALITYCILVLFILTER':
										        if 0 <= Lp and Lm <= 0:
										            Result = 515
										        else:
										            Result = CalcStat("CreepILvlCurr",L)
									    else:
									        Result = RoundDblLotro(CalcStat("VitalityCIRaw",L,N))
								    else:
								        if Lm <= 25:
								            Result = 0.5
								        elif Lm <= 50:
								            Result = 0.6
								        elif Lm <= 60:
								            Result = 0.7
								        elif Lm <= 79:
								            Result = 0.8
								        elif Lm <= 80:
								            Result = 0.9
								        else:
								            Result = 1
							    elif SN > 'VITALITYCIRAW':
								    if SN < 'VMASTERY':
									    if SN < 'VITALITYT':
										    if SN == 'VITALITYCRAW':
										        Result = StatLinInter("","CreepTraitPntS","CreepTraitProgB","",L,CalcStat("VitalityCIRaw",CalcStat("VitalityCILvlFilter",N),N),99)
									    elif SN > 'VITALITYT':
										    if SN == 'VITALITYTADJ':
										        if Lm <= 25:
										            Result = 0.5
										        elif Lm <= 50:
										            Result = 0.6
										        elif Lm <= 60:
										            Result = 0.7
										        elif Lm <= 65:
										            Result = 0.8
										        elif Lm <= 75:
										            Result = 0.9
										        else:
										            Result = 1
									    else:
									        Result = RoundDblDown(StatLinInter("PntMPVitalityT","TraitPntSVital","ProgBVitality","VitalityTAdj",L,N,0))
								    elif SN > 'VMASTERY':
									    if SN < 'VMHIGH':
										    if SN == 'VMASTERYOLD':
										        Result = CalcStat("VMastery",L,N)
									    elif SN > 'VMHIGH':
										    if SN == 'VMLOW':
										        if 1 <= Lp:
										            Result = CalcStat(C,CalcStat("VRnkToILvl",L),0.6)
									    else:
									        if 1 <= Lp:
									            Result = CalcStat(C,CalcStat("VRnkToILvl",L),2.0)
								    else:
								        Result = EquSng(StatLinInter("PntMPMastery","ItemPntSVirtueMastery","ProgBMastery","AdjVirtueMas",L,N,0))
							    else:
							        Result = StatLinInter("PntMPVitalityC","ItemPntS","ProgBVitality","AdjCreepItem",L,N,4)
						    else:
						        Result = CalcStat("VSPhyMasM",L)
					    elif SN > 'VMMASTERYPSV':
						    if SN < 'VSCRITHITH':
							    if SN < 'VSAGILITYL':
								    if SN < 'VRNKCAP':
									    if SN < 'VMMORALEPSV':
										    if SN == 'VMMEDIUM':
										        if 1 <= Lp:
										            Result = CalcStat(C,CalcStat("VRnkToILvl",L),1.0)
									    elif SN > 'VMMORALEPSV':
										    if SN == 'VMORALE':
										        Result = EquSng(StatLinInter("PntMPMoraleVirtues","ItemPntSVirtueMorale","ProgBMorale","AdjVirtueMorale",L,N,0))
									    else:
									        if 1 <= Lp:
									            Result = CalcStat("VMorale",CalcStat("VRnkToILvl",L),0.3)
								    elif SN > 'VRNKCAP':
									    if SN < 'VRNKTOILVL':
										    if SN == 'VRNKLVLCAP':
										        if Lm <= 4:
										            Result = 2
										        elif Lm <= 110:
										            Result = RoundDblDown(L/2)
										        elif Lm <= 139:
										            Result = L-55
										        elif Lm <= 140:
										            Result = L-54
										        elif Lm <= 149:
										            Result = L-53
										        else:
										            Result = 98
									    elif SN > 'VRNKTOILVL':
										    if SN == 'VSAGILITYH':
										        Result = CalcStat("VMHigh",L,"Agility")
									    else:
									        if Lm <= 0:
									            Result = 0
									        elif Lm <= 38:
									            Result = LinFmod(1,4,78,1,38,L)
									        elif Lm <= 48:
									            Result = LinFmod(1,78,178,38,48,L)
									        elif Lm <= 49:
									            Result = LinFmod(1,178,190,48,49,L)
									        elif Lm <= 50:
									            Result = LinFmod(1,190,210,49,50,L)
									        elif Lm <= 51:
									            Result = LinFmod(1,210,222,50,51,L)
									        elif Lm <= 52:
									            Result = LinFmod(1,222,236,51,52,L)
									        elif Lm <= 53:
									            Result = LinFmod(1,236,260,52,53,L)
									        elif Lm <= 55:
									            Result = LinFmod(1,260,292,53,55,L)
									        elif Lm <= 68:
									            Result = LinFmod(1,292,396,55,68,L)
									        else:
									            Result = LinFmod(1,396,706,68,130,L)
								    else:
								        Result = 96
							    elif SN > 'VSAGILITYL':
								    if SN < 'VSARMOURM':
									    if SN < 'VSARMOURH':
										    if SN == 'VSAGILITYM':
										        Result = CalcStat("VMMedium",L,"Agility")
									    elif SN > 'VSARMOURH':
										    if SN == 'VSARMOURL':
										        Result = CalcStat("VMLow",L,"Varmour")
									    else:
									        Result = CalcStat("VMHigh",L,"Varmour")
								    elif SN > 'VSARMOURM':
									    if SN < 'VSCRITDEFL':
										    if SN == 'VSCRITDEFH':
										        Result = CalcStat("VMHigh",L,"CritDef")
									    elif SN > 'VSCRITDEFL':
										    if SN == 'VSCRITDEFM':
										        Result = CalcStat("VMMedium",L,"CritDef")
									    else:
									        Result = CalcStat("VMLow",L,"CritDef")
								    else:
								        Result = CalcStat("VMMedium",L,"Varmour")
							    else:
							        Result = CalcStat("VMLow",L,"Agility")
						    elif SN > 'VSCRITHITH':
							    if SN < 'VSFATEM':
								    if SN < 'VSEVADEL':
									    if SN < 'VSCRITHITM':
										    if SN == 'VSCRITHITL':
										        Result = CalcStat("VMLow",L,"CritHit")
									    elif SN > 'VSCRITHITM':
										    if SN == 'VSEVADEH':
										        Result = CalcStat("VMHigh",L,"Evade")
									    else:
									        Result = CalcStat("VMMedium",L,"CritHit")
								    elif SN > 'VSEVADEL':
									    if SN < 'VSFATEH':
										    if SN == 'VSEVADEM':
										        Result = CalcStat("VMMedium",L,"Evade")
									    elif SN > 'VSFATEH':
										    if SN == 'VSFATEL':
										        Result = CalcStat("VMLow",L,"Fate")
									    else:
									        Result = CalcStat("VMHigh",L,"Fate")
								    else:
								        Result = CalcStat("VMLow",L,"Evade")
							    elif SN > 'VSFATEM':
								    if SN < 'VSICMRH':
									    if SN < 'VSFINESSEL':
										    if SN == 'VSFINESSEH':
										        Result = CalcStat("VMHigh",L,"Finesse")
									    elif SN > 'VSFINESSEL':
										    if SN == 'VSFINESSEM':
										        Result = CalcStat("VMMedium",L,"Finesse")
									    else:
									        Result = CalcStat("VMLow",L,"Finesse")
								    elif SN > 'VSICMRH':
									    if SN < 'VSICMRM':
										    if SN == 'VSICMRL':
										        Result = CalcStat("VMLow",L,"ICMR")
									    elif SN > 'VSICMRM':
										    if SN == 'VSINHEALH':
										        Result = CalcStat("VMHigh",L,"InHeal")
									    else:
									        Result = CalcStat("VMMedium",L,"ICMR")
								    else:
								        Result = CalcStat("VMHigh",L,"ICMR")
							    else:
							        Result = CalcStat("VMMedium",L,"Fate")
						    else:
						        Result = CalcStat("VMHigh",L,"CritHit")
					    else:
					        if 1 <= Lp:
					            Result = CalcStat("VMastery",CalcStat("VRnkToILvl",L),0.2)
				    elif SN > 'VSINHEALL':
					    if SN < 'VSWILLH':
						    if SN < 'VSPOWERM':
							    if SN < 'VSPHYMASH':
								    if SN < 'VSMIGHTM':
									    if SN < 'VSMIGHTH':
										    if SN == 'VSINHEALM':
										        Result = CalcStat("VMMedium",L,"InHeal")
									    elif SN > 'VSMIGHTH':
										    if SN == 'VSMIGHTL':
										        Result = CalcStat("VMLow",L,"Might")
									    else:
									        Result = CalcStat("VMHigh",L,"Might")
								    elif SN > 'VSMIGHTM':
									    if SN < 'VSMORALEL':
										    if SN == 'VSMORALEH':
										        Result = CalcStat("VMHigh",L,"VMorale")
									    elif SN > 'VSMORALEL':
										    if SN == 'VSMORALEM':
										        Result = CalcStat("VMMedium",L,"VMorale")
									    else:
									        Result = CalcStat("VMLow",L,"VMorale")
								    else:
								        Result = CalcStat("VMMedium",L,"Might")
							    elif SN > 'VSPHYMASH':
								    if SN < 'VSPHYMITL':
									    if SN < 'VSPHYMASM':
										    if SN == 'VSPHYMASL':
										        Result = CalcStat("VMLow",L,"PhyMas")
									    elif SN > 'VSPHYMASM':
										    if SN == 'VSPHYMITH':
										        Result = CalcStat("VMHigh",L,"PhyMit")
									    else:
									        Result = CalcStat("VMMedium",L,"PhyMas")
								    elif SN > 'VSPHYMITL':
									    if SN < 'VSPOWERH':
										    if SN == 'VSPHYMITM':
										        Result = CalcStat("VMMedium",L,"PhyMit")
									    elif SN > 'VSPOWERH':
										    if SN == 'VSPOWERL':
										        Result = CalcStat("VMLow",L,"Power")
									    else:
									        Result = CalcStat("VMHigh",L,"Power")
								    else:
								        Result = CalcStat("VMLow",L,"PhyMit")
							    else:
							        Result = CalcStat("VMHigh",L,"PhyMas")
						    elif SN > 'VSPOWERM':
							    if SN < 'VSTACMITL':
								    if SN < 'VSTACMASH':
									    if SN < 'VSRESISTL':
										    if SN == 'VSRESISTH':
										        Result = CalcStat("VMHigh",L,"Resist")
									    elif SN > 'VSRESISTL':
										    if SN == 'VSRESISTM':
										        Result = CalcStat("VMMedium",L,"Resist")
									    else:
									        Result = CalcStat("VMLow",L,"Resist")
								    elif SN > 'VSTACMASH':
									    if SN < 'VSTACMASM':
										    if SN == 'VSTACMASL':
										        Result = CalcStat("VMLow",L,"TacMas")
									    elif SN > 'VSTACMASM':
										    if SN == 'VSTACMITH':
										        Result = CalcStat("VMHigh",L,"TacMit")
									    else:
									        Result = CalcStat("VMMedium",L,"TacMas")
								    else:
								        Result = CalcStat("VMHigh",L,"TacMas")
							    elif SN > 'VSTACMITL':
								    if SN < 'VSVITALITYM':
									    if SN < 'VSVITALITYH':
										    if SN == 'VSTACMITM':
										        Result = CalcStat("VMMedium",L,"TacMit")
									    elif SN > 'VSVITALITYH':
										    if SN == 'VSVITALITYL':
										        Result = CalcStat("VMLow",L,"Vitality")
									    else:
									        Result = CalcStat("VMHigh",L,"Vitality")
								    elif SN > 'VSVITALITYM':
									    if SN < 'VSVPPHYMAS':
										    if SN == 'VSVPMORALE':
										        Result = CalcStat("VMMoralePsv",L)
									    elif SN > 'VSVPPHYMAS':
										    if SN == 'VSVPTACMAS':
										        Result = CalcStat("VMMasteryPsv",L)
									    else:
									        Result = CalcStat("VMMasteryPsv",L)
								    else:
								        Result = CalcStat("VMMedium",L,"Vitality")
							    else:
							        Result = CalcStat("VMLow",L,"TacMit")
						    else:
						        Result = CalcStat("VMMedium",L,"Power")
					    elif SN > 'VSWILLH':
						    if SN < 'WARDENCDBASEICMR':
							    if SN < 'WARDENCDAGILITYTOPHYMIT':
								    if SN < 'WARDENCDAGILITYTOCRITHIT':
									    if SN < 'VSWILLM':
										    if SN == 'VSWILLL':
										        Result = CalcStat("VMLow",L,"Will")
									    elif SN > 'VSWILLM':
										    if SN == 'WARDENCDAGILITYTOBLOCK':
										        Result = 2
									    else:
									        Result = CalcStat("VMMedium",L,"Will")
								    elif SN > 'WARDENCDAGILITYTOCRITHIT':
									    if SN < 'WARDENCDAGILITYTOPARRY':
										    if SN == 'WARDENCDAGILITYTOOUTHEAL':
										        Result = 3
									    elif SN > 'WARDENCDAGILITYTOPARRY':
										    if SN == 'WARDENCDAGILITYTOPHYMAS':
										        Result = 3
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'WARDENCDAGILITYTOPHYMIT':
								    if SN < 'WARDENCDARMOURTOTACMIT':
									    if SN < 'WARDENCDARMOURTOCOMPHYMIT':
										    if SN == 'WARDENCDAGILITYTOTACMIT':
										        Result = 1
									    elif SN > 'WARDENCDARMOURTOCOMPHYMIT':
										    if SN == 'WARDENCDARMOURTONONPHYMIT':
										        Result = 0.2
									    else:
									        Result = 1
								    elif SN > 'WARDENCDARMOURTOTACMIT':
									    if SN < 'WARDENCDBASEAGILITY':
										    if SN == 'WARDENCDARMOURTYPE':
										        Result = 2
									    elif SN > 'WARDENCDBASEAGILITY':
										    if SN == 'WARDENCDBASEFATE':
										        Result = CalcStat("ClassBaseFate",L)
									    else:
									        Result = CalcStat("ClassBaseAgilityH",L)
								    else:
								        Result = 0.2
							    else:
							        Result = 1
						    elif SN > 'WARDENCDBASEICMR':
							    if SN < 'WARDENCDBASEWILL':
								    if SN < 'WARDENCDBASENCMR':
									    if SN < 'WARDENCDBASEMIGHT':
										    if SN == 'WARDENCDBASEICPR':
										        Result = CalcStat("ClassBaseICPR",L)
									    elif SN > 'WARDENCDBASEMIGHT':
										    if SN == 'WARDENCDBASEMORALE':
										        Result = CalcStat("ClassBaseMorale",L)
									    else:
									        Result = CalcStat("ClassBaseMightM",L)
								    elif SN > 'WARDENCDBASENCMR':
									    if SN < 'WARDENCDBASEPOWER':
										    if SN == 'WARDENCDBASENCPR':
										        Result = CalcStat("ClassBaseNCPR",L)
									    elif SN > 'WARDENCDBASEPOWER':
										    if SN == 'WARDENCDBASEVITALITY':
										        Result = CalcStat("ClassBaseVitality",L)
									    else:
									        Result = CalcStat("ClassBasePower",L)
								    else:
								        Result = CalcStat("ClassBaseNCMRH",L)
							    elif SN > 'WARDENCDBASEWILL':
								    if SN < 'WARDENCDCANBLOCK':
									    if SN < 'WARDENCDCALCTYPENONPHYMIT':
										    if SN == 'WARDENCDCALCTYPECOMPHYMIT':
										        Result = 13
									    elif SN > 'WARDENCDCALCTYPENONPHYMIT':
										    if SN == 'WARDENCDCALCTYPETACMIT':
										        Result = 26
									    else:
									        Result = 13
								    elif SN > 'WARDENCDCANBLOCK':
									    if SN < 'WARDENCDFATETOPOWER':
										    if SN == 'WARDENCDFATETONCPR':
										        Result = 0.07
									    elif SN > 'WARDENCDFATETOPOWER':
										    if SN > 'WARDENCDHASPOWER':
											    if SN == 'WARDENCDMIGHTTOBLOCK':
											        Result = 1
										    elif SN == 'WARDENCDHASPOWER':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = CalcStat("ClassBaseWillL",L)
						    else:
						        Result = CalcStat("ClassBaseICMRH",L)
					    else:
					        Result = CalcStat("VMHigh",L,"Will")
				    else:
				        Result = CalcStat("VMLow",L,"InHeal")
			    else:
			        Result = CalcStat("VSPhyMasH",L)
		    elif SN > 'WARDENCDMIGHTTOCRITHIT':
			    if SN < 'WORTHTABK':
				    if SN < 'WORTHTABAQ':
					    if SN < 'WORTHEXT':
						    if SN < 'WARDINGLOREPHYMIT':
							    if SN < 'WARDENCDVITALITYTOMORALE':
								    if SN < 'WARDENCDPHYMITTOCOMPHYMIT':
									    if SN < 'WARDENCDMIGHTTOOUTHEAL':
										    if SN == 'WARDENCDMIGHTTOFINESSE':
										        Result = 1.5
									    elif SN > 'WARDENCDMIGHTTOOUTHEAL':
										    if SN == 'WARDENCDMIGHTTOPHYMAS':
										        Result = 2
									    else:
									        Result = 2
								    elif SN > 'WARDENCDPHYMITTOCOMPHYMIT':
									    if SN < 'WARDENCDTACMASTOOUTHEAL':
										    if SN == 'WARDENCDPHYMITTONONPHYMIT':
										        Result = 1
									    elif SN > 'WARDENCDTACMASTOOUTHEAL':
										    if SN == 'WARDENCDVITALITYTOICMR':
										        Result = 0.012
									    else:
									        Result = 1
								    else:
								        Result = 1
							    elif SN > 'WARDENCDVITALITYTOMORALE':
								    if SN < 'WARDENCDWILLTOPHYMAS':
									    if SN < 'WARDENCDWILLTOFINESSE':
										    if SN == 'WARDENCDVITALITYTONCMR':
										        Result = 0.12
									    elif SN > 'WARDENCDWILLTOFINESSE':
										    if SN == 'WARDENCDWILLTOOUTHEAL':
										        Result = 1
									    else:
									        Result = 1
								    elif SN > 'WARDENCDWILLTOPHYMAS':
									    if SN < 'WARDENCDWILLTORESIST':
										    if SN == 'WARDENCDWILLTOPHYMIT':
										        Result = 1.5
									    elif SN > 'WARDENCDWILLTORESIST':
										    if SN == 'WARDENCDWILLTOTACMIT':
										        Result = 1.5
									    else:
									        Result = 1
								    else:
								        Result = 1
							    else:
							        Result = 4.5
						    elif SN > 'WARDINGLOREPHYMIT':
							    if SN < 'WEAVERCDCALCTYPECOMPHYMIT':
								    if SN < 'WARLEADERCDCALCTYPENONPHYMIT':
									    if SN < 'WARLEADERCANBLOCK':
										    if SN == 'WARDINGLORETACMIT':
										        if Lm <= 105:
										            Result = CalcStat("Mitigation",L,1.6)
										        elif 120 <= Lp and Lm <= 120 or 130 <= Lp and Lm <= 130:
										            Result = CalcStat("TacMitT",L,1.6)
										        else:
										            Result = CalcStat("TacMitT",L,1.2)
									    elif SN > 'WARLEADERCANBLOCK':
										    if SN == 'WARLEADERCDCALCTYPECOMPHYMIT':
										        Result = 14
									    else:
									        Result = 1
								    elif SN > 'WARLEADERCDCALCTYPENONPHYMIT':
									    if SN < 'WARLEADERCDHASPOWER':
										    if SN == 'WARLEADERCDCALCTYPETACMIT':
										        Result = 27
									    elif SN > 'WARLEADERCDHASPOWER':
										    if SN == 'WEAVERCANBLOCK':
										        Result = 1
									    else:
									        Result = 1
								    else:
								        Result = 14
							    elif SN > 'WEAVERCDCALCTYPECOMPHYMIT':
								    if SN < 'WILL':
									    if SN < 'WEAVERCDCALCTYPETACMIT':
										    if SN == 'WEAVERCDCALCTYPENONPHYMIT':
										        Result = 14
									    elif SN > 'WEAVERCDCALCTYPETACMIT':
										    if SN == 'WEAVERCDHASPOWER':
										        Result = 1
									    else:
									        Result = 27
								    elif SN > 'WILL':
									    if SN < 'WILLCI':
										    if SN == 'WILLC':
										        Result = CalcStat("MainC",L,N)
									    elif SN > 'WILLCI':
										    if SN == 'WILLT':
										        Result = CalcStat("MainT",L,N)
									    else:
									        Result = CalcStat("MainCI",L,N)
								    else:
								        Result = CalcStat("Main",L,N)
							    else:
							        Result = 13
						    else:
						        if Lm <= 105:
						            Result = CalcStat("Mitigation",L,1.6)
						        elif 120 <= Lp and Lm <= 120 or 130 <= Lp and Lm <= 130:
						            Result = CalcStat("PhyMitT",L,1.6)
						        else:
						            Result = CalcStat("PhyMitT",L,1.2)
					    elif SN > 'WORTHEXT':
						    if SN < 'WORTHTABAB':
							    if SN < 'WORTHMPF':
								    if SN < 'WORTHMPB':
									    if SN < 'WORTHEXT8LIN':
										    if SN == 'WORTHEXT4LIN':
										        if Lm <= 501:
										            Result = CalcStat("WorthExt",L,C)
										        elif Lm <= 601:
										            Result = CalcStat("WorthExt",501,C)+(L-501)*4
									    elif SN > 'WORTHEXT8LIN':
										    if SN == 'WORTHMPA':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,1.1,1.15,1.2,1.3),L))
									    else:
									        if Lm <= 501:
									            Result = CalcStat("WorthExt",L,C)
									        elif Lm <= 601:
									            Result = CalcStat("WorthExt",501,C)+(L-501)*8
								    elif SN > 'WORTHMPB':
									    if SN < 'WORTHMPD':
										    if SN == 'WORTHMPC':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,1,1,1,1),L))
									    elif SN > 'WORTHMPD':
										    if SN == 'WORTHMPE':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,1.1,1.15,1.2,1.25),L))
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = EquSng(DataTableValue((1,1,1,2,3),L))
								    else:
								        if 1 <= Lp and Lm <= 5:
								            Result = EquSng(DataTableValue((1,1.2,2,3,4),L))
							    elif SN > 'WORTHMPF':
								    if SN < 'WORTHMPJ':
									    if SN < 'WORTHMPH':
										    if SN == 'WORTHMPG':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,2,3,4,5),L))
									    elif SN > 'WORTHMPH':
										    if SN == 'WORTHMPI':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,2,2.5,3,10),L))
									    else:
									        if 1 <= Lp and Lm <= 5:
									            Result = EquSng(DataTableValue((1,1.2,1.8,3.2,5),L))
								    elif SN > 'WORTHMPJ':
									    if SN < 'WORTHTABA':
										    if SN == 'WORTHMPK':
										        if 1 <= Lp and Lm <= 5:
										            Result = EquSng(DataTableValue((1,1.2,1.3,1.35,1.4),L))
									    elif SN > 'WORTHTABA':
										    if SN == 'WORTHTABAA':
										        Result = CalcStat("WorthTabD",L)+20
									    else:
									        if Lm <= 1:
									            Result = 1
									        else:
									            Result = CalcStat("WorthTabAF",L)
								    else:
								        if 1 <= Lp and Lm <= 5:
								            Result = EquSng(DataTableValue((1,1,1,1,5),L))
							    else:
							        if 1 <= Lp and Lm <= 5:
							            Result = EquSng(DataTableValue((0.5,1,1.25,1.5,2),L))
						    elif SN > 'WORTHTABAB':
							    if SN < 'WORTHTABAJ':
								    if SN < 'WORTHTABAF':
									    if SN < 'WORTHTABAD':
										    if SN == 'WORTHTABAC':
										        Result = CalcStat("WorthTabE",L)-30
									    elif SN > 'WORTHTABAD':
										    if SN == 'WORTHTABAE':
										        Result = CalcStat("WorthTabE",L)
									    else:
									        Result = 7*L+100
								    elif SN > 'WORTHTABAF':
									    if SN < 'WORTHTABAH':
										    if SN == 'WORTHTABAG':
										        Result = CalcStat("WorthTabAF",L)+25
									    elif SN > 'WORTHTABAH':
										    if SN == 'WORTHTABAI':
										        if Lm <= 16:
										            Result = 10.73*L+54.3
										        elif Lm <= 34:
										            Result = 10.735*L+54
										        elif Lm <= 35:
										            Result = 429
										        elif Lm <= 41:
										            Result = 10.65*L+57.1
										        elif Lm <= 49:
										            Result = 10.7*L+55.3
										        else:
										            Result = 9*L+141
									    else:
									        if Lm <= 49:
									            Result = CalcStat("WorthTabALBase",L+7)-66
									        else:
									            Result = 9*L+72
								    else:
								        if Lm <= 49:
								            Result = 2.5*L
								        else:
								            Result = 3*L-25
							    elif SN > 'WORTHTABAJ':
								    if SN < 'WORTHTABAM':
									    if SN < 'WORTHTABAL':
										    if SN == 'WORTHTABAK':
										        if Lm <= 49:
										            Result = CalcStat("WorthTabALBase",L+1)
										        else:
										            Result = 9*L+78
									    elif SN > 'WORTHTABAL':
										    if SN == 'WORTHTABALBASE':
										        Result = 9.86*L+23.51+RoundDbl(L*0.1+0.3)*0.4
									    else:
									        if Lm <= 49:
									            Result = CalcStat("WorthTabALBase",L)
									        else:
									            Result = 9*L+69
								    elif SN > 'WORTHTABAM':
									    if SN < 'WORTHTABAO':
										    if SN == 'WORTHTABAN':
										        if Lm <= 50:
										            Result = 8.25*L+27.75
										        else:
										            Result = 8*L+40
									    elif SN > 'WORTHTABAO':
										    if SN == 'WORTHTABAP':
										        Result = CalcStat("WorthTabAQ",L)
									    else:
									        Result = CalcStat("WorthTabE",L)
								    else:
								        Result = CalcStat("WorthTabB",L)
							    else:
							        Result = CalcStat("WorthTabAH",L)
						    else:
						        Result = 7*L+50
					    else:
					        if Lm <= 360:
					            Result = RoundDbl(CalcStat("StatC",L,C))
					        elif Lm <= 601:
					            Result = RoundDbl(CalcStat("StatC",L-1,C))
				    elif SN > 'WORTHTABAQ':
					    if SN < 'WORTHTABBU':
						    if SN < 'WORTHTABBE':
							    if SN < 'WORTHTABAY':
								    if SN < 'WORTHTABAU':
									    if SN < 'WORTHTABAS':
										    if SN == 'WORTHTABAR':
										        Result = CalcStat("WorthTabD",L)+37.5
									    elif SN > 'WORTHTABAS':
										    if SN == 'WORTHTABAT':
										        if Lm <= 4:
										            Result = RoundDbl(3*L+20,-1)
										        elif Lm <= 7:
										            Result = 60
										        elif Lm <= 10:
										            Result = 100
										        elif Lm <= 13:
										            Result = 180
										        elif Lm <= 16:
										            Result = 270
										        elif Lm <= 19:
										            Result = 310
										        elif Lm <= 40:
										            Result = RoundDbl(3.2*L+274,-1)
										        elif Lm <= 43:
										            Result = 400
										        elif Lm <= 53:
										            Result = RoundDbl(1.9*L+334,-1)
										        elif Lm <= 56:
										            Result = 460
										        elif Lm <= 59:
										            Result = 480
										        else:
										            Result = 20*L-680
									    else:
									        Result = CalcStat("WorthTabU",L)
								    elif SN > 'WORTHTABAU':
									    if SN < 'WORTHTABAW':
										    if SN == 'WORTHTABAV':
										        if Lm <= 4:
										            Result = RoundDbl(3*L+20,-1)
										        elif Lm <= 7:
										            Result = 70
										        elif Lm <= 10:
										            Result = 140
										        elif Lm <= 13:
										            Result = 270
										        elif Lm <= 16:
										            Result = 400
										        elif Lm <= 19:
										            Result = 460
										        elif Lm <= 25:
										            Result = RoundDbl(3*L+447.5,-1)
										        elif Lm <= 46:
										            Result = RoundDbl(3.2*L+455,-1)
										        elif Lm <= 50:
										            Result = 620
										        else:
										            Result = 20*L-360
									    elif SN > 'WORTHTABAW':
										    if SN == 'WORTHTABAX':
										        if Lm <= 16:
										            Result = 10.75*L+54
										        elif Lm <= 34:
										            Result = 10.75*L+53.7
										        elif Lm <= 35:
										            Result = 429
										        elif Lm <= 41:
										            Result = 10.65*L+57.1
										        elif Lm <= 49:
										            Result = 10.68*L+56.25
										        else:
										            Result = 12*L-9
									    else:
									        if Lm <= 1:
									            Result = 50
									        elif Lm <= 49:
									            Result = 2.5*L+102.5
									        elif Lm <= 80:
									            Result = 3*L+78
									        elif Lm <= 120:
									            Result = 2.97*L+79.5
									        else:
									            Result = 3*L+75
								    else:
								        Result = CalcStat("WorthTabBN",L)*1.25
							    elif SN > 'WORTHTABAY':
								    if SN < 'WORTHTABBA':
									    if SN < 'WORTHTABAZBASE':
										    if SN == 'WORTHTABAZ':
										        if Lm <= 10:
										            Result = CalcStat("WorthTabAZBase",L)*62.5
										        elif Lm <= 65:
										            Result = CalcStat("WorthTabAZBase",L)*125
										        else:
										            Result = CalcStat("WorthTabAZBase",L)*25
									    elif SN > 'WORTHTABAZBASE':
										    if SN == 'WORTHTABB':
										        if Lm <= 50:
										            Result = 8.25*L+22.25
										        else:
										            Result = 8*L+35
									    else:
									        if Lm <= 44:
									            Result = RoundDbl(0.0525*L+0.7)
									        elif Lm <= 65:
									            Result = RoundDbl(0.19*L-4.85)
									        elif Lm <= 81:
									            Result = RoundDbl(0.19*L+28.15)
									        else:
									            Result = RoundDbl(0.19*L+28.15+RoundDbl(L*0.05-4.55)*0.2)
								    elif SN > 'WORTHTABBA':
									    if SN < 'WORTHTABBC':
										    if SN == 'WORTHTABBB':
										        if Lm <= 1:
										            Result = 40
										        elif Lm <= 10:
										            Result = RoundDbl(0.35*L-0.1)*20
										        elif Lm <= 13:
										            Result = 100
										        elif Lm <= 19:
										            Result = RoundDbl(0.35*L+1.6)*20
										        elif Lm <= 25:
										            Result = RoundDbl(2*L+150,-1)
										        elif Lm <= 40:
										            Result = RoundDbl(2*L+164,-1)
										        elif Lm <= 49:
										            Result = RoundDbl(L+201,-1)
										        else:
										            Result = 20*L-740
									    elif SN > 'WORTHTABBC':
										    if SN == 'WORTHTABBD':
										        Result = CalcStat("WorthTabK",L)+1
									    else:
									        if Lm <= 34:
									            Result = RoundDbl(L/15+0.8)*3750+1250
									        elif Lm <= 35:
									            Result = 100000
									        else:
									            Result = 125500
								    else:
								        Result = 5*L+385
							    else:
							        Result = 5*L
						    elif SN > 'WORTHTABBE':
							    if SN < 'WORTHTABBM':
								    if SN < 'WORTHTABBI':
									    if SN < 'WORTHTABBG':
										    if SN == 'WORTHTABBF':
										        Result = CalcStat("WorthTabAV",L)+20
									    elif SN > 'WORTHTABBG':
										    if SN == 'WORTHTABBH':
										        if Lm <= 80:
										            Result = RoundDbl(0.05*L-0.05)+RoundDbl(0.05*L+0.45)
										        else:
										            Result = RoundDbl(0.05*L-0.1)+RoundDbl(0.05*L+0.45)
									    else:
									        if Lm <= 7:
									            Result = RoundDbl(0.2*L-0.4)*2+1
									        elif Lm <= 16:
									            Result = RoundDbl(L/3-2)*6
									        elif Lm <= 22:
									            Result = RoundDbl(L/3+1)*3
									        elif Lm <= 25:
									            Result = RoundDbl(L/3+1)*3-2
									        elif Lm <= 80:
									            Result = RoundDbl(L/3+18)-2
									        else:
									            Result = L-37
								    elif SN > 'WORTHTABBI':
									    if SN < 'WORTHTABBK':
										    if SN == 'WORTHTABBJ':
										        Result = RoundDbl(0.1*L+0.45)*3
									    elif SN > 'WORTHTABBK':
										    if SN == 'WORTHTABBL':
										        if Lm <= 35:
										            Result = 126600
										        elif Lm <= 46:
										            Result = 150600
										        elif Lm <= 47:
										            Result = 180720
										        else:
										            Result = 150600
									    else:
									        if Lm <= 10:
									            Result = RoundDbl(0.1*L+0.45)
									        else:
									            Result = RoundDbl(0.1*L-0.6)*2
								    else:
								        Result = CalcStat("WorthTabG",L)-25
							    elif SN > 'WORTHTABBM':
								    if SN < 'WORTHTABBQ':
									    if SN < 'WORTHTABBO':
										    if SN == 'WORTHTABBN':
										        if Lm <= 1:
										            Result = 400
										        else:
										            Result = 20*L+800
									    elif SN > 'WORTHTABBO':
										    if SN == 'WORTHTABBP':
										        if Lm <= 10:
										            Result = 156.25*L+1562.5
										        elif Lm <= 20:
										            Result = 312.5*L
										        elif Lm <= 30:
										            Result = 625*L-6250
										        elif Lm <= 40:
										            Result = 1250*L-25000
										        else:
										            Result = 2500*L-75000
									    else:
									        if Lm <= 10:
									            Result = 10
									        elif Lm <= 40:
									            Result = RoundDbl(0.1*L-0.55)*50-25
									        elif Lm <= 80:
									            Result = RoundDbl(0.1*L-0.55)*50
									        else:
									            Result = RoundDbl(0.1*L-0.55)*25+175
								    elif SN > 'WORTHTABBQ':
									    if SN < 'WORTHTABBS':
										    if SN == 'WORTHTABBR':
										        if Lm <= 49:
										            Result = CalcStat("WorthTabBQ",L)*2
										        else:
										            Result = 4*L+250
									    elif SN > 'WORTHTABBS':
										    if SN == 'WORTHTABBT':
										        Result = 62500
									    else:
									        Result = CalcStat("WorthTabBR",L)*2
								    else:
								        if Lm <= 1:
								            Result = 50
								        elif Lm <= 49:
								            Result = RoundDbl(2.5*L+100)
								        else:
								            Result = 3*L+75
							    else:
							        if Lm <= 1:
							            Result = 10
							        else:
							            Result = 20*L-20
						    else:
						        if Lm <= 1:
						            Result = 60
						        elif Lm <= 7:
						            Result = RoundDbl(L/3)*40+30
						        elif Lm <= 13:
						            Result = RoundDbl(L/3)*130-210
						        elif Lm <= 19:
						            Result = RoundDbl(L/3)*60+140
						        elif Lm <= 25:
						            Result = RoundDbl(L/3)*10+480
						        elif Lm <= 46:
						            Result = RoundDbl(L/3)*10+490
						        elif Lm <= 50:
						            Result = 660
						        else:
						            Result = 20*L-320
					    elif SN > 'WORTHTABBU':
						    if SN < 'WORTHTABCJ':
							    if SN < 'WORTHTABCB':
								    if SN < 'WORTHTABBY':
									    if SN < 'WORTHTABBW':
										    if SN == 'WORTHTABBV':
										        if Lm <= 29:
										            Result = 1250
										        else:
										            Result = RoundDbl(0.05*L-1)*2500
									    elif SN > 'WORTHTABBW':
										    if SN == 'WORTHTABBX':
										        if Lm <= 10:
										            Result = RoundDbl(0.1*L+0.45)*3
										        elif Lm <= 140:
										            Result = RoundDbl(0.1*L-0.6)*6
										        else:
										            Result = RoundDbl(0.1*L+0.4)*4+22
									    else:
									        if Lm <= 1:
									            Result = 645
									        elif Lm <= 9:
									            Result = 20*L+980
									        else:
									            Result = 50*L+920
								    elif SN > 'WORTHTABBY':
									    if SN < 'WORTHTABC':
										    if SN == 'WORTHTABBZ':
										        if Lm <= 10:
										            Result = 27.42*L+273.1
										        elif Lm <= 20:
										            Result = 54.69*L
										        elif Lm <= 30:
										            Result = 109.35*L-1093
										        elif Lm <= 40:
										            Result = 218.75*L-4375
										        elif Lm <= 80:
										            Result = 437.5*L-13125
										        else:
										            Result = 437*L-13085
									    elif SN > 'WORTHTABC':
										    if SN == 'WORTHTABCA':
										        if Lm <= 10:
										            Result = 7.25*L+72.25
										        elif Lm <= 20:
										            Result = 14.49*L+0.11
										        elif Lm <= 30:
										            Result = 29*L-290
										        elif Lm <= 35:
										            Result = 57.99*L-1160.16
										        elif Lm <= 40:
										            Result = 57.99*L-1160.12
										        elif Lm <= 80:
										            Result = 115.94*L-3478.2
										        else:
										            Result = 116*L-3483
									    else:
									        Result = CalcStat("WorthTabD",L)+20
								    else:
								        Result = 90000
							    elif SN > 'WORTHTABCB':
								    if SN < 'WORTHTABCF':
									    if SN < 'WORTHTABCD':
										    if SN == 'WORTHTABCC':
										        Result = CalcStat("WorthTabBK",L)*5
									    elif SN > 'WORTHTABCD':
										    if SN == 'WORTHTABCE':
										        Result = CalcStat("WorthTabBN",L)*10
									    else:
									        Result = CalcStat("WorthTabBK",L)*25
								    elif SN > 'WORTHTABCF':
									    if SN < 'WORTHTABCH':
										    if SN == 'WORTHTABCG':
										        Result = 20
									    elif SN > 'WORTHTABCH':
										    if SN == 'WORTHTABCI':
										        Result = 40000
									    else:
									        Result = 50000
								    else:
								        if Lm <= 20:
								            Result = RoundDbl(0.1*L-0.55)*600+200
								        elif Lm <= 40:
								            Result = RoundDbl(0.1*L-0.55)*1000-500
								        elif Lm <= 60:
								            Result = RoundDbl(0.1*L-0.55)*2000-4000
								        elif Lm <= 70:
								            Result = 8500
								        elif Lm <= 140:
								            Result = RoundDbl(0.1*L-0.55)*2500-7500
								        elif Lm <= 200:
								            Result = RoundDbl(0.1*L-0.55)*3000-14000
								        else:
								            Result = RoundDbl(0.1*L-0.55)*2500-3500
							    else:
							        Result = 0.1
						    elif SN > 'WORTHTABCJ':
							    if SN < 'WORTHTABCR':
								    if SN < 'WORTHTABCN':
									    if SN < 'WORTHTABCL':
										    if SN == 'WORTHTABCK':
										        Result = 15000
									    elif SN > 'WORTHTABCL':
										    if SN == 'WORTHTABCM':
										        Result = 7500
									    else:
									        Result = 12500
								    elif SN > 'WORTHTABCN':
									    if SN < 'WORTHTABCP':
										    if SN == 'WORTHTABCO':
										        Result = CalcStat("WorthTabAB",L)
									    elif SN > 'WORTHTABCP':
										    if SN == 'WORTHTABCQ':
										        if Lm <= 10:
										            Result = RoundDbl(0.3*L+0.2)*2
										        elif Lm <= 16:
										            Result = RoundDbl(0.25*L-1)*6
										        elif Lm <= 22:
										            Result = RoundDbl(0.3*L+5.5)*2
										        elif Lm <= 50:
										            Result = RoundDbl((1/6)*L+8.75)*2
										        elif Lm <= 80:
										            Result = RoundDbl((1/3)*L-11.5)*6
										        else:
										            Result = RoundDbl(0.25*L-4.6)*6
									    else:
									        Result = 1
								    else:
								        Result = RoundDbl(0.1*L+0.5)*10000
							    elif SN > 'WORTHTABCR':
								    if SN < 'WORTHTABF':
									    if SN < 'WORTHTABD':
										    if SN == 'WORTHTABCS':
										        Result = CalcStat("WorthTabBR",L)*3
									    elif SN > 'WORTHTABD':
										    if SN == 'WORTHTABE':
										        if Lm <= 9:
										            Result = 30*L+50
										        else:
										            Result = 7*L+280
									    else:
									        if Lm <= 49:
									            Result = 7.5*L
									        else:
									            Result = 8*L-25
								    elif SN > 'WORTHTABF':
									    if SN < 'WORTHTABH':
										    if SN == 'WORTHTABG':
										        if Lm <= 1:
										            Result = 50
										        else:
										            Result = CalcStat("WorthTabAF",L)+100
									    elif SN > 'WORTHTABH':
										    if SN > 'WORTHTABI':
											    if SN == 'WORTHTABJ':
											        if Lm <= 4:
											            Result = 2.5*L+7.5
											        elif Lm <= 5:
											            Result = 23
											        else:
											            Result = 4*L
										    elif SN == 'WORTHTABI':
										        if Lm <= 4:
										            Result = 1
										        elif Lm <= 10:
										            Result = 0.7*L-1
										        elif Lm <= 15:
										            Result = 1.4*L-7
										        elif Lm <= 24:
										            Result = 1.25*L-5
										        elif Lm <= 49:
										            Result = 2.5*L-35
										        else:
										            Result = 3*L-60
									    else:
									        if Lm <= 2:
									            Result = L
									        elif Lm <= 9:
									            Result = 1.48*L-2.85
									        elif Lm <= 11:
									            Result = 2.5*L-13
									        elif Lm <= 24:
									            Result = 2.5*L-10
									        else:
									            Result = 5*L-70
								    else:
								        Result = 0.1
							    else:
							        Result = CalcStat("WorthTabM",L)-15
						    else:
						        Result = 20000
					    else:
					        if Lm <= 80:
					            Result = 20*L+300
					        else:
					            Result = 10*L+1100
				    else:
				        if Lm <= 10:
				            Result = 7.5*L+60
				        elif Lm <= 49:
				            Result = 5.5*L+80
				        else:
				            Result = 6*L+55
			    elif SN > 'WORTHTABK':
				    if SN < 'WORTHVALBU':
					    if SN < 'WORTHVALAP':
						    if SN < 'WORTHVALA':
							    if SN < 'WORTHTABS':
								    if SN < 'WORTHTABO':
									    if SN < 'WORTHTABM':
										    if SN == 'WORTHTABL':
										        Result = CalcStat("WorthTabB",L)+19.25
									    elif SN > 'WORTHTABM':
										    if SN == 'WORTHTABN':
										        Result = CalcStat("WorthTabAF",L)+25
									    else:
									        if Lm <= 9:
									            Result = 10*L+11
									        elif Lm <= 49:
									            Result = 4*L+65
									        else:
									            Result = 5*L+15
								    elif SN > 'WORTHTABO':
									    if SN < 'WORTHTABQ':
										    if SN == 'WORTHTABP':
										        Result = CalcStat("WorthTabE",L)
									    elif SN > 'WORTHTABQ':
										    if SN == 'WORTHTABR':
										        if Lm <= 9:
										            Result = 12*L+30
										        else:
										            Result = 7*L+75
									    else:
									        Result = 7*L+25
								    else:
								        Result = CalcStat("WorthTabB",L)+11
							    elif SN > 'WORTHTABS':
								    if SN < 'WORTHTABW':
									    if SN < 'WORTHTABU':
										    if SN == 'WORTHTABT':
										        if Lm <= 1:
										            Result = 54
										        elif Lm <= 17:
										            Result = 10.73*L+43.57
										        elif Lm <= 35:
										            Result = 10.735*L+43.265
										        elif Lm <= 36:
										            Result = 429
										        elif Lm <= 42:
										            Result = 10.65*L+46.45
										        elif Lm <= 49:
										            Result = 10.7*L+44.6
										        else:
										            Result = 9*L+130
									    elif SN > 'WORTHTABU':
										    if SN == 'WORTHTABV':
										        Result = CalcStat("WorthTabB",L)-2.75
									    else:
									        if Lm <= 10:
									            Result = 9*L+20
									        elif Lm <= 49:
									            Result = 5.5*L+55
									        else:
									            Result = 6*L+30
								    elif SN > 'WORTHTABW':
									    if SN < 'WORTHTABY':
										    if SN == 'WORTHTABX':
										        Result = CalcStat("WorthTabAF",L)+75
									    elif SN > 'WORTHTABY':
										    if SN == 'WORTHTABZ':
										        Result = CalcStat("WorthTabR",L)-15
									    else:
									        Result = CalcStat("WorthTabD",L)+30
								    else:
								        Result = CalcStat("WorthTabD",L)+25
							    else:
							        Result = CalcStat("WorthTabD",L)+17.5
						    elif SN > 'WORTHVALA':
							    if SN < 'WORTHVALAH':
								    if SN < 'WORTHVALAD':
									    if SN < 'WORTHVALAB':
										    if SN == 'WORTHVALAA':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAA")))
									    elif SN > 'WORTHVALAB':
										    if SN == 'WORTHVALAC':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAC")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAB")))
								    elif SN > 'WORTHVALAD':
									    if SN < 'WORTHVALAF':
										    if SN == 'WORTHVALAE':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAE")))
									    elif SN > 'WORTHVALAF':
										    if SN == 'WORTHVALAG':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAG")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAF")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAD")))
							    elif SN > 'WORTHVALAH':
								    if SN < 'WORTHVALAL':
									    if SN < 'WORTHVALAJ':
										    if SN == 'WORTHVALAI':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabAI")))
									    elif SN > 'WORTHVALAJ':
										    if SN == 'WORTHVALAK':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabAK")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabAJ")))
								    elif SN > 'WORTHVALAL':
									    if SN < 'WORTHVALAN':
										    if SN == 'WORTHVALAM':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAM")))
									    elif SN > 'WORTHVALAN':
										    if SN == 'WORTHVALAO':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAO")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAN")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabAL")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabAH")))
						    else:
						        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabA")))
					    elif SN > 'WORTHVALAP':
						    if SN < 'WORTHVALBE':
							    if SN < 'WORTHVALAX':
								    if SN < 'WORTHVALAT':
									    if SN < 'WORTHVALAR':
										    if SN == 'WORTHVALAQ':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAQ")))
									    elif SN > 'WORTHVALAR':
										    if SN == 'WORTHVALAS':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAS")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAR")))
								    elif SN > 'WORTHVALAT':
									    if SN < 'WORTHVALAV':
										    if SN == 'WORTHVALAU':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAU")))
									    elif SN > 'WORTHVALAV':
										    if SN == 'WORTHVALAW':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAW")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAV")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAT")))
							    elif SN > 'WORTHVALAX':
								    if SN < 'WORTHVALBA':
									    if SN < 'WORTHVALAZ':
										    if SN == 'WORTHVALAY':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabAY")))
									    elif SN > 'WORTHVALAZ':
										    if SN == 'WORTHVALB':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabB")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabAZ")))
								    elif SN > 'WORTHVALBA':
									    if SN < 'WORTHVALBC':
										    if SN == 'WORTHVALBB':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBB")))
									    elif SN > 'WORTHVALBC':
										    if SN == 'WORTHVALBD':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBD")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBC")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBA")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAX")))
						    elif SN > 'WORTHVALBE':
							    if SN < 'WORTHVALBM':
								    if SN < 'WORTHVALBI':
									    if SN < 'WORTHVALBG':
										    if SN == 'WORTHVALBF':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBF")))
									    elif SN > 'WORTHVALBG':
										    if SN == 'WORTHVALBH':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBH")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBG")))
								    elif SN > 'WORTHVALBI':
									    if SN < 'WORTHVALBK':
										    if SN == 'WORTHVALBJ':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBJ")))
									    elif SN > 'WORTHVALBK':
										    if SN == 'WORTHVALBL':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBL")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBK")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBI")))
							    elif SN > 'WORTHVALBM':
								    if SN < 'WORTHVALBQ':
									    if SN < 'WORTHVALBO':
										    if SN == 'WORTHVALBN':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBN")))
									    elif SN > 'WORTHVALBO':
										    if SN == 'WORTHVALBP':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBP")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpG",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBO")))
								    elif SN > 'WORTHVALBQ':
									    if SN < 'WORTHVALBS':
										    if SN == 'WORTHVALBR':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBR")))
									    elif SN > 'WORTHVALBS':
										    if SN == 'WORTHVALBT':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBT")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBS")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBQ")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBM")))
						    else:
						        Result = RoundDbl(EquSng(CalcStat("WorthMpJ",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBE")))
					    else:
					        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabAP")))
				    elif SN > 'WORTHVALBU':
					    if SN < 'WORTHVALJ':
						    if SN < 'WORTHVALCJ':
							    if SN < 'WORTHVALCB':
								    if SN < 'WORTHVALBY':
									    if SN < 'WORTHVALBW':
										    if SN == 'WORTHVALBV':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpD",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBV")))
									    elif SN > 'WORTHVALBW':
										    if SN == 'WORTHVALBX':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBX")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBW")))
								    elif SN > 'WORTHVALBY':
									    if SN < 'WORTHVALC':
										    if SN == 'WORTHVALBZ':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBZ")))
									    elif SN > 'WORTHVALC':
										    if SN == 'WORTHVALCA':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCA")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabC")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabBY")))
							    elif SN > 'WORTHVALCB':
								    if SN < 'WORTHVALCF':
									    if SN < 'WORTHVALCD':
										    if SN == 'WORTHVALCC':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabCC")))
									    elif SN > 'WORTHVALCD':
										    if SN == 'WORTHVALCE':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpH",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCE")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabCD")))
								    elif SN > 'WORTHVALCF':
									    if SN < 'WORTHVALCH':
										    if SN == 'WORTHVALCG':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCG")))
									    elif SN > 'WORTHVALCH':
										    if SN == 'WORTHVALCI':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCI")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCH")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabCF")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCB")))
						    elif SN > 'WORTHVALCJ':
							    if SN < 'WORTHVALCR':
								    if SN < 'WORTHVALCN':
									    if SN < 'WORTHVALCL':
										    if SN == 'WORTHVALCK':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCK")))
									    elif SN > 'WORTHVALCL':
										    if SN == 'WORTHVALCM':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCM")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCL")))
								    elif SN > 'WORTHVALCN':
									    if SN < 'WORTHVALCP':
										    if SN == 'WORTHVALCO':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCO")))
									    elif SN > 'WORTHVALCP':
										    if SN == 'WORTHVALCQ':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpK",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCQ")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCP")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpI",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCN")))
							    elif SN > 'WORTHVALCR':
								    if SN < 'WORTHVALF':
									    if SN < 'WORTHVALD':
										    if SN == 'WORTHVALCS':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpE",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCS")))
									    elif SN > 'WORTHVALD':
										    if SN == 'WORTHVALE':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabE")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabD")))
								    elif SN > 'WORTHVALF':
									    if SN < 'WORTHVALH':
										    if SN == 'WORTHVALG':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabG")))
									    elif SN > 'WORTHVALH':
										    if SN == 'WORTHVALI':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabI")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabH")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabF")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCR")))
						    else:
						        Result = RoundDbl(EquSng(CalcStat("WorthMpC",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabCJ")))
					    elif SN > 'WORTHVALJ':
						    if SN < 'WORTHVALZ':
							    if SN < 'WORTHVALR':
								    if SN < 'WORTHVALN':
									    if SN < 'WORTHVALL':
										    if SN == 'WORTHVALK':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabK")))
									    elif SN > 'WORTHVALL':
										    if SN == 'WORTHVALM':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabM")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabL")))
								    elif SN > 'WORTHVALN':
									    if SN < 'WORTHVALP':
										    if SN == 'WORTHVALO':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabO")))
									    elif SN > 'WORTHVALP':
										    if SN == 'WORTHVALQ':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabQ")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabP")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabN")))
							    elif SN > 'WORTHVALR':
								    if SN < 'WORTHVALV':
									    if SN < 'WORTHVALT':
										    if SN == 'WORTHVALS':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabS")))
									    elif SN > 'WORTHVALT':
										    if SN == 'WORTHVALU':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabU")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt8Lin",L,"WorthTabT")))
								    elif SN > 'WORTHVALV':
									    if SN < 'WORTHVALX':
										    if SN == 'WORTHVALW':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabW")))
									    elif SN > 'WORTHVALX':
										    if SN == 'WORTHVALY':
										        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabY")))
									    else:
									        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabX")))
								    else:
								        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabV")))
							    else:
							        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabR")))
						    elif SN > 'WORTHVALZ':
							    if SN < 'WRDCRITDEF':
								    if SN < 'WPNDMGMIN':
									    if SN < 'WOUNDRESISTT':
										    if SN == 'WOUNDRESIST':
										        Result = CalcStat("ResistAdd",L,N)
									    elif SN > 'WOUNDRESISTT':
										    if SN == 'WPNDMGMAX':
										        Result = EquSng((2/(2-CalcStat("WpnDPSVarianceType",WpnCodeIndex(C,2))))*CalcStat("CombatBaseWpnDPS",L,C))
									    else:
									        Result = CalcStat("ResistAddT",L,N)
								    elif SN > 'WPNDMGMIN':
									    if SN < 'WPNDPSVARIANCETYPE':
										    if SN == 'WPNDPS':
										        Result = CalcStat("CombatBaseWpnDPS",L,C)
									    elif SN > 'WPNDPSVARIANCETYPE':
										    if SN == 'WRDBATSTRIKESCRITDEF':
										        Result = -CalcStat("CritDefT",L,CalcStat("Trait123Choice",N)*0.4)
									    else:
									        if 1 <= Lp and Lm <= 3:
									            Result = EquSng(DataTableValue((0.25,0.25,0.25),L))
								    else:
								        Result = EquSng(((2-2*CalcStat("WpnDPSVarianceType",WpnCodeIndex(C,2)))/(2-CalcStat("WpnDPSVarianceType",WpnCodeIndex(C,2))))*CalcStat("CombatBaseWpnDPS",L,C))
							    elif SN > 'WRDCRITDEF':
								    if SN < 'WRDRECKLESSNCRITHIT':
									    if SN < 'WRDIMPRBLADESPARRY':
										    if SN == 'WRDFINESSE':
										        Result = CalcStat("FinesseT",L,CalcStat("Trait12345Choice",N)*0.4)
									    elif SN > 'WRDIMPRBLADESPARRY':
										    if SN == 'WRDPHYMAS':
										        Result = CalcStat("PhyMasT",L,CalcStat("Trait123455Choice",N)*0.4)
									    else:
									        Result = CalcStat("ParryT",L,2.8)
								    elif SN > 'WRDRECKLESSNCRITHIT':
									    if SN < 'WRDSHIELDTACTCRITDEF':
										    if SN == 'WRDSHIELDMASBLOCK':
										        Result = CalcStat("BlockT",L,2.8)
									    elif SN > 'WRDSHIELDTACTCRITDEF':
										    if SN > 'WRDSTDYOURGRBLOCK':
											    if SN == 'WRDSTDYOURGRPARRY':
											        Result = CalcStat("ParryT",L,CalcStat("Trait1234Choice",N)*0.4)
										    elif SN == 'WRDSTDYOURGRBLOCK':
										        Result = CalcStat("BlockT",L,CalcStat("Trait1234Choice",N)*0.4)
									    else:
									        Result = CalcStat("CritDefT",L,2)
								    else:
								        Result = CalcStat("CritHitT",L,2.4)
							    else:
							        Result = CalcStat("CritDefT",L,1.0)
						    else:
						        Result = RoundDbl(EquSng(CalcStat("WorthMpB",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabZ")))
					    else:
					        Result = RoundDbl(EquSng(CalcStat("WorthMpA",QualityCodeIndex(C))*CalcStat("WorthExt",L,"WorthTabJ")))
				    else:
				        Result = RoundDbl(EquSng(CalcStat("WorthMpF",QualityCodeIndex(C))*CalcStat("WorthExt4Lin",L,"WorthTabBU")))
			    else:
			        if Lm <= 9:
			            Result = 12*L+24
			        else:
			            Result = 7*L+74
		    else:
		        Result = 1.5
	    else:
	        Result = CalcStat("MitHeavyPRatPCapR",L)
    else:
        Result = 1

    return Result

# Support defs for CalcStat. These consist of implementations of more complex calculation types, decode methods for parameter "C" and rounding/min/max/compare defs for floating point numbers.

# ****************** Calculation Type support defs ******************

# DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
# DataTableValue: Takes a value from an array table.

def DataTableValue(vDataArray, dIndex):

    iIndex = RoundDbl(dIndex)
    return vDataArray[0] if iIndex <= 1 else vDataArray[len(vDataArray)-1] if iIndex >= len(vDataArray) else vDataArray[iIndex-1]

# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# ExpFmod: Exponential function based on percentage.
# Common percentage values are around ~5.5% for between levels and ~20% jumps between level segments.

def ExpFmod(dVal, dLstart, dPlvl, dLvl, vDec = None, vAdd = 0):

    dRng = dLvl - dLstart + 1
    if dRng <= DblCalcDev:
        return dVal
    else:
        dFac = 1 + dPlvl / 100
        dAdd = vAdd if type(vAdd) in (float, int) else 0
        if vDec is None:
            dFacExp = pow(dFac, dRng)
            return dVal * dFacExp + dAdd * ((dFacExp - 1) / (dFac - 1))
        else:
            dResult = dVal
            dLm = dLstart - DblCalcDev
            while dLm <= dLvl:
                dResult = RoundDbl(dResult * dFac + dAdd, vDec)
                dLm += 1
            return dResult

# PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
# CalcPercAB: Calculates the percentage out of a rating based on the AB formula.

def CalcPercAB(dA, dB, dPCap, dR):

    if dR <= DblCalcDev:
        return 0
    else:
        dResult = dA / (1 + dB / dR)
        return dPCap if dResult >= dPCap - DblCalcDev else dResult

# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# CalcRatAB: Calculates the rating out of a percentage based on the AB formula.

def CalcRatAB(dA, dB, dCapR, dP):

    if dP <= DblCalcDev:
        return 0
    else:
        dResult = dB / (dA / dP - 1)
        return dCapR if dResult >= dCapR - DblCalcDev else dResult

# SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
# StatLinInter: (Normalized) Stat Linear Interpolating

def StatLinInter(sPntMP, sProgScheme, sProgBase, sAdj, dLvl, vNorC, vRoundType):

    # parameter processing
    dN = 1
    sC = ''
    match vNorC:
        case str():
            sC = vNorC
        case float() | int():
            dN = vNorC

    iRoundType = 0
    if type(vRoundType) in (float, int):
        iRoundType = vRoundType
    
    dProgScheme = CalcStat(sProgScheme, dLvl)
    if type(dProgScheme) is not tuple:
        return 0

    # find level interval
    dLvlMinus = dLvl - DblCalcDev
    iPointIndexHigh = 1
    iPointIndexMax = len(dProgScheme[0]) - 1
    while iPointIndexHigh < iPointIndexMax:
        if dLvlMinus <= dProgScheme[0][iPointIndexHigh]:
            break
        iPointIndexHigh += 1

    iPointIndexLow = iPointIndexHigh - 1

    dAccessLvlLow = dProgScheme[0][iPointIndexLow]
    dAccessLvlHigh = dProgScheme[0][iPointIndexHigh]
    dBaseLvlLow = dProgScheme[1][iPointIndexLow]
    dBaseLvlHigh = dProgScheme[1][iPointIndexHigh]

    # get values from base progression
    dValLow = CalcStat(sProgBase, dBaseLvlLow, sC)
    dValHigh = CalcStat(sProgBase, dBaseLvlHigh, sC)

    # graph point multiplications
    if type(sPntMP) is str and not (sPntMP == '' or sPntMP.isspace()):
        dValLow *= CalcStat(sPntMP, dAccessLvlLow, sC)
        dValHigh *= CalcStat(sPntMP, dAccessLvlHigh, sC)
    if type(sAdj) is str and not (sAdj == '' or sAdj.isspace()):
        dValLow *= CalcStat(sAdj, dAccessLvlLow, sC)
        dValHigh *= CalcStat(sAdj, dAccessLvlHigh, sC)
    dValLow *= dN
    dValHigh *= dN

    # graph point roundings
    match iRoundType:
        case 0:
            dValLow = RoundDblLotro(dValLow)
            dValHigh = RoundDblLotro(dValHigh)
        case 1:
            dValLow = RoundDblUp(dValLow, 2 if -100 <= dValLow and dValLow <= 100 else 1) if -1000 <= dValLow and dValLow <= 1000 else RoundDblLotro(dValLow)
            dValHigh = RoundDblUp(dValHigh, 2 if -100 <= dValHigh and dValHigh <= 100 else 1) if -1000 <= dValHigh and dValHigh <= 1000 else RoundDblLotro(dValHigh)
        case 2:
            dValLow = RoundDblLotro(dValLow)
            dValLow = -2 if dValLow == -1 else dValLow
            dValHigh = RoundDblLotro(dValHigh)
            dValHigh = -2 if dValHigh == -1 else dValHigh
        case 3:
            dValLow = RoundDblProg(dValLow)
            dValHigh = RoundDblProg(dValHigh)
        case 4:
            dValLow = RoundDbl(dValLow, 0)
            dValHigh = RoundDbl(dValHigh, 0)

    # return interpolated value from the calculated graph points
    return LinFmod(1, dValLow, dValHigh, dAccessLvlLow, dAccessLvlHigh, dLvl)

# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# LinFmod: Linear line function between 2 points with some optional modifications.
# Connects point (dLstart,dVal*dFstart) with (dLend,dVal*dFend).
# Usually used with dVal=1 and dFstart/dFend containing unrelated points or dVal=# and dFstart/dFend containing multiplier factors.
# Modification for in-between points on the line: rounding.

def LinFmod(dVal, dFstart, dFend, dLstart, dLend, dLvl, vDec = None):

    if type(vDec) == str:
        sRoundType = vDec.strip().upper()
        match sRoundType:
            case 'P':
                return LinFmod(1, RoundDblProg(dVal * dFstart), RoundDblProg(dVal * dFend), dLstart, dLend, dLvl)
            case 'L':
                return LinFmod(1, RoundDblLotro(dVal * dFstart), RoundDblLotro(dVal * dFend), dLstart, dLend, dLvl)
            case _:
                return LinFmod(1, dVal * dFstart, dVal * dFend, dLstart, dLend, dLvl)

    if dLstart - DblCalcDev <= dLvl and dLvl <= dLstart + DblCalcDev:
        return dVal * dFstart
    elif dLend - DblCalcDev <= dLvl and dLvl <= dLend + DblCalcDev:
        return dVal * dFend
    elif dLstart == dLend:
        return 0
    elif vDec is None:
        return dVal * (dFstart * (dLend - dLvl) + (dLvl - dLstart) * dFend) / (dLend - dLstart)
    else:
        return RoundDbl(dVal * (dFstart * (dLend - dLvl) + (dLvl - dLstart) * dFend) / (dLend - dLstart), vDec)

# ****************** Parameter "C" decode support functions ******************

# ArmCodeIndex: returns a specified index from an Armour Code.
# sACode string:
# 1st position: H=heavy, M=medium, L=light
# 2nd position: H=head, S=shoulders, CL=cloak/back, C=chest, G=gloves, L=leggings, B=boots, Sh=shield
# 3rd position: W=white/common, Y=yellow/uncommon, P=purple/rare, T=teal/blue/incomparable, G=gold/legendary/epic
# Note: no such thing exists as a heavy, medium or light cloak, so no H/M/L in cloak codes (cloaks go automatically in the M class since U23, although historically this was L)

def ArmCodeIndex(sACode, iI):

    sArmCode = sACode.strip().upper()

    # get positional codes and make some corrections
    sArmCat = sArmCode[0]
    sArmType = sArmCode[1]
    sArmCol = sArmCode[2]
    if sArmType == 'S' and sArmCol == 'H':
        sArmType = 'SH'
        sArmCol = sArmCode[3]
    elif sArmCat == 'C' and sArmType == 'L':
        sArmCat = 'M'
        sArmType = 'CL'
    else:
        sArmType = ' ' + sArmType

    match iI:
        case 1:
            return 'HML'.find(sArmCat) + 1
        case 2:
            return ' H SCL C G L BSH'.find(sArmType) // 2 + 1
        case 3:
            return 'WYPTG'.find(sArmCol) + 1
        case _:
            return 0

# QualityCodeIndex: returns a quality index from a Quality Code.
# sQCode string: W=white/common, Y=yellow/uncommon, P=purple/rare, T=teal/blue/incomparable, G=gold/legendary/epic

def QualityCodeIndex(sQCode):

    return 'WYPTG'.find(sQCode.strip()[0].upper()) + 1

# WpnCodeIndex: returns a specified index from a Weapon Code.
# sWCode string:
# 1st position: H=heavy, L=light
# 2nd position: O=one-handed, T=two-handed, B=bow
# 3rd position: W=white/common, Y=yellow/uncommon, P=purple/rare, T=teal/blue/incomparable, G=gold/legendary/epic

def WpnCodeIndex(sWCode, iI):

    sWpnCode = sWCode.strip().upper()
    sWpnCat = sWpnCode[0]
    sWpnType = sWpnCode[1]
    sWpnCol = sWpnCode[2]

    match iI:
        case 1:
            return 'HL'.find(sWpnCat) + 1
        case 2:
            return 'OTB'.find(sWpnType) + 1
        case 3:
            return 'WYPTG'.find(sWpnCol) + 1
        case _:
            return 0

# RomanRankDecode: converts a string with a Roman number in characters, to an integer number.
# used for Legendary Item Title calculation.

RomanCharsToValues = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

def RomanRankDecode(sNumber):

    if sNumber != '':
        for sRomanRankChar, iRomanRankValue in RomanCharsToValues.items():
            if sNumber[:len(sRomanRankChar)].upper() == sRomanRankChar:
                return iRomanRankValue + RomanRankDecode(sNumber[len(sRomanRankChar):])

    return 0

# ****************** Misc. floating point support functions ******************

# Misc. functions for floating point: rounding etc.
# For roundings: vDec is number of decimals.

def CorrectDbl(dNum, dCorrection, dDec):
    lSign = -1 if dNum < 0 else 1
    if -DblCalcDev <= dDec and dDec <= DblCalcDev:
        return lSign * int(lSign * dNum + dCorrection)
    else:
        if dDec >= 0:
            dFactor = pow(10, int(dDec + DblCalcDev))
            return (lSign * int(lSign * (dNum * dFactor) + dCorrection)) / dFactor
        else:
            dFactor = pow(10, int(-dDec + DblCalcDev))
            return (lSign * int(lSign * (dNum / dFactor) + dCorrection)) * dFactor

def RoundDbl(dNum, vDec = 0):
    return CorrectDbl(dNum, 0.5 + DblCalcDev, vDec)

def RoundDblDown(dNum, vDec = 0):
    return CorrectDbl(dNum, DblCalcDev, vDec)

def RoundDblUp(dNum, vDec = 0):
    return CorrectDbl(dNum, 1 - DblCalcDev, vDec)

def RoundDblLotro(dNum):
    dCorrection = 1 - DblCalcDev
    lSign = -1 if dNum < 0 else 1

    iNumCeiled = int(lSign * dNum + dCorrection)
    if iNumCeiled <= 1000:
        return lSign * iNumCeiled

    iFactor = 1
    iTestNum = iNumCeiled // 1000
    while iTestNum > 0:
        iTestNum //= 10
        iFactor *= 10

    return lSign * int((iNumCeiled / iFactor) + dCorrection) * iFactor

def RoundDblProg(dNum):
    if -DblCalcDev <= dNum and dNum <= DblCalcDev:
        return 0

    dCorrection = 0.5 + DblCalcDev
    lSign = -1 if dNum < 0 else 1

    dTestNum = dNum / (0.5 * (lSign * 63))
    lDec = -math.floor(math.log10(dTestNum))

    if lDec == 0:
        return lSign * int(lSign * dNum + dCorrection)
    else:
        if lDec > 0:
            dFactor = pow(10, int(lDec + DblCalcDev))
            return (lSign * int(lSign * (dNum * dFactor) + dCorrection)) / dFactor
        else:
            dFactor = pow(10, int(-lDec + DblCalcDev))
            return (lSign * int(lSign * (dNum / dFactor) + dCorrection)) * dFactor

# converts a double value into the equivalent of a single float value
def EquSng(vVal):
    return struct.unpack('>f', struct.pack('>f', vVal))[0]

# converts a double value into the decimal representation of an equivalent single float value
def DecSng(vVal):
    dVal = EquSng(vVal)
    if dVal == 0.0:
        # return 0 when 0
        return 0.0
    # calculate decimals interval for a max total of 8 digit precision
    # 0.09#######: 9 to 2
    # 0.9#######: 8 to 1
    # 9.#######: 7 to 0
    # 9#.######: 6 to -1
    # 9##.#####: 5 to -2 etc
    iDecMin = 8 - (int(math.log10(math.fabs(dVal))) + 1)
    iDecMax = iDecMin - 7
    # result always needs to be rounded at least once, even if the result is not the same as the original equiv. float value
    dResult = CorrectDbl(dVal, 0.5, iDecMin)
    # search for the least number of decimals, while still keeping the same single value
    iDec = iDecMin - 1
    while iDec >= iDecMax:
        dTest = CorrectDbl(dVal, 0.5, iDec) # test value with ever less precision
        if dTest != dResult:
            if EquSng(dTest) == dVal:
                dResult = dTest
            else:
                # (test)value contains no longer the same single value
                break
        iDec = iDec - 1
    return dResult

