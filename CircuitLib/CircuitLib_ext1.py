from skidl import *

# Common Parts
# Vertical Resistor
vres = Part('device', 'R_US', dest=TEMPLATE, footprint='Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P1.90mm_Vertical')
# Vertical Polarized Capacitor
pcap = Part('device', 'CP1', dest=TEMPLATE, footprint='Capacitor_THT:CP_Radial_D6.3mm_P2.50mm')
# NPN Transistor
npn = Part('Transistor_BJT', 'BC107', dest=TEMPLATE, footprint='Package_TO_SOT_THT:TO-92')
# Connectors
conn = Part('Connector', 'Screw_Terminal_01x02', dest=TEMPLATE, footprint='TerminalBlock:TerminalBlock_Altech_AK300-2_P5.0mm')
# Global Nets
gnd = Net('GND')
gnd.drive = POWER
vdd = Net('5-24V')
vdd.drive = POWER

# Buildout of parts
R1 = vres(value='18k')
R2 = vres(value='2K2')
R3 = vres(value='2k7')
R4 = vres(value='220')
R5 = vres(value='100K')
R6 = vres(value='12k')
R7 = vres(value='10K')
R8 = vres(value='1k')
R9 = vres(value='1k')

C1 = pcap(value='4u7')
C2 = pcap(value='1u')
C3 = pcap(value='1u')
C4 = pcap(value='10uf')

NPN1 = npn()
NPN2 = npn()

ConnPwr = conn()
ConnPwr.name = 'Pwr'
ConnIn = conn()
ConnIn.name = 'Input'
ConnOut = conn()
ConnOut.name = 'Output'


# Connections
# Ground Connections
gnd += ConnIn[2], R2[2], R4[2], R6[2], R8[2], ConnOut[2], ConnPwr[2], C4[2]
# Power Input
vdd += ConnPwr[1], R9[2]
# Signal Input
ConnIn[1] += C1[2]
# Signal Output
ConnOut[1] += C3[2]

# other
R9[1] += R7[1], R5[1], R3[1], R1[1], C4[1]
C1[1] += R2[1], R1[2], NPN1['B']
NPN1['C'] += R3[2], C2[1]
NPN1['E'] += R4[1]
C2[2] += R5[2], NPN2['B'], R6[1]
NPN2['C'] += R7[2], C3[1]
NPN2['E'] += R8[1]


ERC()
generate_netlist()
