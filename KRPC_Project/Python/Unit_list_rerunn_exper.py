import krpc
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

for part in rerunnable_experiments:
    if part.has_data:
        if part.data.transmit_value > 0:
            part.transmit()
            print("Transmitting: "+str(part.science_subject)+" on "+str(part.biome))
        else:
            part.dump()
    print("Running: "+str(part.science_subject))
    part.run()
