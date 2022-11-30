PWR_CR0 = {
    "name": "CR0",
    "displayName": "CR0",
    "description": "Power control register 0",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DBP",
            "description": "Disable the write protection for backup domain registers",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "REGMODE",
            "description": "Configure the state of the voltage regulator when it enters stop mode",
            "bitOffset": "1",
            "bitWidth": "2",
        },
        "field_2": {
            "name": "FCLKSD",
            "description": "Reduce the frequency of Cortex ® -M3 FCLK",
            "bitOffset": "3",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "PDDS",
            "description": "Configure the working state of the device when the Cortex ® -M3 enters deep sleep mode",
            "bitOffset": "5",
            "bitWidth": "2",
        },
        "field_4": {
            "name": "REGCFG",
            "description": "Configure the voltage change direction of the voltage regulator",
            "bitOffset": "7",
            "bitWidth": "2",
        },
        "field_5": {
            "name": "REGLVL",
            "description": "Configure the step value of the voltage regulator",
            "bitOffset": "9",
            "bitWidth": "3",
        },
        "field_6": {
            "name": "FREGMODE",
            "description": "Configure the state of the flash regulator when it enters stop mode",
            "bitOffset": "12",
            "bitWidth": "2",
        },
        "field_7": {
            "name": "BGMODE",
            "description": "Configure the status of the bandgap when it enters the stop mode",
            "bitOffset": "14",
            "bitWidth": "2",
        },
        "field_8": {
            "name": "PORMODE",
            "description": "Configure the status of the POR BG when it enters stop mode",
            "bitOffset": "16",
            "bitWidth": "1",
        },
        "field_9": {
            "name": "FLASHMODE",
            "description": "Configure the state of the flash memory when it enters stop mode",
            "bitOffset": "17",
            "bitWidth": "1",
        },
        "field_10": {
            "name": "S32KMODE",
            "description": "Configure the state of 32K SRAM when it enters stop mode",
            "bitOffset": "18",
            "bitWidth": "1",
        },
        "field_11": {
            "name": "S4KMODE",
            "description": "Configure the state of 4K SRAM when it enters stop mode",
            "bitOffset": "19",
            "bitWidth": "1",
        }
    }
}

PWR_CR1 = {
    "name": "CR1",
    "displayName": "CR1",
    "description": "Control register 1",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CWUF",
            "description": "Clear WUF flag bit",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "CSBF",
            "description": "Clear SBF flag bit",
            "bitOffset": "1",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "CSPF",
            "description": "Clear SPF flag bit",
            "bitOffset": "2",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "CCKF",
            "description": "Clear CKF flag bit",
            "bitOffset": "3",
            "bitWidth": "1",
        }
    }
}

PWR_CR2 = {
    "name": "CR2",
    "displayName": "CR2",
    "description": "Control register 2",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "EWUP",
            "description": "Enable WKUP pin",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

PWR_SR0 = {
    "name": "SR0",
    "displayName": "SR0",
    "description": "Status register 0",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "PVD0",
            "description": "PVD output",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

PWR_SR1 = {
    "name": "SR1",
    "displayName": "SR1",
    "description": "Status register 1",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "WUF",
            "description": "Wakeup flag",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "SBF",
            "description": "Standby flag",
            "bitOffset": "1",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "SPF",
            "description": "Stop flag",
            "bitOffset": "2",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "CKF",
            "description": "CKF Flag",
            "bitOffset": "3",
            "bitWidth": "1",
        }
    }
}

PWR_GPREG0 = {
    "name": "GPREG0",
    "displayName": "GPREG0",
    "description": "General purpose register 0",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "GPREG0",
            "description": "General purpose register 0",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

PWR_GPREG1 = {
    "name": "GPREG1",
    "displayName": "GPREG1",
    "description": "General purpose register 1",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "GPREG1",
            "description": "General purpose register 1",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

PWR_CFGR = {
    "name": "CFGR",
    "displayName": "CFGR",
    "description": "Configuration register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x000003BE",
    "fields": {
        "field_0": {
            "name": "LPCFG",
            "description": "Configure the time to enter and exit low power mode",
            "bitOffset": "0",
            "bitWidth": "13",
        }
    }
}

PWR_ANAKEY1 = {
    "name": "ANAKEY1",
    "displayName": "ANAKEY1",
    "description": "Analog enable register 1",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    # 有争议
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "ANAKEY1",
            "description": "Analog enable register 1",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

PWR_ANAKEY2 = {
    "name": "ANAKEY2",
    "displayName": "ANAKEY2",
    "description": "Analog enable register 2",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    # 有争议
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "ANAKEY2",
            "description": "Analog enable register 2",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

pwr_define = {
    "name": "PWR",
    "description": "Power control",
    "groupName": "PWR",
    "baseAddress": "0x40010000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": PWR_CR0,
        "register_1": PWR_CR1,
        "register_2": PWR_CR2,
        "register_3": PWR_SR0,
        "register_4": PWR_SR1,
        "register_5": PWR_GPREG0,
        "register_6": PWR_GPREG1,
        "register_7": PWR_CFGR,
        "register_8": PWR_ANAKEY1,
        "register_9": PWR_ANAKEY2,
    }
}
