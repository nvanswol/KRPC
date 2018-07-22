
from krpc import Vessel.parts
'''
Methods for SRTU (Sounding Rocket Telemetry Unit)
The Science module for Sounding Rocket probe
v1 Transmit Science continuously
'''
rerunnable_experiments = []

def init(krpc_vessel):
    for part in experiments:
        if part.rerunnable:
            rerunnable_experiments.append(part)

def collect_data(krpc_vessel):
    for part in rerunnable_experiments:
        if part.has_data:
            if part.data.transmit_value > 0:
                part.transmit()
                print("Transmitting: "+str(part.science_subject)+" on "+str(part.biome))
            else:
                part.dump()
        part.run()
