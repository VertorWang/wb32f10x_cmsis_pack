TIM_CR1 = {
    "name": "CR1",
    "displayName": "CR1",
    "description": "Timer control register 1",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CEN",
            "description": "Counter enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "UDIS",
            "description": "Update disable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "URS",
            "description": "Update request source",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "OPM",
            "description": "One pulse mode",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "DIR",
            "description": "Counter Direction",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "CMS",
            "description": "Center-aligned mode selection",
            "bitRange": "[6:5]",
        },
        "field_6": {
            "name": "ARPE",
            "description": "Auto-reload preload enable",
            "bitRange": "[7:7]",
        },
        "field_7": {
            "name": "CKD",
            "description": "Clock division",
            "bitRange": "[9:8]",
        }
    }
}

TIM_CR2_TIM1 = {
    "name": "CR2_TIM1",
    "displayName": "CR2_TIM1",
    "description": "Timer 1 control register 2",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCPC",
            "description": "Capture/compare preload control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CCUS",
            "description": "Capture/compare update selection",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CCDS",
            "description": "Capture/compare DMA selection",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "MMS",
            "description": "Master mode selection",
            "bitRange": "[6:4]",
            "enumeratedValues": {
                "name": "MasterMode_Select",
                "enumeratedValue_0": {
                    "name": "TIM_TRGOSource_Reset",
                    "description": "Timer reset event selected as trigger output",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "TIM_TRGOSource_Enable",
                    "description": "Timer enable event selected as trigger output",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "TIM_TRGOSource_Update",
                    "description": "Timer update event selected as trigger output",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "TIM_TRGOSource_OC1",
                    "description": "Timer capture/compare event selected as trigger output",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "TIM_TRGOSource_OC1Ref",
                    "description": "Timer channel 1 output compare event selected as trigger output",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "TIM_TRGOSource_OC2Ref",
                    "description": "Timer channel 2 output compare event selected as trigger output",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "TIM_TRGOSource_OC3Ref",
                    "description": "Timer channel 3 output compare event selected as trigger output",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "TIM_TRGOSource_OC4Ref",
                    "description": "Timer channel 4 output compare event selected as trigger output",
                    "value": "7",
                },
            }
        },
        "field_4": {
            "name": "TI1S",
            "description": "TI1 selection",
            "bitRange": "[7:7]",
        },
        "field_5": {
            "name": "OIS",
            "description": "Out idle state 1",
            "bitRange": "[8:8]",
        },
        "field_6": {
            "name": "OIS1N",
            "description": "Negative out idle state 1",
            "bitRange": "[9:9]",
        },
        "field_7": {
            "name": "OIS2",
            "description": "Out idle state 2",
            "bitRange": "[10:10]",
        },
        "field_8": {
            "name": "OIS2N",
            "description": "Negative out idle state 2",
            "bitRange": "[11:11]",
        },
        "field_9": {
            "name": "OIS3",
            "description": "Out idle state 1",
            "bitRange": "[12:12]",
        },
        "field_10": {
            "name": "OIS3N",
            "description": "Negative out idle state 3",
            "bitRange": "[13:13]",
        },
        "field_11": {
            "name": "OIS4",
            "description": "Out idle state 4",
            "bitRange": "[14:14]",
        }
    }
}

TIM_CR2 = {
    "name": "CR2",
    "displayName": "CR2",
    "description": "Timer control register 2",
    "alternateRegister": "CR2_TIM1",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCDS",
            "description": "Capture/compare DMA selection",
            "bitRange": "[3:3]",
        },
        "field_1": {
            "name": "MMS",
            "description": "Master mode selection",
            "bitRange": "[6:4]",
            "enumeratedValues": {
                "name": "MasterMode_Select",
                "enumeratedValue_0": {
                    "name": "TIM_TRGOSource_Reset",
                    "description": "Timer reset event selected as trigger output",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "TIM_TRGOSource_Enable",
                    "description": "Timer enable event selected as trigger output",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "TIM_TRGOSource_Update",
                    "description": "Timer update event selected as trigger output",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "TIM_TRGOSource_OC1",
                    "description": "Timer capture/compare event selected as trigger output",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "TIM_TRGOSource_OC1Ref",
                    "description": "Timer channel 1 output compare event selected as trigger output",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "TIM_TRGOSource_OC2Ref",
                    "description": "Timer channel 2 output compare event selected as trigger output",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "TIM_TRGOSource_OC3Ref",
                    "description": "Timer channel 3 output compare event selected as trigger output",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "TIM_TRGOSource_OC4Ref",
                    "description": "Timer channel 4 output compare event selected as trigger output",
                    "value": "7",
                },
            }
        },
        "field_2": {
            "name": "TI1S",
            "description": "TI1 selection",
            "bitRange": "[7:7]",
        }
    }
}

TIM_SMCR = {
    "name": "SMCR",
    "displayName": "SMCR",
    "description": "Timer slave mode control register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SMS",
            "description": "Slave mode selection",
            "bitRange": "[2:0]",
            "enumeratedValues": {
                "name": "SlaveMode_Select",
                "enumeratedValue_0": {
                    "name": "TIM_MasterSlaveMode_Disable",
                    "description": "Turn off slave mode",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "TIM_EncoderMode_TI1",
                    "description": "Encode mode 1",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "TIM_EncoderMode_TI2",
                    "description": "Encode mode2",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "TIM_EncoderMode_TI12",
                    "description": "Encode mode 3",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "TIM_SlaveMode_Reset",
                    "description": "Reset mode",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "TIM_SlaveMode_Gated",
                    "description": "Gated mode",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "TIM_SlaveMode_Trigger",
                    "description": "Trigger mode",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "TIM_SlaveMode_External1",
                    "description": "External clock mode",
                    "value": "7",
                },
            }
        },
        "field_1": {
            "name": "TS",
            "description": "Trigger selection",
            "bitRange": "[6:4]",
        },
        "field_2": {
            "name": "MSM",
            "description": "Master/slave mode",
            "bitRange": "[7:7]",
        },
        "field_3": {
            "name": "ETF",
            "description": "External trigger filter",
            "bitRange": "[11:8]",
        },
        "field_4": {
            "name": "ETPS",
            "description": "External trigger prescaler",
            "bitRange": "[13:12]",
        },
        "field_5": {
            "name": "ECE",
            "description": "External clock enable",
            "bitRange": "[14:14]",
        },
        "field_6": {
            "name": "ETP",
            "description": "External trigger polarity",
            "bitRange": "[15:15]",
        }
    }
}

TIM_DIER_TIM1 = {
    "name": "DIER_TIM1",
    "displayName": "DIER_TIM1",
    "description": "Timer 1 DMA/interruption enable register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UIE",
            "description": "Update interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1IE",
            "description": "Capture/Compare 1 interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2IE",
            "description": "Capture/Compare 2 interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3IE",
            "description": "Capture/Compare 3 interrupt enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4IE",
            "description": "Capture/Compare 4 interrupt enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "TIE",
            "description": "Trigger interrupt enable",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "BIE",
            "description": "Break interrupt enable",
            "bitRange": "[7:7]",
        },
        "field_7": {
            "name": "UDE",
            "description": "Update DMA request enable",
            "bitRange": "[8:8]",
        },
        "field_8": {
            "name": "CC1DE",
            "description": "Capture/Compare 1 DMA request enable",
            "bitRange": "[9:9]",
        },
        "field_9": {
            "name": "CC2DE",
            "description": "Capture/Compare 2 DMA request enable",
            "bitRange": "[10:10]",
        },
        "field_10": {
            "name": "CC3DE",
            "description": "Capture/Compare 3 DMA request enable",
            "bitRange": "[11:11]",
        },
        "field_11": {
            "name": "CC4DE",
            "description": "Capture/Compare 4 DMA request enable",
            "bitRange": "[12:12]",
        },
        "field_12": {
            "name": "COMDE",
            "description": "COM DMA request enable",
            "bitRange": "[13:13]",
        },
        "field_13": {
            "name": "TDE",
            "description": "Trigger DMA request enable",
            "bitRange": "[14:14]",
        },
    }
}

TIM_DIER = {
    "name": "DIER",
    "displayName": "DIER",
    "description": "Timer DMA/interruption enable register",
    "alternateRegister": "DIER_TIM1",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UIE",
            "description": "Update interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1IE",
            "description": "Capture/Compare 1 interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2IE",
            "description": "Capture/Compare 2 interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3IE",
            "description": "Capture/Compare 3 interrupt enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4IE",
            "description": "Capture/Compare 4 interrupt enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "TIE",
            "description": "Trigger interrupt enable",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "UDE",
            "description": "Update DMA request enable",
            "bitRange": "[8:8]",
        },
        "field_7": {
            "name": "CC1DE",
            "description": "Capture/Compare 1 DMA request enable",
            "bitRange": "[9:9]",
        },
        "field_8": {
            "name": "CC2DE",
            "description": "Capture/Compare 2 DMA request enable",
            "bitRange": "[10:10]",
        },
        "field_9": {
            "name": "CC3DE",
            "description": "Capture/Compare 3 DMA request enable",
            "bitRange": "[11:11]",
        },
        "field_10": {
            "name": "CC4DE",
            "description": "Capture/Compare 4 DMA request enable",
            "bitRange": "[12:12]",
        },
        "field_11": {
            "name": "TDE",
            "description": "Trigger DMA request enable",
            "bitRange": "[14:14]",
        },
    }
}

TIM_SR_TIM1 = {
    "name": "SR_TIM1",
    "displayName": "SR_TIM1",
    "description": "Timer 1 state register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UIF",
            "description": "Update interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1IF",
            "description": "Capture/Compare 1 interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2IF",
            "description": "Capture/Compare 2 interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3IF",
            "description": "Capture/Compare 3 interrupt flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4IF",
            "description": "Capture/Compare 4 interrupt flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "COMIF",
            "description": "COM interrupt flag",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "TIF",
            "description": "Trigger interrupt flag",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "BIF",
            "description": "Break interrupt flag",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "CC1OF",
            "description": "Capture/Compare 1 overcapture flag",
            "bitRange": "[9:9]",
        },
        "field_9": {
            "name": "CC2OF",
            "description": "Capture/Compare 2 overcapture flag",
            "bitRange": "[10:10]",
        },
        "field_10": {
            "name": "CC3OF",
            "description": "Capture/Compare 3 overcapture flag",
            "bitRange": "[11:11]",
        },
        "field_11": {
            "name": "CC4OF",
            "description": "Capture/Compare 4 overcapture flag",
            "bitRange": "[12:12]",
        }
    }
}

TIM_SR = {
    "name": "SR",
    "displayName": "SR",
    "description": "Timer state register",
    "alternateRegister": "SR_TIM1",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UIF",
            "description": "Update interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1IF",
            "description": "Capture/Compare 1 interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2IF",
            "description": "Capture/Compare 2 interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3IF",
            "description": "Capture/Compare 3 interrupt flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4IF",
            "description": "Capture/Compare 4 interrupt flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "TIF",
            "description": "Trigger interrupt flag",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "CC1OF",
            "description": "Capture/Compare 1 overcapture flag",
            "bitRange": "[9:9]",
        },
        "field_7": {
            "name": "CC2OF",
            "description": "Capture/Compare 2 overcapture flag",
            "bitRange": "[10:10]",
        },
        "field_8": {
            "name": "CC3OF",
            "description": "Capture/Compare 3 overcapture flag",
            "bitRange": "[11:11]",
        },
        "field_9": {
            "name": "CC4OF",
            "description": "Capture/Compare 4 overcapture flag",
            "bitRange": "[12:12]",
        }
    }
}

TIM_EGR_TIM1 = {
    "name": "EGR_TIM1",
    "displayName": "EGR_TIM1",
    "description": "Timer 1 event generation register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UG",
            "description": "Update generation",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1G",
            "description": "Capture/compare 1 generation",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2G",
            "description": "Capture/compare 2 generation",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3G",
            "description": "Capture/compare 3 generation",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4G",
            "description": "Capture/compare 4 generation",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "COMG",
            "description": "Capture/Compare control update generation",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "TG",
            "description": "Trigger generation",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "BG",
            "description": "Break generation",
            "bitRange": "[7:7]",
        }
    }
}

TIM_EGR = {
    "name": "EGR",
    "displayName": "EGR",
    "description": "Timer event generation register",
    "alternateRegister": "EGR_TIM1",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UG",
            "description": "Update generation",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1G",
            "description": "Capture/compare 1 generation",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2G",
            "description": "Capture/compare 2 generation",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC3G",
            "description": "Capture/compare 3 generation",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC4G",
            "description": "Capture/compare 4 generation",
            "bitRange": "[4:4]",
        },
        "field_6": {
            "name": "TG",
            "description": "Trigger generation",
            "bitRange": "[6:6]",
        }
    }
}

# 输出比较模式
TIM_CCMR1_OUTPUT = {
    "name": "CCMR1_OUTPUT",
    "displayName": "CCMR1_OUTPUT",
    "description": "Capture/compare mode register 1 for output",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC1S",
            "description": "Capture/Compare 1 selection",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "OC1FE",
            "description": "Output compare 1 fast enable",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "OC1PE",
            "description": "Output compare 1 preload enable",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "OC1M",
            "description": "Output compare 1 enable",
            "bitRange": "[6:4]",
        },
        "field_4": {
            "name": "OC1CE",
            "description": "Output compare 1 clear enable",
            "bitRange": "[7:7]",
        },
        "field_5": {
            "name": "CC2S",
            "description": "Capture/Compare 2 selection",
            "bitRange": "[9:8]",
        },
        "field_6": {
            "name": "OC2FE",
            "description": "Output compare 2 fast enable",
            "bitRange": "[10:10]",
        },
        "field_7": {
            "name": "OC2PE",
            "description": "Output compare 2 preload enable",
            "bitRange": "[11:11]",
        },
        "field_8": {
            "name": "OC2M",
            "description": "Output compare 2 enable",
            "bitRange": "[14:12]",
        },
        "field_9": {
            "name": "OC2CE",
            "description": "Output compare 2 clear enable",
            "bitRange": "[15:15]",
        }
    }
}

# 输入捕获模式
TIM_CCMR1_INPUT = {
    "name": "CCMR1_INPUT",
    "displayName": "CCMR1_INPUT",
    "description": "Capture/compare mode register 1 for input",
    "alternateRegister": "CCMR1_OUTPUT",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC1S",
            "description": "Capture/Compare 1 selection",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "IC1PSC",
            "description": "Input capture 1 prescaler",
            "bitRange": "[3:2]",
        },
        "field_2": {
            "name": "IC1F",
            "description": "Input capture 1 filter",
            "bitRange": "[7:4]",
        },
        "field_3": {
            "name": "CC2S",
            "description": "Capture/Compare 2 selection",
            "bitRange": "[9:8]",
        },
        "field_4": {
            "name": "IC2PSC",
            "description": "Input capture 2 prescaler",
            "bitRange": "[11:10]",
        },
        "field_5": {
            "name": "IC2F",
            "description": "Input capture 2 filter",
            "bitRange": "[15:12]",
        }
    }
}

# 输出比较模式
TIM_CCMR2_OUTPUT = {
    "name": "CCMR2_OUTPUT",
    "displayName": "CCMR2_OUTPUT",
    "description": "Capture/compare mode register 2 for output",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC3S",
            "description": "Capture/Compare 3 selection",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "OC3FE",
            "description": "Output compare 3 fast enable",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "OC3PE",
            "description": "Output compare 3 preload enable",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "OC3M",
            "description": "Output compare 3 enable",
            "bitRange": "[6:4]",
        },
        "field_4": {
            "name": "OC3CE",
            "description": "Output compare 3 clear enable",
            "bitRange": "[7:7]",
        },
        "field_5": {
            "name": "CC4S",
            "description": "Capture/Compare 4 selection",
            "bitRange": "[9:8]",
        },
        "field_6": {
            "name": "OC4FE",
            "description": "Output compare 4 fast enable",
            "bitRange": "[10:10]",
        },
        "field_7": {
            "name": "OC4PE",
            "description": "Output compare 4 preload enable",
            "bitRange": "[11:11]",
        },
        "field_8": {
            "name": "OC4M",
            "description": "Output compare 4 enable",
            "bitRange": "[14:12]",
        },
        "field_9": {
            "name": "OC4CE",
            "description": "Output compare 4 clear enable",
            "bitRange": "[15:15]",
        }
    }
}

# 输入捕获模式
TIM_CCMR2_INPUT = {
    "name": "CCMR2_INPUT",
    "displayName": "CCMR2_INPUT",
    "description": "Capture/compare mode register 2 for input",
    "alternateRegister": "CCMR2_OUTPUT",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC3S",
            "description": "Capture/Compare 3 selection",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "IC3PSC",
            "description": "Input capture 3 prescaler",
            "bitRange": "[3:2]",
        },
        "field_2": {
            "name": "IC3F",
            "description": "Input capture 3 filter",
            "bitRange": "[7:4]",
        },
        "field_3": {
            "name": "CC4S",
            "description": "Capture/Compare 4 selection",
            "bitRange": "[9:8]",
        },
        "field_4": {
            "name": "IC4PSC",
            "description": "Input capture 4 prescaler",
            "bitRange": "[11:10]",
        },
        "field_5": {
            "name": "IC4F",
            "description": "Input capture 4 filter",
            "bitRange": "[15:12]",
        }
    }
}

TIM_CCER_TIM1 = {
    "name": "CCER_TIM1",
    "displayName": "CCER_TIM1",
    "description": "Timer 1 capture/compare enable register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC1E",
            "description": "Capture/Compare 1 output enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1P",
            "description": "Capture/Compare 1 output polarity",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC1NE",
            "description": "Capture/Compare 1 negative output enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CC1NP",
            "description": "Capture/Compare 1 negative output polarity",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CC2E",
            "description": "Capture/Compare 2 output enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "CC2P",
            "description": "Capture/Compare 2 output polarity",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "CC2NE",
            "description": "Capture/Compare 2 negative output enable",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "CC2NP",
            "description": "Capture/Compare 2 negative output polarity",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "CC3E",
            "description": "Capture/Compare 3 output enable",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "CC3P",
            "description": "Capture/Compare 3 output polarity",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "CC3NE",
            "description": "Capture/Compare 3 negative output enable",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "CC3NP",
            "description": "Capture/Compare 3 negative output polarity",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "CC4E",
            "description": "Capture/Compare 4 output enable",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "CC4P",
            "description": "Capture/Compare 4 output polarity",
            "bitRange": "[13:13]",
        },
        "field_14": {
            "name": "CC4NE",
            "description": "Capture/Compare 4 negative output enable",
            "bitRange": "[14:14]",
        },
        "field_15": {
            "name": "CC4NP",
            "description": "Capture/Compare 4 negative output polarity",
            "bitRange": "[15:15]",
        }
    }
}

TIM_CCER = {
    "name": "CCER",
    "displayName": "CCER",
    "description": "Timer capture/compare enable register",
    "alternateRegister": "CCER_TIM1",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CC1E",
            "description": "Capture/Compare 1 output enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CC1P",
            "description": "Capture/Compare 1 output polarity",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CC2E",
            "description": "Capture/Compare 2 output enable",
            "bitRange": "[4:4]",
        },
        "field_3": {
            "name": "CC2P",
            "description": "Capture/Compare 2 output polarity",
            "bitRange": "[5:5]",
        },
        "field_4": {
            "name": "CC3E",
            "description": "Capture/Compare 3 output enable",
            "bitRange": "[8:8]",
        },
        "field_5": {
            "name": "CC3P",
            "description": "Capture/Compare 3 output polarity",
            "bitRange": "[9:9]",
        },
        "field_6": {
            "name": "CC4E",
            "description": "Capture/Compare 4 output enable",
            "bitRange": "[12:12]",
        },
        "field_7": {
            "name": "CC4P",
            "description": "Capture/Compare 4 output polarity",
            "bitRange": "[13:13]",
        }
    }
}

TIM_CNT = {
    "name": "CNT",
    "displayName": "CNT",
    "description": "Counter register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CNT",
            "description": "Counter value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_PSC = {
    "name": "PSC",
    "displayName": "PSC",
    "description": "Prescaler register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PSC",
            "description": "Prescaler value",
            "bitRange": "[15:0]",
        }
    }
}

TIM_ARR = {
    "name": "ARR",
    "displayName": "ARR",
    "description": "Auto reload register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ARR",
            "description": "Auto reload value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_RCR = {
    "name": "RCR",
    "displayName": "RCR",
    "description": "Repetition counter register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "REP",
            "description": "Repetition counter value",
            "bitRange": "[7:0]",
        }
    }
}

TIM_CCR1 = {
    "name": "CCR1",
    "displayName": "CCR1",
    "description": "Capture/compare 1 register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCR1",
            "description": "Capture/Compare 1 value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_CCR2 = {
    "name": "CCR2",
    "displayName": "CCR2",
    "description": "Capture/compare 2 register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCR2",
            "description": "Capture/Compare 2 value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_CCR3 = {
    "name": "CCR3",
    "displayName": "CCR3",
    "description": "Capture/compare 3 register",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCR3",
            "description": "Capture/Compare 3 value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_CCR4 = {
    "name": "CCR4",
    "displayName": "CCR4",
    "description": "Capture/compare 4 register",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CCR4",
            "description": "Capture/Compare 4 value",
            "bitRange": "[19:0]",
        }
    }
}

TIM_BDTR = {
    "name": "BDTR",
    "displayName": "BDTR",
    "description": "Break and dead-time register",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UTG",
            "description": "Dead-time generator setup",
            "bitRange": "[7:0]",
        },
        "field_1": {
            "name": "LOCK",
            "description": "Lock configuration",
            "bitRange": "[9:8]",
        },
        "field_2": {
            "name": "OSSI",
            "description": "Off-state selection for idle mode",
            "bitRange": "[10:10]",
        },
        "field_3": {
            "name": "OSSR",
            "description": "Off-state selection for Run mode",
            "bitRange": "[11:11]",
        },
        "field_4": {
            "name": "BKE",
            "description": "Break enable",
            "bitRange": "[12:12]",
        },
        "field_5": {
            "name": "BKP",
            "description": "Break polarity",
            "bitRange": "[13:13]",
        },
        "field_6": {
            "name": "AOE",
            "description": "Automatic output enable",
            "bitRange": "[14:14]",
        },
        "field_7": {
            "name": "MOE",
            "description": "Main output enable",
            "bitRange": "[15:15]",
        }
    }
}


tim1_define = {
    "name": "TIM1",
    "description": "Timer 1",
    "groupName": "TIM",
    "baseAddress": "0x40001C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "TIM1_BRK",
        "description": "TIM1 break interrupt",
        "value": "17",
    },
    "interrupt_1": {
        "name": "TIM1_UP",
        "description": "TIM1 update interrupt",
        "value": "18",
    },
    "interrupt_2": {
        "name": "TIM1_TRG_COM",
        "description": "TIM1 trigger or communication interrupt",
        "value": "19",
    },
    "interrupt_3": {
        "name": "TIM1_CC",
        "description": "TIM1 capture or compare interrupt",
        "value": "20",
    },
    "registers": {
        "register_0 ": TIM_CR1,
        "register_1 ": TIM_CR2_TIM1,
        "register_2 ": TIM_SMCR,
        "register_3 ": TIM_DIER_TIM1,
        "register_4 ": TIM_SR_TIM1,
        "register_5 ": TIM_EGR_TIM1,
        "register_6 ": TIM_CCMR1_OUTPUT,
        "register_7 ": TIM_CCMR1_INPUT,
        "register_8 ": TIM_CCMR2_OUTPUT,
        "register_9 ": TIM_CCMR2_INPUT,
        "register_10": TIM_CCER_TIM1,
        "register_11": TIM_CNT,
        "register_12": TIM_PSC,
        "register_13": TIM_ARR,
        "register_14": TIM_RCR,
        "register_15": TIM_CCR1,
        "register_16": TIM_CCR2,
        "register_17": TIM_CCR3,
        "register_18": TIM_CCR4,
        "register_19": TIM_BDTR,
    }
}


tim2_define = {
    "name": "TIM2",
    "description": "Timer 2",
    "groupName": "TIM",
    "baseAddress": "0x40002000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "TIM2",
        "description": "TIM2 interrupt",
        "value": "21",
    },
    "registers": {
        "register_0 ": TIM_CR1,
        "register_1 ": TIM_CR2,
        "register_2 ": TIM_SMCR,
        "register_3 ": TIM_DIER,
        "register_4 ": TIM_SR,
        "register_5 ": TIM_EGR,
        "register_6 ": TIM_CCMR1_OUTPUT,
        "register_7 ": TIM_CCMR1_INPUT,
        "register_8 ": TIM_CCMR2_OUTPUT,
        "register_9 ": TIM_CCMR2_INPUT,
        "register_10": TIM_CCER,
        "register_11": TIM_CNT,
        "register_12": TIM_PSC,
        "register_13": TIM_ARR,
        "register_14": TIM_RCR,
        "register_15": TIM_CCR1,
        "register_16": TIM_CCR2,
        "register_17": TIM_CCR3,
        "register_18": TIM_CCR4,
    }
}


tim3_define = {
    "name": "TIM3",
    "description": "Timer 3",
    "groupName": "TIM",
    "baseAddress": "0x40002400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "TIM3",
        "description": "TIM3 interrupt",
        "value": "22",
    },
    "registers": {
        "register_0 ": TIM_CR1,
        "register_1 ": TIM_CR2,
        "register_2 ": TIM_SMCR,
        "register_3 ": TIM_DIER,
        "register_4 ": TIM_SR,
        "register_5 ": TIM_EGR,
        "register_6 ": TIM_CCMR1_OUTPUT,
        "register_7 ": TIM_CCMR1_INPUT,
        "register_8 ": TIM_CCMR2_OUTPUT,
        "register_9 ": TIM_CCMR2_INPUT,
        "register_10": TIM_CCER,
        "register_11": TIM_CNT,
        "register_12": TIM_PSC,
        "register_13": TIM_ARR,
        "register_14": TIM_RCR,
        "register_15": TIM_CCR1,
        "register_16": TIM_CCR2,
        "register_17": TIM_CCR3,
        "register_18": TIM_CCR4,
    }
}


tim4_define = {
    "name": "TIM4",
    "description": "Timer 4",
    "groupName": "TIM",
    "baseAddress": "0x40002800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "TIM4",
        "description": "TIM4 interrupt",
        "value": "23",
    },
    "registers": {
        "register_0 ": TIM_CR1,
        "register_1 ": TIM_CR2,
        "register_2 ": TIM_SMCR,
        "register_3 ": TIM_DIER,
        "register_4 ": TIM_SR,
        "register_5 ": TIM_EGR,
        "register_6 ": TIM_CCMR1_OUTPUT,
        "register_7 ": TIM_CCMR1_INPUT,
        "register_8": TIM_CCMR2_OUTPUT,
        "register_9": TIM_CCMR2_INPUT,
        "register_10": TIM_CCER,
        "register_11": TIM_CNT,
        "register_12": TIM_PSC,
        "register_13": TIM_ARR,
        "register_14": TIM_RCR,
        "register_15": TIM_CCR1,
        "register_16": TIM_CCR2,
        "register_17": TIM_CCR3,
        "register_18": TIM_CCR4,
    }
}
