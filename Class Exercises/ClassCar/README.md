Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a.	Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
b.	O consumo é especificado no construtor e o nível de combustível inicial é 0.
c.	Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
d.	Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e.	Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:


NomeDoCarro= Carro(15);           # 15 quilômetros por litro de combustível. 
NomeDoCarro.adicionarGasolina(20);  # abastece com 20 litros de combustível. 
NomeDoCarro.andar(100);            # anda 100 quilômetros.
NomeDoCarro.obterGasolina();        # Imprime o combustível que resta no tanque.

--------------------------------------------------------------------------------------------------------------------

Car class: Implement a class called Car with the following properties:
The. A vehicle has a certain fuel consumption (measured in km/liter) and a certain amount of fuel in the tank.
B. Consumption is specified in the builder and the initial fuel level is 0.
ç. Provide a walk( ) method that simulates driving the vehicle a certain distance, reducing the fuel level in the gas tank.
d. Provide a getGasoline() method, which returns the current fuel level.
and. Provide an addGasoline() method to fill the tank. Example of use:


CarName = Car(15);   # 15 kilometers per liter of fuel.
CarName.addGasoline(20);    # refills with 20 liters of fuel.
CarName.floor(100);   # walk 100 kilometers.
CarName.getGasoline();   # Print the fuel remaining in the tank.
