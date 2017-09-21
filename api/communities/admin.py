from django.contrib import admin
from api.communities.models import Community, CommunityPhoto

admin.site.register([Community, CommunityPhoto])
