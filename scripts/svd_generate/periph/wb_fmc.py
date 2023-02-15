FMC_CRCON = {
    "name": "CRCON",
    "displayName": "CRCON",
    "description": "CRC control register",
    "addressOffset": "0x004",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000F000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CRCEN",
            "description": "CRC enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CRCF",
            "description": "CRC calculation complete flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "PAUSE",
            "description": "CRC pause",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SLOWRD",
            "description": "Control CRC calculation interval period",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CRCFIE",
            "description": "CRC calculation complete interrupt enable",
            "bitRange": "[8:8]",
        },
        "field_5": {
            "name": "PERIOD",
            "description": "Period to read flash while CRC calculation",
            "bitRange": "[15:12]",
        },
        "field_6": {
            "name": "CRCLEN",
            "description": "CRC calculation length",
            "bitRange": "[25:16]",
        }
    }
}

FMC_ADDR = {
    "name": "ADDR",
    "displayName": "ADDR",
    "description": "Address register",
    "addressOffset": "0x010",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Adress data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_DATA1 = {
    "name": "DATA1",
    "displayName": "DATA1",
    "description": "Data 1 register",
    "addressOffset": "0x01C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Address data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF0 = {
    "name": "BUF0",
    "displayName": "BUF0",
    "description": "Buffer 0 register",
    "addressOffset": "0x100",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF1 = {
    "name": "BUF1",
    "displayName": "BUF1",
    "description": "Buffer 1 register",
    "addressOffset": "0x104",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF2 = {
    "name": "BUF2",
    "displayName": "BUF2",
    "description": "Buffer 2 register",
    "addressOffset": "0x108",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF3 = {
    "name": "BUF3",
    "displayName": "BUF3",
    "description": "Buffer 3 register",
    "addressOffset": "0x10C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF4 = {
    "name": "BUF4",
    "displayName": "BUF4",
    "description": "Buffer 4 register",
    "addressOffset": "0x110",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF5 = {
    "name": "BUF5",
    "displayName": "BUF5",
    "description": "Buffer 5 register",
    "addressOffset": "0x114",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF6 = {
    "name": "BUF6",
    "displayName": "BUF6",
    "description": "Buffer 6 register",
    "addressOffset": "0x118",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF7 = {
    "name": "BUF7",
    "displayName": "BUF7",
    "description": "Buffer 7 register",
    "addressOffset": "0x11C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF8 = {
    "name": "BUF8",
    "displayName": "BUF8",
    "description": "Buffer 8 register",
    "addressOffset": "0x120",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF9 = {
    "name": "BUF9",
    "displayName": "BUF9",
    "description": "Buffer 9 register",
    "addressOffset": "0x124",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF10 = {
    "name": "BUF10",
    "displayName": "BUF10",
    "description": "Buffer 10 register",
    "addressOffset": "0x128",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF11 = {
    "name": "BUF11",
    "displayName": "BUF11",
    "description": "Buffer 11 register",
    "addressOffset": "0x12C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF12 = {
    "name": "BUF12",
    "displayName": "BUF12",
    "description": "Buffer 12 register",
    "addressOffset": "0x130",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF13 = {
    "name": "BUF13",
    "displayName": "BUF13",
    "description": "Buffer 13 register",
    "addressOffset": "0x134",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF14 = {
    "name": "BUF14",
    "displayName": "BUF14",
    "description": "Buffer 14 register",
    "addressOffset": "0x138",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF15 = {
    "name": "BUF15",
    "displayName": "BUF15",
    "description": "Buffer 15 register",
    "addressOffset": "0x13C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF16 = {
    "name": "BUF16",
    "displayName": "BUF16",
    "description": "Buffer 16 register",
    "addressOffset": "0x140",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF17 = {
    "name": "BUF17",
    "displayName": "BUF17",
    "description": "Buffer 17 register",
    "addressOffset": "0x144",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF18 = {
    "name": "BUF18",
    "displayName": "BUF18",
    "description": "Buffer 18 register",
    "addressOffset": "0x148",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF19 = {
    "name": "BUF19",
    "displayName": "BUF19",
    "description": "Buffer 19 register",
    "addressOffset": "0x14C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF20 = {
    "name": "BUF20",
    "displayName": "BUF20",
    "description": "Buffer 20 register",
    "addressOffset": "0x150",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF21 = {
    "name": "BUF21",
    "displayName": "BUF21",
    "description": "Buffer 21 register",
    "addressOffset": "0x154",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF22 = {
    "name": "BUF22",
    "displayName": "BUF22",
    "description": "Buffer 22 register",
    "addressOffset": "0x158",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF23 = {
    "name": "BUF23",
    "displayName": "BUF23",
    "description": "Buffer 23 register",
    "addressOffset": "0x15C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF24 = {
    "name": "BUF24",
    "displayName": "BUF24",
    "description": "Buffer 24 register",
    "addressOffset": "0x160",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF25 = {
    "name": "BUF25",
    "displayName": "BUF25",
    "description": "Buffer 25 register",
    "addressOffset": "0x164",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF26 = {
    "name": "BUF26",
    "displayName": "BUF26",
    "description": "Buffer 26 register",
    "addressOffset": "0x168",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF27 = {
    "name": "BUF27",
    "displayName": "BUF27",
    "description": "Buffer 27 register",
    "addressOffset": "0x16C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF28 = {
    "name": "BUF28",
    "displayName": "BUF28",
    "description": "Buffer 28 register",
    "addressOffset": "0x170",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF29 = {
    "name": "BUF29",
    "displayName": "BUF29",
    "description": "Buffer 29 register",
    "addressOffset": "0x174",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF30 = {
    "name": "BUF30",
    "displayName": "BUF30",
    "description": "Buffer 30 register",
    "addressOffset": "0x178",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF31 = {
    "name": "BUF31",
    "displayName": "BUF31",
    "description": "Buffer 31 register",
    "addressOffset": "0x17C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF32 = {
    "name": "BUF32",
    "displayName": "BUF32",
    "description": "Buffer 32 register",
    "addressOffset": "0x180",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF33 = {
    "name": "BUF33",
    "displayName": "BUF33",
    "description": "Buffer 33 register",
    "addressOffset": "0x184",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF34 = {
    "name": "BUF34",
    "displayName": "BUF34",
    "description": "Buffer 34 register",
    "addressOffset": "0x188",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF35 = {
    "name": "BUF35",
    "displayName": "BUF35",
    "description": "Buffer 35 register",
    "addressOffset": "0x18C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF36 = {
    "name": "BUF36",
    "displayName": "BUF36",
    "description": "Buffer 36 register",
    "addressOffset": "0x190",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF37 = {
    "name": "BUF37",
    "displayName": "BUF37",
    "description": "Buffer 37 register",
    "addressOffset": "0x194",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF38 = {
    "name": "BUF38",
    "displayName": "BUF38",
    "description": "Buffer 38 register",
    "addressOffset": "0x198",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF39 = {
    "name": "BUF39",
    "displayName": "BUF39",
    "description": "Buffer 39 register",
    "addressOffset": "0x19C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF40 = {
    "name": "BUF40",
    "displayName": "BUF40",
    "description": "Buffer 40 register",
    "addressOffset": "0x1A0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF41 = {
    "name": "BUF41",
    "displayName": "BUF41",
    "description": "Buffer 41 register",
    "addressOffset": "0x1A4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF42 = {
    "name": "BUF42",
    "displayName": "BUF42",
    "description": "Buffer 42 register",
    "addressOffset": "0x1A8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF43 = {
    "name": "BUF43",
    "displayName": "BUF43",
    "description": "Buffer 43 register",
    "addressOffset": "0x1AC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF44 = {
    "name": "BUF44",
    "displayName": "BUF44",
    "description": "Buffer 44 register",
    "addressOffset": "0x1B0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF45 = {
    "name": "BUF45",
    "displayName": "BUF45",
    "description": "Buffer 45 register",
    "addressOffset": "0x1B4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF46 = {
    "name": "BUF46",
    "displayName": "BUF46",
    "description": "Buffer 46 register",
    "addressOffset": "0x1B8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF47 = {
    "name": "BUF47",
    "displayName": "BUF47",
    "description": "Buffer 47 register",
    "addressOffset": "0x1BC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF48 = {
    "name": "BUF48",
    "displayName": "BUF48",
    "description": "Buffer 48 register",
    "addressOffset": "0x1C0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF49 = {
    "name": "BUF49",
    "displayName": "BUF49",
    "description": "Buffer 49 register",
    "addressOffset": "0x1C4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF50 = {
    "name": "BUF50",
    "displayName": "BUF50",
    "description": "Buffer 50 register",
    "addressOffset": "0x1C8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF51 = {
    "name": "BUF51",
    "displayName": "BUF51",
    "description": "Buffer 51 register",
    "addressOffset": "0x1CC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF52 = {
    "name": "BUF52",
    "displayName": "BUF52",
    "description": "Buffer 52 register",
    "addressOffset": "0x1D0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF53 = {
    "name": "BUF53",
    "displayName": "BUF53",
    "description": "Buffer 53 register",
    "addressOffset": "0x1D4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF54 = {
    "name": "BUF54",
    "displayName": "BUF54",
    "description": "Buffer 54 register",
    "addressOffset": "0x1D8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF55 = {
    "name": "BUF55",
    "displayName": "BUF55",
    "description": "Buffer 55 register",
    "addressOffset": "0x1DC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF56 = {
    "name": "BUF56",
    "displayName": "BUF56",
    "description": "Buffer 56 register",
    "addressOffset": "0x1E0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF57 = {
    "name": "BUF57",
    "displayName": "BUF57",
    "description": "Buffer 57 register",
    "addressOffset": "0x1E4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF58 = {
    "name": "BUF58",
    "displayName": "BUF58",
    "description": "Buffer 58 register",
    "addressOffset": "0x1E8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF59 = {
    "name": "BUF59",
    "displayName": "BUF59",
    "description": "Buffer 59 register",
    "addressOffset": "0x1EC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF60 = {
    "name": "BUF60",
    "displayName": "BUF60",
    "description": "Buffer 60 register",
    "addressOffset": "0x1F0",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF61 = {
    "name": "BUF61",
    "displayName": "BUF61",
    "description": "Buffer 61 register",
    "addressOffset": "0x1F4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF62 = {
    "name": "BUF62",
    "displayName": "BUF62",
    "description": "Buffer 62 register",
    "addressOffset": "0x1F8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

FMC_BUF63 = {
    "name": "BUF63",
    "displayName": "BUF63",
    "description": "Buffer 63 register",
    "addressOffset": "0x1FC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "Data",
            "description": "Buffer data",
            "bitRange": "[31:0]",
        }
    }
}

fmc_define = {
    "name": "FMC",
    "description": "Flash memory controller",
    "groupName": "FMC",
    "baseAddress": "0x40017800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "FMC",
        "description": "FMC interrupt",
        "value": "4",
    },
    "registers": {
        "register_0 ": FMC_CRCON,
        "register_1 ": FMC_ADDR,
        "register_2 ": FMC_DATA1,
        "register_3 ": FMC_BUF0,
        "register_4 ": FMC_BUF1,
        "register_5 ": FMC_BUF2,
        "register_6 ": FMC_BUF3,
        "register_7 ": FMC_BUF4,
        "register_8 ": FMC_BUF5,
        "register_9 ": FMC_BUF6,
        "register_10": FMC_BUF7,
        "register_11": FMC_BUF8,
        "register_12": FMC_BUF9,
        "register_13": FMC_BUF10,
        "register_14": FMC_BUF11,
        "register_15": FMC_BUF12,
        "register_16": FMC_BUF13,
        "register_17": FMC_BUF14,
        "register_18": FMC_BUF15,
        "register_19": FMC_BUF16,
        "register_20": FMC_BUF17,
        "register_21": FMC_BUF18,
        "register_22": FMC_BUF19,
        "register_23": FMC_BUF20,
        "register_24": FMC_BUF21,
        "register_25": FMC_BUF22,
        "register_26": FMC_BUF23,
        "register_27": FMC_BUF24,
        "register_28": FMC_BUF25,
        "register_29": FMC_BUF26,
        "register_30": FMC_BUF27,
        "register_31": FMC_BUF28,
        "register_32": FMC_BUF29,
        "register_33": FMC_BUF30,
        "register_34": FMC_BUF31,
        "register_35": FMC_BUF32,
        "register_36": FMC_BUF33,
        "register_37": FMC_BUF34,
        "register_38": FMC_BUF35,
        "register_39": FMC_BUF36,
        "register_40": FMC_BUF37,
        "register_41": FMC_BUF38,
        "register_42": FMC_BUF39,
        "register_43": FMC_BUF40,
        "register_44": FMC_BUF41,
        "register_45": FMC_BUF42,
        "register_46": FMC_BUF43,
        "register_47": FMC_BUF44,
        "register_48": FMC_BUF45,
        "register_49": FMC_BUF46,
        "register_50": FMC_BUF47,
        "register_51": FMC_BUF48,
        "register_52": FMC_BUF49,
        "register_53": FMC_BUF50,
        "register_54": FMC_BUF51,
        "register_55": FMC_BUF52,
        "register_56": FMC_BUF53,
        "register_57": FMC_BUF54,
        "register_58": FMC_BUF55,
        "register_59": FMC_BUF56,
        "register_60": FMC_BUF57,
        "register_61": FMC_BUF58,
        "register_62": FMC_BUF59,
        "register_63": FMC_BUF60,
        "register_64": FMC_BUF61,
        "register_65": FMC_BUF62,
        "register_66": FMC_BUF63,
    }
}
