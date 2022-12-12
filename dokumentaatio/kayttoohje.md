# Käyttöohje

Lataa uusin [release](https://github.com/suitsuke/ot-harjoitustyo/releases/tag/viikko6).


## Käynnistäminen

1. Avaa terminaali pääkansiossa. Asenna ensiksi riippuvuudet (kansiossa jossa on pyproject.toml):

```bash
poetry install
```

2. Käynnistä sovellus:

```bash
poetry run invoke start
```

### Ongelmatilanteissa
Varmista että poetry on ajan tasalla. Aja komento
```bash
poetry update
```

## Valikot

### Kirjautumisnäkymä

Ohjelma avautuu kirjautumisnäkymään. Valitse käyttäjätunnus jota käytät, käyttäjätunnuksia on 1, 2 ja 3.

### Päävalikko

Tässä näkymässä voit suorittaa toimintoja ja kerätä niistä tarroja. Toimintoja on 3 erilaista.
Toimintonappia klikkaamalla ohjelma lisää tarran tarrakirjaan. Tarrakirjaa pääsee katsomaan collection-nappia painamalla.
Päävalikosta pääsee lisäksi takaisin kirjautumiseen ja käyttäjäasetuksiin.

### Kokoelma

Kokoelmassa näkyy kaikki kerätyt tarrat. Kokoelmasta pääsee takaisin päävalikkoon.

### Käyttäjäasetukset

(TODO)



