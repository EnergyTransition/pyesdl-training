# import pandas as pd
from esdl import esdl
from esdl.esdl_handler import EnergySystemHandler


def tutorial1_esdl(folder_name, file_name):
    # Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files
    energy_system_handler = EnergySystemHandler()

    # TODO: Show the function in esdl_handler
    # Create an empty EnergySystem with a name, a description, and an Instance
    # An EnergySystem contains at least 1 instance of the Instance class.
    # An Instance always contains 1 Area, the largest area relevant to this use case.
    # End TODO
    energy_system = energy_system_handler.create_empty_energy_system(name="Tutorial1 Energy System",
                                                                     inst_title="Tutorial1 Instance",
                                                                     area_title="Tutorial1 Area")

    # Get the energy system area to be able to append assets later on
    # To make the type explicit, use ": esdl.Area"
    tutorial1_area = energy_system.instance[0].area

    # Create carriers and commodities
    # Carriers and commodities are a part of energy system information
    energy_system_information = esdl.EnergySystemInformation(id="es-info-ID")
    # Create natural gas commodity
    natural_gas_commodity = esdl.GasCommodity(id="natural-gas-commodity-ID", name="Natural Gas")

    # Create electricity commodity
    electricity_commodity = esdl.ElectricityCommodity(id="electricity-commodity-ID", name="Electricity")

    energy_carriers = esdl.Carriers(id="energy-carriers-ID")
    energy_carriers.carrier.append(natural_gas_commodity)
    energy_carriers.carrier.append(electricity_commodity)

    energy_system_information.carriers = energy_carriers

    energy_system.energySystemInformation = energy_system_information

    # Create ESDL Carriers and append gas and electricity

    # Create an EnergySystem with an Import, a PowerPlant and an ElectricityDemand
    # Create an Import with 1TW power
    natural_gas_import = esdl.Import(id="natural-gas-import-ID", name="Natural Gas Import", power=1000000000000.0,
                                     prodType=esdl.RenewableTypeEnum.FOSSIL)
    # Create a location for the Import
    natural_gas_import_location = esdl.Point(lat=52.044, lon=4.3004)
    natural_gas_import.geometry = natural_gas_import_location

    # Create an OutPort to connect to other assets
    natural_gas_out_port = esdl.OutPort(id="natural-gas-import-out-port-ID")
    natural_gas_import.port.append(natural_gas_out_port)
    # Assign the gas commodity to the port
    natural_gas_out_port.carrier = natural_gas_commodity
    # Add the NaturalGas Import to the area
    tutorial1_area.asset.append(natural_gas_import)

    # Create a gas-powered PowerPlant with 2GW power and 0.6 efficiency
    power_plant = esdl.PowerPlant(id="power-plant-ID", name="Power Plant", efficiency=0.6, power=2000000000.0)
    # Create a location for the PowerPlant
    power_plant_location = esdl.Point(lat=52.044, lon=4.3008)
    power_plant.geometry = power_plant_location
    # Create PowerPlant's InPort, add commodity and connect to Import
    power_plant_in_port = esdl.InPort(id="power-plant-in-port-ID", connectedTo=[natural_gas_out_port])
    power_plant_in_port.carrier = natural_gas_commodity
    # Create PowerPlant's OutPort, add commodity
    power_plant_out_port = esdl.OutPort(id="power-plant-out-port-ID")
    power_plant_out_port.carrier = electricity_commodity
    # Append ports to PowerPlant
    power_plant.port.append(power_plant_in_port)
    power_plant.port.append(power_plant_out_port)
    # Add the PowerPlant to the area
    tutorial1_area.asset.append(power_plant)

    # Create an ElectricityDemand with an 800 MWh flat profile
    electricity_demand = esdl.ElectricityDemand(id="electricity-demand-ID", name="Electricity Demand")
    # Create a location for the ElectricityDemand
    electricity_demand_location = esdl.Point(lat=52.044, lon=4.3012)
    electricity_demand.geometry = electricity_demand_location
    # Create an InPort connected to the PowerPlant, add commodity, append the port
    electricity_demand_in_port = esdl.InPort(id="electricity-demand-in-port-ID", connectedTo=[power_plant_out_port])
    electricity_demand_in_port.carrier = electricity_commodity
    electricity_demand.port.append(electricity_demand_in_port)
    # Create a SingleValue profile (no unit at the moment)
    electricity_demand_profile = esdl.SingleValue(id="electricity-demand-profile-ID", value=800.0)
    # Create QuantityAndUnitType and assign it to the profile
    mwh_qty_unit = esdl.QuantityAndUnitType(id="mwh-qty-unit-ID", physicalQuantity=esdl.PhysicalQuantityEnum.ENERGY,
                                            unit=esdl.UnitEnum.WATTHOUR, multiplier=esdl.MultiplierEnum.MEGA,
                                            description="Energy in MWh")
    electricity_demand_profile.profileQuantityAndUnit = mwh_qty_unit
    # Append the profile to the InPort
    electricity_demand_in_port.profile.append(electricity_demand_profile)
    # Add the ElectricityDemand to the area
    tutorial1_area.asset.append(electricity_demand)

    # Save the ESDL
    energy_system_handler.save(folder_name + "/" + file_name)

    return


# Load an existing ESDL file, iterate over ESDL elements, and change PowerPlant's efficiency
def tutorial2_esdl(folder_name, file_name_to_edit, file_name_to_save):
    # Create an EnergySystemHandler to retrieve and manipulate an EnergySystem
    # Retrieve the EnergySystem from Tutorial1

    # Iterate over ESDL elements
    # Check if an element is a PowerPlant
    # Change the PowerPlant's efficiency to 0.7

    # Save the ESDL

    # TODO: Delete
    return


# Create a WindPark and add a wind profile from EDR to it
def tutorial3_esdl(folder_name, file_name_to_edit, file_name_to_save):
    # Create an EnergySystemHandler to retrieve and manipulate an EnergySystem
    # Retrieve the EnergySystem from Tutorial2

    # Create a wind park
    # Create a polygon

    # Get the ElectricityDemand's InPort by ID to connect to

    # Create an OutPort, connect it to ED's InPort, and attach a profile to it

    # Get the electricity commodity by ID and assign it to the WindPark's OutPort

    # Create an EDR Client to get an EDR wind profile

    # TODO: Debug the following line to show how to get a list of all the profiles and their IDs - if ID is unkown
    # profiles_list = edr_client.get_objects_list("InfluxDBProfile")
    # Get the InfluxDBProfile from EDR by ID - single WindTurbine
    # Create a WindPark with 100 wind turbines - set the multiplier
    # Append the profile to to the WindPark's port
    # Append the port to the WindPark
    # Add WindPark to the area
    # Retrieve the ESDL area to append to

    # Save the ESDL

    # TODO: Delete
    return


# Write EnergyAsset parameters to CSV
def tutorial4_esdl(folder_name, file_name):
    # Create an EnergySystemHandler to retrieve and manipulate an EnergySystem
    # Retrieve the EnergySystem from Tutorial3

    # Create lists to write the ESDL parameters to
    # asset_types_list = []
    # asset_ids_list = []
    # asset_names_list = []
    # asset_powers_list = []
    # asset_efficiencies_list = []
    #
    # Create a DataFrame to append the lists to (later saved to Excel)
    # asset_parameters = pd.DataFrame()

    # Iterate through all ESDL elements
    # Find all the EnergyAssets

    # Write the asset type to the list
    # Write the asset ID to the list
    # Write the asset name to the list

    # For all producers, consumers and conversions, write the power to the list
    # For all other assets, write ""

    # For all conversions, write the efficiency to the list
    # For all other assets, write ""

    # Add the lists to the DataFrame
    # asset_parameters["Type"] = asset_types_list
    # asset_parameters["ID"] = asset_ids_list
    # asset_parameters["Name"] = asset_names_list
    # asset_parameters["Power"] = asset_powers_list
    # asset_parameters["Efficiency"] = asset_efficiencies_list
    #
    # filename = 'asset_parameters.csv'
    # Save the DataFrame to CSV
    # asset_parameters.to_csv(filename,
    #                         index=False,
    #                         sep=';')

    # TODO: Delete
    return
