from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='desc')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc')
        self.workout.suggested_for.set([self.user])
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=42)

    def test_user(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)

    def test_workout(self):
        self.assertIn(self.user, self.workout.suggested_for.all())

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 42)
