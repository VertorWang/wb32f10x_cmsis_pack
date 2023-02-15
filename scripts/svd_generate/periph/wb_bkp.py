BKP_RTCCR = {
    "name": "RTCCR",
    "displayName": "RTCCR",
    "description": "RTC signal output control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CAL",
            "description": "RTC clock calibration value",
            "bitRange": "[6:0]",
        },
        "field_1": {
            "name": "COO",
            "description": "RTC clock calibration output enable",
            "bitRange": "[7:7]",
        },
        "field_2": {
            "name": "ASOE",
            "description": "RTC alarm or second signal output enable",
            "bitRange": "[8:8]",
        },
        "field_3": {
            "name": "ASOS",
            "description": "RTC output selection",
            "bitRange": "[9:9]",
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
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TPE",
            "description": "TAMPER detection enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TPAL",
            "description": "TAMPER pin active level",
            "bitRange": "[1:1]",
        }
    }
}

BKP_CSR = {
    "name": "CSR",
    "displayName": "CSR",
    "description": "Tamper control and status register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CTE",
            "description": "Tamper event reset",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CTI",
            "description": "Tamper interrupt reset",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TPIE",
            "description": "Tamper interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TEF",
            "description": "Tamper event flag",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "TIF",
            "description": "Tamper interrupt flag",
            "bitRange": "[9:9]",
        }
    }
}

BKP_DR1 = {
    "name": "DR1",
    "displayName": "DR1",
    "description": "Backup data 1 register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR2 = {
    "name": "DR2",
    "displayName": "DR2",
    "description": "Backup data 2 register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR3 = {
    "name": "DR3",
    "displayName": "DR3",
    "description": "Backup data 3 register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR4 = {
    "name": "DR4",
    "displayName": "DR4",
    "description": "Backup data 4 register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR5 = {
    "name": "DR5",
    "displayName": "DR5",
    "description": "Backup data 5 register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR6 = {
    "name": "DR6",
    "displayName": "DR6",
    "description": "Backup data 6 register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR7 = {
    "name": "DR7",
    "displayName": "DR7",
    "description": "Backup data 7 register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR8 = {
    "name": "DR8",
    "displayName": "DR8",
    "description": "Backup data 8 register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR9 = {
    "name": "DR9",
    "displayName": "DR9",
    "description": "Backup data 9 register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR10 = {
    "name": "DR10",
    "displayName": "DR10",
    "description": "Backup data 10 register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR11 = {
    "name": "DR11",
    "displayName": "DR11",
    "description": "Backup data 11 register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR12 = {
    "name": "DR12",
    "displayName": "DR12",
    "description": "Backup data 12 register",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR13 = {
    "name": "DR13",
    "displayName": "DR13",
    "description": "Backup data 13 register",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR14 = {
    "name": "DR14",
    "displayName": "DR14",
    "description": "Backup data 14 register",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR15 = {
    "name": "DR15",
    "displayName": "DR15",
    "description": "Backup data 15 register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR16 = {
    "name": "DR16",
    "displayName": "DR16",
    "description": "Backup data 16 register",
    "addressOffset": "0x4C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR17 = {
    "name": "DR17",
    "displayName": "DR17",
    "description": "Backup data 17 register",
    "addressOffset": "0x50",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR18 = {
    "name": "DR18",
    "displayName": "DR18",
    "description": "Backup data 18 register",
    "addressOffset": "0x54",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR19 = {
    "name": "DR19",
    "displayName": "DR19",
    "description": "Backup data 19 register",
    "addressOffset": "0x58",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR20 = {
    "name": "DR20",
    "displayName": "DR20",
    "description": "Backup data 20 register",
    "addressOffset": "0x5C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
        }
    }
}

BKP_DR21 = {
    "name": "DR21",
    "displayName": "DR21",
    "description": "Backup data 21 register",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Backup data",
            "bitRange": "[31:0]",
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
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSEON",
            "description": "External low-speed oscillator enable Set and cleared by software",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "LSERDY",
            "description": "External low-speed oscillator ready",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSEBYP",
            "description": "External Low-speed oscillator bypass",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RTCSEL",
            "description": "RTC clock source selection",
            "bitRange": "[9:8]",
        },
        "field_4": {
            "name": "RTCEN",
            "description": "RTC clock enable control, software set or clear this bit",
            "bitRange": "[15:15]",
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
    "interrupt_0": {
        "name": "Tamper",
        "description": "Tamper interrupt",
        "value": "2",
    },
    "registers": {
        "register_0 ": BKP_RTCCR,
        "register_1 ": BKP_CR,
        "register_2 ": BKP_CSR,
        "register_3 ": BKP_DR1,
        "register_4 ": BKP_DR2,
        "register_5 ": BKP_DR3,
        "register_6 ": BKP_DR4,
        "register_7 ": BKP_DR5,
        "register_8 ": BKP_DR6,
        "register_9 ": BKP_DR7,
        "register_10": BKP_DR8,
        "register_11": BKP_DR9,
        "register_12": BKP_DR10,
        "register_13": BKP_DR11,
        "register_14": BKP_DR12,
        "register_15": BKP_DR13,
        "register_16": BKP_DR14,
        "register_17": BKP_DR15,
        "register_18": BKP_DR16,
        "register_19": BKP_DR17,
        "register_20": BKP_DR18,
        "register_21": BKP_DR19,
        "register_22": BKP_DR20,
        "register_23": BKP_DR21,
        "register_24": BKP_BDCR,
    }
}
