#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright (C) 2008 GestorPsi
     
    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

'''
    script to create receive Fortnightly
    create a new receive for each covenant
'''

import header

from datetime import datetime

from gestorpsi.financial.models import Receive
from gestorpsi.referral.models import Referral

'''
    Covenant.charge = 11 : Fortnightlyt
'''
covenant_charge = 11

print
print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # "
print "# Payment - Creating covenant Fortnightlyt"

# main code
for r in Referral.objects.filter(covenant__isnull=False, covenant__charge=covenant_charge, referraldischarge__isnull=True): 

    '''
        filter for all referall that don't have discharge
    '''
    
    # create a receive for each covenant of referral
    for c in r.covenant.filter(charge=covenant_charge):

        # new
        receive = Receive()
        receive.created = datetime.today()
        receive.launch_date = datetime.today()
        receive.name = c.name
        receive.price = c.price
        receive.off = 0
        receive.total = c.price
        receive.covenant_charge = c.charge
        receive.covenant_id = c.id

        # clear all
        receive.covenant_payment_way_options = ''
        for pw in c.payment_way.all():
            x = "(%s,'%s')," % ( pw.id , pw.name ) # need be a dict
            receive.covenant_payment_way_options += x

        # add referral
        receive.referral = r

        # save
        receive.save()

        print u"--- %s " % receive
