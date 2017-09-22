# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
from anyblok.column import String, Integer, Decimal, Boolean
from anyblok.relationship import Many2One
from decimal import Decimal as decimalType


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.REA)
class IncrementCommitment(Model.REA.Entity):
    """
    Commitment is a promise or obligation of economic agents to perform
    an economic event in the future. For example, line items on a sales order
    represent commitments to sell goods.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """
    id = Integer(primary_key=True, foreign_key=Model.REA.Entity.use('id'))

    provider = Many2One(label="Agent provider", model=Model.REA.Agent, nullable=False)

    resource = Many2One(label="Reservation Resource", model=Model.REA.Resource, nullable=False)

    value = Decimal(label="Value increment", default=decimalType(0))

    fulfilled = Boolean(label="Is Fulfilled", default=False)

    def fulfill(self):
        """
        :return: True if commitment is fulfilled
        """
        if not self.fulfilled:
            self.registry.REA.IncrementEvent.create_event_from_commitment(self)
            self.fulfilled = True
            return True
        return False


@register(Model.REA)
class DecrementCommitment(Model.REA.Entity):
    """
    Commitment is a promise or obligation of economic agents to perform
    an economic event in the future. For example, line items on a sales order
    represent commitments to sell goods.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """
    id = Integer(primary_key=True, foreign_key=Model.REA.Entity.use('id'))

    recipient = Many2One(label="Agent recipient", model=Model.REA.Agent, nullable=False)

    resource = Many2One(label="Reservation Resource", model=Model.REA.Resource, nullable=False)

    value = Decimal(label="Value decrement", default=decimalType(0))

    fulfilled = Boolean(label="Is Fulfilled", default=False)

    def fulfill(self):
        """
        :return: True if commitment is fulfilled
        """
        if not self.fulfilled:
            self.registry.REA.DecrementEvent.create_event_from_commitment(self)
            self.fulfilled = True
            return True
        return False


@register(Model.REA)
class IncrementEvent:

    fulfillment = Many2One(label="FulFilled commitment", model=Model.REA.IncrementCommitment)

    @classmethod
    def create_event_from_commitment(cls, commitment):
        return cls.registry.REA.IncrementEvent.insert(
            resource=commitment.resource, value=commitment.value, provider=commitment.provider,
            fulfillment=commitment)


@register(Model.REA)
class DecrementEvent:

    fulfillment = Many2One(label="FulFilled commitment", model=Model.REA.DecrementCommitment)

    @classmethod
    def create_event_from_commitment(cls, commitment):
        return cls.registry.REA.DecrementEvent.insert(
            resource=commitment.resource, value=commitment.value, recipient=commitment.recipient,
            fulfillment=commitment)
