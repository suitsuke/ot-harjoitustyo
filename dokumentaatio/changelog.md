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
- repo + services osaa poistaa tarroja + automatisoitu testaus
- servicellä on metodit lisätä tietty tarra ja lisätä random-tarra
- todo: menun napit lisäävät tarran oikealle käyttäjälle (toiminee mutta tietokanta ei tallennu niin evt)
- collection-ui tietää minkä käyttäjän collectionia näytetään
- collection-ui osaa näyttää kaikki löytyneet tarrat tietyltä käyttäjältä
- data/userstickers.db tallentaa tiedot kun ohjelma suljetaan
- testaus toimii nyt ilman koodin muokkaamista välissä suoraan invoke-komennolla
- github release
- koodia siivottu, pylint-virheitä alle 5
- readme päivitetty
- readmehen linkki releaseen
- dokumentaatioon sekvenssikaavio (arkkitehtuuri-osastolla)
- testaus cubblilla

## Viikko 6
- korjattu niin, että toimii python-versiolla 3.8
- käyttäjäasetuksia
    - change_username toimii + testattu servicellä ja repolla
    - find_username toimii + testattu servicellä ja repolla
    - lisätty käyttäjäasetukset käyttöliittymään
- login ja menu osaa hakea oikeat tekstit nappeihin
- dokumentaatiota lisätty sekä koodiin että omille sivuille
- testaus cubblilla

## Viikko 7
- lisätty remove all stickers -button asetuksiin
- käyttöliittymää siistitty paljon
- jos tarraa ei omisteta, näkyy tyhjä ympyrä sen kohdalla
- korjattu käyttäjänimen ja action-painikkeen pituusrajoitus ja ilmoitukset
- testausdokumentti, käyttöohje kirjoitettu

- todo: collection screen: jos tarroja = 0: display label "no stickers yet"
- todo: arkkitehtuuri-sivulla uuden rakennekaavion piirto
- todo: python libraries used
- todo: testaus cubblilla
