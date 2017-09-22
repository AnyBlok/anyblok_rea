# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from sqlalchemy.sql import func
from decimal import Decimal as Dec


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Utility:

    @classmethod
    def create_resource(cls):
        return cls.registry.REA.Resource.insert()

    @classmethod
    def create_agent(cls):
        return cls.registry.REA.Agent.insert()

    @classmethod
    def get_resource_value(cls, resource, agent):
        """ Get all event value about an agent and a resource.

        :param agent: Which agent is used to compute resource value
        :param resource: What resource is used to compute resource value
        :return: value
        """
        decrement_event = cls.registry.DecrementEvent
        increment_event = cls.registry.IncrementEvent

        value_incre = increment_event.query(func.sum(increment_event.value).label('total_value')).\
            filter(increment_event.provider == agent).\
            filter(increment_event.resource == resource).\
            first()
        value_decre = decrement_event.query(func.sum(decrement_event.value).label('total_value')).\
            filter(decrement_event.recipient == agent).\
            filter(decrement_event.resource == resource).\
            first()

        debit = value_incre[0] if value_incre[0] is not None else Dec(0)
        credit = value_decre[0] if value_decre[0] is not None else Dec(0)

        return debit - credit

    @classmethod
    def create_decrement_event(cls, agent, resource):
        return cls.registry.REA.DecrementEvent.insert(recipient=agent, resource=resource)

    @classmethod
    def create_increment_event(cls, agent, resource):
        return cls.registry.REA.IncrementEvent.insert(provider=agent, resource=resource)
