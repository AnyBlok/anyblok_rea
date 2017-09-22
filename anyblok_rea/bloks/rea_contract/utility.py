# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Utility:

    @classmethod
    def create_contract(cls):
        return cls.registry.REA.Contract.insert()

    @classmethod
    def get_provider_contract(cls, agent):
        """
        :param agent: Economic Agent
        :return: SA Collections of contract where the agent is provider
        """
        return cls.registry.REA.Contract.query().join(
            cls.registry.REA.Contract.commitments_increment_ids).filter(
                cls.registry.REA.IncrementCommitment.provider == agent).all()

    @classmethod
    def get_receiver_contract(cls, agent):
        """
        :param agent: Economic Agent
        :return: SA Collections of contract where the agent is receiver
        """
        return cls.registry.REA.Contract.query().join(
            cls.registry.REA.Contract.commitments_decrement_ids).filter(
                cls.registry.REA.DecrementCommitment.recipient == agent).all()