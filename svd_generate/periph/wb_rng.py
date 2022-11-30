RNG_RAND = {
    "name": "RAND",
    "displayName": "RAND",
    "description": "Random number generator register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "RAND",
            "description": "Generated 8-bit random number",
            "bitOffset": "0",
            "bitWidth": "8",
        }
    }
}

RNG_STOP = {
    "name": "STOP",
    "displayName": "STOP",
    "description": "RNG STOP register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "STOP",
            "description": "RNG STOP control",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

RNG_REC = {
    "name": "REC",
    "displayName": "REC",
    "description": "RNG Record register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "REC",
            "description": "The random data being read last time",
            "bitOffset": "0",
            "bitWidth": "8",
        }
    }
}

rng_define = {
    "name": "RNG",
    "description": "Random Number Generator",
    "groupName": "RNG",
    "baseAddress": "0x4000B800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": RNG_RAND,
        "register_1": RNG_STOP,
        "register_2": RNG_REC
    }
}
