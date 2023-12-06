<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" description="Hello pyESDL training Energy System" name="Training_EnergySystem" id="fbe21528-a9a1-4cdb-9ba4-1141bd8fce03">
  <instance xsi:type="esdl:Instance" name="Tutorial1_Instance" id="d62d1f25-d9e9-46b6-8c81-cb81fedc4fc5">
    <area xsi:type="esdl:Area" name="Tutorial1_Area" id="38fc3895-c75d-41fa-a6ce-86fadbd8bf88">
      <asset xsi:type="esdl:Import" id="natural-gas-import-ID" power="1000000000000.0" name="NaturalGas_Import" prodType="FOSSIL">
        <port xsi:type="esdl:OutPort" carrier="natural-gas-commodity-ID" connectedTo="power-plant-in-port-ID" id="natural-gas-import-out-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3004" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:PowerPlant" id="gas-powered-power-plant-ID" name="GasPowered_PowerPlant" efficiency="0.7" power="2000000000.0">
        <port xsi:type="esdl:InPort" connectedTo="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID" id="power-plant-in-port-ID"/>
        <port xsi:type="esdl:OutPort" carrier="electricity-commodity-ID" connectedTo="electricity-demand-in-port-ID" id="power-plant-out-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3008" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="electricity-demand-ID" name="ElectricityDemand">
        <port xsi:type="esdl:InPort" connectedTo="power-plant-out-port-ID wind-park-out-port-ID" id="electricity-demand-in-port-ID" carrier="electricity-commodity-ID">
          <profile xsi:type="esdl:SingleValue" value="800.0" id="electricity-demand-profile-ID">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="ENERGY" id="ed-megawatthour-ID" description="Energy in MWh" multiplier="MEGA" unit="WATTHOUR"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Point" lon="4.3012" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:WindPark" id="wind-park-ID" name="WindPark">
        <port xsi:type="esdl:OutPort" id="wind-park-out-port-ID" connectedTo="electricity-demand-in-port-ID" carrier="electricity-commodity-ID">
          <profile xsi:type="esdl:InfluxDBProfile" startDate="2015-01-01T00:00:00.000000+0000" host="https://edr-profiles.hesi.energy" database="edr-profiles" measurement="profile_kW_2015_Hub_east_160m" name="profile_kW_2015_Hub_east_160m - power_kW [POWER in kW]" id="34f024d4-eb15-4cd3-85a7-ba47ca9b99e1" field="power_kW" endDate="2015-12-31T23:00:00.000000+0000" multiplier="100.0" port="443">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="POWER" id="c7c61174-2abb-47e9-bc3f-2acecaee646d" multiplier="KILO" unit="WATT"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Polygon">
          <exterior xsi:type="esdl:SubPolygon">
            <point xsi:type="esdl:Point" lon="4.3002596497535714" lat="52.04386412846831"/>
            <point xsi:type="esdl:Point" lon="4.300523847341538" lat="52.04386577818243"/>
            <point xsi:type="esdl:Point" lon="4.300515800714494" lat="52.04376349579175"/>
            <point xsi:type="esdl:Point" lon="4.30023953318596" lat="52.043746173750776"/>
          </exterior>
        </geometry>
      </asset>
    </area>
  </instance>
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="es_information-ID">
    <carriers xsi:type="esdl:Carriers" id="energy-carriers-ID">
      <carrier xsi:type="esdl:GasCommodity" id="natural-gas-commodity-ID" name="NaturalGas"/>
      <carrier xsi:type="esdl:ElectricityCommodity" id="electricity-commodity-ID" name="Electricity"/>
    </carriers>
  </energySystemInformation>
</esdl:EnergySystem>
