import USBRelay
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='USB Relay')

    parser.add_argument('-p', '--device_path', required=True, help='HID device path e.g. /dev/hidraw4')
    parser.add_argument('-t', '--type', required=True, choices=['power', 'misc'])
    parser.add_argument('-i', '--id', required=True)
    parser.add_argument('-v', '--value', required=True, choices=['0', '1'], help="0 = off, 1 - on")

    args = parser.parse_args()
    usb_relay = USBRelay.USBRelay(args.device_path)
    value = args.value == '1'

    if args.type == "power":
        relay_id = int(args.id)
        if relay_id < 1 or relay_id > 3:
            print("Power relay it must be between 1 and 3.")
            sys.exit(1)


        usb_relay.switch_power(relay_id, value)
    elif args.type == "misc":
        relay_id = int(args.id)
        if relay_id < 1 or relay_id > 2:
            print("Misc relay it must be between 1 and 2.")
            sys.exit(1)

        usb_relay.switch_misc(relay_id, value)
    else:
        print("Wrong type.")
        sys.exit(1)



