import csv

from django.core.management.base import BaseCommand, CommandError

from cats.models import Hunting, Cat


class Command(BaseCommand):
    help = 'Generate csv file with all hunts for selected cat id'

    def add_arguments(self, parser):
        parser.add_argument('cat_id', nargs='+', type=int)

    def handle(self, *args, **options):
        if len(options['cat_id']) > 1:
            raise CommandError('Too many ids')
        cat_id = options['cat_id'][0]
        cat = Cat.objects.filter(id=cat_id)
        if cat.count():
            with open(f"cat_{cat_id}.csv", 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([cat_id, cat[0].cat_name])
                for hunt in Hunting.objects.filter(cat_id=cat_id):
                    writer.writerow([f'{hunt.hunting_duration} hours', f'{hunt.hunting_prey} caught'])

        self.stdout.write(self.style.SUCCESS('File successfully generated.'))
