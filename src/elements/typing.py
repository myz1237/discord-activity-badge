"""
Copyright 2021 Janrey "CodexLink" Licas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


if __name__ == "__main__":
    from .exceptions import IsolatedExecNotAllowed

    raise IsolatedExecNotAllowed

from typing import NewType as _N

HttpsURL = _N("HttpsURL", str)
HttpsURLPath = _N("HttpsURLPath", str)
Base64 = _N("Base64", str)
ResolvedHTTPResponse = _N("ResolvedHTTPResponse", dict)
BadgeStructure = _N("BadgeStructure", str)
RegExp = _N("RegExp", str)
ColorHEX = _N("ColorHEX", str)
ActivityDictName = _N("ActivityDictName", str)