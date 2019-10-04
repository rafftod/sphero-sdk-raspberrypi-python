#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x18-sensors.json
# Device ID:          0x18
# Device Name:        sensor
# Timestamp:          10/02/2019 @ 17:09:49.589216 (UTC)

from enum import IntEnum


__all__ = ['MotorIndexesEnum',
           'ThermalProtectionStatusEnum',
           'StreamingDataSizesEnum',
           'StreamingServiceStatesEnum',
           'GyroMaxFlagsBitmask',
           'LocatorFlagsBitmask',
           'InfraredSensorLocationsBitmask']


class CommandsEnum(IntEnum): 
    enable_gyro_max_notify = 0x0F
    gyro_max_notify = 0x10
    reset_locator_x_and_y = 0x13
    set_locator_flags = 0x17
    get_bot_to_bot_infrared_readings = 0x22
    get_rgbc_sensor_values = 0x23
    magnetometer_calibrate_to_north = 0x25
    magnetometer_north_yaw_notify = 0x26
    start_robot_to_robot_infrared_broadcasting = 0x27
    start_robot_to_robot_infrared_following = 0x28
    stop_robot_to_robot_infrared_broadcasting = 0x29
    robot_to_robot_infrared_message_received_notify = 0x2C
    get_ambient_light_sensor_value = 0x30
    stop_robot_to_robot_infrared_following = 0x32
    start_robot_to_robot_infrared_evading = 0x33
    stop_robot_to_robot_infrared_evading = 0x34
    enable_color_detection_notify = 0x35
    color_detection_notify = 0x36
    get_current_detected_color_reading = 0x37
    enable_color_detection = 0x38
    configure_streaming_service = 0x39
    start_streaming_service = 0x3A
    stop_streaming_service = 0x3B
    clear_streaming_service = 0x3C
    streaming_service_data_notify = 0x3D
    enable_robot_infrared_message_notify = 0x3E
    send_infrared_message = 0x3F
    motor_current_notify = 0x40
    enable_motor_current_notify = 0x41
    get_motor_temperature = 0x42
    get_motor_thermal_protection_status = 0x4B
    enable_motor_thermal_protection_status_notify = 0x4C
    motor_thermal_protection_status_notify = 0x4D


class MotorIndexesEnum(IntEnum):
    left_motor_index = 0
    right_motor_index = 1


class ThermalProtectionStatusEnum(IntEnum):
    ok = 0
    warn = 1
    critical = 2


class StreamingDataSizesEnum(IntEnum):  # TODO: should we split out the two sets of data here?
    eight_bit = 0x00
    sixteen_bit = 0x01
    thirty_two_bit = 0x02
    uint_8_max = 255
    uint_16_max = 65535
    uint_32_max = 4294967295
    int_32_min = -2147483648
    int_32_max = 2147483647
    int_64_min = -9223372036854775808
    int_64_max = 9223372036854775807


class StreamingServiceStatesEnum(IntEnum):  # TODO: this isn't autogen'd
    Unknown = 0  #: 
    Stop = 1  #: 
    Start = 2  #: 
    Restart = 3  #: 


class GyroMaxFlagsBitmask(IntEnum):
    none = 0
    max_plus_x = 1
    max_minus_x = 2
    max_plus_y = 4
    max_minus_y = 8
    max_plus_z = 16
    max_minus_z = 32


class LocatorFlagsBitmask(IntEnum):
    none = 0
    auto_calibrate = 1


class InfraredSensorLocationsBitmask(IntEnum):
    none = 0
    front_left = 0x000000FF
    front_right = 0x0000FF00
    back_right = 0x00FF0000
    back_left = 0xFF000000
