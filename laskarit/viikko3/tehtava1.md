# Monopoli

```mermaid
classDiagram
	Pelilauta"1" --> "2-8" Pelaaja 
	Pelaaja "1" --> "1" Pelinappula 
	Pelinappula "*" --> "1" Ruutu
	Pelilauta"1" --> "40" Ruutu
	
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
