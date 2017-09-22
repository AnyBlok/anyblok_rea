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
from decimal import Decimal as Dec


class TestContract(ReaTestCase):

    def test_contract_name(self):
        contract = self.utility.create_contract()
        self.assertEqual(str(contract)[:9], "CONTRACT_")
        self.assertEqual(contract.entity_type, 'Model.REA.Contract')

    def test_contract_with_commitment(self):
        contract = self.utility.create_contract()
        customer = self.utility.create_agent()
        resource = self.utility.create_resource()
        self.assert_(contract.add_increment_commitment(customer, resource, 1))
        self.assert_(contract.add_decrement_commitment(customer, resource, 1))

    def test_fulfill_commitment(self):
        contract = self.utility.create_contract()
        customer = self.utility.create_agent()
        resource = self.utility.create_resource()
        decr_commitment = contract.add_decrement_commitment(customer, resource, 1)
        incr_commitment = contract.add_increment_commitment(customer, resource, 1)
        self.assert_(incr_commitment.fulfill())
        self.assert_(decr_commitment.fulfill())
        self.assert_(incr_commitment.fulfilled)
        self.assert_(decr_commitment.fulfilled)

    def test_resource_value(self):
        contract = self.utility.create_contract()
        customer = self.utility.create_agent()
        pizza = self.utility.create_resource()
        cash = self.utility.create_resource()
        decr_commitment = contract.add_decrement_commitment(customer, pizza, 3)
        incr_commitment = contract.add_increment_commitment(customer, cash, Dec("22.50"))
        incr_commitment.fulfill()
        decr_commitment.fulfill()

        # WARNING: Why flush here ? ? ? we always use insert(). If we don't flush, event can't be query :(
        self.registry.flush()
        value = self.utility.get_resource_value(cash, customer)
        self.assertEqual(value, Dec("22.50"))
        value = self.utility.get_resource_value(pizza, customer)
        self.assertEqual(value, Dec("-3"))