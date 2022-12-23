# Ohjelmistotekniikka, harjoitustyö

## Stickers app

Sovelluksen avulla käyttäjä voi kerätä tarroja suoritetuista arkiaskareista. Käyttäjä voi itse asettaa itselleen nimen ja mitä kolmea askaretta hän haluaa suorittaa. Sovellusta voi käyttää muutama käyttäjä, ja kaikilla on oma tarrakokoelmansa.

Sovellus on kehitetty harjoitustyöksi Helsingin yliopiston Ohjelmistotekniikan kurssille syksyllä 2022.

** Uusin [release](https://github.com/suitsuke/ot-harjoitustyo/releases/tag/viikko6) **


## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Asennus

1. Asenna ensiksi riippuvuudet (kansiossa jossa on pyproject.toml):

```bash
poetry install
```

2. Käynnistä sovellus:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma käynnistyy komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit saat kommennolla:
Huom! Testaaminen tyhjentää ja alustaa ohjelman oletusasetuksiin.

```bash
poetry run invoke test
```

#### Ongelmatilanteet
Ongelmatilanteiden pitäisi ratketa päivittämällä poetry komennolla:

```bash
poetry update
```

### Testikattavuus

Testikattavuusraportin saa komennolla:

```bash
poetry run invoke coverage
```
jonka jälkeen komento
```bash
poetry run invoke coverage-report
```
generoi raportin html-muodossa kansioon _htmlcov_.

### Pylint
Pylintin tulosteen saat komennolla
```bash
poetry run invoke lint
```
