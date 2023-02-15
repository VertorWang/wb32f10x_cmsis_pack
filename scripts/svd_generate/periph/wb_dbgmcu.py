DBGMCU_CR = {
    "name": "CR",
    "displayName": "CR",
    "description": "Control register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DBG_SLEEP",
            "description": "Debug sleep mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DBG_STOP",
            "description": "Debug stop mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "DBG_STANDBY",
            "description": "Debug standby mode",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TRACE_IOEN",
            "description": "Trace IO enable",
            "bitRange": "[5:5]",
        },
        "field_4": {
            "name": "DBG_IWDG_STOP",
            "description": "Independent watchdog stop working in debug mode",
            "bitRange": "[8:8]",
        },
        "field_5": {
            "name": "DBG_WWDG_STOP",
            "description": "Window watchdog stop working in debug mode",
            "bitRange": "[9:9]",
        },
        "field_6": {
            "name": "DBG_TIM1_STOP",
            "description": "Timer 1 stop working in debug mode",
            "bitRange": "[10:10]",
        },
        "field_7": {
            "name": "DBG_TIM2_STOP",
            "description": "Timer 2 stop working in debug mode",
            "bitRange": "[11:11]",
        },
        "field_8": {
            "name": "DBG_TIM3_STOP",
            "description": "Timer 3 stop working in debug mode",
            "bitRange": "[12:12]",
        },
        "field_9": {
            "name": "DBG_TIM4_STOP",
            "description": "Timer 4 stop working in debug mode",
            "bitRange": "[13:13]",
        }
    }
}


dbgmcu_define = {
    "name": "DBGMCU",
    "description": "Debug MCU",
    "groupName": "DBGMCU",
    "baseAddress": "0xE0042000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": DBGMCU_CR,
    }
}
