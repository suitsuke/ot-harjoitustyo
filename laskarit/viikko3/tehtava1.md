# Monopoli

```mermaid
classDiagram
	Pelilauta"1" --> "2-8" Pelaaja --> "1" Pelinappula --> "1" Ruutu
	Pelilauta"1"-->Ruutu "40"
class Ruutu{
	seuraava ruutu
	}
class Pelaaja{
	nimi
	}
class Pelinappula{
	väri
	}
class Pelilauta{
	monopoli
	}
