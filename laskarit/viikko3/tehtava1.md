# Monopoli

```mermaid
classDiagram
	Pelilauta"1" --> "2-8" Pelaaja 
	Pelaaja "1" --> "1" Pelinappula 
	Pelinappula "*" --> "1" Ruutu
	Pelilauta"1" --> "40" Ruutu
	Monopoli --> "1" Pelilauta
	Monopoli --> "2" Noppa
	
class Ruutu{
	seuraava ruutu
	}
class Pelaaja{
	nimi
	}
class Pelinappula{
	väri
	}

