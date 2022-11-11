# Sekvenssikaavio

```mermaid
sequenceDiagram
	participant *
	participant Machine
	*->>Machine:__init__()
	participant FuelTank
	Machine ->> FuelTank:__init__()
	Machine->>Fueltank:fill(40)
	Machine ->> Engine(FuelTank)
	*->>Machine:drive()
	Machine ->> Engine:start()
	

	
