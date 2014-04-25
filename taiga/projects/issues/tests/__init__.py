# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db.models.loading import get_model


def create_issue(id, owner, project, milestone=None, save=True):
    model = get_model("issues", "Issue")

    instance = model(
       subject="Issue {0}".format(id),
       description="The issue description.",
       project=project,
       milestone=milestone,
       status=project.issue_statuses.all()[0],
       severity=project.severities.all()[0],
       priority=project.priorities.all()[0],
       type=project.issue_types.all()[0],
       owner=owner
    )

    if save:
        instance.save()
    return instance
