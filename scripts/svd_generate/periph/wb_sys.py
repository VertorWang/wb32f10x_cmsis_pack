SYS_ID = {
    "name": "ID",
    "displayName": "ID",
    "description": "ID Register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x3A000000",
    "resetMask": "0xFF000000",
    "fields": {
        "field_0": {
            "name": "MASK_VER",
            "description": "MASK version",
            "bitRange": "[17:14]",
        },
        "field_1": {
            "name": "CHIP_ID",
            "description": "Part No",
            "bitRange": "[23:18]",
        }
    }
}

SYS_MEMSZ = {
    "name": "MEMSZ",
    "displayName": "MEMSZ",
    "description": "Memory control Register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "FLASH_SIZE",
            "description": "FLASH density",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "SRAM_SIZE",
            "description": "SRAM density",
            "bitRange": "[5:4]",
        }
    }
}

SYS_BTCR = {
    "name": "BTCR",
    "displayName": "BTCR",
    "description": "Security control Register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "RD_PROT",
            "description": "Read protection control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SWD_DIS",
            "description": "SWD control",
            "bitRange": "[8:8]",
        },
        "field_3": {
            "name": "SRAM_DIS",
            "description": "SRAM boot contro",
            "bitRange": "[16:16]",
        },
        "field_4": {
            "name": "SMEM_DIS",
            "description": "System memory boot control",
            "bitRange": "[24:24]",
        },
    }
}

SYS_MEMWEN = {
    "name": "MEMWEN",
    "displayName": "MEMWEN",
    "description": "FLASH write protection register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "MAIN_WEN",
            "description": "FLASH Write protection control",
            "bitRange": "[31:0]",
        }
    }
}

SYS_SENDEV = {
    "name": "SENDEV",
    "displayName": "SENDEV",
    "description": "Secondary development control Register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "SENDEV_SIZE",
            "description": "Secondary development code space control, the granuality is 1K Byte",
            "bitRange": "[11:0]",
        },
        "field_1": {
            "name": "SENDEV_EN",
            "description": "Secondary development control",
            "bitRange": "[16:16]",
        }
    }
}

SYS_RSTCR = {
    "name": "RSTCR",
    "displayName": "RSTCR",
    "description": "Reboot control Register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFF0",
    "fields": {
        "field_0": {
            "name": "IWDG_EN",
            "description": "IWDG start control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RST_STOP",
            "description": "Stop mode reset control",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RST_STBY",
            "description": "Standby Mode reset control",
            "bitRange": "[2:2]",
        }
    }
}

SYS_IF4LCK = {
    "name": "IF4LCK",
    "displayName": "IF4LCK",
    "description": "Information block 4 protection register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFF0",
    "fields": {
        "field_0": {
            "name": "SYS_IF4LCK",
            "description": "4th Information block Erase/Write control",
            "bitRange": "[0:0]",
        }
    }
}

SYS_IF5LCK = {
    "name": "IF5LCK",
    "displayName": "IF5LCK",
    "description": "Information block 5 protection register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFF0",
    "fields": {
        "field_0": {
            "name": "SYS_IF5LCK",
            "description": "5th Information block Erase/Write control",
            "bitRange": "[0:0]",
        }
    }
}

SYS_IF6LCK = {
    "name": "IF6LCK",
    "displayName": "IF6LCK",
    "description": "Information block 6 protection register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFF0",
    "fields": {
        "field_0": {
            "name": "SYS_IF6LCK",
            "description": "6th Information block Erase/Write control",
            "bitRange": "[0:0]",
        }
    }
}

SYS_IF7LCK = {
    "name": "IF7LCK",
    "displayName": "IF7LCK",
    "description": "Information block 7 protection register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFF0",
    "fields": {
        "field_0": {
            "name": "SYS_IF7LCK",
            "description": "7th Information block Erase/Write control",
            "bitRange": "[0:0]",
        }
    }
}

SYS_BTSR = {
    "name": "BTSR",
    "displayName": "BTSR",
    "description": "Boot control Register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BOOT_MODE",
            "description": "Boot mode",
            "bitRange": "[1:0]",
        }
    }
}

sys_define = {
    "name": "SYS",
    "description": "System configuration",
    "groupName": "SYS",
    "baseAddress": "0x40016400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0 ": SYS_ID,
        "register_1 ": SYS_MEMSZ,
        "register_2 ": SYS_BTCR,
        "register_3 ": SYS_MEMWEN,
        "register_4 ": SYS_SENDEV,
        "register_5 ": SYS_RSTCR,
        "register_6 ": SYS_IF4LCK,
        "register_7 ": SYS_IF5LCK,
        "register_8 ": SYS_IF6LCK,
        "register_9 ": SYS_IF7LCK,
        "register_10": SYS_BTSR,
    }
}
