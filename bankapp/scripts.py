import csv

from bankapp.models import Banks, Branches


def bank_creation_script_run():
    with open('bank_branches.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # The header row values become your keys
            bank_id = row['bank_id']
            bank_name = row['bank_name']

            new_bank = Banks.objects.get_or_create(pk=bank_id, name=bank_name)

def branch_creation_script_run():
    with open('bank_branches.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        count = 0
        for row in reader:
            # The header row values become your keys
            ifsc = row['ifsc']
            bank_id = row['bank_id']
            branch = row['branch']
            address = row['address']
            city = row['city']
            district = row['district']
            state = row['state']

            if count < 10000:
                bank_obj = Banks.objects.get(pk=bank_id)
                new_branch = Branches.objects.get_or_create(
                    ifsc=ifsc,
                    bank_id=bank_obj,
                    branch=branch,
                    address=address,
                    city=city,
                    district=district,
                    state=state
                )
                count = count + 1
