# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok_rea.bloks.rea.tests.reatestcase import ReaTestCase


class TestGroup(ReaTestCase):

    def test_create_group(self):
        group = self.utility.create_group()
        self.assert_(group)

    def test_add_entities_to_group(self):
        group = self.utility.create_group()
        self.assert_(group)
        agent = self.utility.create_agent()
        resource = self.utility.create_resource()
        resource2 = self.utility.create_resource()
        self.utility.add_entities_to_group(group, [agent, resource, resource2])
        self.assertEqual(len(group.entities), 3)