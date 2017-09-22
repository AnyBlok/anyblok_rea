# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import DBTestCase


class TestAgent(DBTestCase):

    blok_entry_points = ('bloks', 'test_bloks')

    def test_install_test1_create_customer(self):
        registry = self.init_registry(None)
        registry.upgrade(install=('rea_test_1',))
        customer = registry.Agent.Customer.insert(name="My customer")
        self.assertIs(customer, registry.Entity.query().one())

    def test_install_test1_create_pizza(self):
        registry = self.init_registry(None)
        registry.upgrade(install=('rea_test_1',))
        pizza = registry.Resource.Pizza.insert(name="4 fromages")
        self.assertIs(pizza, registry.Entity.query().one())
