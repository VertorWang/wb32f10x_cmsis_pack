CRC_MODE = {
    "name": "MODE",
    "displayName": "MODE",
    "description": "CRC mode register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CRC_POLY",
            "description": "Select CRC polynomial field",
            "bitOffset": "0",
            "bitWidth": "2",
        },
        "field_1": {
            "name": "BIT_RVS_WR",
            "description": "Select bit order for CRC_WR_DATA",
            "bitOffset": "2",
            "bitWidth": "1",
        },
        "field_2": {
            "name": "CMPL_WR",
            "description": "Select one's complement for CRC_WR_DATA",
            "bitOffset": "3",
            "bitWidth": "1",
        },
        "field_3": {
            "name": "BIT_RVS_SUM",
            "description": "Select bit order revers for CRC_SUM",
            "bitOffset": "4",
            "bitWidth": "1",
        },
        "field_4": {
            "name": "CMPL_SUM",
            "description": "Select one's complement for CRC_SUM",
            "bitOffset": "5",
            "bitWidth": "1",
        },
        "field_5": {
            "name": "SEED_OP",
            "description": "CRC seed option set",
            "bitOffset": "6",
            "bitWidth": "1",
        },
        "field_6": {
            "name": "SEED_SET",
            "description": "Load seed to CRC generator",
            "bitOffset": "7",
            "bitWidth": "1",
        }
    }
}
CRC_SEED = {
    "name": "SEED",
    "displayName": "SEED",
    "description": "CRC seed register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000FFFF",
    "fields": {
        "field_0": {
            "name": "SEED",
            "description": "CRC seed value",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}
CRC_SUM = {
    "name": "SUM",
    "displayName": "SUM",
    "description": "CRC checksum register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000FFFF",
    "fields": {
        "field_0": {
            "name": "SUM",
            "description": "CRC checksum",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}
CRC_WDATA = {
    "name": "WDATA",
    "displayName": "WDATA",
    "description": "CRC data register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "write",
    # 有争议
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "WDATA",
            "description": "CRC data",
            "bitOffset": "0",
            "bitWidth": "32",
        }
    }
}

crc_define = {
    "name": "CRC",
    "description": "Cyclic Redundancy Check",
    "groupName": "CRC",
    "baseAddress": "0x40014800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": CRC_MODE,
        "register_1": CRC_SEED,
        "register_2": CRC_SUM,
        "register_3": CRC_WDATA,
    }
}
