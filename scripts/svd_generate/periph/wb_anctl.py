ANCTL_BGCR2 = {
    "name": "BGCR2",
    "displayName": "BGCR2",
    "description": "BG control register 2",
    "addressOffset": "0x01C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TEMPOUTEN",
            "description": "Bandgap temperature sensor output enable",
            "bitRange": "[1:1]",
        }
    }
}


ANCTL_MHSIENR = {
    "name": "MHSIENR",
    "displayName": "MHSIENR",
    "description": "MHSI enable register",
    "addressOffset": "0x02C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MHSION",
            "description": "Internal MHSI enable",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_MHSISR = {
    "name": "MHSISR",
    "displayName": "MHSISR",
    "description": "MHSI enable register",
    "addressOffset": "0x030",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MHSIRDY",
            "description": "Internal MHSI output status",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_FHSIENR = {
    "name": "FHSIENR",
    "displayName": "FHSIENR",
    "description": "FHSI enable register",
    "addressOffset": "0x038",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FHSION",
            "description": "Internal FHSI enable control",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_FHSISR = {
    "name": "FHSISR",
    "displayName": "FHSISR",
    "description": "FHSI Status register",
    "addressOffset": "0x03C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FHSIRDY",
            "description": "Internal FHSI clock output status",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_LSIENR = {
    "name": "LSIENR",
    "displayName": "LSIENR",
    "description": "LSI enable register",
    "addressOffset": "0x044",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSION",
            "description": "Internal LSI enable",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_LSISR = {
    "name": "LSISR",
    "displayName": "LSISR",
    "description": "LSI Status register",
    "addressOffset": "0x048",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSIRDY",
            "description": "Internal LSI clock output Status",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_HSECR0 = {
    "name": "HSECR0",
    "displayName": "HSECR0",
    "description": "HSE control register 0",
    "addressOffset": "0x04C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HSEON",
            "description": "HSE enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "BYPASS",
            "description": "External clock input mode enable",
            "bitRange": "[1:1]",
        }
    }
}


ANCTL_HSECR1 = {
    "name": "HSECR1",
    "displayName": "HSECR1",
    "description": "HSE control register 1",
    "addressOffset": "0x050",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PADOEN",
            "description": "HSE clock loop back from PAD",
            "bitRange": "[1:1]",
        }
    }
}

ANCTL_HSESR = {
    "name": "HSESR",
    "displayName": "HSESR",
    "description": "HSE Status register",
    "addressOffset": "0x058",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HSERDY",
            "description": "HSE clock output Status",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_PLLCR = {
    "name": "PLLCR",
    "displayName": "PLLCR",
    "description": "PLL control register",
    "addressOffset": "0x074",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLMUL",
            "description": "PLL multiplier factor",
            "bitRange": "[7:6]",
        }
    }
}


ANCTL_PLLENR = {
    "name": "PLLENR",
    "displayName": "PLLENR",
    "description": "PLL enable control register",
    "addressOffset": "0x078",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLON",
            "description": "PLL enable control",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_PLLSR = {
    "name": "PLLSR",
    "displayName": "PLLSR",
    "description": "PLL Status register",
    "addressOffset": "0x07C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLRDY",
            "description": "PLL clock output Status",
            "bitRange": "[1:0]",
        }
    }
}


ANCTL_PVDCR = {
    "name": "PVDCR",
    "displayName": "PVDCR",
    "description": "PVD control register",
    "addressOffset": "0x080",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000004",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLS",
            "description": "PVD threshold voltage selection",
            "bitRange": "[2:0]",
        }
    }
}


ANCTL_PVDENR = {
    "name": "PVDENR",
    "displayName": "PVDENR",
    "description": "PVD enable register",
    "addressOffset": "0x084",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PVDE",
            "description": "PVD enable control",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_SARENR = {
    "name": "SARENR",
    "displayName": "SARENR",
    "description": "SARADC enable register",
    "addressOffset": "0x08C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000001E",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SAREN",
            "description": "SARADC enable control",
            "bitRange": "[0:0]",
        }
    }
}

ANCTL_USBPCR = {
    "name": "USBPCR",
    "displayName": "USBPCR",
    "description": "USB PHY control register",
    "addressOffset": "0x090",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "USBPEN",
            "description": "USB PHY enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DPPUEN",
            "description": "DP pull enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "HIGHRESEN",
            "description": "High resistance enable",
            "bitRange": "[2:2]",
        },
        "field_4": {
            "name": "DMSTEN",
            "description": "DM Schmidt enable",
            "bitRange": "[3:3]",
        },
        "field_5": {
            "name": "DPSTEN",
            "description": "DP Schmidt enable",
            "bitRange": "[4:4]",
        }
    }
}

ANCTL_PORCR = {
    "name": "PORCR",
    "displayName": "PORCR",
    "description": "POR control register",
    "addressOffset": "0x094",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000841",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "POREN",
            "description": "POR enable control",
            "bitRange": "[11:0]",
        }
    }
}


ANCTL_CMPACR = {
    "name": "CMPACR",
    "displayName": "CMPACR",
    "description": "CMPA control register",
    "addressOffset": "0x098",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PSEL",
            "description": "CMPA positive input channel selection",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "NSEL",
            "description": "CMPA negative input channel selection",
            "bitRange": "[7:4]",
        },
        "field_2": {
            "name": "CMPAEN",
            "description": "CMPA enable control",
            "bitRange": "[8:8]",
        }
    }
}


ANCTL_CMPBCR = {
    "name": "CMPBCR",
    "displayName": "CMPBCR",
    "description": "CMPB control register",
    "addressOffset": "0x09C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PSEL",
            "description": "CMPB positive input channel selection",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "NSEL",
            "description": "CMPB negative input channel selection",
            "bitRange": "[7:4]",
        },
        "field_2": {
            "name": "CMPBEN",
            "description": "CMPB enable control",
            "bitRange": "[8:8]",
        },
    }
}


ANCTL_ISR = {
    "name": "ISR",
    "displayName": "ISR",
    "description": "INT Status register",
    "addressOffset": "0x0A0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000003",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MHSIIS",
            "description": "MHSI clock output stable flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FHSIIS",
            "description": "FHSI clock output stable flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSIIS",
            "description": "LSI clock output stable flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HSEIS",
            "description": "HSE clock output stable flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "LSEIS",
            "description": "LSE clock output stable flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "PLLIS",
            "description": "PLL clock output stable flag",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "CSSIS",
            "description": "HSE clock failure detection interrupt flag",
            "bitRange": "[7:7]",
        }
    }
}


ANCTL_IER = {
    "name": "IER",
    "displayName": "IER",
    "description": "INT enable register",
    "addressOffset": "0x0A4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MHSIIE",
            "description": "MHSI clock stable interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FHSIIE",
            "description": "FHSI clock stable interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSIIE",
            "description": "LSI clock stable interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HSEIE",
            "description": "HSE clock stable interrupt enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "LSEIE",
            "description": "LSE clock stable interrupt enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "PLLIE",
            "description": "PLL clock stable interrupt enable",
            "bitRange": "[5:5]",
        }
    }
}


ANCTL_ICR = {
    "name": "ICR",
    "displayName": "ICR",
    "description": "INT clear register",
    "addressOffset": "0x0A8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MHSIIC",
            "description": "clear MHSI clock output stable interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FHSIIC",
            "description": "clear FHSI clock output stable interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSIIC",
            "description": "clear LSI clock output stable interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HSEIC",
            "description": "clear HSE clock output stable interrupt flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "LSEIC",
            "description": "clear LSE clock output stable interrupt flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "PLLIC",
            "description": "clear PLL clock output stable interrupt flag",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "CSSIC",
            "description": "clear HSE clock failure detection interrupt flag",
            "bitRange": "[7:7]",
        }
    }
}


ANCTL_CMPASR = {
    "name": "CMPASR",
    "displayName": "CMPASR",
    "description": "CMPA Status register",
    "addressOffset": "0x0AC",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CMPAOUT",
            "description": "CMPA comparison result",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_CMPBSR = {
    "name": "CMPBSR",
    "displayName": "CMPBSR",
    "description": "CMPB Status register",
    "addressOffset": "0x0B0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CMPBOUT",
            "description": "CMPB comparison result",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_CSSENR = {
    "name": "CSSENR",
    "displayName": "CSSENR",
    "description": "CSS enable register",
    "addressOffset": "0x0B4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CSSON",
            "description": "HSE clock failure detection control",
            "bitRange": "[0:0]",
        }
    }
}


ANCTL_CSSCR = {
    "name": "CSSCR",
    "displayName": "CSSCR",
    "description": "CSS configuration register",
    "addressOffset": "0x0B8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FREQCNT",
            "description": "Configure CSS count value, must be configured to 0x03",
            "bitRange": "[11:0]",
        }
    }
}


anctl_define = {
    "name": "ANCTL",
    "description": "Analog control",
    "groupName": "ANCTL",
    "baseAddress": "0x40010400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0 ": ANCTL_BGCR2,
        "register_1 ": ANCTL_MHSIENR,
        "register_2 ": ANCTL_MHSISR,
        "register_3 ": ANCTL_FHSIENR,
        "register_4 ": ANCTL_FHSISR,
        "register_5 ": ANCTL_LSIENR,
        "register_6 ": ANCTL_LSISR,
        "register_7 ": ANCTL_HSECR0,
        "register_8 ": ANCTL_HSECR1,
        "register_9 ": ANCTL_HSESR,
        "register_10": ANCTL_PLLCR,
        "register_11": ANCTL_PLLENR,
        "register_12": ANCTL_PLLSR,
        "register_13": ANCTL_PVDCR,
        "register_14": ANCTL_PVDENR,
        "register_15": ANCTL_SARENR,
        "register_16": ANCTL_USBPCR,
        "register_17": ANCTL_PORCR,
        "register_18": ANCTL_CMPACR,
        "register_19": ANCTL_CMPBCR,
        "register_20": ANCTL_ISR,
        "register_21": ANCTL_IER,
        "register_22": ANCTL_ICR,
        "register_23": ANCTL_CMPASR,
        "register_24": ANCTL_CMPBSR,
        "register_25": ANCTL_CSSENR,
        "register_26": ANCTL_CSSCR,
    }
}
