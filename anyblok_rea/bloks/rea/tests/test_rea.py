# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok_rea.bloks.rea.tests.reatestcase import ReaTestCase


class TestRea(ReaTestCase):

    def test_create_agent(self):
        agent = self.utility.create_agent()
        self.assert_(agent)

    def test_create_resource(self):
        resource = self.utility.create_resource()
        self.assert_(resource)

    def test_create_increment_event(self):
        agent = self.utility.create_agent()
        resource = self.utility.create_resource()
        inc_event = self.utility.create_increment_event(agent, resource)
        dec_event = self.utility.create_decrement_event(agent, resource)
        self.assert_(inc_event)
        self.assert_(dec_event)