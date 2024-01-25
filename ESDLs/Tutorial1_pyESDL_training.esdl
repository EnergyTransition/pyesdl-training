<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" name="Tutorial1 Energy System" id="b91a8831-7b00-4bf9-9dc2-643e5221fae4">
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="es-info-ID">
    <carriers xsi:type="esdl:Carriers" id="energy-carriers-ID">
      <carrier xsi:type="esdl:GasCommodity" name="Natural Gas" id="natural-gas-commodity-ID"/>
      <carrier xsi:type="esdl:ElectricityCommodity" name="Electricity" id="electricity-commodity-ID"/>
    </carriers>
  </energySystemInformation>
  <instance xsi:type="esdl:Instance" id="cf063269-2b67-4ff8-8e04-515bdab8b655" name="Tutorial1 Instance">
    <area xsi:type="esdl:Area" name="Tutorial1 Area" id="295a4577-decc-4192-866c-5b026c08c772">
      <asset xsi:type="esdl:Import" prodType="FOSSIL" id="natural-gas-import-ID" power="1000000000000.0" name="Natural Gas Import">
        <port xsi:type="esdl:OutPort" id="natural-gas-import-out-port-ID" carrier="natural-gas-commodity-ID" connectedTo="power-plant-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3004" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:PowerPlant" power="2000000000.0" id="power-plant-ID" name="Power Plant" efficiency="0.6">
        <port xsi:type="esdl:InPort" carrier="natural-gas-commodity-ID" id="power-plant-in-port-ID" connectedTo="natural-gas-import-out-port-ID"/>
        <port xsi:type="esdl:OutPort" id="power-plant-out-port-ID" carrier="electricity-commodity-ID" connectedTo="electricity-demand-in-port-ID"/>
        <geometry xsi:type="esdl:Point" lon="4.3008" lat="52.044"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="electricity-demand-ID" name="Electricity Demand">
        <port xsi:type="esdl:InPort" connectedTo="power-plant-out-port-ID" id="electricity-demand-in-port-ID" carrier="electricity-commodity-ID">
          <profile xsi:type="esdl:SingleValue" id="electricity-demand-profile-ID" value="800.0">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="WATTHOUR" physicalQuantity="ENERGY" id="mwh-qty-unit-ID" description="Energy in MWh" multiplier="MEGA"/>
          </profile>
        </port>
        <geometry xsi:type="esdl:Point" lon="4.3012" lat="52.044"/>
      </asset>
    </area>
  </instance>
</esdl:EnergySystem>
