

def bill_for_residents(apartment_type, water_supply_ratio):
    pass

def bill_for_guests(number_of_guests):
    pass

def bill_for_month(res_bill, guest_bill):
    pass

def parse_commands_file(cmd_file):
    with open(cmd_file, 'r') as cmd_read:
        cmds = cmd_read.read()

    cmds = cmds.split('\n')
    return cmds

def run_commands(cmd):
    cmd = cmd.split()
    if "ALLOT_WATER" in cmd:
        apartment_type = cmd[1]
        water_supply_ratio = cmd[2]
        res_water_consumed, res_bill = bill_for_residents(apartment_type, water_supply_ratio)
        return res_water_consumed, res_bill

    elif "ADD_GUESTS" in cmd:
        number_of_guests = cmd[1]
        guest_water_consumed, guest_bill = bill_for_guests(number_of_guests)
        return guest_water_consumed, guest_bill

    elif "BILL" in cmd:
        bill_for_month(res_water_consumed, guest_water_consumed res_bill, guest_bill)

if __name__ == '__main__':
    cmd_file = sys.argv[0]
    cmds = parse_commands_file(cmd_file)
