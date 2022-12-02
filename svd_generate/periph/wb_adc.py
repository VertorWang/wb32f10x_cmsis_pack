ADC_SR = {
    "name": "SR",
    "displayName": "SR",
    "description": "ADC status register",
    "addressOffset": "0x000",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "AWD",
            "description": "Analog watchdog flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "EOC",
            "description": "End of conversion",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "JEOC",
            "description": "Injected channel end of conversion",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "JSTRT",
            "description": "Injected channel Start flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "STRT",
            "description": "Regular channel Start flag",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "EMPF",
            "description": "Regular channel FIFO empty flag",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "OVF",
            "description": "Regular channel FIFO overflow flag",
            "bitRange": "[6:6]",
        }
    }
}


ADC_CR1 = {
    "name": "CR1",
    "displayName": "CR1",
    "description": "ADC control register 1",
    "addressOffset": "0x004",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "AWDCH",
            "description": "Analog watchdog channel select bits",
            "bitRange":"[4:0]",
            "enumeratedValues": {
                "name": "Channel_Select",
                "enumeratedValue_0": {
                    "name": "Channel",
                    "description": "Channel0",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Channel",
                    "description": "Channel1",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "Channel",
                    "description": "Channel2",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "Channel",
                    "description": "Channel3",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "Channel",
                    "description": "Channel4",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "Channel",
                    "description": "Channel5",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "Channel",
                    "description": "Channel6",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "Channel",
                    "description": "Channel7",
                    "value": "7",
                },
                "enumeratedValue_8": {
                    "name": "Channel",
                    "description": "Channel8",
                    "value": "8",
                },
                "enumeratedValue_9": {
                    "name": "Channel",
                    "description": "Channel9",
                    "value": "9",
                },
                "enumeratedValue_10": {
                    "name": "Channel",
                    "description": "Channel10",
                    "value": "10",
                },
                "enumeratedValue_11": {
                    "name": "Channel",
                    "description": "Channel11",
                    "value": "11",
                },
                "enumeratedValue_12": {
                    "name": "Channel",
                    "description": "Channel12",
                    "value": "12",
                },
                "enumeratedValue_13": {
                    "name": "Channel",
                    "description": "Channel13",
                    "value": "13",
                },
                "enumeratedValue_14": {
                    "name": "Channel",
                    "description": "Channel14",
                    "value": "14",
                },
                "enumeratedValue_15": {
                    "name": "Channel",
                    "description": "Channel15",
                    "value": "15",
                },
                "enumeratedValue_16": {
                    "name": "Channel",
                    "description": "Channel16",
                    "value": "16",
                },
                "enumeratedValue_17": {
                    "name": "Channel",
                    "description": "Channel17",
                    "value": "17",
                },
            }
        },

        "field_1": {
            "name": "EOCIE",
            "description": "Interrupt enable for EOC",
            "bitRange":"[5:5]",
        },

        "field_2": {
            "name": "AWDIE",
            "description": "Analog watchdog interrupt enable",
            "bitRange":"[6:6]",
        },

        "field_3": {
            "name": "JEOCIE",
            "description": "Interrupt enable for injected channels",
            "bitRange":"[7:7]",
        },

        "field_4": {
            "name": "SCAN",
            "description": "Scan mode",
            "bitRange":"[8:8]",
        },

        "field_5": {
            "name": "AWDSGL",
            "description": "Enable the watchdog on a single channel in scan mode",
            "bitRange":"[9:9]",
        },

        "field_6": {
            "name": "JAUTO",
            "description": "Automatic Injected Group conversion",
            "bitRange":"[10:10]",
        },

        "field_7": {
            "name": "DISCEN",
            "description": "Discontinuous mode on regular channels",
            "bitRange":"[11:11]",
        },

        "field_8": {
            "name": "JDISCEN",
            "description": "Discontinuous mode on injected channels",
            "bitRange":"[12:12]",
        },

        "field_9": {
            "name": "DISCNUM",
            "description": "Discontinuous mode channel count",
            "bitRange":"[15:13]",
            "enumeratedValues": {
                "name": "Channel_Count",
                "enumeratedValue_0": {
                    "name": "Channel_Count",
                    "description": "1Channel",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Channel_Count",
                    "description": "2Channel",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "Channel_Count",
                    "description": "3Channel",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "Channel_Count",
                    "description": "4Channel",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "Channel_Count",
                    "description": "5Channel",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "Channel_Count",
                    "description": "6Channel",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "Channel_Count",
                    "description": "7Channel",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "Channel_Count",
                    "description": "8Channel",
                    "value": "7",
                }
            }
        },

        "field_10": {
            "name": "JAWDEN",
            "description": "Analog watchdog enable on injected channels",
            "bitRange":"[22:22]",
        },

        "field_11": {
            "name": "AWDEN",
            "description": "Analog watchdog enable on regular channels",
            "bitRange":"[23:23]",
        }
    }
}


ADC_CR2 = {
    "name": "CR2",
    "displayName": "CR2",
    "description": "ADC control register 2",
    "addressOffset": "0x008",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ADON",
            "description": "A/D on-off controller",
            "bitRange":"[0:0]",
        },

        "field_1": {
            "name": "CONT",
            "description": "Continuous conversion",
            "bitRange":"[1:1]",
        },

        "field_2": {
            "name": "CAL",
            "description": "A/D calibration",
            "bitRange":"[2:2]",
        },

        "field_3": {
            "name": "RSTCAL",
            "description": "Reset calibration",
            "bitRange":"[3:3]",
        },

        "field_4": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange":"[7:4]",
        },

        "field_5": {
            "name": "DMAEN",
            "description": "Regular channel DMA enable",
            "bitRange":"[8:8]",
        },

        "field_6": {
            "name": "JDMAEN",
            "description": "Injected channel DMA enable",
            "bitRange":"[9:9]",
        },

        "field_7": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange":"[10:10]",
        },

        "field_8": {
            "name": "ALGN",
            "description": "Data alignment",
            "bitRange":"[11:11]",
        },

        "field_9": {
            "name": "JEXSEL",
            "description": "External event select for injected group",
            "bitRange":"[14:12]",
            "enumeratedValues": {
                "name": "Trigger_Select",
                "enumeratedValue_0": {
                    "name": "TIM1_TRGO",
                    "description": "Timer1 trigger output event",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "TIM1_CC4",
                    "description": "Timer1 channel_4 capture/compare event",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "TIM2_TRGO",
                    "description": "Timer2 trigger output event",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "TIM2_CC1",
                    "description": "Timer2 channel_1 capture/compare event",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "TIM3_CC4",
                    "description": "Timer3 channel_4 capture/compare event",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "TIM4_TRGO",
                    "description": "Timer4 trigger output event",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "EXTI15",
                    "description": "External line 15 event",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "JSWSTART",
                    "description": "Software start event for injected channels",
                    "value": "7",
                }
            }
        },

        "field_10": {
            "name": "JEXTTRIG",
            "description": "External trigger conversion mode for injected channels",
            "bitRange":"[15:15]",
        },

        "field_11": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange":"[16:16]",
        },

        "field_12": {
            "name": "EXTISEL",
            "description": "External event select for regular group",
            "bitRange":"[19:17]",
            "enumeratedValues": {
                "name": "Trigger_Select",
                "enumeratedValue_0": {
                    "name": "TIM1_CC1",
                    "description": "Timer1 channel_1 capture/compare event",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "TIM1_CC2",
                    "description": "Timer1 channel_2 capture/compare event",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "TIM1_CC3",
                    "description": "Timer1 channel_3 capture/compare event",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "TIM2_CC2",
                    "description": "Timer2 channel_2 capture/compare event",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "TIM3_TRGO",
                    "description": "Timer1 trigger output event",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "TIM4_CC4",
                    "description": "Timer4 channel_4 capture/compare event",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "EXTI11",
                    "description": "External line 11 event",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "SWSTART",
                    "description": "Software start event for regular channels",
                    "value": "7",
                }
            }
        },

        "field_13": {
            "name": "EXTTRIG",
            "description": "External trigger conversion mode for regular channels",
            "bitRange": "[20:20]",
        },

        "field_14": {
            "name": "JSWSTART",
            "description": "Start conversion of injected channels",
            "bitRange":"[21:21]",
        },

        "field_15": {
            "name": "SWSTART",
            "description": "Start conversion of regular channels",
            "bitRange":"[22:22]",
        },

        "field_16": {
            "name": "TSVREFE",
            "description": "Temperature sensor and VREFINT enable",
            "bitRange":"[23:23]",
        },

        "field_17": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange":"[31:24]",
        }
    }
}


ADC_SMPR1 = {
    "name": "FHSIENR",
    "displayName": "FHSIENR",
    "description": "FHSI enable SFR",
    "addressOffset": "0x038",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FHSION",
            "description": "Internal FHSI enable control",
            "bitRange":"[0:0]",
        }
    }
}


ADC_SMPR2 = {
    "name": "FHSISR",
    "displayName": "FHSISR",
    "description": "FHSI Status SFR",
    "addressOffset": "0x03C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FHSIRDY",
            "description": "Internal FHSI clock output status",
            "bitRange":"[0:0]",
        }
    }
}


ADC_JOFR = {
    "name": "LSIENR",
    "displayName": "LSIENR",
    "description": "LSI enable SFR",
    "addressOffset": "0x044",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSION",
            "description": "Internal LSI enable",
            "bitRange":"[0:0]",
        }
    }
}


ADC_LTR = {
    "name": "LSISR",
    "displayName": "LSISR",
    "description": "LSI Status SFR",
    "addressOffset": "0x048",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSIRDY",
            "description": "Internal LSI clock output Status",
            "bitRange":"[0:0]",
        }
    }
}


ADC_SQR1 = {
    "name": "HSECR0",
    "displayName": "HSECR0",
    "description": "HSE control SFR 0",
    "addressOffset": "0x04C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HSEON",
            "description": "HSE enable",
            "bitRange":"[0:0]",
        },
        "field_1": {
            "name": "BYPASS",
            "description": "External clock input mode enable",
            "bitRange":"[1:1]",
        }
    }
}


ADC_SQR2 = {
    "name": "HSECR1",
    "displayName": "HSECR1",
    "description": "HSE control SFR 1",
    "addressOffset": "0x050",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PADOEN",
            "description": "HSE clock loop back from PAD",
            "bitRange":"[1:1]",
        }
    }
}

ADC_SQR3 = {
    "name": "HSESR",
    "displayName": "HSESR",
    "description": "HSE Status SFR",
    "addressOffset": "0x058",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HSERDY",
            "description": "HSE clock output Status",
            "bitRange":"[0:0]",
        }
    }
}


ADC_JSQR = {
    "name": "PLLCR",
    "displayName": "PLLCR",
    "description": "PLL control SFR",
    "addressOffset": "0x074",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLMUL",
            "description": "PLL multiplier factor",
            "bitRange":"[7:6]",
        }
    }
}


ADC_SQR = {
    "name": "PLLENR",
    "displayName": "PLLENR",
    "description": "PLL enable control",
    "addressOffset": "0x078",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLON",
            "description": "PLL enable control",
            "bitRange":"[0:0]",
        }
    }
}


ADC_DR = {
    "name": "PLLSR",
    "displayName": "PLLSR",
    "description": "PLL Status SFR",
    "addressOffset": "0x07C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLLRDY",
            "description": "PLL clock output Status",
            "bitRange":"[1:0]",
        }
    }
}


ADC_CR3 = {
    "name": "PVDCR",
    "displayName": "PVDCR",
    "description": "PVD control SFR",
    "addressOffset": "0x080",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000004",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PLS",
            "description": "PVD threshold voltage selection",
            "bitRange":"[2:0]",
        }
    }
}


ADC_JDMAR = {
    "name": "PVDENR",
    "displayName": "PVDENR",
    "description": "PVD enable SFR",
    "addressOffset": "0x084",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PVDE",
            "description": "PVD enable control",
            "bitRange":"[0:0]",
        }
    }
}


adc_define = {
    "name": "ADC",
    "description": "Analog to digital conversion",
    "groupName": "ADC",
    "baseAddress": "0x40003C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": ADC_SR,
        "register_1": ADC_CR1,
        "register_2": ADC_CR2,
        "register_3": ADC_SMPR1,
        "register_4": ADC_SMPR2,
        "register_5": ADC_JOFR,
        "register_6": ADC_LTR,
        "register_7": ADC_SQR1,
        "register_8": ADC_SQR2,
        "register_9": ADC_SQR3,
        "register_10": ADC_JSQR,
        "register_11": ADC_SQR,
        "register_12": ADC_DR,
        "register_13": ADC_CR3,
        "register_14": ADC_JDMAR,
    }
}