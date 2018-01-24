create table InformazioniRicovero (
progressivoSDO varchar(8) NOT NULL,
codiceIstitutoDiCura varchar(8) NOT NULL,
tipoTrasmissione int(1) NOT NULL,
regimeRicovero int(1) NOT NULL,
dataPrenotazione date NULL,
classePriorita varchar(1),
dataRicovero date,
oraRicovero time NULL,
unitaOperativaAmmissione varchar(4) NOT NULL,
onereDegenza int(1) NOT NULL,
provenienzaPaziente int(2) NOT NULL,
tipoRicovero int(1),
traumatismiIntossicazioni int(1),
codiceCausaEsterna varchar(5),
riscontroAutoptico int(1),
motivoRicoveroRegimeDiurno int(1),
numGiornateRicoveroDiurno int(1),
pesoNascita int(4),
rilevazioneDolore int(1) NULL,
pressioneArteriosaSistolica float(4, 2) NULL,
creatininaSerica int(2) NULL,
frazioneEiezione int(2) NULL,
PRIMARY KEY (progressivoSDO)
);

create table Trasferimenti (
id int(10) auto_increment NOT NULL,
dataTrasferimento date,
oraTrasferimento time NULL,
unitaTrasferimento varchar(4) NOT NULL,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);

create table dimissione (
id int(10) auto_increment NOT NULL,
unitaOperativaDimissione int(12) NOT NULL,
dataDimissioneMorte date NOT NULL,
modalitaDimissione int(2) NOT NULL,
oraDimissioneMorte time,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);


create table diagnosiPrincipale (
id int(10) auto_increment NOT NULL,
diagnosiPrincipaleDimissione varchar(4) NOT NULL,
diagnosiPrincipaleDimissioneAlRicovero int(1) NULL,
Lateralita int(1) NULL,
stadiazioneCondensata int(1) NULL,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);

create table diagnosiSecondarie (
id int(10) auto_increment NOT NULL,
diagnosiSecondarieDimissione varchar(3) NOT NULL,
diagnosiSecondarieDimissioneAlRicovero int(1) NULL,
Lateralita int(1) NULL,
stadiazioneCondensata int(1) NULL,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);

create table interventoPrincipale (
id int(10) auto_increment NOT NULL,
interventoPrincipale int(3) NOT NULL,
interventoPrincipaleEsterno int(1) NULL,
dataInterventoPrincipale date,
oraInterventoPrincipale time NULL,
chirurgoInterventoPrincipale varchar(88) NULL,
anestesistaInterventoPrincipale varchar(88) NULL,
ckListSalaOperatoriaInterventoPrincipale int(1) NULL,
Lateralita int(1) NULL,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);

create table interventiSecondari (
id int(10) auto_increment NOT NULL,
interventiSecondari int(3) NOT NULL,
interventiSecondariEsterni int(1) NULL,
dataInterventoSecondario date,
oraInizioInterventoSecondario time NULL,
chirurgoInterventoSecondario varchar(88) NULL,
anestesistaInterventoSecondario varchar(88) NULL,
ckListSalaOperatoriaInterventoSecondario int(1) NULL,
Lateralita int(1) NULL,
progressivoSDO varchar(8) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero(progressivoSDO)
);

