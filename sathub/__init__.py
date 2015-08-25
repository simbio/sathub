# -*- coding: utf-8 -*-
#
# sathub/__init__.py
#
# Copyright 2015 Base4 Sistemas Ltda ME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__version__ = '0.1'

from sathub.comum.config import conf as sathubconf
from satcfe.config import conf as satcfeconf

satcfeconf.codigo_ativacao = sathubconf.codigo_ativacao
sathubconf.descrever()

from flask import Flask

class MyConfig(object):
	RESTFUL_JSON = {'encoding': 'iso-8859-1'}

app = Flask(__name__)
app.config.from_object(MyConfig)

import sathub.api
import sathub.views
