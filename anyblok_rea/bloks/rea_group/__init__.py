# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.blok import Blok


class REAGroupBlok(Blok):
    """ Group pattern REA blok """
    version = '0.0.1'

    required = [
        'rea',
    ]

    @classmethod
    def import_declaration_module(cls):
        from . import entity
        from . import utility

    @classmethod
    def reload_declaration_module(cls, reload):
        from . import entity
        reload(entity)
        from . import utility
        reload(utility)