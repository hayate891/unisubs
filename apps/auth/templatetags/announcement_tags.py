# Amara, universalsubtitles.org
#
# Copyright (C) 2013 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

from django import template

from auth.models import Announcement

register = template.Library()

@register.inclusion_tag('auth/_announcement.html', takes_context=True)
def announcement(context):
    return {
        'announcement': Announcement.last(),
        'add_content_class': False,
    }

@register.inclusion_tag('auth/_announcement.html', takes_context=True)
def new_announcement(context):
    return {
        'announcement': Announcement.last(),
        'add_content_class': True,
    }
