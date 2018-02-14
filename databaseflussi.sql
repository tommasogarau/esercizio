CREATE TABLE InformazioniRicovero (
  progressivoSDO     VARCHAR(8)  NOT NULL,
  codiceIstitutoDiCura        VARCHAR(8)  NOT NULL,
  tipoTrasmissione            INT(1),
  regimeRicovero              INT(1)      NOT NULL,
  dataPrenotazione            DATE        NULL,
  classePriorita              INT(1),
  dataRicovero                DATE,
  oraRicovero                 TIME        NULL,
  unitaOperativaAmmissione    VARCHAR(4)  NOT NULL,
  onereDegenza                INT(1)      NOT NULL,
  provenienzaPaziente         INT(2)      NOT NULL,
  tipoRicovero                INT(1),
  traumatismiIntossicazioni   INT(1),
  codiceCausaEsterna          VARCHAR(5),
  riscontroAutoptico          INT(1),
  motivoRicoveroRegimeDiurno  INT(1),
  numGiornateRicoveroDiurno   INT(1),
  pesoNascita                 INT(4),
  rilevazioneDolore           INT(1)      NULL,
  pressioneArteriosaSistolica FLOAT(4, 2) NULL,
  creatininaSerica            INT(2)      NULL,
  frazioneEiezione            INT(2)      NULL,
  PRIMARY KEY (progressivoSDO)
);


CREATE TABLE Trasferimenti (
  id                 INT(10) AUTO_INCREMENT NOT NULL,
  dataTrasferimento  DATE,
  oraTrasferimento   TIME                   NULL,
  unitaTrasferimento VARCHAR(4)             NULL,
  progressivoSDO     VARCHAR(8)             NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);


CREATE TABLE dimissione (
  id                       INT(10) AUTO_INCREMENT NOT NULL,
  unitaOperativaDimissione INT(12)                NOT NULL,
  dataDimissioneMorte      DATE                   NOT NULL,
  modalitaDimissione       INT(2)                 NOT NULL,
  oraDimissioneMorte       TIME,
  progressivoSDO           VARCHAR(8)             NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);


CREATE TABLE diagnosiPrincipale (
  id                                     INT(10) AUTO_INCREMENT NOT NULL,
  diagnosiPrincipaleDimissione           VARCHAR(10)            NOT NULL,
  diagnosiPrincipaleDimissioneAlRicovero INT(1)                 NULL,
  Lateralita                             INT(1)                 NULL,
  stadiazioneCondensata                  INT(1)                 NULL,
  progressivoSDO                         VARCHAR(8)             NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);


CREATE TABLE diagnosiSecondarie (
  id                                     INT(10) AUTO_INCREMENT NOT NULL,
  diagnosiSecondarieDimissione           VARCHAR(10)            NOT NULL,
  diagnosiSecondarieDimissioneAlRicovero INT(1)                 NULL,
  Lateralita                             INT(1)                 NULL,
  stadiazioneCondensata                  INT(1)                 NULL,
  progressivoSDO                         VARCHAR(8)             NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);


CREATE TABLE interventoPrincipale (
  id                                       INT(10) AUTO_INCREMENT NOT NULL,
  interventoPrincipale                     INT(9)                 NULL,
  interventoPrincipaleEsterno              INT(1)                 NULL,
  dataInterventoPrincipale                 DATE,
  oraInterventoPrincipale                  TIME                   NULL,
  chirurgoInterventoPrincipale             VARCHAR(88)            NULL,
  anestesistaInterventoPrincipale          VARCHAR(88)            NULL,
  ckListSalaOperatoriaInterventoPrincipale INT(1)                 NULL,
  Lateralita                               INT(1)                 NULL,
  progressivoSDO                           VARCHAR(8)             NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);

CREATE TABLE interventiSecondari (
  id                                       INT(10) AUTO_INCREMENT NOT NULL,
  interventiSecondari                      INT(3)                 NOT NULL,
  interventiSecondariEsterni               INT(1)                 NULL,
  dataInterventoSecondario                 DATE,
  oraInizioInterventoSecondario            TIME                   NULL,
  chirurgoInterventoSecondario             VARCHAR(88)            NULL,
  anestesistaInterventoSecondario          VARCHAR(88)            NULL,
  ckListSalaOperatoriaInterventoSecondario INT(1)                 NULL,
  Lateralita                               INT(1)                 NULL,
  progressivoSDO                           VARCHAR(8)             NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (progressivoSDO) REFERENCES InformazioniRicovero (progressivoSDO)
);
