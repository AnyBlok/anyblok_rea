# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
from anyblok.column import String, Integer, Decimal, DateTime, Boolean, Selection
from datetime import datetime
from anyblok.relationship import Many2One
from decimal import Decimal as decimalType


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.REA)
class Contract:
    """
    Contract is a collection of increment and decrement commitments and
    terms. Under the conditions specified by the terms, a contract can create
    additional commitments. Thus, the contract can specify what should happen
    if the commitments are not fulfilled. For example, a sales order is a
    contract containing commitments to sell goods and to receive payments.
    The terms of the sales order contract can specify penalties (additional
    commitments) if the goods or payments have not been received as promised.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """
    id = Integer(label="ID", primary_key=True)

    def __str__(self):
        return "CONTRACT_" + str(self.id)

    entity_type = String(label="Entity type")

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Contract, cls).define_mapper_args()
        if cls.__registry_name__ == Model.REA.Contract.__registry_name__:
            mapper_args.update({
                'polymorphic_identity': cls.__registry_name__,
                'polymorphic_on': cls.entity_type,
            })
        else:
            mapper_args.update({
                'polymorphic_identity': cls.__registry_name__,
            })
        return mapper_args

    def add_increment_commitment(self, provider, resource, value):
        return self.registry.REA.IncrementCommitment.insert(
            contract=self, provider=provider, resource=resource, value=value)

    def add_decrement_commitment(self, recipient, resource, value):
        return self.registry.REA.DecrementCommitment.insert(
            contract=self, resource=resource, recipient=recipient, value=value)


@register(Model)
class IncrementCommitment:
    contract = Many2One(label="Contract", model=Model.REA.Contract,
                        one2many='commitments_increment_ids', nullable=True)


@register(Model)
class DecrementCommitment:
    contract = Many2One(label="Contract", model=Model.REA.Contract,
                        enable_typechecks=False,
                        one2many='commitments_decrement_ids', nullable=True)