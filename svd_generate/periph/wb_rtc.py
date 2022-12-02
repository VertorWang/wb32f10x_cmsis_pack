RTC_CRH = {
    "name": "CRH",
    "displayName": "CRH",
    "description": "Control high register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "SECIE",
            "description": "Second interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "ALRIE",
            "description": "Alarm interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "OWIE",
            "description": "Overflow interrupt enable",
            "bitRange": "[2:2]",
        }
    }
}

RTC_CRL = {
    "name": "CRL",
    "displayName": "CRL",
    "description": "Control low register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "SECF",
            "description": "Second flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "ALRF",
            "description": "Alarm flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "OWF",
            "description": "Overflow flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RSF",
            "description": "Register synchronization flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CNF",
            "description": "Configuration flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "RTOFF",
            "description": "RTC operation turn-off flag",
            "bitRange": "[5:5]",
        }
    }
}

RTC_PRLH = {
    "name": "PRLH",
    "displayName": "PRLH",
    "description": "Prescaler high register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "PRL",
            "description": "Prescaler high bits",
            "bitRange": "[3:0]",
        }
    }
}

RTC_PRLL = {
    "name": "PRLL",
    "displayName": "PRLL",
    "description": "Prescaler low register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "PRL",
            "description": "Prescaler low bits",
            "bitRange": "[15:0]",
        }
    }
}

RTC_DIVH = {
    "name": "DIVH",
    "displayName": "DIVH",
    "description": "RTC clock divider high register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DIV",
            "description": "RTC clock divider high",
            "bitRange": "[3:0]",
        }
    }
}

RTC_DIVL = {
    "name": "DIVL",
    "displayName": "DIVL",
    "description": "RTC clock divider low register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DIV",
            "description": "RTC clock divider low",
            "bitRange": "[15:0]",
        }
    }
}

RTC_CNTH = {
    "name": "CNTH",
    "displayName": "CNTH",
    "description": "RTC counter high register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CNT",
            "description": "RTC counter high",
            "bitRange": "[15:0]",
        }
    }
}

RTC_CNTL = {
    "name": "CNTL",
    "displayName": "CNTL",
    "description": "RTC counter low register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "name": "CNT",
            "description": "RTC counter low",
            "bitRange": "[15:0]",
        }
    }
}

RTC_ALRH = {
    "name": "ALRH",
    "displayName": "ALRH",
    "description": "RTC alarm high register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000FFFF",
    "fields": {
        "field_0": {
            "name": "ALR",
            "description": "RTC alarm high",
            "bitRange": "[15:0]",
        }
    }
}

RTC_ALRL = {
    "name": "ALRL",
    "displayName": "ALRL",
    "description": "RTC alarm low register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000FFFF",
    "fields": {
        "field_0": {
            "name": "ALR",
            "description": "RTC alarm low",
            "bitRange": "[15:0]",
        }
    }
}


rtc_define = {
    "name": "RTC",
    "description": "RTC",
    "groupName": "RTC",
    "baseAddress": "0x40015800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": RTC_CRH,
        "register_1": RTC_CRL,
        "register_2": RTC_PRLH,
        "register_3": RTC_PRLL,
        "register_4": RTC_DIVH,
        "register_5": RTC_DIVL,
        "register_6": RTC_CNTH,
        "register_7": RTC_CNTL,
        "register_8": RTC_ALRH,
        "register_9": RTC_ALRL,
    }
}
