from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator


Ingener='Ingener'
Call_operator='Call operator'
Ceo='CEO'
USER_ROLES = (
    (Ingener, Ingener),
    (Call_operator, Call_operator),
    (Ceo, Ceo),
)

Came='Came'
Gone='Gone'
CHECKING_STATUS = (
    (Came, Came),
    (Gone, Gone)
)

Active='Active'
Passive='Passive'
USER_STATUS = (
    (Active, Active),
    (Passive, Passive)
)

class UserModel(models.Model):
    
    finger_id = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3),
        RegexValidator(r'^\d+$', message="FINGER ID must be numeric.")],
        unique=True,  
        primary_key=True,)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(choices=USER_ROLES, null=True, blank=True, max_length=255, default=Ingener)
    status = models.CharField(max_length=10, choices=USER_STATUS, default=Active)
    def __str__(self):
        return f"{self.full_name}"
    
class ChechingModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='time')
    checking_status = models.CharField(choices=CHECKING_STATUS, max_length=7)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"User ID: {self.user.finger_id} Name: {self.time}"