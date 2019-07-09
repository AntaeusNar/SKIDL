from skidl import *

# Common Parts
# Vertical Resistor
vres = Part('device', 'R_US', dest=TEMPLATE, footprint='Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P1.90_Vertical')
# Vertical Polarized Capacitor
pcap = Part('device', 'CP1', dest=TEMPLATE, footprint='Capacitor_THT:CP_Radial_D6.3mm_P2.50mm')


# Global Nets
gnd = Net('GND')
gnd.drive = POWER
vdd = Net('5-24V')
vdd.drive = POWER

# Header Connector
j1 = Part('Connector', 'Conn_01x06_Male', footprint='Connector_PinHeader_1.00mm:PinHeader_1x06_P1.00mm_Vertical')
j1[2, 4, 6] += gnd
j1[3] += vdd


# Create parts

r1, r2, r3, r4, r5, r6, r7 = 7 * Part('device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')
r1.value = '100K'
r2.value = '100K'
r3.value = '100K'
r4.value = '100K'
r5.value = '100K'
r6.value = '100K'
r7.value = '2k2'

c1, c2, c3, c4, c5 = 5 * Part('device', 'CP', footprint='Capacitor_THT:CP_Radial_D4.0mm_P1.50mm')
c1.value = '10uF'
c2.value = '10uF'
c3.value = '10uF'
c4.value = '10uF'
c5.value = '10uF'

rv1 = Part('device', 'R_Variable_US', footprint='Potentiometer_THT:Potentiometer_ACP_CA6-H2,5_Horizontal')
rv1.value = '200K'

ic1 = Part('Amplifier_Operational', 'LM2904', footprint='Package_DIP:DIP-8_W7.62mm')

# Build the connections
afin += r1[1], c2[2], j1[1]
afout += r6[1], c5[2], j1[5]
gnd += r1[2], c1[2], r3[2], ic1[4], j1[2], j1[4], j1[6], r6[2]
vin += j1[3], r4[1], ic1[8]

ERC()
generate_netlist()

