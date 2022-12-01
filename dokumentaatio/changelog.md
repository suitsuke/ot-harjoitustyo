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
- Stickerservice osaa hakea tiedon mitä kaikkia tarroja löytyy käyttäjältä listassa 
- stickerservice osaa pyytää userstickers-repo laittamaan tarran jollekkin käyttäjälle
- stickerservice osaa kysyä montako tarraa tietyllä käyttäjällä on
- koko ohjelmalla on nyt yksi service jolla on yksi repo
- haarautumakattavuus >20% (coverage) 
- pylint ajettu
- aloitettu collection-ui kuvien näyttämistä
- kuvien näyttämiseen tarvitaan PIL(low), joka asennettu poetryyn

## Viikko 5
- todo: collection-ui: osaa näyttää kaikki löytyneet tarrat tietyltä käyttäjältä
- todo: repo + services osaa poistaa tarroja
- todo: näiden automatisoitu testaus
- todo: menun napit lisäävät tarran oikealle käyttäjälle
- todo: random-testaaminen?
- todo: data/userstickers.db tyhjenee kun ohjelma suljetaan

- todo: github release
- todo: readmehen linkki releaseen
- todo: coverage >40%
- todo: pylint-virheitä <5
- todo: dokumentaatioon sekvenssikaavio
- todo: readme kuntoon

## Viikko 6
- todo: ehkä tarrahistorian katselmointi
- todo: ehkä käyttäjäasetuksia
