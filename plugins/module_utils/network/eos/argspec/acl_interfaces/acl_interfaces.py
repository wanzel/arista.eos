#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# pylint: skip-file

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the eos_acl_interfaces module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Acl_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the eos_acl_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "access_groups": {
                    "elements": "dict",
                    "options": {
                        "acls": {
                            "elements": "dict",
                            "options": {
                                "direction": {
                                    "required": True,
                                    "choices": ["in", "out"],
                                    "type": "str",
                                },
                                "name": {"required": True, "type": "str"},
                            },
                            "type": "list",
                        },
                        "afi": {
                            "required": True,
                            "choices": ["ipv4", "ipv6"],
                            "type": "str",
                        },
                    },
                    "type": "list",
                },
                "name": {"required": True, "type": "str"},
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "parsed",
                "rendered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
