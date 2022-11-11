```mermaid
sequenceDiagram
participant main
participant laitehallinto
activate main
main->>laitehallinto:HKLLaitehallinto()
participant rautatietori
main ->>rautatietori:Lataajalaite()
participant ratikka6
main ->> ratikka6: Lukijalaite()
participant bussi244
main ->> bussi244: Lukijalaite()
main ->> laitehallinto: lisaa_lataaja(rautatietori)
activate laitehallinto
deactivate laitehallinto
main ->> laitehallinto: lisaa_lukija(ratikka6)
activate laitehallinto
deactivate laitehallinto
main ->> laitehallinto: lisaa_lukija(bussi244)
activate laitehallinto
deactivate laitehallinto

participant lippu_luukku
main ->> lippu_luukku: Kioski()
participant kallen_kortti
lippu_luukku ->> kallen_kortti: osta_matkakortti(kallen_kortti, None)
activate kallen_kortti


deactivate kallen_kortti

deactivate main
