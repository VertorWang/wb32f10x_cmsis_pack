LED_CON = {
    "name": "CON",
    "displayName": "CON",
    "description": "Control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LED_RUN",
            "description": "LED enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "LED_CHNUM",
            "description": "LED chanel number",
            "bitRange": "[5:4]",
        }
    }
}

LED_CYC = {
    "name": "CYC",
    "displayName": "CYC",
    "description": "Cycle register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LED_CYC",
            "description": "LED cycle",
            "bitRange": "[15:0]",
        }
    }
}

LED_ECO = {
    "name": "ECO",
    "displayName": "ECO",
    "description": "Electric output register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LED_SEGD4",
            "description": "Segment 4 control output bits",
            "bitRange": "[7:0]",
        },
        "field_1": {
            "name": "LED_SEGD5",
            "description": "Segment 5 control output bits",
            "bitRange": "[15:8]",
        },
        "field_2": {
            "name": "LED_SEGD6",
            "description": "Segment 6 control output bits",
            "bitRange": "[23:16]",
        },
        "field_3": {
            "name": "LED_SEGD7",
            "description": "Segment 7 control output bits",
            "bitRange": "[31:24]",
        }
    }
}

LED_SEGH = {
    "name": "SEGH",
    "displayName": "SEGH",
    "description": "Segment control high register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LED_SEGD4",
            "description": "Segment 4 control output bits",
            "bitRange": "[7:0]",
        },
        "field_1": {
            "name": "LED_SEGD5",
            "description": "Segment 5 control output bits",
            "bitRange": "[15:8]",
        },
        "field_2": {
            "name": "LED_SEGD6",
            "description": "Segment 6 control output bits",
            "bitRange": "[23:16]",
        },
        "field_3": {
            "name": "LED_SEGD7",
            "description": "Segment 7 control output bits",
            "bitRange": "[31:24]",
        }
    }
}

LED_SEGL = {
    "name": "SEGL",
    "displayName": "SEGL",
    "description": "Segment control low register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LED_SEGD0",
            "description": "Segment 0 control output bits",
            "bitRange": "[7:0]",
        },
        "field_1": {
            "name": "LED_SEGD1",
            "description": "Segment 1 control output bits",
            "bitRange": "[15:8]",
        },
        "field_2": {
            "name": "LED_SEGD2",
            "description": "Segment 2 control output bits",
            "bitRange": "[23:16]",
        },
        "field_3": {
            "name": "LED_SEGD3",
            "description": "Segment 3 control output bits",
            "bitRange": "[31:24]",
        }
    }
}


led_define = {
    "name": "LED",
    "description": "LED driver controller",
    "groupName": "LED",
    "baseAddress": "0x4000BC00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": LED_CON,
        "register_1": LED_CYC,
        "register_2": LED_ECO,
        "register_3": LED_SEGH,
        "register_4": LED_SEGL,
    }
}
