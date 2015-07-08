from lifxlan import *
import sys
from time import sleep

def main():
    num_lights = None
    if len(sys.argv) != 2:
        print("\nDiscovery will go much faster if you provide the number of lights on your LAN:")
        print("  python {} <number of lights on LAN>\n".format(sys.argv[0]))
    else:
        num_lights = int(sys.argv[1])

    # instantiate LifxLAN client, num_lights may be None (unknown)
    print("Discovering lights...")
    lifx = LifxLAN(num_lights)

    original_colors = lifx.get_color_all_lights()
    original_powers = lifx.get_power_all_lights()

    print("Turning on all lights...")
    lifx.set_power_all_lights(True)
    sleep(1)

    print("Flashy fast rainbow")
    rainbow(lifx, 0.1)

    print("Smooth slow rainbow")
    rainbow(lifx, 1, smooth=True)

    print("Restoring original power and color...")
    # restore original power
    bulb.set_power(original_power)
    # restore original color
    sleep(0.5) # for looks
    bulb.set_color(original_color)

def rainbow(lan, duration_secs=0.5, smooth=False):
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
    transition_time_ms = duration_secs*1000 if smooth else 0
    rapid = True if duration_secs < 1 else False
    for color in colors:
        lan.set_color_all_lights(color, transition_time_ms, rapid)
        sleep(duration_secs)

if __name__=="__main__":
    main()