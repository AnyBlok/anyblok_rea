# This file is a part of the AnyBlok REA project
#
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
from anyblok.relationship import Many2Many
from anyblok.column import String, Integer


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin



@register(Model.REA)
class Group(Model.REA.Entity):
    """
    Introduce a group as a structural element of the REA application model.
    An REA entity group represents a set of REA entities that have something
    in common. The group entity is related to its members by a grouping rela-
    tionship. Members of the group can be any entity in the REA model: re-
    sources, events, agents, commitments, claims, contracts, types, or other
    groups.

    # Model-Driven Design Using Business Patterns
    # Authors: Hruby, Pavel
    # ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    # ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York
    """
    id = Integer(primary_key=True, foreign_key=Model.REA.Entity.use('id'))
    name = String()
    entities = Many2Many(model=Model.REA.Entity)