from skidl import *

# Some common parts used as templates.
res = Part('device', 'R', footprint='Resistors_SMD:R_0603', dest=TEMPLATE)
cap = Part('device', 'C', footprint='Capacitors_SMD:C_0603', dest=TEMPLATE)

# Global nets
gnd = Net('GND')
gnd.drive = POWER
vusb = Net('VUSB')
vusb.drive = POWER
vdd = Net('+3.3V')


# Voltage Regulator
vreg = Part('Regulator_Linear', 'TPS79318-EP', footprint='Package_TO_SOT_SMD:SOT-23-5')
vreg['IN, EN'] += vusb
vreg['GND'] += gnd
vreg['OUT'] += vdd

noise_cap = cap(value='0.01uf')
noise_cap[1, 2] += vreg['BP'], gnd

# Microcontroller
pic32 = Part('MCU_Microchip_PIC32', 'PIC32MX210F016D-IPT', footprint='Package_SO:SSOP-28_5.3x10.2mm_P0.65mm')
pic32['VSS'] += gnd
pic32['VDD'] += vdd         # Main CPU power
pic32['VUSB3V3'] += vdd     # Power to USB Transceiver
pic32['^VBUS$'] += vusb     # Monitor power pin of USB connector.

# Bypass capacitors for microcontroller.
bypass = cap(3, value='0.1uf')
bypass[0][1, 2] += vdd, gnd
bypass[1][1, 2] += vdd, gnd
bypass[2][1, 2] += pic32['VCAP'], gnd

# Microcontroller MCLR circuitry:
#   Pull-up resistor to VDD.
#   Filter capacitor to delay exit of reset or eliminate glitches.
#   Series resistor to isolate capacitor from device programmer.
r_pullup = res(value='10K')
filter_cap = cap(value='0.1uf')
r_pullup[2] += vdd
filter_cap[1, 2] += r_pullup[1], gnd
r_series = res(value='1K')
r_series[1, 2] += r_pullup[1], pic32['MCLR']




