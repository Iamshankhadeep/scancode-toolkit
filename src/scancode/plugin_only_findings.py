#
# Copyright (c) 2018 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import unicode_literals

from plugincode.output_filter import OutputFilterPlugin
from plugincode.output_filter import output_filter_impl
from scancode import CommandLineOption
from scancode import OUTPUT_FILTER_GROUP


@output_filter_impl
class OnlyFindings(OutputFilterPlugin):
    """
    Filter files or directories without scan findings for the requested scans.
    """

    options = [
        CommandLineOption(('--only-findings',), is_flag=True,
            help='Only return files or directories with findings for the '
                 'requested scans. Files and directories without findings are '
                 'omitted (file information is not treated as findings).',
            help_group=OUTPUT_FILTER_GROUP)
    ]

    def is_enabled(self):
        return self.is_command_option_enabled('only_findings')

    def process_resource(self, resource):
        """
        Return True if `resource` has finding e.g. if they have no scan data, no
        errors.
        """
        return has_findings(resource)


def has_findings(resource):
    """
    Return True if this resource has findings.
    """
    return any(resource.get_scans().values() + resource.errors)
