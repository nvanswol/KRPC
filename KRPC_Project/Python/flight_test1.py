import krpc

logging = 'DEBUG'
conn = krpc.connect()
if logging in ('DEBUG'):
    print(conn.krpc.get_status().version)
vessel = conn.space_center.active_vessel

def launch():
    print('Launch!')
    vessel.control.activate_next_stage()

launch()
