import krpc
import vessel_sounder1

logging = 'DEBUG'
launch_count = 3

conn = krpc.connect()
if logging in ('DEBUG'):
    print(conn.krpc.get_status().version)

vehicle = vessel_sounder1(conn)

def launch():
    print("STARTING LAUNCH COUNTDOWN: ")
    i = launch_count
    while i > 0:
        print("... "+i)
        i = i - 1
    print('Launch!')
    vehile.launch()

start_vehicle(conn)
launch()


vessel = conn.space_center.active_vessel
