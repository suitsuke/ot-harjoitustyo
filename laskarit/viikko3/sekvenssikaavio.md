# Sekvenssikaavio

```mermaid
sequenceDiagram
	participant *
	participant Machine
	*->>Machine:__init__()
	participant FuelTank
	Machine ->> FuelTank:__init__()
	Machine->>Fueltank:fill(40)
	participant Engine
	Machine ->> Engine: __init__(FuelTank)
	*->>Machine:drive()
	Machine ->> Engine:start()
	

	
