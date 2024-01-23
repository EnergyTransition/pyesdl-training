import esdl_generator

if __name__ == '__main__':
    folder_name = "ESDLs"
    tutorial1_filename = "Tutorial1_pyESDL.esdl"
    tutorial2_filename = "Tutorial2_pyESDL.esdl"
    tutorial3_filename = "Tutorial3_pyESDL.esdl"

    # esdl_generator.test_retrieve_profile()

    # # Tutorial 1
    # esdl_generator.tutorial1_esdl(folder_name, tutorial1_filename)
    #
    # # Tutorial 2
    # esdl_generator.tutorial2_esdl(folder_name, tutorial1_filename, tutorial2_filename)
    #
    # # Tutorial 3
    esdl_generator.tutorial3_esdl(folder_name, tutorial2_filename, tutorial3_filename)

    # Tutorial 4
    #esdl_generator.tutorial4_esdl(folder_name, tutorial3_filename)
