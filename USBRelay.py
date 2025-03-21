import sys

class USBRelay:
    def __init__(self, device_path):
        self._device_path = device_path

    def _make_operation(self, relay_no, value_on):
        if relay_no < 1 or relay_no > 8:
            print("Relay number must be between 1 and 8")
            return
            
        try:
            f = open(self._device_path, 'rb')
        except OSError:
            print ("Could not open/read file:")
            return

        with open(self._device_path, 'wb') as f:
            print(self._device_path)
            prefix=int('A1',16)
            command = 1 if value_on else 0
            checksum = prefix+relay_no+command
            buffer=bytearray([prefix, relay_no, command, checksum])
            f.write(buffer)
            print("Written")

    def switch_power(self, connector_no, value_on):
        if connector_no < 1 or connector_no > 3:
            print("power connector number must be between 1 and 2")
            return
        relay_no = 4 - connector_no
        self._make_operation(relay_no, value_on)

    def switch_misc(self, connector_no, value_on):
        if connector_no < 1 or connector_no > 2:
            print("misc connector number must be between 1 and 2")
            return

        relay_no = 9 - connector_no
        self._make_operation(relay_no, value_on)
