import argparse

from bs4 import BeautifulSoup


def checkIfEmptyAndFill(mustcheck, tagname):
    if mustcheck.strip():
        tagname.string = mustcheck


def newIntSec(appendThere, otherProc, otherProcDate):
    tempSec = """<interventiSecondari>
        <interventiSecondari></interventiSecondari>
        <interventiSecondariEsterni></interventiSecondariEsterni>
        <dataInterventoSecondario></dataInterventoSecondario>
        <oraInizioInterventoSecondario></oraInizioInterventoSecondario>
        <chirurgoInterventoSecondario></chirurgoInterventoSecondario>
        <anestesistaInterventoSecondario></anestesistaInterventoSecondario>
        <ckListSalaOperatoriaInterventoSecondario></ckListSalaOperatoriaInterventoSecondario>
        <Lateralita></Lateralita>
    </interventiSecondari>"""

    if otherProcDate.strip():
        mustAppend = BeautifulSoup(tempSec, "xml")
        mustAppend.find_all("interventiSecondari")[1].string = otherProc
        mustAppend.dataInterventoSecondario.string = otherProcDate
        appendThere.append(mustAppend.interventiSecondari)
    else:
        mustAppend = BeautifulSoup(tempSec, "xml")
        mustAppend.find_all("interventiSecondari")[1].string = otherProc
        appendThere.append(mustAppend.interventiSecondari)


def main(template, tracks, output_file, limit=None):
    toappend1 = "<rilevazioneDolore></rilevazioneDolore>"
    toappend2 = "<pressioneArteriosaSistolica></pressioneArteriosaSistolica>"
    toappend3 = "<creatininaSerica></creatininaSerica>"
    toappend4 = "<frazioneEiezione></frazioneEiezione>"

    empty = " "

    with open(template, "r") as file, open(tracks, "r") as file1, \
            open(output_file, "w") as file2:

        xmlDoc = file.read()

        template = '<bInformazioniRicovero  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

        soup1 = BeautifulSoup(template, 'xml')

        for index, line in enumerate(file1):
            if index == limit:
                break

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

            soup.informazioniRicovero.dataRicovero.string = recDate
            soup.informazioniRicovero.unitaOperativaAmmissione.string = repNum
            soup.informazioniRicovero.onereDegenza.string = degOn
            soup.informazioniRicovero.provenienzaPaziente.string = patFrom
            checkIfEmptyAndFill(recType, soup.informazioniRicovero.tipoRicovero)
            checkIfEmptyAndFill(traOrInt, soup.informazioniRicovero.traumatismiIntossicazioni)

            moveDate = soup.informazioniRicovero.find_all("dataTrasferimento")
            moveUnit = soup.informazioniRicovero.find_all("unitaTrasferimento")
            moveMin = soup.informazioniRicovero.find_all("oraTrasferimento")

            checkIfEmptyAndFill(repTransfDate1, moveDate[0])
            checkIfEmptyAndFill(repTransf1, moveUnit[0])
            checkIfEmptyAndFill(repTransfDate2, moveDate[1])
            checkIfEmptyAndFill(repTransf2, moveUnit[1])
            checkIfEmptyAndFill(repTransfDate3, moveDate[2])
            checkIfEmptyAndFill(repTransf3, moveUnit[2])

            soup.informazioniRicovero.unitaOperativaDimissione.string = repDim
            soup.informazioniRicovero.dataDimissioneMorte.string = dimDate
            soup.informazioniRicovero.modalitaDimissione.string = dimMod

            checkIfEmptyAndFill(autRisc, soup.informazioniRicovero.riscontroAutoptico)
            checkIfEmptyAndFill(recDueDo, soup.informazioniRicovero.motivoRicoveroRegimeDiurno)
            checkIfEmptyAndFill(numDH, soup.informazioniRicovero.numGiornateRicoveroDiurno)
            checkIfEmptyAndFill(birthWeight, soup.informazioniRicovero.pesoNascita)

            soup.informazioniRicovero.diagnosiPrincipaleDimissione.string = princDiag

            checkIfEmptyAndFill(secDiag1, soup.diagnosiSecondarieDimissione)
            checkIfEmptyAndFill(princSurgOrBirth, soup.informazioniRicovero.interventoPrincipale.interventoPrincipale)
            checkIfEmptyAndFill(princSurgOrBirthDate, soup.dataInterventoPrincipale)

            procedures = [otherProc1, otherProcDate1, otherProc2, otherProcDate2, otherProc3, otherProcDate3,
                          otherProc4, empty, otherProc5, empty, otherProc6, empty]

            for i in [0, 2, 4, 6, 8, 10]:
                if str(procedures[i]) != "    ":
                    newIntSec(soup.informazioniRicovero, procedures[i], procedures[i + 1])

            # for j in range(2, -1, -1):
            #     if soup.informazioniRicovero.find_all("Trasferimenti")[j].contents == ['\n', '\n', '\n', '\n']:
            #         soup.informazioniRicovero.find_all("Trasferimenti")[j].decompose()

            soup.informazioniRicovero.append(BeautifulSoup(toappend1, "xml").rilevazioneDolore)
            soup.informazioniRicovero.append(BeautifulSoup(toappend2, "xml").pressioneArteriosaSistolica)
            soup.informazioniRicovero.append(BeautifulSoup(toappend3, "xml").creatininaSerica)
            soup.informazioniRicovero.append(BeautifulSoup(toappend4, "xml").frazioneEiezione)

            soup1.bInformazioniRicovero.append(soup.informazioniRicovero)

        file2.write(str(soup1.prettify()))

        print("All done, check %s to see the file converted" % args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", help="choose an xml file to use as template")
    parser.add_argument("--tracks", help="choose a file containing the tracks in txt format you want to convert in xml")
    parser.add_argument("--output", help="choose a file where to save the xml containing the data from the tracks",
                        default="output.xml")
    parser.add_argument("--limit", help="the number of line to process. If not specified it will process all",
                        required=False, type=int)
    args = parser.parse_args()

    main(args.template, args.tracks, args.output, args.limit)
