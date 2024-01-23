#import pandas as pd

def tutorial1_esdl(folder_name, file_name):
    # Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

    # TODO: Show the function in esdl_handler
    # Create an empty EnergySystem with a name, a description, and an Instance
    # An EnergySystem contains at least 1 instance of the Instance class.
    # An Instance always contains 1 Area, the largest area relevant to this use case.
    # End TODO

    # Get the energy system area to be able to append assets later on
    # To make the type explicit, use ": esdl.Area"

    # Create carriers and commodities
    # Carriers and commodities are a part of energy system information
    # Create natural gas commodity
    # TODO: Show the OOP inheritance for GasCommodity on github.io

    # End TODO
    # Create electricity commodity

    # Create ESDL Carriers and append gas and electricity

    # Create an EnergySystem with an Import, a PowerPlant and an ElectricityDemand
    # Create an Import with 1TW power
    # Create a location for the Import
    # Create an OutPort to connect to other assets
    # Assign the gas commodity to the port
    # Add the NaturalGas Import to the area

    # Create a gas-powered PowerPlant with 2GW power and 0.6 efficiency
    # Create a location for the PowerPlant
    # Create PowerPlant's InPort, add commodity and connect to Import
    # Create PowerPlant's OutPot, add commodity
    # Append ports to PowerPlant
    # Add the PowerPlant to the area

    # Create an ElectricityDemand with an 800 MWh flat profile
    # Create a location for the ElectricityDemand
    # TODO: Explain that profiles are attached to ports, show on github.io and on MapEditor
    # Create an InPort connected to the PowerPlant, add commodity, append the port
    # Create a SingleValue profile (no unit at the moment)
    # Create QuantityAndUnitType and assgin it to the profile
    # Append the profile to the InPort
    # Add the ElectricityDemand to the area

    # Save the ESDL

    # TODO: Delete
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
    #profiles_list = edr_client.get_objects_list("InfluxDBProfile")
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