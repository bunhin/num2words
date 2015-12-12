# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

class Num2WordsDETest(TestCase):
    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(7, ordinal=True, lang='de'), "siebte")
        self.assertEqual(num2words(8, ordinal=True, lang='de'), "achte")
        self.assertEqual(num2words(12, ordinal=True, lang='de'), "zwölfte")
        self.assertEqual(num2words(17, ordinal=True, lang='de'), "siebzehnte")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(num2words(81, ordinal=True, lang='de'), "einundachtzigste")

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(num2words(100, ordinal=True, lang='de'), "hundertste")
        self.assertEqual(num2words(1000, ordinal=True, lang='de'), "tausendste")
        self.assertEqual(num2words(4000, ordinal=True, lang='de'), "viertausendste")
        self.assertEqual(num2words(2000000, ordinal=True, lang='de'), "zwei millionenste")
        self.assertEqual(num2words(5000000000, ordinal=True, lang='de'), "fünf milliardenste")