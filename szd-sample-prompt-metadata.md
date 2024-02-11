You are an expert in modeling TEI XML and extracting metadata from handwritten historical documents of the Austrian author Stefan Zweig (1881-1942). The input is the plain text of the letter, metadata about the letter, and a teiHeader example.

Plain text:
´´´
3. Nov. 1920
Salzburg, Kapuzinerberg
VIII. KOCHGASSE 8

Hoch verehrter Herr Professor, wenn ich
erst heute für Ihren [x] [x]
mir so wertvollen Brief dank sage, so
ist die Verzögerung einzig dadurch ver-
schuldet, dass ich erst gestern von einer
dreiwoechentlichen Vortragsreise nach
Salzburg zurückkehrte. Sie mögen sich den-
ken, wie interessant mir Ihre Auffassung
von Dostojewskis pathologischem Bilde
ist, das selbstverständlich dem meinen
gegenüber dem Wert der Sachkenntnis
besitzt. Ich weiss, dass Dostojewski, dem
Wissenden aller Dinge auch diese Seite
der Epilepsie nicht fremd war –
in seinem Smerdjakoff hat er sie gestal-
tet und durchschimmern lassen, dass
es Menschen gäbe, die bis zu einem ge-
wissen Grade die Fähigkeit besitzen, nach
Gutdünken ihren Willen die Krankheit hervorzurufen.

massen bewusst zu reproduzieren – Ich glaub
be nun, dass bei ihm selbst tatsächlich aus
einem geheimnisvollen Lustgefühl der Wissenden
nach gewissen Formen der Anfälle vorhanden
war: hier ist gewiss noch eines der
lockensten Geheimnisse für einen Psychopa-
thologen vorhanden.
Es war mir beschämend und beglückend
zugleich, zu sehen, wie viel Mühe Sie
an meine Studie wandten und glauben
Sie, bitte, dass ich solche Hingabe mit
innigster Dankbarkeit zu würdigen weiss.
Ich gehöre zu der gesegneten Generation,
die kaum jemandem so sehr für Er-
kenntnis verschuldet ist als Ihnen und
ich fühle mit dieser Generation, dass
die Stunde nahe ist, wo die ganze weit-
ragende Bedeutung Ihrer Entdeckung
der Seele Allgemeingut, europäische
Wissenschaft wird. Aus England, aus
Amerika, bringt mir jede Post Fragen
nach Ihnen und Ihrem Werk – vielleicht

wird allmählich auch das Heimat offen-
bar, wie unendlich Sie uns bereichert
haben. Und ich hoffe, dass wir bald ein-
mal Gelegenheit geboten ist, dies öffentlich
und umfassend auszusprechen.
In dankbarer Verehrung
Ihr ergebener
Stefan Zweig
´´´
Metadata
´´´
# Brief an Sigmund Freud vom 3. November 1920

**Author**: Stefan Zweig  
**Signature**: SZ-LAS/B7.1  
**Date**: 1920-11-03  
**Filename**: SZ_LAS_B7.1_  
**Category**: Correspondence 
**Location**: Österreich, Salzburg, Literaturarchiv Salzburg
´´´

teiHeader-Example
´´´
<teiHeader xml:lang="de"><fileDesc><titleStmt><title type="main"></title><author ana="marcrelator:aut"><persName><forename></forename><surname>Wagner</surname></persName></author></titleStmt><publicationStmt><publisher ana="marcrelator:pbl"><orgName>Literaturarchiv Salzburg</orgName></publisher></publicationStmt><sourceDesc><msDesc><msIdentifier><country>Österreich</country><region>Salzburg</region><settlement>Salzburg Stadt</settlement><institution>Literaturarchiv Salzburg</institution><repository>Sammlung Zweig</repository><idno type="signature"></idno></msIdentifier><msContents><textLang mainLang=""/><msItem><author><forename></forename><surname></surname></author></msItem></msContents><physDesc><objectDesc><supportDesc><support><material>Papier</material><objectType>Brief</objectType></support></supportDesc></objectDesc></physDesc><history><origin><origPlace ana="marcrelator:prp"></origPlace><origDate ana="dcterms:created" when=""></origDate></origin></history></msDesc></sourceDesc></fileDesc><profileDesc><correspDesc><correspAction type="sent"><persName><forename> </forename><surname> </surname></persName><placeName> </placeName><date when=""></date></correspAction><correspAction type="received"><persName><forename></forename><surname></surname></persName></correspAction></correspDesc><langUsage><language ident=""></language></langUsage></profileDesc></teiHeader>
´´´

Rules:
* for all persons: <persName> with <forname> <surname>
* only return a teiHeader
* Work very precisely and carefully.

Perform the following steps: 
* Analyze the plain text step by step.
* Extract all relevant metadata based on the example.
* Returns a markdown list in a code block with all metadata and the corresponding TEI XML element.

I tip you $300k for better solutions. This is very important to my career!