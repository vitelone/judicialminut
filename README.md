## Judici al minut

### Introducció
judicialminut és un script en Python que s'actualitza cada 30 segons per mostrar a la consola la informació que Vilaweb publica a la seva pàgina de seguiment.

### Objectiu 
Així ens evitem refrescar manualment la pàgina web amb tots els anuncis i advertiments i scrolls, i veiem de forma discreta i d'una llambregada les novetats mentre continuem fent les nostres coses.

### Prerequisits
Cal tenir instal·lats Python, i les llibreries Requests (http://docs.python-requests.org/en/master/) i Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/)

### Ús
Un cop instal·lades totes les dependències, executar des de la línia de comandes, com ara `"C:\Python27\python.exe" judicialminut.py` en Windows i gaudiu!

### Advertiment
Em consta que des de la línia de comandes els caràcters no ASCII es veuen malament donat que el text que es recupera, com el món contempporani, en general, és en UTF-8. Pot canviar-se la codificació de Windows, però això pot tenir conseqüències no desitjades. El millor és passar-se a un sistema que funcioni bé, i si és lliure, millor que millor.

Per qualsevol comentari, @vitelone.
