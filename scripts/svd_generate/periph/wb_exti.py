EXTI_IMR = {
    "name": "IMR",
    "displayName": "IMR",
    "description": "Interrupt mask register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MRx",
            "description": "Interrupt mask on line x",
            "bitRange": "[18:0]",
        }
    }
}

EXTI_EMR = {
    "name": "EMR",
    "displayName": "EMR",
    "description": "Event mask register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MRx",
            "description": "Event mask on line x",
            "bitRange": "[18:0]",
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
            "bitRange": "[18:0]",
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
            "bitRange": "[18:0]",
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
            "bitRange": "[18:0]",
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
            "bitRange": "[18:0]",
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
    "interrupt_0": {
        "name": "EXTI0",
        "description": "EXTI Line0 interrupt",
        "value": "6",
    },
    "interrupt_1": {
        "name": "EXTI1",
        "description": "EXTI Line1 interrupt",
        "value": "7",
    },
    "interrupt_2": {
        "name": "EXTI2",
        "description": "EXTI Line2 interrupt",
        "value": "8",
    },
    "interrupt_3": {
        "name": "EXTI3",
        "description": "EXTI Line3 interrupt",
        "value": "9",
    },
    "interrupt_4": {
        "name": "EXTI4",
        "description": "EXTI Line4 interrupt",
        "value": "10",
    },
    "interrupt_5": {
        "name": "EXTI9_5",
        "description": "EXTI Line[9:5] interrupt",
        "value": "16",
    },
    "interrupt_6": {
        "name": "EXTI15_10",
        "description": "EXTI Line[15:10] interrupt",
        "value": "33",
    },
    "registers": {
        "register_0": EXTI_IMR,
        "register_1": EXTI_EMR,
        "register_2": EXTI_RTSR,
        "register_3": EXTI_FTSR,
        "register_4": EXTI_SWIER,
        "register_5": EXTI_PR,
    }
}
