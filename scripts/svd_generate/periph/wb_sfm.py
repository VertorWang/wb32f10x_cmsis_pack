SFM_CTRL = {
    "name": "CTRL",
    "displayName": "CTRL",
    "description": "Control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EXPRATE",
            "description": "Expand rate",
            "bitRange": "[2:0]",
        },
        "field_1": {
            "name": "EXPEN",
            "description": "Expand enable",
            "bitRange": "[3:3]",
        }
    }
}

SFM_DATA = {
    "name": "DATA",
    "displayName": "DATA",
    "description": "Data register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Data",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR0 = {
    "name": "DOUTR0",
    "displayName": "DOUTR0",
    "description": "Data output register 0",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR1 = {
    "name": "DOUTR1",
    "displayName": "DOUTR1",
    "description": "Data output register 1",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR2 = {
    "name": "DOUTR2",
    "displayName": "DOUTR2",
    "description": "Data output register 2",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR3 = {
    "name": "DOUTR3",
    "displayName": "DOUTR3",
    "description": "Data output register 3",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR4 = {
    "name": "DOUTR4",
    "displayName": "DOUTR4",
    "description": "Data output register 4",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR5 = {
    "name": "DOUTR5",
    "displayName": "DOUTR5",
    "description": "Data output register 5",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR6 = {
    "name": "DOUTR6",
    "displayName": "DOUTR6",
    "description": "Data output register 6",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_DOUTR7 = {
    "name": "DOUTR7",
    "displayName": "DOUTR7",
    "description": "Data output register 7",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DOUT",
            "description": "Data output",
            "bitRange": "[31:0]",
        }
    }
}

SFM_USBPSDCSR = {
    "name": "USBPSDCSR",
    "displayName": "USBPSDCSR",
    "description": "Usb port state detect control/status register",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SE0F",
            "description": "USB switches to SE0 state from port state flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "JSTATF",
            "description": "USB switches to J state from port state flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "KSTATF",
            "description": "USB switches to K state from port state flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SE1F",
            "description": "USB switches to SE1 state from port state flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SE0EN",
            "description": "USB SE0 state detect enable",
            "bitRange": "[8:8]",
        },
        "field_5": {
            "name": "JSTATEN",
            "description": "USB J state detect enable",
            "bitRange": "[9:9]",
        },
        "field_6": {
            "name": "KSTATEN",
            "description": "USB K state detect enable",
            "bitRange": "[10:10]",
        },
        "field_7": {
            "name": "SE1EN",
            "description": "USB SE1 state detect enable",
            "bitRange": "[11:11]",
        }
    }
}

SFM_USBPSTAT = {
    "name": "USBPSTAT",
    "displayName": "USBPSTAT",
    "description": "Usb port state register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000008",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SUSPEND",
            "description": "Suspend state",
            "bitRange": "[4:4]",
        },
        "field_1": {
            "name": "FULL_SPEED",
            "description": "Full speed state",
            "bitRange": "[5:5]",
        }
    }
}

sfm_define = {
    "name": "SFM",
    "description": "Special function macro",
    "groupName": "SFM",
    "baseAddress": "0x40014C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0 ": SFM_CTRL,
        "register_1 ": SFM_DATA,
        "register_2 ": SFM_DOUTR0,
        "register_3 ": SFM_DOUTR1,
        "register_4 ": SFM_DOUTR2,
        "register_5 ": SFM_DOUTR3,
        "register_6 ": SFM_DOUTR4,
        "register_7 ": SFM_DOUTR5,
        "register_8 ": SFM_DOUTR6,
        "register_9 ": SFM_DOUTR7,
        "register_10": SFM_USBPSDCSR,
        "register_11": SFM_USBPSTAT,
    }
}
