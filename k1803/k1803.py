from skidl import *

# Common Parts
# Vertical Resistor
vres = Part('device', 'R_US', dest=TEMPLATE, footprint='Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P1.90mm_Vertical')
# Vertical Polarized Capacitor
pcap = Part('device', 'CP1', dest=TEMPLATE, footprint='Capacitor_THT:CP_Radial_D6.3mm_P2.50mm')


# Global Nets
gnd = Net('GND')
gnd.drive = POWER
vdd = Net('5-24V')
vdd.drive = POWER

# Parts
r = vres(6, value='100K')
r[0][2] += gnd
r[2][2] += gnd
r[3][1] += vdd
r[5][2] += gnd


r7 = vres(value='2k2')
c = pcap(5, value='10uf')
c[1][2] += r[1][1]
c[0][1] += gnd
rv1 = Part('device', 'R_Variable_US', footprint='Potentiometer_THT:Potentiometer_ACP_CA6-H2,5_Horizontal', value='200k')

# Header Connector
j1 = Part('Connector', 'Conn_01x06_Male', footprint='Connector_PinHeader_1.00mm:PinHeader_1x06_P1.00mm_Vertical')
j1[1] += (c[1][1] | r[0][1])
j1[2, 4, 6] += gnd
j1[3] += vdd
j1[5] += (c[4][1] | r[5][1])

ic1 = Part('Amplifier_Operational', 'LM2904', footprint='Package_DIP:DIP-8_W7.62mm')
ic1['V+', 'V-'] += vdd, gnd
ic1[1] += (r[4][2] | c[2][1])
ic1[2] += (r[1][2] | r[4][1])
ic1[3] += (r[3][2] | c[0][2] | ic1[5] | r[2][1])
ic1[6] += (r7[2] | rv1[1])
ic1[7] += (rv1[2] | c[4][2])

c[2][2] += c[3][1]
c[3][2] += r7[1]


ERC()
generate_netlist()

