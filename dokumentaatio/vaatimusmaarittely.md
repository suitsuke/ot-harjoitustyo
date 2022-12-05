# Vaatimusmäärittely

## Sovelluksen tarkoitus

Yksinkertainen tehtäväseuranta. Sovelluksen avulla käyttäjä voi kerätä suorituskertoja erilaisista onnistuneista arjen askareista, kuten siististi syöminen, hampaiden pesu, pukeutuminen, nukkumaan meneminen. 
Jokaisesta suorituskerrasta saa satunnaisesti (tai puolisatunnaisesti) valitun tarran jota ei vielä ole aiemmin saanut tarrakirjaan.

Sovelluksen kohderyhmä on lapset niiden vanhempien avustuksella tai muut käyttäjät joilla on alentunut toimintakyky arjen askareissa.

## Käyttäjät

Sovellusta voi käyttää useampi käyttäjä kirjautumalla tai vaihtamalla käyttäjää, ja 
jokaisella käyttäjällä on eri historia ja tarrakokoelma.

## Käyttöliittymä

![image](kayttoliittyma.jpeg)

## Perusversion toiminnallisuus

### Ennen kirjautumista

- Käyttäjä valitsee tai luo käyttäjätunnuksen (tehty)
- Käyttäjiä 3 (tehty)
- Jos kirjautuminen epäonnistuu, ilmoitetaan siitä ja palataan käyttäjävalikkoon
- Graafinen selkeä sopiva kirjautumisnäkymä (tehty)

### Kirjautumisen jälkeen

- Käyttäjä voi valita askareen jota suoritetaan klikkaamalla
- Suorituksesta saa merkin kirjaan/kalenteriin, ja satunnaisesti valitun tarran joka lisätään tarrakirjaan (tehty)
- Käyttäjän keräämät tarrat (numeroitu) ja niiden tekstikuvaus tallennetaan tietokantaan. (tehty)
- Tarrat on omassa tietokannassa ja toinen tietokanta pitää huolen mikä käyttäjä (id) on kerännyt mitkäkin tarrat. (tehty)
- Käyttäjä voi avata tarrakirjan, josta näkee kaikki kerätyt tarrat (tehty)
- Käyttäjä voi avata kalenterin/login josta näkee eri suoritetut askareet päivämäärän ja ajan mukaan
- Asetuksista voi muuttaa käyttäjäpreferenssejä

## Jatkokehitysideoita

- Enemmän tarroja
- Kirjautumiseen voidaan asettaa salasana tai onnistunut haastava kertolasku
- Käyttäjiä enemmän (esim. 5)
- Tarrojen luokittelu eri askareiden mukaan niin että tietyntyyppiset askareet suosivat 
tietyn tyyppisiä tarroja
- Tarrojen vaihtaminen käyttäjien välillä
- Tilastojen luominen askareista
- Pisteiden kerääminen askareista ja "tarrakauppa"
- Mahdollisuus käyttäjälle määritellä erilaiset askareet perustoiminnallisuuksien ohella
- Mahdollisuus käyttäjälle itse valita mitkä askareet kuuluvat päävalikon nappuloihin 
