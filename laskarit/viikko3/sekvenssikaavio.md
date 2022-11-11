# Sekvenssikaavio

```mermaid
sequenceDiagram
	participant *
	participant Machine
	*->>Machine:__init__()
	activate Machine
	participant FuelTank
	Machine ->> FuelTank:__init__()
	activate FuelTank
	Machine->>FuelTank:fill(40)
	deactivate FuelTank

	participant Engine
	Machine ->> Engine: __init__(FuelTank)
	deactivate Machine
	*->>Machine:drive()
	activate Machine
	Machine ->> Engine:start()
	activate Engine
	Machine ->> Engine:_engine_is_running()
	Engine ->> FuelTank:fuel_contents()
	activate FuelTank
	FuelTank -->> Engine: 40
	deactivate FuelTank
	Engine -->> Machine: True
	deactivate Engine
	Machine ->> Engine: use_energy()
	activate Engine
	Engine ->> FuelTank:consume(10)
	deactivate Engine
	deactivate Machine
	
	

	
