from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl

if __name__ == '__main__':
    energy_system_handler = EnergySystemHandler()

    energy_system: esdl.EnergySystem = energy_system_handler.load_file('Hands_On.esdl')

    # Create and add EnergySystemInformation and Carriers to the EnergySystem
    energy_system_information = esdl.EnergySystemInformation(id="es_information-ID")
    electricity_commodity = esdl.ElectricityCommodity(id="electricity-commodity-ID", name="Electricity")

    energy_carriers = esdl.Carriers(id="energy-carriers-ID")
    energy_carriers.carrier.append(electricity_commodity)

    energy_system_information.carriers = energy_carriers
    energy_system.energySystemInformation = energy_system_information

    ### Start the hands-on part
    # TODO: Iterate over assets and assign the electricity commodity to all the asset ports
    # END TODO


    # Save the ESDL
    energy_system_handler.save('Hands_On.esdl')