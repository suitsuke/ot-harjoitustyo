# Changelog

## Viikko 3

- Käyttöliittymä aloitettu
- Menut (login, main menu, collection, settings, tarrojenhankintanapit) olemassa
- Tietokantoja aloitettu, tietokantojen ekat testaukset toimii
- Poetryn invoket toimii, lisätty tasks.py alkuun korjaus python 3.11 versiolle [tämän](https://github.com/pyinvoke/invoke/issues/833) ongelman vuoksi 
- Testattu toimivuus laitoksen koneella (virtuaalityöasema Cubbli Linux)

## Viikko 4
- Pylint otettu käyttöön
- Dokumentaatio: pakkausrakenne + rakenneluokka
- Käyttöliittymä pitää huolta millä käyttäjällä ollaan ja osaa kutsua services-oliota sillä tiedolla
- Stickerservice osaa hakea tiedon mitä kaikkia tarroja löytyy käyttäjältä listassa (toimii mutta jokin bugi tietokannan luomisen kanssa)
- todo: stickerservice osaa pyytää userstickers-repo laittamaan tarran jollekkin käyttäjälle
- Todo: koeajo cubblilla
- Todo: haarautumakattavuus >20% (coverage) 
- Todo: pylint

## Viikko 5
- todo: collection-ui: osaa näyttää kaikki löytyneet tarrat
