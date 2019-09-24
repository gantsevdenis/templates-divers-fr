#!/bin/env python3.7
output_filename = "/home/denis/Desktop/contrat_location"
######################################
bailleur = ""
bailleur_addresse = ""
addresse_locataire = ""
locataire = ""
date_naissance_locataire = ""
addresse_immeuble = ""
surface_logement = ""
nb_pieces_logement = ""
debut_bail = ""
fin_bail = ""
loyer_mensuel = ""
charges_mensuelles = ""
loyer_et_charges = ""
indice_reference_loyers = ""
montant_garantie = ""
date_dpe = ""
societe_dpe = ""
departement_prefecture = ""
######################################
contrat_txt = f"""
Entre les soussignés:
1. {bailleur},désigné le bailleur, demeurant à {bailleur_addresse}. En cas de changement de propriétaire, le nouveau bailleur s'engage à notifier au locataire
de son nom ou de sa dénomination sociale, son domicile ou siège social et le cas échéant ceux de 
son mandataire.
ET
2.  {locataire}, né le {date_naissance_locataire}, démeurant à {addresse_locataire}, désigné(s) locataire.

Il a été convenu ce qui suit.
Le bailleur loue, aux clauses et conditions ci-dessous énoncées aux locataires qui accept(ent)
conjointement et solidairement entre eux les lieux ci-après désignés.


DESIGNATION DES LIEUX

Les biens et droits immobiliers ci-après dépendent d'un Batiment sis à 
{addresse_immeuble}
Ce logement d'une surface habitable de {surface_logement} comprend notament {nb_pieces_logement}

Designation des locaux et équipements privatifs:
L'appartement est composé de cuisine/séjour, une chambre, douche et lavabo avec wc. Hall d'entrée commun.
Lo locataire déclare avoir visité les lieux et constaté que les éléments ci-dessus désignés existent.


Article 1. Destination des lieux
L'immeuble soumis à la location devra etre loué à titre de résidence principale, et etre
occupé au moins 8 mois par an. Il doit répondre aux condition d'occupation suffisantes telles que
définies dans l'article 621-2 du Code de la Construction et de l'Habitation. En conséquence,
le locataire ne pourra y exercer, meme dans une partie, une activité commerciale, artisanale,
professionnelle ou industrielle.

Article 2. Durée et prise d'effet
Le présent bail prend effet à compter du {debut_bail} et s'achève le  {fin_bail}.
Il sera reconduit tacitement, par des périodes de 3 ans.

Article 3. Loyer
Le loyer est de {loyer_mensuel} par mois, sans charges.
Les charges sont de {charges_mensuelles} et comprennent eau, électricité et chauffage
Le total de {loyer_et_charges} est payable le 5 de chaque mois par virement au bailleur, 
à compter du {debut_bail}.
En cas de non paiement de toutes sommes dues, le preneur devra payer après une mise en demeur
au bailleur. les intérets de retard au taux légal. Si le recouvremen de la créance devra nécessiter
l'inteervention d'un huissier de justcce, les frais de recouvrement, y compris la totalité
des droits proportionnels du à l'huissier de justice, seraient à la charge du locataire.
ainsi qu'une indemnité forfaitaire fixée à 10% du montant de la somme due, destinée à dédommager
le bailleur tant du préjudice pouvant résulter du retard dans le paiement que des
désagréments causés par les démarches et dilligences nécessaires pour parvenir au recouvrement
de la créance. Le bailleur se réserve le droit de réclamer des dommages et intérets supplémentaires
s'il était contraint de saisir le tribunal pour faire valoir ses droits.

Article 4. Revision de loyer
Le bailleur a le droit de réviser le montant de loyer sans notification, si la location perdure
au delà d'un an, en fonction de la variation de l'indice national de référence des loyers publié
par l'INSEE. Dans le cas ou l'indexation devient inapplicatble, les parties conviendraient  d'une
nouvelle indexation, sans laquelle le contrat n'aurait plus d'existence.

Les indices de référence seront: le dernier indice publié avant la signature du contrat, et l'indice
correspondant à la date de révision

L'indice de base est l'indice de: INDICE DE REFERENCE DES LOYERS selon l'INSEE.
Dernier cours connu est {indice_reference_loyers} en date de {debut_bail}.

Article 5. Congé donné par le locataire
Le présent bail pourra etre résilié par les locataires ou par l'un d'entre eux à tout moment,
en respectant un délai de préavis de 3 mois. 
Toutefois, dans les cas:
- D'obtention d'un premier emploi, CDD ou CDI
- De mutation professionnnelle, la date de mutation doit etre proche de la date de délivrance du congé
- De perte d'emploi: licenciement, fin de CDD ou rupture conventionnelle
- De nouvel emploi consécutif à une perte d'emploi - la perte d'emploi et le nouvel emploi doivent
intervenir au cours du meme bail
- Si le locataire est allocataire du RSA, ou l'allocation adule handicapé
- Si la raison de santé du locataire justifie un changement de domicile
- Attribution d'un logement social à un locataire vivant dans le parc privé
Le préavis est alors réduit à 1 mois.

Article 6. Charges et prestations récupérables
Les charges récupérables, sommes accéssoires au loyer principal, sont éxigibles en contrepartie:
- Des services rendus à l'usage des différents élements de la chose louée
- Des dépenses d'entretien courant et des menues réparations sur les éléments dusage commun de la chose
louée
- Des impositions en principal et accessoires, présentes et à venir, qui correspondent à des
services dont le locataire profite directement

Les charges locatives peuvent donner lieu au versement de provisions et doivent, en ce cas, faire
l'objet d'une régularisation au moins annuelle. Les demandes de provisions sont justifiées par la 
communication de résultats antérieurs arrétés lors de la précédente régularisation.
Un mois avant cette régularisation, le bailleur en communique au locataire le décompte par nature
des charges, ainsi que le mode de répartition entre les locataires. Durant un mois à compter
de l'envoi de ce décompte, les pièces justificatices sont tenues à la disposition des locataires.

La provision sur charges est de {charges_mensuelles} (basée sur 1 personne occupant les lieux)
mensuels et selon justificatif, peut subir une régularisation, à la baisse, ou à la hausse.

Article 7. Depot de garantie
A la signature du présent bail, le locataire a versé au bailleur, qui le reconnait,
la somme de {montant_garantie} affectée à  garantir la bonne éxecution de ses obligations
locatives. Cette somme est restituée sans intérets au locataire en fin du bail

Article 8. Diagnostic de performance energetique (DPE)
Conformément au Code de la Construction et de l'Habitation, DPE est annexé au
contrat de la location lors de sa signature.
Il a été étable le {date_dpe} par la société {societe_dpe}, dont un exemplaire sera annexé
au présent contrat. Le DPE porte une valeur informative.

Article 9. Etat des Risques naturelles et technologiques
Si le logement es situé dans une zone couverte par un plan de prévention des risques
technologiques, naturels prévisibles ou sismiques, un état des risques natuels et technologiques,
dans le cadre de l'information des locataire de biens immobiliers, conformément à l'arrété préfectoral
de la préfécture {departement_prefecture} listant les communes et les zones concernées, doit
alors etre annexé au présent contrat.
En l'occurence, le bien loué est situé à {addresse_immeuble}:
- Non listée par l'arrété préfectoral sus mentionné
- N'a pas fait l'objet d'une indemnisation au titre d'une catastrophe naturelle ou technologique

Article 10. Constat de risque d'exposition au plomb
Si le logement est situé dans un immeuble construit avant 1er janvier 1949, alors un constat
d'exposition au plomb devra etre fourni par le bailleur.
Il doit avoir moins de 6 ans si le contrat est positif. S'il établit l'absence de risque d'exposition
au plomb, alors sa durée n'est pas limitée dans le temps.

Article 11. Detection de fumée
L'Habitation doit etre equiée d'au moins un détecteur de fumée, fourni par le bailleur. Il appartient
au locataire de veiller à son bon fonctionnement.

Article 13. Etat des lieux et travaux
1. Le bailleur délivrera le logement décent et en bon état d'usage et de réparations et les 
équipements mentionnés au bail en bon état de fonctionnement. Toutefois, les parties peuvent 
convenir d'une clause expresse de travaux que le locataire éxecutera o fera éxecuter et des modalités
d'imputation sur le loyer. La clause prévoir la durée de cette imputation, et en ca de départ
anticipé du locataire, les modlités de son dédommagement sur justification de dépenses effectuées.
Cette clause ne concerne que des logements correspondant aux critères de décence.
2. Un état des lieux, établi contradictoirement par les parties, ou à défaut par l'huissier à
l'initiative de la partie la plus diligente et aux frais partagés par moitié, et joint au bail.
3. Le locataire prend à sa charge l'entretien courant du logement, des équipements fournis.
4. Le locataire subira tous travaux d'entretien ou d'amélioration dans les lieux louées et dans
es autres parties de l'immeuble.
Il laissera le bailleur ou son mandataire visiter les lieux loués chaque fois qu'il sera
nécessaire pour l'entretien, les réparation ou la sécurité de l'immeuble.
Il avisera le bailleur, sans délai, de toutes les dégradations constatées dans les lieux loués
et justifiant de réparations à la charge du bailleur. A defaut, il ne pourra réclamer aucune 
indemnité pour le préjudice résultant pour lui de la prolongation du dommage au dela de la date
ou il en avisé le bailleur.
5. Le locataire ne transformera pas les locaux, jardins et équipements loués sans accors écrit
du bailleur.

Article 14. Joussance des lieux
- Le locataire usera paisiblement des lieux loués et répondra pour les dégradations qui surviennent
pendant la durée du contrat
- Le locataire tiendra pendant la durée du bail les lieux constamment garnis de meuble et objets
mobiliers en quantité suffisante pour garantir le paiement des loyers et charges
- Le locataire utilisera les lieux loués uniquement pour habitation principale
- Le locataire assurera contre l'incendie, les dégats des eux, et les risques éectriques, le recours
des voisins, les explosions de toute nature et pour l'animal familier dont il peut etre responsable
et plus généralement contre tous les risques dont il doit répondre en sa qualité de locataire
Il en justifiera à son entée dans les lieux puis chaque année à la demande du bailleur par la remise à 
celui ci d'une attestation de son assureur.
- Le locataire ne commetra aucun abus de jouissance susceptible de nuire à la solidité ou à la bonne
tenue de l'immeuble soit d'engager la responsabilité du bailleur envers les autress occupants
de l'immeuble ou envers le voisinage
En particulier, il ne pourra déposer aucun objet sur les appuis de fenetres, balcons, et ouvertures
quelconques, et ni étendre aucun linge ou tapis
Il devra éviter tout bruit de nature à géner les voisins
- Le locataire assurera la protection contre le gel de toutes les canalisations et appareils à
compteurs réservés à son usage personnel dans les lieux. Il sera tenu pour responsable des dégats
qui surviendrait du fait de sa négligence
- En cas de mise en vente de l'immeuble ou de logement, le locataire laussera visiter les locaux
tous les jours ouvrables pendant deux heures par jour
Il devra également les memes jours et heures, de laisser visiter les lieux en cas de cessation du bail,
pendant trois mois qui précéderont son échéance.
- Toute cession ou sous location du présent bail, total ou partielle, sont interdites
- La détention de chiens de 1 catégie est interdite, ainsi que tout animal non considéré comme
animal de compagnie. Le locataire reste responsable de toute dégradtion portée au logement par 
l'animal

Article 15. Solidarité et indivisibilité
Pour l'execution de toutes les obligations résultant du présent contrat, il y ura
solidarité et indivisibilité entre les parties désignées sous le nom de locataire,
entre les héritiers ou représentants du locataire venant à décéder.

Article 16. 
A defaut de paiement,de tout ou partie du loyer, du dépot de garantie, le présent bail sera résilié
Cette résiliation produira effet un  mois après le commandement demeuré infructueux en cas de defaut
d'assurance et deux mois après en cas de défaut de paiement
A peine de nullité, le commandement reproduit en cas de non paiement les dispositions des quatres
premiers alinéas de l'article 24 modifié de la loi du 6 juillet 1989 et l'article 6 de la loi
du 31 mai 1990, et en cas de de defaut d'assurance les deux alinéas de l'article 7g) de la première
loi précitée
Enfin, conformément à la loi du 5 mars 2007, le bail sera résulité de plein droit pour non respect
de l'obligation d'user paisiblement des locaux loués, en cas de troubles de voisinage constatés par 
une décision judiciaire définitive

Article 17 Election de domicile
Pour l'execution du présent bail, les parties font élection de domicile
- Le bailleur, et son domicile {bailleur_addresse}
- Le locataire dans les locaux présentement loués
"""

with open(output_filename, "w") as f:
    f.write(contrat_txt.format(**locals()))