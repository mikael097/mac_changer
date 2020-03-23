import subprocess
import optparse
import re


class MacChanger:

    def __init__(self):
        pass

    @staticmethod
    def change_mac(int_face, mac_id):
        print("[+] Changing the mac address for interface " + int_face + " to " + mac_id)
        subprocess.call(["ifconfig", int_face, "down"])
        subprocess.call(["ifconfig", int_face, "hw", "ether", mac_id])
        subprocess.call(["ifconfig", int_face, "up"])

    @staticmethod
    def get_arguments():
        obj = optparse.OptionParser()
        obj.add_option("-i", "--interface", dest="interface", help="The required interface")
        obj.add_option("-m", "--new-mac", dest="New_Mac", help="The new mac ID ")
        (options, arguments) = obj.parse_args()
        if not options.interface:
            obj.error("[-] Please specify the interface. Use --help for more info")
        if not options.New_Mac:
            obj.error("[-] Please specify the mac address. Use --help for more info")
        if options.interface not in str(subprocess.check_output(["ifconfig"])):
            obj.error("[-] No such interface")
        return options

    @staticmethod
    def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_add_ifconfig_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        if mac_add_ifconfig_result:
            return mac_add_ifconfig_result.group(0)
        else:
            print("[-] Couldn't read mac address.")

    def run_mac_changer(self):
        options = self.get_arguments()
        print("Current Mac=" + str(self.get_current_mac(options.interface)))
        self.change_mac(options.interface, options.New_Mac)
        new_mac = self.get_current_mac(options.interface)
        if new_mac == options.New_Mac:
            print("[+] MAC address successfully changed to " + new_mac)
        else:
            print("[-] MAC address couldn't be changed.")


mac_changer_object = MacChanger()
mac_changer_object.run_mac_changer()
