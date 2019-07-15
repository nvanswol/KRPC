import krpc
import sys

connection = krpc.connect()
print("KRPC VERSION:" + connection.krpc.get_status().version+"\n")

# vehicle = vessel_sounder1(conn)
vehicle = connection.space_center.active_vessel
print("Connected to " + str(vehicle.type) + str(vehicle.name)+"\n")

try:
    GNC = vehicle.control
    print("Performing gyro check")
    print(str(GNC.source))
    GNC_data = vehicle.flight()
    print("Accelermometer: "+ str(GNC_data.g_force))
    print("Pitch, Heading, Roll: " +str(GNC_data.pitch)+", "+str(GNC_data.heading)+", "+str(GNC_data.roll))
    print("\n")
except Exception as e:
    raise e
    print("Unable to get vehicle controls")

try:
    radio = vehicle.comms
    print("Connection to command:" + str(radio.can_communicate) + str(radio.signal_strength))
    print("Signal delay: "+str(radio.signal_delay))
    print("\n")
except Exception as e:
    raise e
    print("Radio hardware unresponsive")

print("Contents: "+str(vehicle.resources.names))
for stuff in vehicle.resources.names:
    if vehicle.resources.has_resource(stuff):
        print(stuff+": "+str(vehicle.resources.amount(stuff)))

diagnostic = input("Run experiments(Y/N): \n")
if diagnostic == "Y":
    print("\nChecking Experiments:")
    for science in vehicle.parts.experiments:
        if science.rerunnable:
            print(str(science.part.name)+" cannot be rerun.")
            run = input("Do you wish to continue?(Y/N)")
            if run == "Y":
                science.run()
        else:
            science.run()
        print(science.part.name)

diagnostic = input("Perform full diagnostic(Y/N): \n")
if diagnostic == "Y":
    print("\nParts: "+str(vehicle.resources.names))
    for bits in vehicle.parts.all:
        print(bits.name)
    print("\nChecking Engines:")
    for bits in vehicle.parts.engines:
        print(bits.part.name)
    print("\nChecking Experiments:")
    for bits in vehicle.parts.experiments:
        print(bits.part.name)
else:
    print("Exiting system check...")