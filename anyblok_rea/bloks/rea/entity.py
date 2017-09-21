# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import String, Integer, Decimal, DateTime
from datetime import datetime
from anyblok.relationship import Many2One
from decimal import Decimal as decimalType


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Entity:

    id = Integer(primary_key=True)

    entity_type = String(label="Entity type")

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Entity, cls).define_mapper_args()
        if cls.__registry_name__ == Model.Entity.__registry_name__:
            mapper_args.update({
                'polymorphic_identity': cls.__registry_name__,
                'polymorphic_on': cls.entity_type,
            })
        else:
            mapper_args.update({
                'polymorphic_identity': cls.__registry_name__,
            })
        return mapper_args


@register(Model)
class Resource(Model.Entity):
    """
    Economic Resource is a thing that is scarce, and has utility for
    economic agents, and is something users of business applications
    want to plan, monitor, and control. Examples of economic resources
    are products and services, money, raw materials, labor, tools, and
    services the enterprise uses.

    *******************************************************************

    Just like agents, Resources contain an ID and Name. In addition a re-
    source has a Value which is defined as the value in US dollars of a single
    unit of the resource, i.e., the price of a single pizza

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """

    id = Integer(primary_key=True, foreign_key=Model.Entity.use('id'))


@register(Model)
class Agent(Model.Entity):
    """
    Economic Agent is an individual or organization capable of having
    control over economic resources, and transferring or receiving the control
    to or from other individuals or organizations. Examples of economic agents
    are customers, vendors, employees, and enterprises. The enterprise is an
    economic agent from whose perspective we create the REA model.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """

    id = Integer(primary_key=True, foreign_key=Model.Entity.use('id'))


@register(Model)
class IncrementEvent(Model.Entity):
    """
    Economic Event represents either an increment or a decrement in the
    value of economic resources that are under the control of the enterprise.
    Some economic events occur instantaneously, such as sales of goods; some
    occur over time, such as rentals, labor acquisition, and provision and use
    of services.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """
    id = Integer(primary_key=True, foreign_key=Model.Entity.use('id'))

    provider = Many2One(label="Agent provider", model=Model.Agent, nullable=False)

    resource = Many2One(label='Resource Inflow', model=Model.Resource, nullable=False)

    value = Decimal(label="increment value", default=decimalType(0))

    date = DateTime(label="Event Date", default=lambda **kwargs: datetime.now())


@register(Model)
class DecrementEvent(Model.Entity):
    """
    Economic Event represents either an increment or a decrement in the
    value of economic resources that are under the control of the enterprise.
    Some economic events occur instantaneously, such as sales of goods; some
    occur over time, such as rentals, labor acquisition, and provision and use
    of services.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """

    id = Integer(primary_key=True, foreign_key=Model.Entity.use('id'))

    recipient = Many2One(label="Agent recipient", model=Model.Agent, nullable=False)

    resource = Many2One(label='Resource Outflow', model=Model.Resource, nullable=False)

    value = Decimal(label="decrement value", default=decimalType(0))

    date = DateTime(label="Event Date", default=lambda **kwargs: datetime.now())
