from django.contrib import admin

from player.models import Plans, Player, Wallet , Profile

# Register your models here.
admin.site.register(Player)
admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Plans)

