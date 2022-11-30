BKP_RTCCR = {
    "name": "RTCCR",
    "displayName": "RTCCR",
    "description": "RTC signal output control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CAL",
            "description": "RTC clock calibration value",
            "bitOffset": "0",
            "bitWidth": "7",
        },
        "field_1": {
            "name": "COO",
            "description": "RTC clock calibration output enable",
            "bitOffset": "7",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "ASOE",
            "description": "RTC alarm or second signal output enable",
            "bitOffset": "8",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "ASOS",
            "description": "RTC output selection",
            "bitOffset": "9",
            "bitWidth": "1",
        }
    }
}

BKP_CR = {
    "name": "CR",
    "displayName": "CR",
    "description": "Tamper pin control register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "TPE",
            "description": "TAMPER detection enable",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "TPAL",
            "description": "TAMPER pin active level",
            "bitOffset": "1",
            "bitWidth": "1",
        }
    }
}

BKP_CSR = {
    "name": "CSR",
    "displayName": "CSR",
    "description": "Tamper control and status register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CTE",
            "description": "Tamper event reset",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "CTI",
            "description": "Tamper interrupt reset",
            "bitOffset": "1",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "TPIE",
            "description": "Tamper interrupt enable",
            "bitOffset": "2",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "TEF",
            "description": "Tamper event flag",
            "bitOffset": "8",
            "bitWidth": "1",
        },
        "field_4": {
            "name": "TIF",
            "description": "Tamper interrupt flag",
            "bitOffset": "9",
            "bitWidth": "1",
        }
    }
}

# 有争议
BKP_DR = {
    "dim": "21",
    "dimIncrement": "4",
    "dimIndex": "1-21",
    "name": "DR%s",
    "displayName": "DR%s",
    "description": "Backup data register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

BKP_BDCR = {
    "name": "BDCR",
    "displayName": "BDCR",
    "description": "Backup domain control register",
    "addressOffset": "0x100",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "LSEON",
            "description": "External low-speed oscillator enable Set and cleared by software",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "LSERDY",
            "description": "External low-speed oscillator ready",
            "bitOffset": "1",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "LSEBYP",
            "description": "External Low-speed oscillator bypass",
            "bitOffset": "2",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "RTCSEL",
            "description": "RTC clock source selection",
            "bitOffset": "8",
            "bitWidth": "2",
        },
        "field_4": {
            "name": "RTCEN",
            "description": "RTC clock enable control, software set or clear this bit",
            "bitOffset": "15",
            "bitWidth": "1",
        },
    }
}

bkp_define = {
    "name": "BKP",
    "description": "Backup registers",
    "groupName": "BKP",
    "baseAddress": "0x40015C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": BKP_RTCCR,
        "register_1": BKP_CR,
        "register_2": BKP_CSR,
        "register_3": BKP_DR,
        "register_4": BKP_BDCR,
    }
}
