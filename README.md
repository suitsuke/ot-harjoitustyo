# Ohjelmistotekniikka, harjoitustyö

## Stickers app

Sovelluksen avulla käyttäjä voi kerätä tarroja suoritetuista arkiaskareista. Sovellusta voi käyttää muutama käyttäjä, ja kaikilla on oma tarrakokoelmansa.

Sovellus on kehitetty harjoitustyöksi Helsingin yliopiston Ohjelmistotekniikan kurssille syksyllä 2022.


### Huomio Python-versiosta

Ohjelmaa on testattu ja kehitetty versiolla 3.11. Vanhemmat versiot saattavat aiheuttaa ongelmia erityisesti tkinter-moduulin ja invoken kanssa.

## Dokumentaatio

- Käyttöohje
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- Arkkitehtuurikuvaus
- Testausdokumentti
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
