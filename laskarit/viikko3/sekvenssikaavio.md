# Sekvenssikaavio

```mermaid
sequenceDiagram
	participant *
	participant Machine
	*->>Machine:__init__()
	participant FuelTank
	Machine ->> FuelTank:__init__()
	Machine->>FuelTank:fill(40)
	participant Engine
	Machine ->> Engine: __init__(FuelTank)
	*->>Machine:drive()
	Machine ->> Engine:start()
	Machine ->> Engine:_engine_is_running()
	Engine ->> FuelTank:fuel_contents()
	FuelTank -->> Engine: 40
	Engine -->> Machine :True
	Machine ->> Engine: use_energy()
	Engine ->> FuelTank:consume(10)
	
	

	