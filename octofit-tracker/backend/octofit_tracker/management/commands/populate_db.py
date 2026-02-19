from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Cancellazione dati precedenti...'))
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Popolamento teams...'))
            marvel = Team.objects.create(name='Marvel', description='Team Marvel')
            dc = Team.objects.create(name='DC', description='Team DC')

            self.stdout.write(self.style.SUCCESS('Popolamento users...'))
            users = [
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            ]

            self.stdout.write(self.style.SUCCESS('Popolamento activities...'))
            Activity.objects.create(user=users[0], type='Running', duration=30, date='2024-01-01')
            Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2024-01-02')
            Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2024-01-03')
            Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2024-01-04')

            self.stdout.write(self.style.SUCCESS('Popolamento workouts...'))
            w1 = Workout.objects.create(name='Cardio Blast', description='Allenamento cardio intenso')
            w2 = Workout.objects.create(name='Strength Power', description='Allenamento forza')
            w1.suggested_for.set([users[0], users[2]])
            w2.suggested_for.set([users[1], users[3]])

            self.stdout.write(self.style.SUCCESS('Popolamento leaderboard...'))
            Leaderboard.objects.create(user=users[0], score=100)
            Leaderboard.objects.create(user=users[1], score=80)
            Leaderboard.objects.create(user=users[2], score=120)
            Leaderboard.objects.create(user=users[3], score=90)

            self.stdout.write(self.style.SUCCESS('Database popolato con dati di test!'))
