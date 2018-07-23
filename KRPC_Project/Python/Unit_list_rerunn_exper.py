import krpc
import time
# Unit Test: List rerunnable_experiments

def print_list(list):
    print("Printing list:")
    for thing in list:
        print(str(thing.name))

conn = krpc.connect()
print("KRPC Version:"+str(conn.krpc.get_status().version))

krpc_vessel = conn.space_center.active_vessel
print (krpc_vessel.name)

print_list(krpc_vessel.parts.all)

rerunnable_experiments = []

for experiment in krpc_vessel.parts.experiments:
    print("Examing: "+str(experiment))
    if experiment.rerunnable:
        print("Adding: "+str(experiment))
        rerunnable_experiments.append(experiment)

print(str(rerunnable_experiments))

cycles = 10
i = 0
while i < cycles:
    for part in rerunnable_experiments:
        if part.has_data:
            # info = part.science_subject <- Appears to not have constructor in krpc
            place = part.biome
            part.transmit()
            print("Transmitting: "+str(part.data)+" from "+place)
            #if part.data.transmit_value > 0:
            part.dump()
            time.sleep(1)
        print("Running: "+str(part))
        part.run()
        time.sleep(1)
    i = i + 1
