from periph.wb_crc import crc_define
from periph.wb_rng import rng_define
from periph.wb_pwr import pwr_define
from periph.wb_bkp import bkp_define
from periph.wb_gpio import afio_define, gpioa_define, gpiob_define, gpioc_define, gpiod_define
from periph.wb_sys import sys_define
from periph.wb_rcc import rcc_define
from periph.wb_exti import exti_define
from periph.wb_anctl import anctl_define
from periph.wb_adc import adc_define
from periph.wb_tim import tim1_define, tim2_define, tim3_define, tim4_define
from periph.wb_led import led_define
from periph.wb_rtc import rtc_define
from periph.wb_dmac import dmac1_define, dmac2_define
from periph.wb_wwdg import wwdg_define
from periph.wb_iwdg import iwdg_define
from periph.wb_dbgmcu import dbgmcu_define
from periph.wb_sfm import sfm_define
from periph.wb_cache import cache_define
from periph.wb_i2c import i2c1_define, i2c2_define
from periph.wb_spi import spis1_define, spim2_define, spis2_define
from periph.wb_fmc import fmc_define
from periph.wb_qspi import qspi_define
from periph.wb_iso import iso_define
from periph.wb_uart import uart1_define,uart2_define,uart3_define
from periph.wb_usb import usb_define
from periph.wb_iis import iis_define

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

        "peripheral_13": adc_define,

        "peripheral_14": tim1_define,
        "peripheral_15": tim2_define,
        "peripheral_16": tim3_define,
        "peripheral_17": tim4_define,

        "peripheral_18": led_define,

        "peripheral_19": rtc_define,

        "peripheral_20": dmac1_define,
        "peripheral_21": dmac2_define,

        "peripheral_22": wwdg_define,

        "peripheral_23": iwdg_define,

        "peripheral_24": dbgmcu_define,

        "peripheral_25": sfm_define,

        "peripheral_26": cache_define,

        "peripheral_27": i2c1_define,
        "peripheral_28": i2c2_define,

        "peripheral_29": spis1_define,
        "peripheral_30": spim2_define,
        "peripheral_31": spis2_define,

        "peripheral_32": fmc_define,

        "peripheral_33": qspi_define,

        "peripheral_34": iso_define,

        "peripheral_35": uart1_define,
        "peripheral_36": uart2_define,
        "peripheral_37": uart3_define,

        "peripheral_38": usb_define,

        "peripheral_39": iis_define,

    },
}
