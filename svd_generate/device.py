from periph.wb_crc import crc_define
from periph.wb_rng import rng_define
from periph.wb_pwr import pwr_define
from periph.wb_bkp import bkp_define
from periph.wb_gpio import afio_define, gpioa_define, gpiob_define, gpioc_define, gpiod_define
from periph.wb_sys import sys_define
from periph.wb_rcc import rcc_define
from periph.wb_exti import exti_define
from periph.wb_anctl import anctl_define

dataSvd = {
    "name": "WB32F10x",
    "version": "1.2",
    "description": "WB32F10x",
    "licenseText": "ARM Limited (ARM) is supplying this software for use with Cortex-M\n"
                   "    processor based microcontroller, but can be equally used for other\n"
                   "    suitable  processor architectures. This file can be freely distributed.\n"
                   "    Modifications to this file shall be clearly marked.\n\n"
                   "    THIS SOFTWARE IS PROVIDED \"AS IS\".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED\n"
                   "    OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF\n"
                   "    MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.\n"
                   "    ARM SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL, OR\n"
                   "    CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.",
    "cpu": {
        "name": "CM3",
        "revision": "r2p0",
        "endian": "little",
        "mpuPresent": "true",
        "fpuPresent": "false",
        "nvicPrioBits": "4",
        "vendorSystickConfig": "false",
    },
    "addressUnitBits": "8",
    "width": "32",
    "size": "0x20",
    "resetValue": "0x0",
    "resetMask": "0xFFFFFFFF",
    "peripherals": {
        "peripheral_0": crc_define,

        "peripheral_1": rng_define,

        "peripheral_2": pwr_define,

        "peripheral_3": bkp_define,

        "peripheral_4": afio_define,

        "peripheral_5": gpioa_define,
        "peripheral_6": gpiob_define,
        "peripheral_7": gpioc_define,
        "peripheral_8": gpiod_define,

        "peripheral_9": sys_define,

        "peripheral_10": rcc_define,

        "peripheral_11": exti_define,

        "peripheral_12": anctl_define,
    },
}
