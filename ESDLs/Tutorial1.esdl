<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" description="Hello pyESDL training Energy System" name="Training_EnergySystem" id="f1dc5e14-2a24-488c-8832-3230ff8bcffb">
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="es_information-ID">
    <carriers xsi:type="esdl:Carriers" id="energy-carriers-ID">
      <carrier xsi:type="esdl:GasCommodity" name="NaturalGas" id="natural-gas-commodity-ID"/>
      <carrier xsi:type="esdl:ElectricityCommodity" name="Electricity" id="electricity-commodity-ID"/>
    </carriers>
  </energySystemInformation>
  <instance xsi:type="esdl:Instance" id="a57ebfb8-57fb-4319-85f7-2c90611dc7c7" name="Tutorial1_Instance">
    <area xsi:type="esdl:Area" id="39df4c9d-f256-4696-afcf-e998dbba0aee" name="Tutorial1_Area">
      <asset xsi:type="esdl:Import" power="1000000000000.0" name="NaturalGas_Import" prodType="FOSSIL" id="natural-gas-import-ID">
        <port xsi:type="esdl:OutPort" id="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID" connectedTo="power-plant-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3004" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:PowerPlant" efficiency="0.6" name="GasPowered_PowerPlant" power="2000000000.0" id="gas-powered-power-plant-ID">
        <port xsi:type="esdl:InPort" id="power-plant-in-port-ID" connectedTo="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID"/>
        <port xsi:type="esdl:OutPort" id="power-plant-out-port-ID" carrier="electricity-commodity-ID" connectedTo="electricity-demand-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3008" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="ElectricityDemand" id="electricity-demand-ID">
        <port xsi:type="esdl:InPort" id="electricity-demand-in-port-ID" carrier="electricity-commodity-ID" connectedTo="power-plant-out-port-ID">
          <profile xsi:type="esdl:SingleValue" value="800.0" id="electricity-demand-profile-ID">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="ed-megawatthour-ID" description="Energy in MWh" multiplier="MEGA" physicalQuantity="ENERGY" unit="WATTHOUR"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Point" lon="4.3012" lat="52.044"/>
      </asset>
    </area>
  </instance>
</esdl:EnergySystem>
