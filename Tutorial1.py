from esdl import esdl
from esdl.edr.client import EDRClient
from esdl.esdl_handler import EnergySystemHandler
import pandas as pd
from esdl.profiles.influxdbprofilemanager import InfluxDBProfileManager

if __name__ == '__main__':
    folder_name = "ESDLs"
    file_name = "Tutorial1.esdl"

    # Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files
    energy_system_handler = EnergySystemHandler()

    # First, create an empty EnergySystem with a name, a description, and an Instance

    # An EnergySystem contains at least 1 instance of the Instance class.
    # The Instance class makes it possible to describe multiple instances of the energy system in 1 ESDL model ( or 1 ESDL file)
    # (for example for different years or for different aggregation levels).
    # An Instance always contains 1 Area, the largest area relevant to this use case.
    # Areas can contain other Areas.This creates a whole hierarchy of areas (e.g.a country divided into provinces, which in turn are divided into municipalities, etc.).
    # TODO: Show the function in esdl_handler
    energy_system = energy_system_handler.create_empty_energy_system(name="Training_EnergySystem",
                                                                     es_description="Hello pyESDL training Energy System",
                                                                     inst_title="Tutorial1_Instance",
                                                                     area_title="Tutorial1_Area")
    # END TODO

    # Get the energy system area to be able to append assets later on
    # To make the type explicit, use ": esdl.Area"
    # tutorial1_area: esdl.Area = energy_system.instance[0].area
    tutorial1_area = energy_system.instance[0].area

    # TODO: Do after creating the first asset
    # Create carriers and commodities
    # Carriers and commodities are a part of energy system information
    energy_system_information = esdl.EnergySystemInformation(id="es_information-ID")
    # Create natural gas commodity
    # TODO: Show the OOP inheritance for GasCommodity on github.io
    natural_gas_commodity = esdl.GasCommodity(id="natural-gas-commodity-ID", name="NaturalGas")
    # END TODO
    electricity_commodity = esdl.ElectricityCommodity(id="electricity-commodity-ID", name="Electricity")

    energy_carriers = esdl.Carriers(id="energy-carriers-ID")
    energy_carriers.carrier.append(natural_gas_commodity)
    energy_carriers.carrier.append(electricity_commodity)

    energy_system_information.carriers = energy_carriers
    energy_system.energySystemInformation = energy_system_information
    # END TODO

    # An EnergySystem with an Import, a PowerPlant and an ElectricityDemand

    # Create an Import with 1TW power
    # TODO: Show in MapEditor once the Import is created, and show in Notepad++
    natural_gas_import = esdl.Import(name="NaturalGas_Import", id="natural-gas-import-ID", prodType="FOSSIL",
                                     power=1000000000000.0)
    # Create a location for the Import
    natural_gas_import_location = esdl.Point(lat=52.044, lon=4.3004)
    natural_gas_import.geometry = natural_gas_import_location

    # OutPort that connects to other assets
    natural_gas_import_out_port = esdl.OutPort(id="natural-gas-import-out-port-ID")
    # Assign the commodity to he port
    natural_gas_import_out_port.carrier = natural_gas_commodity
    natural_gas_import.port.append(natural_gas_import_out_port)

    # Add the NaturalGas Import to the area
    tutorial1_area.asset.append(natural_gas_import)
    # END TODO

    # Create a gas-powered PowerPlant
    power_plant = esdl.PowerPlant(name="GasPowered_PowerPlant", id="gas-powered-power-plant-ID", power=2000000000.0,
                                  efficiency=0.6)
    # Create a location for the PowerPlant
    power_plant_location = esdl.Point(lat=52.044, lon=4.3008)
    power_plant.geometry = power_plant_location

    # Create PowerPlant's InPort
    power_plant_in_port = esdl.InPort(id="power-plant-in-port-ID", connectedTo=[natural_gas_import_out_port])
    power_plant_in_port.carrier = natural_gas_commodity
    power_plant.port.append(power_plant_in_port)
    # Create PowerPlant's OutPot
    power_plant_out_port = esdl.OutPort(id="power-plant-out-port-ID")
    # Create and append electricity commodity
    power_plant_out_port.carrier = electricity_commodity
    power_plant.port.append(power_plant_out_port)

    # Add the PowerPlant to the area
    tutorial1_area.asset.append(power_plant)

    # Create an ElectricityDemand with a 800 MWh flat profile
    electricity_demand = esdl.ElectricityDemand(name="ElectricityDemand", id="electricity-demand-ID")
    # Create a location for the ElectricityDemand
    electricity_demand_location = esdl.Point(lat=52.044, lon=4.3012)
    electricity_demand.geometry = electricity_demand_location

    # TODO: Explain that profiles are attached to ports, show on github.io and on MapEditor
    electricity_demand_in_port = esdl.InPort(id="electricity-demand-in-port-ID", connectedTo=[power_plant_out_port])
    # END TODO
    electricity_demand_in_port.carrier = electricity_commodity
    electricity_demand.port.append(electricity_demand_in_port)
    # Do not set quantity and unit now
    electricity_demand_profile = esdl.SingleValue(id="electricity-demand-profile-ID", value=800.0)
    # Create QuantityAndUnitReference
    electricity_demand_qty_unit = esdl.QuantityAndUnitType(id='ed-megawatthour-ID', physicalQuantity='ENERGY',
                                                           unit='WATTHOUR', multiplier='MEGA',
                                                           description='Energy in MWh')
    electricity_demand_profile.profileQuantityAndUnit = electricity_demand_qty_unit
    electricity_demand_in_port.profile.append(electricity_demand_profile)
    # Add the ElectricityDemand to the area
    tutorial1_area.asset.append(electricity_demand)

    # Save the ESDL
    energy_system_handler.save(folder_name + "/" + file_name)