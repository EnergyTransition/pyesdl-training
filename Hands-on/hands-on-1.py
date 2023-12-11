from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl

if __name__ == '__main__':
    energy_system_handler = EnergySystemHandler()

    energy_system = energy_system_handler.create_empty_energy_system(name="HandsOn_EnergySystem",
                                                                     es_description="Hello pyESDL training Energy System",
                                                                     inst_title="HandsOnInstance",
                                                                     area_title="HendsOn_Area")

    handson_area: esdl.Area = energy_system.instance[0].area

    # Create an ElectricityImport
    electricity_import = esdl.Import(name="Electricity_Import", id="electricity-import-ID", prodType="FOSSIL",
                                     power=1000000000000.0)
    electricity_import_location = esdl.Point(lat=52.044, lon=4.3004)
    electricity_import.geometry = electricity_import_location

    handson_area.asset.append(electricity_import)

    # Create a Transformer
    transformer = esdl.Transformer(id='transformer-ID', name='Transformer')
    transformer_location = esdl.Point(lat=52.044, lon=4.3008)
    transformer.geometry = transformer_location

    handson_area.asset.append(transformer)

    ### Start the hands-on part
    # TODO: Connect Import and Transformer
    # END TODO

    ### End the hands-on part

    # Save the ESDL
    energy_system_handler.save('Hands_On_1.esdl')