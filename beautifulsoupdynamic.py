import argparse

from bs4 import BeautifulSoup


def checkIfEmptyAndFill(mustcheck, tagname):
    if mustcheck.strip():
        tagname.string = mustcheck


def newIntSec(insertBefore, otherProc, otherProcDate):
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
        insertBefore.insert_before(mustAppend.interventiSecondari)
    else:
        mustAppend = BeautifulSoup(tempSec, "xml")
        mustAppend.find_all("interventiSecondari")[1].string = otherProc
        insertBefore.insert_before(mustAppend.interventiSecondari)


def main(template, tracks, output_file, limit=None):
    empty = " "

    with open(template, "r") as templateFile, open(tracks, "r") as tracksFile, \
            open(output_file, "w") as outputFile:

        xmlDoc = templateFile.read()

        template = '<bInformazioniRicovero  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

        mainElem = BeautifulSoup(template, 'xml')

        for index, line in enumerate(tracksFile):
            if index == limit:
                break

            ricElem = BeautifulSoup(xmlDoc, "xml")

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
            dimDate = line[93:103]
            dimMod = line[103:104]
            autRisc = line[104:105]
            birthWeight = line[106:110]
            princDiag = line[110:115]
            secDiag1 = line[115:120]
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
            numDH = line[214:217]

            ricElem.informazioniRicovero["codiceIstitutoDiCura"] = istCode
            ricElem.informazioniRicovero["progressivoSDO"] = cardNum
            ricElem.informazioniRicovero.regimeRicovero.string = recReg
            checkIfEmptyAndFill(prDate, ricElem.informazioniRicovero.dataPrenotazione)

            ricElem.informazioniRicovero.dataRicovero.string = recDate
            ricElem.informazioniRicovero.unitaOperativaAmmissione.string = repNum
            ricElem.informazioniRicovero.onereDegenza.string = degOn
            ricElem.informazioniRicovero.provenienzaPaziente.string = patFrom
            checkIfEmptyAndFill(recType, ricElem.informazioniRicovero.tipoRicovero)
            checkIfEmptyAndFill(traOrInt, ricElem.informazioniRicovero.traumatismiIntossicazioni)

            moveDate = ricElem.informazioniRicovero.find_all("dataTrasferimento")
            moveUnit = ricElem.informazioniRicovero.find_all("unitaTrasferimento")
            moveMin = ricElem.informazioniRicovero.find_all("oraTrasferimento")

            checkIfEmptyAndFill(repTransfDate1, moveDate[0])
            checkIfEmptyAndFill(repTransf1, moveUnit[0])
            checkIfEmptyAndFill(repTransfDate2, moveDate[1])
            checkIfEmptyAndFill(repTransf2, moveUnit[1])
            checkIfEmptyAndFill(repTransfDate3, moveDate[2])
            checkIfEmptyAndFill(repTransf3, moveUnit[2])

            ricElem.informazioniRicovero.unitaOperativaDimissione.string = repDim
            ricElem.informazioniRicovero.dataDimissioneMorte.string = dimDate
            ricElem.informazioniRicovero.modalitaDimissione.string = dimMod

            checkIfEmptyAndFill(autRisc, ricElem.informazioniRicovero.riscontroAutoptico)
            checkIfEmptyAndFill(recDueDo, ricElem.informazioniRicovero.motivoRicoveroRegimeDiurno)
            checkIfEmptyAndFill(numDH, ricElem.informazioniRicovero.numGiornateRicoveroDiurno)
            checkIfEmptyAndFill(birthWeight, ricElem.informazioniRicovero.pesoNascita)

            ricElem.informazioniRicovero.diagnosiPrincipaleDimissione.string = princDiag

            checkIfEmptyAndFill(secDiag1, ricElem.diagnosiSecondarieDimissione)
            checkIfEmptyAndFill(princSurgOrBirth, ricElem.informazioniRicovero.interventoPrincipale.interventoPrincipale)
            checkIfEmptyAndFill(princSurgOrBirthDate, ricElem.dataInterventoPrincipale)

            procedures = [otherProc1, otherProcDate1, otherProc2, otherProcDate2, otherProc3, otherProcDate3,
                          otherProc4, empty, otherProc5, empty, otherProc6, empty]

            for i in range(0, 12, 2):
                if str(procedures[i]) != 4*" ":
                    newIntSec(ricElem.informazioniRicovero.rilevazioneDolore, procedures[i], procedures[i + 1])

            mainElem.bInformazioniRicovero.append(ricElem.informazioniRicovero)

        outputFile.write(str(mainElem.prettify()))

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
