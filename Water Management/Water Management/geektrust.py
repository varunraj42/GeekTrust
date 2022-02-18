class Apartment:
    PersonsByApartmentType = {"2": 3, "3": 5}

    def __init__(self, apartment_type):
        self.apartment_type = apartment_type

    def calc_apart_capacity(self):
        return Apartment.PersonsByApartmentType[self.apartment_type]


class Resident(Apartment):
    SupplyCapByPerson = 10

    def __init__(self, total_residents):
        self.total_residents = total_residents

    def calc_water_capacity(self):
        return self.total_residents * Resident.SupplyCapByPerson


class Guest(Resident):
    def __init__(self, guest_count):
        self.guest_count = guest_count

    def calc_water_capacity(self):
        return self.guest_count * super().SupplyCapByPerson


class WaterSupplyPricing():
    PricingBySupplyType = {"Co-orporation": 1, "Borwell": 1.5, "Tanker": {"0-500": 2, "500-1500": 3, "1500-3000": 5, "3001-": 8}}


class Coorporation(WaterSupplyPricing):
    def __init__(self, water_cap_required):
        self.water_cap_required = water_cap_required

    def calc_water_price(self):
        return self.water_cap_required * super().PricingBySupplyType["Co-orporation"]


class Borewell(WaterSupplyPricing):
    def __init__(self, water_cap_required):
        self.water_cap_required = water_cap_required

    def calc_water_price(self):
        return self.water_cap_required * super().PricingBySupplyType["Borwell"]


class Tanker(WaterSupplyPricing):
    def __init__(self, water_cap_required):
        self.water_cap_required = water_cap_required

    def calc_water_price(self):
        total_price = 0
        slab_prices = super().PricingBySupplyType["Tanker"]

        for slab_cap in slab_prices:
            slab_cap_split = slab_cap.split('-')
            slab_cap_split = [ int(val) if val!='' else 0 for val in slab_cap_split]
            slab_max_cap = abs(slab_cap_split[1] - slab_cap_split[0])

            if slab_max_cap > 3000:
                total_price += self.water_cap_required * slab_prices[slab_cap]
                self.water_cap_required = 0
            else:
                total_price += min(self.water_cap_required, slab_max_cap) * slab_prices[slab_cap]
                self.water_cap_required -= min(self.water_cap_required, slab_max_cap)

        return total_price

# Utilities
def calc_resident_water_cap_by_ratio(ws_req, coorp_ratio, borewell_ratio):
    import math
    total_wc_parts = coorp_ratio + borewell_ratio
    single_part_wc = ws_req/total_wc_parts
    coorp_ws_req = math.ceil(coorp_ratio * single_part_wc)
    borewell_ws_req = math.ceil(borewell_ratio * single_part_wc)
    return coorp_ws_req, borewell_ws_req

def parse_input_file(input_cmd_file):
    with open(input_cmd_file, "r") as cmd_read:
        cmd_data = cmd_read.read()

    cmd_data = cmd_data.strip()
    cmds = cmd_data.split('\n')

    total_guests = 0
    for cmd in cmds:
        if "ALLOT_WATER" in cmd:
            apart_type, coorp_borwell_ratio = cmd.split(' ')[-2:]
            coorp_ratio = int(coorp_borwell_ratio.split(':')[0])
            borewell_ratio = int(coorp_borwell_ratio.split(':')[1])
        elif "ADD_GUESTS" in cmd:
            total_guests += int(cmd.split(' ')[-1])

    return apart_type, coorp_ratio, borewell_ratio, total_guests


def main(input_cmd_file):
    import sys
    if not input_cmd_file:
        input_cmd_file = sys.argv[1]
    apart_type, coorp_ratio, borewell_ratio, total_guests = parse_input_file(input_cmd_file)
    total_num_days = 30
    apart = Apartment(apart_type)
    resident = Resident(apart.calc_apart_capacity())

# Residents Water Bill Calculated
    residents_per_day_wc = resident.calc_water_capacity()
    residents_monthly_wc = residents_per_day_wc * total_num_days
    coorp_ws_req, borewell_ws_req = calc_resident_water_cap_by_ratio(residents_monthly_wc, coorp_ratio, borewell_ratio)

    coorp = Coorporation(coorp_ws_req)
    monthly_coorp_bill = coorp.calc_water_price()

    borewell = Borewell(borewell_ws_req)
    monthly_borewell_bill = borewell.calc_water_price()


# Guests Water Bill Calculated
    guest_fam = Guest(total_guests)

    final_guest_count = guest_fam.guest_count
    guest_fam_wc = guest_fam.calc_water_capacity()

    guests_per_day_wc = guest_fam_wc
    guests_monthly_wc = guests_per_day_wc * total_num_days

    tanker = Tanker(guests_monthly_wc)
    monthly_tanker_bill = tanker.calc_water_price()

    output = f"{residents_monthly_wc + guests_monthly_wc} {int(monthly_coorp_bill + monthly_borewell_bill + monthly_tanker_bill)}"    
    print(output)
    return output


if __name__ == '__main__':
    input_cmd_file = ''
    main(input_cmd_file)
