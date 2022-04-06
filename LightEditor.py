from yeelight import *
from ipAddress import bridge_ip_address
import time
import schedule

bulb = Bulb(bridge_ip_address, effect="smooth", duration=1000)
bulb.turn_on()
bulb.auto_on = True
bulb.set_color_temp(6000)  # default setting.


def change_light_temperature():
    named_tuple = time.localtime()  # get time, and use just hours.
    time_string = time.strftime("%H", named_tuple)
    print(time_string, "hours")
    if "8" < time_string <= "12":
        bulb.set_color_temp(6000)
    elif "12" < time_string <= "19":
        bulb.set_color_temp(4500)
    else:
        bulb.set_color_temp(3000)


def change_light_colour():
    pass


change_light_temperature()
print(bulb.get_properties())
schedule.every().hour.do(change_light_temperature)

# while True:
#    schedule.run_pending()
#    time.sleep(1)
