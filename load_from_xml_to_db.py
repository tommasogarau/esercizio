import MySQLdb
import argparse
from bs4 import BeautifulSoup

def main():

    parser=argparse.ArgumentParser()
    parser.add_argument("--username", help="type the username used to access the database", default="root")
    parser.add_argument("--password", help="type your password", default="tommaso")
    parser.add_argument("--name", help="type the database name", default="tracks")
    parser.add_argument("--filename", help="choose the file you want to load to the database", default="output.xml")
    args = parser.parse_args()


    db = MySQLdb.connect("localhost", args.username ,
                         args.password , args.name)

    cursor = db.cursor()

    null = "NULL"

    def checkIfEmptyandInsert(mustcheck):
        if mustcheck.string != None :
            return("{returnthis}".format(returnthis=mustcheck.string.strip()))
        else:
            return(null)

    def checkIfEmptyandInsertDate(mustcheck):
        if mustcheck.string != None :
            return('STR_TO_DATE("{returnthis}", "%d/%m/%Y")'.format(returnthis=mustcheck.string.strip()))
        else:
            return(null)


    with open(args.filename , "r") as source :

        xmlDoc = BeautifulSoup(source, "xml")


        for index, pat in enumerate(xmlDoc.find_all("informazioniRicovero")):

            sql = '''INSERT INTO InformazioniRicovero(progressivoSDO, 
            codiceIstitutoDiCura, 
            tipoTrasmissione, 
            regimeRicovero,
            dataPrenotazione, 
            classePriorita, 
            dataRicovero, 
            oraRicovero, 
            unitaOperativaAmmissione, 
            onereDegenza, 
            provenienzaPaziente,
            tipoRicovero, 
            traumatismiIntossicazioni, 
            codiceCausaEsterna, 
            riscontroAutoptico, 
            motivoRicoveroRegimeDiurno,
            numGiornateRicoveroDiurno, 
            pesoNascita, 
            rilevazioneDolore, 
            pressioneArteriosaSistolica, 
            creatininaSerica, 
            frazioneEiezione)
            
            VALUES ('{progr}', '{code}', {type}, '{reg}', {datepr}, {prclass}, {recdate}, {rectime},\
            {opunit}, {degon}, {patfrom}, {rectype}, {traorint}, {ext}, {autrisc}, {recduedo}, {numdh}, {birthweight},\
            {rilevazioneDolore}, {pressioneArteriosaSistolica}, {creatininaSerica}, {frazioneEiezione})'''.\
                format(progr=pat["progressivoSDO"],
                       code=pat["codiceIstitutoDiCura"],
                       type=checkIfEmptyandInsert(pat.tipoTrasmissione),
                       reg=checkIfEmptyandInsert(pat.regimeRicovero),
                       datepr=checkIfEmptyandInsertDate(pat.dataPrenotazione),
                       prclass=checkIfEmptyandInsert(pat.classePriorita),
                       recdate=checkIfEmptyandInsertDate(pat.dataRicovero),
                       rectime=checkIfEmptyandInsert(pat.oraRicovero),
                       opunit=checkIfEmptyandInsert(pat.unitaOperativaAmmissione),
                       degon=checkIfEmptyandInsert(pat.onereDegenza),
                       patfrom=checkIfEmptyandInsert(pat.provenienzaPaziente),
                       rectype=checkIfEmptyandInsert(pat.tipoRicovero),
                       traorint=checkIfEmptyandInsert(pat.traumatismiIntossicazioni),
                       ext=checkIfEmptyandInsert(pat.codiceCausaEsterna),
                       autrisc=checkIfEmptyandInsert(pat.riscontroAutoptico),
                       recduedo=checkIfEmptyandInsert(pat.motivoRicoveroRegimeDiurno),
                       numdh=checkIfEmptyandInsert(pat.numGiornateRicoveroDiurno),
                       birthweight=checkIfEmptyandInsert(pat.pesoNascita),
                       rilevazioneDolore=checkIfEmptyandInsert(pat.rilevazioneDolore),
                       pressioneArteriosaSistolica=checkIfEmptyandInsert(pat.pressioneArteriosaSistolica),
                       creatininaSerica=checkIfEmptyandInsert(pat.creatininaSerica),
                       frazioneEiezione=checkIfEmptyandInsert(pat.frazioneEiezione))

            cursor.execute(sql)

            for j in range(0,3):
                sql2 = """INSERT INTO Trasferimenti(dataTrasferimento, 
                oraTrasferimento, 
                unitaTrasferimento, 
                progressivoSDO) 
                VALUES ({reptransfdate}, {time}, {reptransf}, (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero))""".\
                    format(reptransfdate=checkIfEmptyandInsertDate(pat.find_all("Trasferimenti")[j].dataTrasferimento),
                           time=checkIfEmptyandInsert(pat.find_all("Trasferimenti")[j].oraTrasferimento),
                           reptransf=checkIfEmptyandInsert(pat.find_all("Trasferimenti")[j].unitaTrasferimento) )
                cursor.execute(sql2)

            sql3 = """INSERT INTO dimissione(unitaOperativaDimissione, 
            dataDimissioneMorte, 
            modalitaDimissione, 
            oraDimissioneMorte, 
            progressivoSDO) 
            VALUES ({dimunit}, {dimdate}, {dimmod}, {time}, (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero))""".\
                format(dimunit=checkIfEmptyandInsert(pat.find_all("dimissione")[0].unitaOperativaDimissione),
                       dimdate=checkIfEmptyandInsertDate(pat.find_all("dimissione")[0].dataDimissioneMorte),
                       dimmod=checkIfEmptyandInsert(pat.find_all("dimissione")[0].modalitaDimissione),
                       time=checkIfEmptyandInsert(pat.find_all("dimissione")[0].oraDimissioneMorte))
            cursor.execute(sql3)

            sql4 = """INSERT INTO diagnosiPrincipale(diagnosiPrincipaleDimissione, 
            diagnosiPrincipaleDimissioneAlRicovero, 
            Lateralita, 
            stadiazioneCondensata, 
            progressivoSDO) 
            VALUES ("{princdiag}", {princdiagrec}, {lat}, {stad}, (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero))""".\
                format(princdiag=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].diagnosiPrincipaleDimissione),
                       princdiagrec=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].diagnosiPrincipaleDimissioneAlRicovero),
                       lat=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].Lateralita),
                       stad=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].stadiazioneCondensata))
            cursor.execute(sql4)

            sql5 = """INSERT INTO diagnosiSecondarie(diagnosiSecondarieDimissione, 
            diagnosiSecondarieDimissioneAlRicovero, 
            Lateralita, 
            stadiazioneCondensata, 
            progressivoSDO) 
            VALUES ("{secdiag}", {secdiagrec}, {lat}, {stad}, (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero))""".\
                format(secdiag=checkIfEmptyandInsert(pat.find_all("diagnosiSecondarie")[0].diagnosiSecondarieDimissione),
                       secdiagrec=checkIfEmptyandInsert(pat.find_all("diagnosiSecondarie")[0].diagnosiSecondarieDimissioneAlRicovero),
                       lat=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].Lateralita),
                       stad=checkIfEmptyandInsert(pat.find_all("diagnosiPrincipale")[0].stadiazioneCondensata))
            cursor.execute(sql5)

            sql6 = """INSERT INTO interventoPrincipale(interventoPrincipale, 
            interventoPrincipaleEsterno, 
            dataInterventoPrincipale, 
            oraInterventoPrincipale, 
            chirurgoInterventoPrincipale, 
            anestesistaInterventoPrincipale, 
            ckListSalaOperatoriaInterventoPrincipale, 
            Lateralita, 
            progressivoSDO) 
            VALUES ({princsurg}, {extprincsurg}, {princsurgdate}, {time}, {surg}, {an}, {check}, {lat}, 
            (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero))""".\
                format(princsurg=checkIfEmptyandInsert(pat.interventoPrincipale.interventoPrincipale),
                       extprincsurg=checkIfEmptyandInsert(pat.interventoPrincipale.interventoPrincipaleEsterno),
                       princsurgdate=checkIfEmptyandInsertDate(pat.interventoPrincipale.dataInterventoPrincipale),
                       time=checkIfEmptyandInsert(pat.interventoPrincipale.oraInterventoPrincipale),
                       surg=checkIfEmptyandInsert(pat.interventoPrincipale.chirurgoInterventoPrincipale),
                       an=checkIfEmptyandInsert(pat.interventoPrincipale.anestesistaInterventoPrincipale),
                       check=checkIfEmptyandInsert(pat.interventoPrincipale.ckListSalaOperatoriaInterventoPrincipale),
                       lat=checkIfEmptyandInsert(pat.interventoPrincipale.Lateralita))
            cursor.execute(sql6)

            for k in range(0, len(pat.find_all("interventiSecondari", recursive=False))):
                sql7 = """INSERT INTO interventiSecondari(interventiSecondari, 
                interventiSecondariEsterni, 
                dataInterventoSecondario, 
                oraInizioInterventoSecondario, 
                chirurgoInterventoSecondario, 
                anestesistaInterventoSecondario, 
                ckListSalaOperatoriaInterventoSecondario, 
                Lateralita, 
                progressivoSDO) 
                VALUES ({intsec}, {extinsec}, {intsecdate}, {time} , {surg}, {an}, {check}, {lat}, 
                (SELECT  MAX(progressivoSDO) FROM InformazioniRicovero)) """.\
                    format(intsec=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].interventiSecondari),
                           extinsec=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].interventiSecondariEsterni),
                           intsecdate=checkIfEmptyandInsertDate(pat.find_all("interventiSecondari", recursive=False)[k].dataInterventoSecondario),
                           time=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].oraInizioInterventoSecondario),
                           surg=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].chirurgoInterventoSecondario),
                           an=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].anestesistaInterventoSecondario),
                           check=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].ckListSalaOperatoriaInterventoSecondario),
                           lat=checkIfEmptyandInsert(pat.find_all("interventiSecondari", recursive=False)[k].Lateralita))
                cursor.execute(sql7)

        db.commit()

        db.close()

        print("All done, the data has been loaded to the database")

if __name__ == "__main__":
    main()





