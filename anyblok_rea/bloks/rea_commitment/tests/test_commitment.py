# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok_rea.bloks.rea.tests.reatestcase import ReaTestCase


class TestCommitment(ReaTestCase):
    def test_create_commitment(self):
        agent = self.utility.create_agent()
        resource = self.utility.create_resource()
        inc_commit = self.utility.create_increment_commitment(agent, resource)
        dec_commit = self.utility.create_decrement_commitment(agent, resource)
        self.assert_(inc_commit)
        self.assert_(dec_commit)

    def test_fulfill_commitment(self):
        agent = self.utility.create_agent()
        resource = self.utility.create_resource()
        inc_commit = self.utility.create_increment_commitment(agent, resource)
        dec_commit = self.utility.create_decrement_commitment(agent, resource)
        inc_event = inc_commit.fulfill()
        dec_event = dec_commit.fulfill()
        self.assert_(inc_event)
        self.assert_(dec_event)