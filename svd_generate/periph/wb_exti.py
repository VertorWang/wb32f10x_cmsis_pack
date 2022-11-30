EXTI_INTEN = {
    "name": "INTEN",
    "displayName": "INTEN",
    "description": "Interrupt enable register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MRx",
            "description": "Interrupt enable Bits",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}

EXTI_EMR = {
    "name": "EMR",
    "displayName": "EMR",
    "description": "Event enable register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MRx",
            "description": "Event enable Bits",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}

EXTI_RTSR = {
    "name": "RTSR",
    "displayName": "RTSR",
    "description": "Rising edge trigger enable register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TRx",
            "description": "Rising edge trigger enable",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}

EXTI_FTSR = {
    "name": "FTSR",
    "displayName": "FTSR",
    "description": "Falling edge trigger enable register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TRx",
            "description": "Falling edge trigger enable",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}

EXTI_SWIER = {
    "name": "SWIER",
    "displayName": "SWIER",
    "description": "Software interrupt event register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SWIERx",
            "description": "Interrupt/Event software trigger",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}

EXTI_PR = {
    "name": "PR",
    "displayName": "PR",
    "description": "Pending register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "PRx",
            "description": "Interrupt pending status",
            "bitOffset": "0",
            "bitWidth": "19",
        }
    }
}


exti_define = {
    "name": "EXTI",
    "description": "Interrupt/event controller",
    "groupName": "EXTI",
    "baseAddress": "0x40001800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": EXTI_INTEN,
        "register_1": EXTI_EMR,
        "register_2": EXTI_RTSR,
        "register_3": EXTI_FTSR,
        "register_4": EXTI_SWIER,
        "register_5": EXTI_PR,
    }
}
