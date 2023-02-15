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
            "bitRange": "[4:0]",
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
            "bitRange": "[5:5]",
        },

        "field_2": {
            "name": "AWDIE",
            "description": "Analog watchdog interrupt enable",
            "bitRange": "[6:6]",
        },

        "field_3": {
            "name": "JEOCIE",
            "description": "Interrupt enable for injected channels",
            "bitRange": "[7:7]",
        },

        "field_4": {
            "name": "SCAN",
            "description": "Scan mode",
            "bitRange": "[8:8]",
        },

        "field_5": {
            "name": "AWDSGL",
            "description": "Enable the watchdog on a single channel in scan mode",
            "bitRange": "[9:9]",
        },

        "field_6": {
            "name": "JAUTO",
            "description": "Automatic Injected Group conversion",
            "bitRange": "[10:10]",
        },

        "field_7": {
            "name": "DISCEN",
            "description": "Discontinuous mode on regular channels",
            "bitRange": "[11:11]",
        },

        "field_8": {
            "name": "JDISCEN",
            "description": "Discontinuous mode on injected channels",
            "bitRange": "[12:12]",
        },

        "field_9": {
            "name": "DISCNUM",
            "description": "Discontinuous mode channel count",
            "bitRange": "[15:13]",
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
            "bitRange": "[22:22]",
        },

        "field_11": {
            "name": "AWDEN",
            "description": "Analog watchdog enable on regular channels",
            "bitRange": "[23:23]",
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
            "bitRange": "[0:0]",
        },

        "field_1": {
            "name": "CONT",
            "description": "Continuous conversion",
            "bitRange": "[1:1]",
        },

        "field_2": {
            "name": "CAL",
            "description": "A/D calibration",
            "bitRange": "[2:2]",
        },

        "field_3": {
            "name": "RSTCAL",
            "description": "Reset calibration",
            "bitRange": "[3:3]",
        },

        "field_4": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange": "[7:4]",
        },

        "field_5": {
            "name": "DMAEN",
            "description": "Regular channel DMA enable",
            "bitRange": "[8:8]",
        },

        "field_6": {
            "name": "JDMAEN",
            "description": "Injected channel DMA enable",
            "bitRange": "[9:9]",
        },

        "field_7": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange": "[10:10]",
        },

        "field_8": {
            "name": "ALGN",
            "description": "Data alignment",
            "bitRange": "[11:11]",
        },

        "field_9": {
            "name": "JEXSEL",
            "description": "External event select for injected group",
            "bitRange": "[14:12]",
            "enumeratedValues": {
                "name": "External_Trigger_Selection_Injected",
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
            "bitRange": "[15:15]",
        },

        "field_11": {
            "name": "RESERVED",
            "description": "RESERVED",
            "bitRange": "[16:16]",
        },

        "field_12": {
            "name": "EXTISEL",
            "description": "External event select for regular group",
            "bitRange": "[19:17]",
            "enumeratedValues": {
                "name": "External_Trigger_Selection_Regular",
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
            "bitRange": "[21:21]",
        },

        "field_15": {
            "name": "SWSTART",
            "description": "Start conversion of regular channels",
            "bitRange": "[22:22]",
        },

        "field_16": {
            "name": "TSVREFE",
            "description": "Temperature sensor and VREFINT enable",
            "bitRange": "[23:23]",
        }
    }
}


ADC_SMPR1 = {
    "name": "SMPR1",
    "displayName": "SMPR1",
    "description": "ADC sample time register 1",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "dim": "8",
            "dimIncrement": "3",
            "dimIndex": "10-17",
            "name": "SMP%s",
            "description": "ADC Channel %s Sample time selection",
            "bitRange": "[2:0]",
            "enumeratedValues": {
                "name": "ADC_SampleTime",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "SampleTime",
                    "description": "SampleTime 1.5 cycles",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "SampleTime",
                    "description": "SampleTime 7.5 cycles",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "SampleTime",
                    "description": "SampleTime 13.5 cycles",
                    "value": "1",
                },
                "enumeratedValue_3": {
                    "name": "SampleTime",
                    "description": "SampleTime 28.5 cycles",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "SampleTime",
                    "description": "SampleTime 41.5 cycles",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "SampleTime",
                    "description": "SampleTime 55.5 cycles",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "SampleTime",
                    "description": "SampleTime 71.5 cycles",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "SampleTime",
                    "description": "SampleTime 239.5 cycles",
                    "value": "7",
                },        
            }
        }
    }
}


ADC_SMPR2 = {
    "name": "SMPR2",
    "displayName": "SMPR2",
    "description": "ADC sample time register 2",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "dim": "10",
            "dimIncrement": "3",
            "dimIndex": "0-9",
            "name": "SMP%s",
            "description": "ADC Channel %s Sample time selection",
            "bitRange": "[2:0]",
            "enumeratedValues": {
                "name": "ADC_SampleTime",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "SampleTime",
                    "description": "SampleTime 1.5 cycles",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "SampleTime",
                    "description": "SampleTime 7.5 cycles",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "SampleTime",
                    "description": "SampleTime 13.5 cycles",
                    "value": "1",
                },
                "enumeratedValue_3": {
                    "name": "SampleTime",
                    "description": "SampleTime 28.5 cycles",
                    "value": "3",
                },
                "enumeratedValue_4": {
                    "name": "SampleTime",
                    "description": "SampleTime 41.5 cycles",
                    "value": "4",
                },
                "enumeratedValue_5": {
                    "name": "SampleTime",
                    "description": "SampleTime 55.5 cycles",
                    "value": "5",
                },
                "enumeratedValue_6": {
                    "name": "SampleTime",
                    "description": "SampleTime 71.5 cycles",
                    "value": "6",
                },
                "enumeratedValue_7": {
                    "name": "SampleTime",
                    "description": "SampleTime 239.5 cycles",
                    "value": "7",
                },        
            }
        }
    }
}

ADC_JOFR1 = {
    "name": "JOFR1",
    "displayName": "JOFR1",
    "description": "ADC injected channel data offset register 1",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JOFFSET1",
            "description": "Data offset for injected channel 1",
            "bitRange": "[11:0]",
        }
    }
}

ADC_JOFR2 = {
    "name": "JOFR2",
    "displayName": "JOFR2",
    "description": "ADC injected channel data offset register 2",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JOFFSET2",
            "description": "Data offset for injected channel 2",
            "bitRange": "[11:0]",
        }
    }
}

ADC_JOFR3 = {
    "name": "JOFR3",
    "displayName": "JOFR3",
    "description": "ADC injected channel data offset register 3",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JOFFSET3",
            "description": "Data offset for injected channel 3",
            "bitRange": "[11:0]",
        }
    }
}

ADC_JOFR4 = {
    "name": "JOFR4",
    "displayName": "JOFR4",
    "description": "ADC injected channel data offset register 4",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JOFFSET4",
            "description": "Data offset for injected channel 4",
            "bitRange": "[11:0]",
        }
    }
}

ADC_HTR = {
    "name": "HTR",
    "displayName": "HTR",
    "description": "ADC watchdog high threshold register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000FFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HT",
            "description": "Analog watchdog high threshold",
            "bitRange": "[11:0]",
        }
    }
}


ADC_LTR = {
    "name": "LTR",
    "displayName": "LTR",
    "description": "ADC watchdog low threshold register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LT",
            "description": "Analog watchdog low threshold",
            "bitRange": "[11:0]",
        }
    }
}


ADC_SQR1 = {
    "name": "SQR1",
    "displayName": "SQR1",
    "description": "ADC regular sequence register 1",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "dim": "4",
            "dimIncrement": "5",
            "dimIndex": "13-16",
            "name": "SQ%s",
            "description": "%sth conversion in regular sequence",
            "bitRange": "[4:0]",
        },
        "field_1": {
            "name": "Length",
            "description": "Regular channel sequence length",
            "bitRange": "[23:20]",
        }
    }
}


ADC_SQR2 = {
    "name": "SQR2",
    "displayName": "SQR2",
    "description": "ADC regular sequence register 2",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "dim": "6",
            "dimIncrement": "5",
            "dimIndex": "7-12",
            "name": "SQ%s",
            "description": "%sth conversion in regular sequence",
            "bitRange": "[4:0]",
        },
    }
}


ADC_SQR3 = {
    "name": "SQR3",
    "displayName": "SQR3",
    "description": "ADC regular sequence register 3",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "dim": "6",
            "dimIncrement": "5",
            "dimIndex": "1-6",
            "name": "SQ%s",
            "description": "%sth conversion in regular sequence",
            "bitRange": "[4:0]",
        },
    }
}


ADC_JSQR = {
    "name": "JSQR",
    "displayName": "JSQR",
    "description": "ADC injected sequence register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JSQ1",
            "description": "1st conversion in injected sequence",
            "bitRange": "[4:0]",
        },
        "field_1": {
            "name": "JSQ2",
            "description": "2st conversion in injected sequence",
            "bitRange": "[9:5]",
        },
        "field_2": {
            "name": "JSQ3",
            "description": "3st conversion in injected sequence",
            "bitRange": "[14:10]",
        },
        "field_3": {
            "name": "JSQ4",
            "description": "4st conversion in injected sequence",
            "bitRange": "[19:15]",
        },
        "field_4": {
            "name": "JL",
            "description": "Injected sequence length",
            "bitRange": "[21:20]",
            "enumeratedValues": {
                "name": "InjectedSequence_Length",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "Length",
                    "description": "1 conversion",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Length",
                    "description": "2 conversions",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "Length",
                    "description": "3 conversions",
                    "value": "1",
                },
                "enumeratedValue_3": {
                    "name": "Length",
                    "description": "4 conversions",
                    "value": "3",
                },      
            }
        }
    }
}


ADC_JDR = {
    "dim": "4",
    "dimIncrement": "4",
    "dimIndex": "1-4",
    "name": "JDR%s",
    "displayName": "JDR%s",
    "description": "ADC injected data register %s",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JDATA%s",
            "description": "Injected data %s",
            "bitRange": "[15:0]",
        }
    }
}


ADC_DR = {
    "name": "DR",
    "displayName": "DR",
    "description": "ADC regular data register",
    "addressOffset": "0x4C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DATA",
            "description": "Regular data",
            "bitRange": "[15:0]",
        }
    }
}


ADC_CR3 = {
    "name": "CR3",
    "displayName": "CR3",
    "description": "ADC control register 3",
    "addressOffset": "0x54",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000004",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ADVMODE",
            "description": "Advance mode config",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "SAMCHN",
            "description": "SAMCHN bits",
            "bitRange": "[3:2]",
        },
        "field_2": {
            "name": "12BIT",
            "description": "12-bit enable",
            "bitRange": "[6:6]",
        },
        "field_3": {
            "name": "ADC_PRS",
            "description": "Prescaler to the apb clock input",
            "bitRange": "[15:8]",
        },
        "field_4": {
            "name": "OVFIE",
            "description": "ADC fifo overflow interrupt enable",
            "bitRange": "[16:16]",
        },
        "field_5": {
            "name": "EMPIE",
            "description": "ADC fifo empty interrupt enable",
            "bitRange": "[17:17]",
        }
    }
}


ADC_JDMAR = {
    "name": "JDMAR",
    "displayName": "JDMAR",
    "description": "Injected data",
    "addressOffset": "0x58",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "JDMAR",
            "description": "Injected data",
            "bitRange": "[15:0]",
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
    "interrupt_0": {
        "name": "ADC",
        "description": "Analog/Digital conversion interrupt",
        "value": "13",
    },
    "registers": {
        "register_0 ": ADC_SR,
        "register_1 ": ADC_CR1,
        "register_2 ": ADC_CR2,
        "register_3 ": ADC_SMPR1,
        "register_4 ": ADC_SMPR2,
        "register_6 ": ADC_JOFR1,
        "register_7 ": ADC_JOFR2,
        "register_8 ": ADC_JOFR3,
        "register_9 ": ADC_JOFR4,
        "register_10": ADC_HTR,
        "register_11": ADC_LTR,
        "register_12": ADC_SQR1,
        "register_13": ADC_SQR2,
        "register_14": ADC_SQR3,
        "register_15": ADC_JSQR,
        "register_16": ADC_JDR,
        "register_17": ADC_DR,
        "register_18": ADC_CR3,
        "register_19": ADC_JDMAR,
    }
}
