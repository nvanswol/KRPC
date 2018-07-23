
from krpc import Vessel
import time
import SRTU
# Vessel specific functions implementing krpc Vessel API
stage_count = 2

def start_vehicle(connection):
    vessel = connection.space_center.active_vessel

def launch():
    vessel.control.activate_next_stage()
    time.sleep(1.5)
    vessel.control.activate_next_stage()
