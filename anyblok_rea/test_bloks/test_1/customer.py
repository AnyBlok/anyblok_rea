# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model
Agent = Model.REA.Agent


@register(Model)
class Customer(Agent):
    id = Integer(primary_key=True,
                 foreign_key=Agent.use('id').options(ondelete='cascade'))
    name = String(nullable=False)
