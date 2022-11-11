# Monopoli

```mermaid
classDiagram
	Pelilauta"1" --> "2-8" Pelaaja 
	Pelaaja "1" --> "1" Pelinappula 
	Pelinappula "*" --> "1" Ruutu
	Pelilauta"1" --> "40" Ruutu
	Monopoli --> "1" Pelilauta
	Monopoli --> "2" Noppa
	Monopoli --> "1" Vankilaruutu
	Monopoli --> "1" Aloitusruutu
	Ruutu --> Yhteismaa
	Ruutu --> Sattuma
	Ruutu --> Aloitusruutu
	Ruutu --> Vankilaruutu
	Ruutu --> Asemat_ja_laitokset
	Ruutu --> Normaalit_kadut
	Sattuma --> "*" Kortti
	Yhteismaa --> "*" Kortti
	Normaalit kadut "*" --> "0-1" Pelaaja
	Normaalit kadut "1" --> "0-4" Talo
	Normaalit kadut "1" --> "0-1" Hotelli
	Pelaaja --> "*" Raha

	
	
class Ruutu{
	seuraava ruutu
	}
class Pelaaja{
	nimi
	}
class Pelinappula{
	väri
	}
class Normaalit_kadut{
	nimi
	toiminto
	}
class Sattuma{
	toiminto
	}
class Yhteismaa{
	toiminto
	}
class Asemat_ja_laitokset{
	toiminto
	}
class Vankilaruutu{
	toiminto
	}
class Aloitusruutu{
	toiminto
	}
