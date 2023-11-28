<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" description="Hello pyESDL training Energy System" name="Training_EnergySystem" id="7cc08dc0-747c-44b2-9979-de5aefc423e8">
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="es_information-ID">
    <carriers xsi:type="esdl:Carriers" id="energy-carriers-ID">
      <carrier xsi:type="esdl:GasCommodity" id="natural-gas-commodity-ID" name="NaturalGas"/>
      <carrier xsi:type="esdl:ElectricityCommodity" id="electricity-commodity-ID" name="Electricity"/>
    </carriers>
  </energySystemInformation>
  <instance xsi:type="esdl:Instance" id="45069b55-1c07-4150-9b09-931aa714ec66" name="Tutorial1_Instance">
    <area xsi:type="esdl:Area" id="d0e3ac33-48b8-4878-8336-6bb1e957ffcd" name="Tutorial1_Area">
      <asset xsi:type="esdl:Import" power="1000000000000.0" name="NaturalGas_Import" prodType="FOSSIL" id="natural-gas-import-ID">
        <port xsi:type="esdl:OutPort" connectedTo="power-plant-in-port-ID" id="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID"/>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3004"/>
      </asset>
      <asset xsi:type="esdl:PowerPlant" name="GasPowered_PowerPlant" efficiency="0.7" power="2000000000.0" id="gas-powered-power-plant-ID">
        <port xsi:type="esdl:InPort" carrier="natural-gas-commodity-ID" id="power-plant-in-port-ID" connectedTo="natural-gas-import-out-port-ID"/>
        <port xsi:type="esdl:OutPort" connectedTo="electricity-demand-in-port-ID" id="power-plant-out-port-ID" carrier="electricity-commodity-ID"/>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3008"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="ElectricityDemand" id="electricity-demand-ID">
        <port xsi:type="esdl:InPort" id="electricity-demand-in-port-ID" carrier="electricity-commodity-ID" connectedTo="power-plant-out-port-ID">
          <profile xsi:type="esdl:SingleValue" value="800.0" id="electricity-demand-profile-ID">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="ed-megawatthour-ID" description="Energy in MWh" multiplier="MEGA" unit="WATTHOUR" physicalQuantity="ENERGY"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3012"/>
      </asset>
    </area>
  </instance>
</esdl:EnergySystem>
