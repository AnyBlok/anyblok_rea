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
    def create_group(cls):
        return cls.registry.REA.Group.insert()

    @classmethod
    def add_entities_to_group(cls, group, entities):
        for entity in entities:
            group.entities.append(entity)