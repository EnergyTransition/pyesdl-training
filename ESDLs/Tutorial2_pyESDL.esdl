<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" description="Hello pyESDL training Energy System" name="Training_EnergySystem" id="fbe21528-a9a1-4cdb-9ba4-1141bd8fce03">
  <instance xsi:type="esdl:Instance" id="d62d1f25-d9e9-46b6-8c81-cb81fedc4fc5" name="Tutorial1_Instance">
    <area xsi:type="esdl:Area" id="38fc3895-c75d-41fa-a6ce-86fadbd8bf88" name="Tutorial1_Area">
      <asset xsi:type="esdl:Import" id="natural-gas-import-ID" power="1000000000000.0" name="NaturalGas_Import" prodType="FOSSIL">
        <port xsi:type="esdl:OutPort" id="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID" connectedTo="power-plant-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3004"/>
      </asset>
      <asset xsi:type="esdl:PowerPlant" power="2000000000.0" id="gas-powered-power-plant-ID" name="GasPowered_PowerPlant" efficiency="0.7">
        <port xsi:type="esdl:InPort" id="power-plant-in-port-ID" connectedTo="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID"/>
        <port xsi:type="esdl:OutPort" id="power-plant-out-port-ID" carrier="electricity-commodity-ID" connectedTo="electricity-demand-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3008"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="electricity-demand-ID" name="ElectricityDemand">
        <port xsi:type="esdl:InPort" connectedTo="power-plant-out-port-ID" id="electricity-demand-in-port-ID" carrier="electricity-commodity-ID">
          <profile xsi:type="esdl:SingleValue" id="electricity-demand-profile-ID" value="800.0">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="WATTHOUR" physicalQuantity="ENERGY" id="ed-megawatthour-ID" description="Energy in MWh" multiplier="MEGA"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Point" lat="52.044" lon="4.3012"/>
      </asset>
    </area>
  </instance>
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="es_information-ID">
    <carriers xsi:type="esdl:Carriers" id="energy-carriers-ID">
      <carrier xsi:type="esdl:GasCommodity" name="NaturalGas" id="natural-gas-commodity-ID"/>
      <carrier xsi:type="esdl:ElectricityCommodity" name="Electricity" id="electricity-commodity-ID"/>
    </carriers>
  </energySystemInformation>
</esdl:EnergySystem>
