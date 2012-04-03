#!/usr/bin/python
#
# Copyright 2012 Jonathan Anderson
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

import collections
import re

def author_refs(refs):
	""" Convert a collection of author:id references into an author->ids map. """
	result = collections.defaultdict(list)
	for ref in refs:
		tokens = ref.split(':')
		if len(tokens) == 2:
			(author, id) = tokens
			result[author].append(id)
		else:
			result['unknown'].append(tokens[0])

	return result

def commasep(s):
	""" De-quote and split a comma-separated line (like a LyX citation). """
	if re.match('^".*"$', s): s = s[1:-1]
	return frozenset([ i.strip() for i in s.split(',') ])

