from skidl import *


# input and output sections
afin, afout, vin, gnd = Net('AFIN'), Net('AFOUT'), Net('VI'), Net('GND')

# Create parts

r1, r2, r3, r4, r5, r6, r7 = 7 * Part('device', 'R', TEMPLATE, footprint='Resistor_SMD:R_0805_2012Metric')
r1.value = '100K'
r2.value = '100K'
r3.value = '100K'
r4.value = '100K'
r5.value = '100K'
r6.value = '100K'
r7.value = '2k2'

c1, c2, c3, c4, c5 = 5 * Part('device', 'CP', TEMPLATE, footprint='Capacitor_THT:CP_Radial_D4.0mm_P1.50mm')
c1.value = '10uF'
c2.value = '10uF'
c3.value = '10uF'
c4.value = '10uF'
c5.value = '10uF'

j1 = Part('Connector', 'Conn_01x06_Female', TEMPLATE, footprint='Connector-Generic_MountingPin:Conn_01x08_MountingPin')

rv1 = Part('device', 'R_Variable_US', TEMPLATE, footprint='Potentiometer_THT:Potentiometer_ACP_CA6-H2,5_Horizontal')
rv1.value = '200K'

ic1 = Part('Amplifier_Operational', 'LM2904', TEMPLATE, footprint='Package_DIP:DIP-8_W7.62mm')

# Build the connections
afin += r1[1], c2[2] #, j1[1]
afout += r6[1], c5[2]# , j1[5]
gnd += r1[2], c1[2], r3[2], ic1[4], j1[2], j1[4], j1[6], r6[2]
vin += j1[3], r4[1], ic1[8]

generate_netlist()

