"""
    Command line utility to load Farmer data from CSV.
"""
"""
Upload CSV to farmer model using command line.
"""
import csv
from django.conf import settings
from mapapi.models import Farmer
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load data from Farmer details file'

    def add_arguments(self, parser):
        """ Read args from command line. """
        parser.add_argument('-n', '--name', type=str, help='File name(file in data dir) to CSV file to import data.')
    
    def handle(self, *args, **kwargs):
        """ Handle command from CLI """
        fpath = kwargs['name']
        data_file = settings.BASE_DIR / 'data' / fpath
        fields = ('Sr. No', 'Year', 'Name of Farmers', 'Phone No', 'Village', 'GP', 'Block/ Tahsil',\
                  'District', 'State', 'Amount', 'Latitude', 'Longitude', 'Remarks', 'UID')
        records = []
        try:
            with open(data_file, 'r') as csvfile:
                count = 0
                reader = csv.DictReader(csvfile, fields)
                for row in reader:
                    if count > 0:
                        records.append({k: row[k] for k in fields})
                    count += 1
        except FileNotFoundError as fnf:
            raise fnf
        for record in records:
            # add the data to the database
            Farmer.objects.get_or_create(
                name=record['Name of Farmers'], year=record['Year'], 
                phone=record['Phone No'], village=record['Village'],
                gp=record['GP'], block_tahsil=record['Block/ Tahsil'],
                district=record['District'], state=record['State'],
                amount=record['Amount'], latitude=record['Latitude'],
                longitude=record['Longitude'], remarks=record['Remarks'],
                uid=record['UID']
            )

