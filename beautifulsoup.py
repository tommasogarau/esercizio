from bs4 import BeautifulSoup

template = """<interventiSecondari>
            <interventiSecondari></interventiSecondari>
            <interventiSecondariEsterni></interventiSecondariEsterni>
            <dataInterventoSecondario></dataInterventoSecondario>
            <oraInizioInterventoSecondario></oraInizioInterventoSecondario>
            <chirurgoInterventoSecondario></chirurgoInterventoSecondario>
            <anestesistaInterventoSecondario></anestesistaInterventoSecondario>
            <ckListSalaOperatoriaInterventoSecondario></ckListSalaOperatoriaInterventoSecondario>
            <Lateralita></Lateralita>
        </interventiSecondari>"""

with open("/home/tommaso/Scrivania/elitubo/esercizio/bs.xml", "r") as file, \
        open("/home/tommaso/Scrivania/elitubo/esercizio/904306A2.txt", "r") as file1, \
        open("/home/tommaso/Scrivania/elitubo/esercizio/output.xml", "w") as file2 :

    xmlDoc = file.read()

    template = '<bInformazioniRicovero  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

    soup1 = BeautifulSoup(template, 'xml')
    # newtag = soup1.new_tag("bInformazioniRicovero", xmlns="http://www.w3.org/2001/XMLSchema-instance")
    # soup1.append(newtag)
    # newtag.string = " "

    for index, line in enumerate(file1):

        soup = BeautifulSoup(xmlDoc, "xml")

        istCode = line[0:8]
        cardNum = line[8:16]
        repNum = line[16:20]
        recReg = line[20:21]
        recDate = line[21:31]
        degOn = line[31:32]
        patFrom = line[32:33]
        recType = line[33:34]
        prDate = line[34:44]
        recDueDo = line[44:45]
        traOrInt = line[45:46]
        repTransf1 = line[46:50]
        repTransfDate1 = line[50:60]
        repTransf2 = line[60:64]
        repTransfDate2 = line[64:74]
        repTransf3 = line[74:78]
        repTransfDate3 = line[78:88]
        repDim = line[88:92]
        funDimArea = line[92:93]
        dimDate = line[93:103]
        dimMod = line[103:104]
        autRisc = line[104:105]
        expl = line[105:106]
        birthWeight = line[106:110]
        princDiag = line[110:115]
        secDiag1 = line[115:120]
        secDiag2 = line[120:125]
        secDiag3 = line[125:130]
        secDiag4 = line[130:135]
        secDiag5 = line[135:140]
        secDiag6 = line[140:145]
        princSurgOrBirth = line[145:149]
        princSurgOrBirthDate = line[149:159]
        otherProc1 = line[159:163]
        otherProcDate1 = line[163:173]
        otherProc2 = line[173:177]
        otherProcDate2 = line[177:187]
        otherProc3 = line[187:191]
        otherProcDate3 = line[191:201]
        otherProc4 = line[201:205]
        otherProc5 = line[205:209]
        otherProc6 = line[209:213]
        dayRecDue = line[213:214]
        numDH = line[214:217]
        licenseDays = line[217:219]
        drgCode = line[219:222]
        degCost = line[222:231]
        degCostAA = line[231:240]
        contPos = line[240:241]
        err1 = line[241:242]
        err2 = line[242:243]
        err3 = line[243:244]
        err4 = line[244:245]
        err5 = line[245:246]
        err6 = line[246:247]
        err7 = line[247:248]
        err8 = line[248:249]
        err9 = line[249:250]
        err10 = line[250:251]
        idCode = line[251:271]
        regionOfFirstAdd = line[271:273]

        soup.informazioniRicovero["codiceIstitutoDiCura"] = istCode
        soup.informazioniRicovero["progressivoSDO"] = cardNum
        soup.tipoTrasmissione.string = " "
        soup.regimeRicovero.string = recReg
        soup.dataPrenotazione.string = prDate
        soup.classePriorita.string = " "
        soup.dataRicovero.string = recDate
        soup.oraRicovero.string = " "
        soup.unitaOperativaAmmissione.string = repNum
        soup.onereDegenza.string = degOn
        soup.provenienzaPaziente.string = patFrom
        soup.tipoRicovero.string = recType
        soup.traumatismiIntossicazioni.string = traOrInt
        soup.codiceCausaEsterna.string = " "
        soup.find_all("dataTrasferimento")[0].string = repTransfDate1
        soup.find_all("unitaTrasferimento")[0].string = repTransf1
        soup.find_all("oraTrasferimento")[0].string = " "
        soup.find_all("dataTrasferimento")[1].string = repTransfDate2
        soup.find_all("unitaTrasferimento")[1].string = repTransf2
        soup.find_all("oraTrasferimento")[1].string = " "
        soup.find_all("dataTrasferimento")[2].string = repTransfDate3
        soup.find_all("unitaTrasferimento")[2].string = repTransf3
        soup.find_all("oraTrasferimento")[2].string = " "
        soup.unitaOperativaDimissione.string = repDim
        soup.dataDimissioneMorte.string = dimDate
        soup.oraDimissioneMorte.string = " "
        soup.modalitaDimissione.string = dimMod
        soup.riscontroAutoptico.string = autRisc
        soup.motivoRicoveroRegimeDiurno.string = recDueDo
        soup.numGiornateRicoveroDiurno.string = numDH
        soup.pesoNascita.string = birthWeight
        soup.diagnosiPrincipaleDimissione.string = princDiag
        soup.diagnosiPrincipaleDimissioneAlRicovero.string = " "
        soup.find_all("Lateralita")[0].string = " "
        soup.find_all("stadiazioneCondensata")[0].string = " "
        soup.diagnosiSecondarieDimissione.string = secDiag1
        soup.diagnosiSecondarieDimissioneAlRicovero.string = " "
        soup.find_all("Lateralita")[1].string = " "
        soup.find_all("stadiazioneCondensata")[1].string = " "
        soup.find_all("interventoPrincipale")[1].string = princSurgOrBirth
        soup.interventoPrincipaleEsterno.string = " "
        soup.dataInterventoPrincipale.string = princSurgOrBirthDate
        soup.oraInterventoPrincipale.string = " "
        soup.chirurgoInterventoPrincipale.string = " "
        soup.anestesistaInterventoPrincipale.string = " "
        soup.ckListSalaOperatoriaInterventoPrincipale.string = " "
        soup.find_all("Lateralita")[2].string = " "

        intSec = soup.find_all("interventiSecondari")
        intSecDate = soup.find_all("dataInterventoSecondario")
        intSecExt = soup.find_all("interventiSecondariEsterni")
        intSecHour = soup.find_all("oraInizioInterventoSecondario")
        intSecSurge = soup.find_all("chirurgoInterventoSecondario")
        intSecA = soup.find_all("anestesistaInterventoSecondario")
        intSecCheck = soup.find_all("ckListSalaOperatoriaInterventoSecondario")
        intSecLat = soup.find_all("Lateralita")
        
        intSec[0].contents[1].string = otherProc1  # interventiSecondari = intSec
        intSecDate[0].string = otherProcDate1
        intSecExt[0].string = " "
        intSecHour[0] = " "
        intSecSurge[0].string = " "
        intSecA[0].string = " "
        intSecCheck[0].string = " "
        intSecLat[3].string = " "

        intSec[3].contents[1].string = otherProc2
        intSecDate[1].string = otherProcDate2
        intSecExt[1].string = " "
        intSecHour[1].string = " "
        intSecSurge[1].string = " "
        intSecA[1].string = " "
        intSecCheck[1].string = " "
        intSecLat[4].string = " "

        intSec[5].contents[1].string = otherProc3
        intSecDate[2].string = otherProcDate3
        intSecExt[2].string = " "
        intSecHour[2].string = " "
        intSecSurge[2].string = " "
        intSecA[2].string = " "
        intSecCheck[2].string = " "
        intSecLat[5].string = " "

        intSec[7].contents[1].string = otherProc4
        intSecDate[3].string = " "
        intSecExt[3].string = " "
        intSecHour[3].string = " "
        intSecSurge[3].string = " "
        intSecA[3].string = " "
        intSecCheck[3].string = " "
        intSecLat[6].string = " "

        intSec[9].contents[1].string = otherProc5
        intSecDate[4].string = " "
        intSecExt[4].string = " "
        intSecHour[4].string = " "
        intSecSurge[4].string = " "
        intSecA[4].string = " "
        intSecCheck[4].string = " "
        intSecLat[7].string = " "

        intSec[11].contents[1].string = otherProc6
        intSecDate[5].string = " "
        intSecExt[5].string = " "
        intSecHour[5].string = " "
        intSecSurge[5].string = " "
        intSecA[5].string = " "
        intSecCheck[5].string = " "
        intSecLat[8].string = " "

        intSec[13].contents[1].string = " "
        intSecDate[6].string = " "
        intSecExt[6].string = " "
        intSecHour[6].string = " "
        intSecSurge[6].string = " "
        intSecA[6].string = " "
        intSecCheck[6].string = " "
        intSecLat[9].string = " "

        intSec[15].contents[1].string = " "
        intSecDate[7].string = " "
        intSecExt[7].string = " "
        intSecHour[7].string = " "
        intSecSurge[7].string = " "
        intSecA[7].string = " "
        intSecCheck[7].string = " "
        intSecLat[10].string = " "

        intSec[17].contents[1].string = " "
        intSecDate[8].string = " "
        intSecExt[8].string = " "
        intSecHour[8].string = " "
        intSecSurge[8].string = " "
        intSecA[8].string = " "
        intSecCheck[8].string = " "
        intSecLat[11].string = " "

        intSec[18].string = " "
        intSecDate[9].string = " "
        intSecExt[9].string = " "
        intSecHour[9].string = " "
        intSecSurge[9].string = " "
        intSecA[9].string = " "
        intSecCheck[9].string = " "
        intSecLat[12].string = " "

        soup.rilevazioneDolore.string = " "
        soup.pressioneArteriosaSistolica.string = " "
        soup.creatininaSerica.string = " "
        soup.frazioneEiezione.string = " "

        soup1.bInformazioniRicovero.append(soup.informazioniRicovero)

    file2.write(str(soup1.prettify()))

    print(soup1.prettify())



