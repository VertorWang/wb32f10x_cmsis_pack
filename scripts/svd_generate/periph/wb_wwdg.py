WWDG_CR = {
    "name": "CR",
    "displayName": "CR",
    "description": "Control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000007F",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "T",
            "description": "7 bits counter",
            "bitRange": "[6:0]",
        },
        "field_1": {
            "name": "WDGA",
            "description": "Window watchdog active bit",
            "bitRange": "[7:7]",
        }
    }
}

WWDG_CFR = {
    "name": "CFR",
    "displayName": "CFR",
    "description": "Configuration register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000007F",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "W",
            "description": "7 bits window value",
            "bitRange": "[6:0]",
        },
        "field_1": {
            "name": "WDGTB",
            "description": "Window watchdog time base",
            "bitRange": "[8:7]",
        },
        "field_2": {
            "name": "EWI",
            "description": "Early wakeup interrupt",
            "bitRange": "[9:9]",
        }
    }
}

WWDG_SR = {
    "name": "SR",
    "displayName": "SR",
    "description": "Status register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EWIF",
            "description": "Early wakeup interrupt flag",
            "bitRange": "[0:0]",
        }
    }
}


wwdg_define = {
    "name": "WWDG",
    "description": "Window watchdog",
    "groupName": "WWDG",
    "baseAddress": "0x40009800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "WWDG",
        "description": "WWDG interrupt",
        "value": "0",
    },
    "registers": {
        "register_0": WWDG_CR,
        "register_1": WWDG_CFR,
        "register_2": WWDG_SR,
    }
}
