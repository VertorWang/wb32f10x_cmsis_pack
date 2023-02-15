IWDG_KR = {
    "name": "KR",
    "displayName": "KR",
    "description": "Key register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "KEY",
            "description": "Key value",
            "bitRange": "[15:0]",
        }
    }
}

IWDG_PR = {
    "name": "PR",
    "displayName": "PR",
    "description": "Prescaler divider register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PR",
            "description": "Prescaler divider",
            "bitRange": "[2:0]",
        }
    }
}

IWDG_RLR = {
    "name": "RLR",
    "displayName": "RLR",
    "description": "Reload register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000FFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RL",
            "description": "Watchdog counter reload value",
            "bitRange": "[0:0]",
        }
    }
}

IWDG_SR = {
    "name": "SR",
    "displayName": "SR",
    "description": "Status register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PVU",
            "description": "Watchdog prescaler value update",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RVU",
            "description": "Watchdog counter reload value update",
            "bitRange": "[1:1]",
        }
    }
}

iwdg_define = {
    "name": "IWDG",
    "description": "Independent watchdog",
    "groupName": "IWDG",
    "baseAddress": "0x40010800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": IWDG_KR,
        "register_1": IWDG_PR,
        "register_2": IWDG_RLR,
        "register_3": IWDG_SR,
    }
}
