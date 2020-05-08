#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x10-api_and_shell.json
# Device ID:          0x10
# Device Name:        api_and_shell
# Timestamp:          05/07/2020 @ 14:36:23.262486 (UTC)

from sphero_sdk.common.enums.api_and_shell_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def echo(data, target, timeout): 
    return { 
        'did': DevicesEnum.api_and_shell,
        'cid': CommandsEnum.echo,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='data',
                data_type='uint8_t',
                index=0,
                value=data,
                size=16
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='data',
                data_type='uint8_t',
                index=0,
                size=16,
            ),
        ]
    }
