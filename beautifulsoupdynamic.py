from bs4 import BeautifulSoup

tempSec1 = """<interventiSecondari>
            <interventiSecondari></interventiSecondari>
            <dataInterventoSecondario></dataInterventoSecondario>
        </interventiSecondari>"""

tempSec2 = """<interventiSecondari>
            <interventiSecondari></interventiSecondari>
        </interventiSecondari>"""

def checkIfEmptyAndFill (mustcheck, tagname) :
    if mustcheck.strip() :
        tagname.string = mustcheck
    elif not mustcheck.strip() :
        tagname.decompose()


def checkIfEmptyTag (tagname) :
    for i in tagname.contents :
        if str(i) == "<Lateralita/>" or str(i) == "<stadiazioneCondensata/>" :
            tagname.decompose()
    if tagname.contents == ['\n', '\n', '\n', '\n', '\n'] or tagname.contents == ['\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n'] :
       tagname.decompose()

def newIntSec (appendThere, otherProc, otherProcDate) :
    if otherProcDate.strip():
        mustAppend = BeautifulSoup(tempSec1, "xml")
        mustAppend.find_all("interventiSecondari")[1].string = otherProc
        mustAppend.dataInterventoSecondario.string = otherProcDate
        appendThere.append(mustAppend.interventiSecondari)
    else :
        mustAppend = BeautifulSoup(tempSec2, "xml")
        mustAppend.find_all("interventiSecondari")[1].string = otherProc
        appendThere.append(mustAppend.interventiSecondari)

empty = " "

with open("bs.xml", "r") as file, \
        open("904306A2.txt", "r") as file1, \
        open("output.xml", "w") as file2 :

    xmlDoc = file.read()

    template = '<bInformazioniRicovero  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

    soup1 = BeautifulSoup(template, 'xml')

    for i, line in enumerate(file1):

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

        soup.informazioniRicovero.regimeRicovero.string = recReg

        checkIfEmptyAndFill(prDate, soup.informazioniRicovero.dataPrenotazione)

        soup.informazioniRicovero.classePriorita.decompose()

        soup.informazioniRicovero.dataRicovero.string = recDate

        soup.informazioniRicovero.oraRicovero.decompose()

        soup.informazioniRicovero.unitaOperativaAmmissione.string = repNum

        soup.informazioniRicovero.onereDegenza.string = degOn

        soup.informazioniRicovero.provenienzaPaziente.string = patFrom

        checkIfEmptyAndFill(recType, soup.informazioniRicovero.tipoRicovero)

        checkIfEmptyAndFill(traOrInt, soup.informazioniRicovero.traumatismiIntossicazioni)

        soup.informazioniRicovero.codiceCausaEsterna.decompose()

        moveDate = soup.informazioniRicovero.find_all("dataTrasferimento")
        moveUnit = soup.informazioniRicovero.find_all("unitaTrasferimento")
        moveMin = soup.informazioniRicovero.find_all("oraTrasferimento")

        checkIfEmptyAndFill(repTransfDate1, moveDate[0])

        checkIfEmptyAndFill(repTransf1, moveUnit[0])

        moveMin[0].decompose()

        checkIfEmptyAndFill(repTransfDate2, moveDate[1])

        checkIfEmptyAndFill(repTransf2, moveUnit[1])

        moveMin[1].decompose()

        checkIfEmptyAndFill(repTransfDate3, moveDate[2])

        checkIfEmptyAndFill(repTransf3, moveUnit[2])

        moveMin[2].decompose()

        soup.informazioniRicovero.unitaOperativaDimissione.string = repDim

        soup.informazioniRicovero.dataDimissioneMorte.string = dimDate

        soup.informazioniRicovero.oraDimissioneMorte.decompose()

        soup.informazioniRicovero.modalitaDimissione.string = dimMod

        checkIfEmptyAndFill(autRisc, soup.informazioniRicovero.riscontroAutoptico)

        checkIfEmptyAndFill(recDueDo, soup.informazioniRicovero.motivoRicoveroRegimeDiurno)

        checkIfEmptyAndFill(numDH, soup.informazioniRicovero.numGiornateRicoveroDiurno)

        checkIfEmptyAndFill(birthWeight, soup.informazioniRicovero.pesoNascita)

        soup.informazioniRicovero.diagnosiPrincipaleDimissione.string = princDiag

        array1 = soup.informazioniRicovero.find_all("Lateralita")
        for item in array1[::-1] :
            item.decompose()

        array2 = soup.informazioniRicovero.find_all("stadiazioneCondensata")
        for item in array2[::-1] :
            item.decompose()

        checkIfEmptyAndFill(secDiag1, soup.diagnosiSecondarieDimissione)

        soup.informazioniRicovero.diagnosiSecondarieDimissioneAlRicovero.decompose()

        checkIfEmptyTag(soup.informazioniRicovero.diagnosiSecondarie)

        checkIfEmptyAndFill(princSurgOrBirth, soup.informazioniRicovero.interventoPrincipale.interventoPrincipale)

        soup.informazioniRicovero.interventoPrincipaleEsterno.decompose()

        checkIfEmptyAndFill(princSurgOrBirthDate, soup.dataInterventoPrincipale)

        soup.informazioniRicovero.oraInterventoPrincipale.decompose()

        soup.informazioniRicovero.chirurgoInterventoPrincipale.decompose()

        soup.informazioniRicovero.anestesistaInterventoPrincipale.decompose()

        soup.informazioniRicovero.ckListSalaOperatoriaInterventoPrincipale.decompose()

        checkIfEmptyTag(soup.informazioniRicovero.interventoPrincipale)

        procedures = [otherProc1, otherProcDate1, otherProc2, otherProcDate2, otherProc3, otherProcDate3, otherProc4, empty, otherProc5, empty, otherProc6, empty]

        for i in [0, 2, 4, 6, 8, 10] :
            if str(procedures[i]) != "    " :
                newIntSec(soup.informazioniRicovero, procedures[i], procedures[i+1])


        for j in range(2, -1, -1):
            if soup.informazioniRicovero.find_all("Trasferimenti")[j].contents == ['\n', '\n', '\n', '\n'] :
                soup.informazioniRicovero.find_all("Trasferimenti")[j].decompose()

        soup1.bInformazioniRicovero.append(soup.informazioniRicovero)

    file2.write(str(soup1.prettify()))

    print(soup1.prettify())



