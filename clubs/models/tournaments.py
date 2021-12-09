from django.db import models
from .users import User
from .clubs import Club, Membership
from django.utils import timezone
from datetime import datetime


class Tournament(models.Model):
    class StageTypes(models.TextChoices):
        SIGNUP = 'S'
        ELIMINATION = 'E'
        GROUP_STAGES = 'G'

    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.CharField(max_length=1000, blank=False)
    date = models.DateTimeField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    coorganizers = models.ManyToManyField(User, related_name="coorganizers")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=False)
    capacity = models.IntegerField(null=True)
    deadline = models.DateTimeField(null=True)
    stage = models.CharField(max_length=1, choices=StageTypes.choices, default=StageTypes.SIGNUP)

    def join_tournament(self, user):
        current_datetime = timezone.make_aware(datetime.now(), timezone.utc)
        if current_datetime < self.deadline:
            try:
                membership = Membership.objects.get(user=user, club=self.club)
                if (Membership.UserTypes.MEMBER in membership.get_user_types()):
                    if user != self.organizer:
                        try:
                            current_participants_count = TournamentParticipation.objects.filter(tournament=self).count()
                        except:
                            current_participants_count = 0
                        if (current_participants_count < self.capacity):
                            new_participation = TournamentParticipation(user=user, tournament=self)
                            try:
                                new_participation.full_clean()
                                new_participation.save()
                                return ""
                            except:
                                return "You are already signed up to this tournament."
                        else:
                            return "This tournament has reached max capacity, you cannot join it."
                    else:
                        return "You are organizing this tournament, you cannot join it."
                else:
                    return "You are not a member of this club, you cannot join the tournament."
            except:
                return "You are not a member of this club, you cannot join the tournament."
        else:
            return "You cannot join the tournament once the sign-up deadline has passed."

    def leave_tournament(self, user):
        current_datetime = timezone.make_aware(datetime.now(), timezone.utc)
        if current_datetime < self.deadline:
            try:
                tournament_participation = TournamentParticipation.objects.get(user=user, tournament=self)
                if tournament_participation:
                    tournament_participation.delete()
                    return ""
                else:
                    return "You are not signed-up for this tournament."
            except:
                return "You are not signed-up for this tournament."
        else:
            return "You cannot leave the tournament once the sign-up deadline has passed."


class TournamentParticipation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = ("user", "tournament")


class Match(models.Model):
    class MatchResultTypes(models.TextChoices):
        PENDING = 'P'
        WHITE_WIN = 'W'
        DRAW = 'D'
        BLACK_WIN = 'B'

    white_player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="+")
    black_player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="+")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False, related_name="matches")
    result = models.CharField(max_length=1, choices=MatchResultTypes.choices, default=MatchResultTypes.PENDING)
    stage = models.CharField(max_length=1, choices=Tournament.StageTypes.choices, default=Tournament.StageTypes.ELIMINATION)

    MATCH_AWARDS = {
        "WIN": 1,
        "DRAW": 0.5,
        "LOSS": 0
    }

    def get_match_award_for_user(self, user):
        if user != self.white_player and user != self.black_player:
            raise ValueError("User not participant in match")

        if self.result == self.MatchResultTypes.PENDING:
            return 0

        if self.result == self.MatchResultTypes.DRAW:
            return self.MATCH_AWARDS["DRAW"]
        else:
            if user == self.white_player:
                if self.result == self.MatchResultTypes.WHITE_WIN:
                    return self.MATCH_AWARDS["WIN"]
                else:
                    return self.MATCH_AWARDS["LOSS"]
            else:
                if self.result == self.MatchResultTypes.BLACK_WIN:
                    return self.MATCH_AWARDS["WIN"]
                else:
                    return self.MATCH_AWARDS["LOSS"]

class Group(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False, related_name="groups")
    players = models.ManyToManyField(User)
