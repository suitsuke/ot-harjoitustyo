# Arkkitehtuuri

## Rakenne

```mermaid
graph TD;
    ui --> services;
    services --> repositories;
    repositories --> data;
    services --> data
```
Ohjelmassa ui hoitaa käyttöliittymän ja kutsuu sitten servicen kautta ohjelman toimintoja. Mikäli hoidetaan pysyväistallennusta, kutsuu services repositories toimintoja, muuten se voi itse kutsua datasta tietoa.

## Käyttöliittymä
 Kutsuu services-metodeja ja eristetty muuten logiikasta.

## Sovelluslogiikka

```mermaid
graph TD;
    ui --> services;
    services --> repositories;
    repositories --> data;
    services --> data
```

