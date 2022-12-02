CACHE_CR = {
    "name": "CR",
    "displayName": "CR",
    "description": "Control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x03000000",
    "fields": {
        "field_0": {
            "name": "LATANCY",
            "description": "Flash memory access waiting latency",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "PREFEN",
            "description": "Prefetch instruction enable",
            "bitRange": "[5:4]",
        },
        "field_2": {
            "name": "HIFREQ",
            "description": "High frequency access assistance",
            "bitRange": "[8:8]",
        },
        "field_3": {
            "name": "CHEEN",
            "description": "Cache enable",
            "bitRange": "[25:24]",
        },
    }
}


cache_define = {
    "name": "CACHE",
    "description": "CACHE",
    "groupName": "CACHE",
    "baseAddress": "0x40015400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": CACHE_CR,
    }
}
