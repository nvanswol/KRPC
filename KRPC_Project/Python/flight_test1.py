import krpc
import vessel_sounder1

logging = 'DEBUG'
conn = krpc.connect()
if logging in ('DEBUG'):
    print(conn.krpc.get_status().version)

def start_vehicle(connection):
    vessel = connection.space_center.active_vessel
    vessel_sounder1 =

def launch():
    print('Launch!')
    vessel.control.activate_next_stage()

start_vehicle(conn)
launch()


vessel = conn.space_center.active_vessel
