GPIO_MODER = {
    "name": "MODER",
    "displayName": "MODER",
    "description": "GPIO port mode register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "2",
            "dimIndex": "0-15",
            "name": "MODER%s",
            "description": "Port x configuration bits %s",
            "bitRange": "[1:0]",
            "enumeratedValues": {
                "name": "GPIO_Mode",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "Input",
                    "description": "Input mode",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Output",
                    "description": "General purpose output mode",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "Alternate",
                    "description": "Alternate function mode",
                    "value": "2",
                },
                "enumeratedValue_3": {
                    "name": "Analog",
                    "description": "Analog mode",
                    "value": "3",
                },
            }
        }
    }
}

GPIO_OTYPER = {
    "name": "OTYPER",
    "displayName": "OTYPER",
    "description": "GPIO port output type register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "OTYPE%s",
            "description": "Port x configuration bits %s",
            "bitRange": "[0:0]",
            "enumeratedValues": {
                "name": "GPIO_Otype",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "Push-Pull",
                    "description": "Output push-pull",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Open-Drain",
                    "description": "Output open-drain",
                    "value": "1",
                }
            }
        }
    }
}

GPIO_OSPEEDR = {
    "name": "OSPEEDR",
    "displayName": "OSPEEDR",
    "description": "GPIO port output speed register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "2",
            "dimIndex": "0-15",
            "name": "OSPEEDR%s",
            "description": "Port x configuration bits %s",
            "bitRange": "[1:0]",
            "enumeratedValues": {
                "name": "GPIO_Speed",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "Speed",
                    "description": "High speed",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Speed",
                    "description": "Low speed",
                    "value": "1",
                }
            }
        }
    }
}

GPIO_PUPDR = {
    "name": "PUPDR",
    "displayName": "PUPDR",
    "description": "GPIO port pull-up/pull-down register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "2",
            "dimIndex": "0-15",
            "name": "PUPDR%s",
            "description": "Port x configuration bits %s",
            "bitRange": "[1:0]",
            "enumeratedValues": {
                "name": "GPIO_Pupd",
                "usage": "read-write",
                "enumeratedValue_0": {
                    "name": "Pull",
                    "description": "No pull-up or pull-down",
                    "value": "0",
                },
                "enumeratedValue_1": {
                    "name": "Pull",
                    "description": "Pull-up",
                    "value": "1",
                },
                "enumeratedValue_2": {
                    "name": "Pull",
                    "description": "Pull-down",
                    "value": "1",
                },
                "enumeratedValue_3": {
                    "name": "Pull",
                    "description": "Reserved",
                    "value": "3",
                },
            }
        }
    }
}

GPIO_IDR = {
    "name": "IDR",
    "displayName": "IDR",
    "description": "GPIO port input data register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "IDR%s",
            "description": "Port input data %s",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

GPIO_ODR = {
    "name": "ODR",
    "displayName": "ODR",
    "description": "GPIO port output data register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "0DR%s",
            "description": "Port putput data %s",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

GPIO_BSRR = {
    "name": "BSRR",
    "displayName": "BSRR",
    "description": "GPIO port bit set/reset register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "BS%s",
            "description": "Port x set bit %s",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "BR%s",
            "description": "Port x reset bit %s",
            "bitOffset": "16",
            "bitWidth": "1",
        }
    }
}

GPIO_LCKR = {
    "name": "LCKR",
    "displayName": "LCKR",
    "description": "GPIO port configuration lock register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "LCK%s",
            "description": "Port x lock bit %s",
            "bitOffset": "0",
            "bitWidth": "1",
        },
        "field_1": {
            "name": "LCKK",
            "description": "This bit can be read any time. It can only be modified using the lock key write sequence",
            "bitOffset": "16",
            "bitWidth": "1",
        }
    }
}

GPIO_AFRL = {
    "name": "AFRL",
    "displayName": "AFRL",
    "description": "GPIO alternate function low register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "8",
            "dimIncrement": "4",
            "dimIndex": "0-7",
            "name": "AFR%s",
            "description": "Alternate function selection for port x pin %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}

GPIO_AFRH = {
    "name": "AFRH",
    "displayName": "AFRH",
    "description": "GPIO alternate function high register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "8",
            "dimIncrement": "4",
            "dimIndex": "8-15",
            "name": "AFR%s",
            "description": "Alternate function selection for port x pin %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}

GPIO_SMIT = {
    "name": "SMIT",
    "displayName": "SMIT",
    "description": "GPIO Port Schmitt Register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000007",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "SMIT%s",
            "description": "Port x configuration bit %s",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

GPIO_CURRENT = {
    "name": "CURRENT",
    "displayName": "CURRENT",
    "description": "GPIO Port driver register",
    "addressOffset": "0X2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "2",
            "dimIndex": "0-15",
            "name": "CURRENT%s",
            "description": "Port x configuration bits %s",
            "bitOffset": "0",
            "bitWidth": "2",
        }
    }
}

GPIO_CFGMSK = {
    "name": "CFGMSK",
    "displayName": "CFGMSK",
    "description": "GPIO Port configuration auxiliary register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "16",
            "dimIncrement": "1",
            "dimIndex": "0-15",
            "name": "CFGMSK%s",
            "description": "Port x lock bit %s",
            "bitOffset": "0",
            "bitWidth": "1",
        }
    }
}

AFIO_EXTICR1 = {
    "name": "EXTICR1",
    "displayName": "EXTICR1",
    "description": "External interrupt configuration register 1",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "4",
            "dimIncrement": "4",
            "dimIndex": "0-3",
            "name": "EXTI%s",
            "description": "EXTI x configuration %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}

AFIO_EXTICR2 = {
    "name": "EXTICR2",
    "displayName": "EXTICR2",
    "description": "External interrupt configuration register 2",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "4",
            "dimIncrement": "4",
            "dimIndex": "4-7",
            "name": "EXTI%s",
            "description": "EXTI x configuration %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}

AFIO_EXTICR3 = {
    "name": "EXTICR3",
    "displayName": "EXTICR3",
    "description": "External interrupt configuration register 3",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "4",
            "dimIncrement": "4",
            "dimIndex": "8-11",
            "name": "EXTI%s",
            "description": "EXTI x configuration %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}

AFIO_EXTICR4 = {
    "name": "EXTICR4",
    "displayName": "EXTICR4",
    "description": "External interrupt configuration register 4",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "fields": {
        "field_0": {
            "dim": "4",
            "dimIncrement": "4",
            "dimIndex": "12-15",
            "name": "EXTI%s",
            "description": "EXTI x configuration %s",
            "bitOffset": "0",
            "bitWidth": "4",
        }
    }
}




afio_define = {
    "name": "AFIO",
    "description": "AFIO registers",
    "groupName": "AFIO",
    "baseAddress": "0x40001400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": AFIO_EXTICR1,
        "register_1": AFIO_EXTICR2,
        "register_2": AFIO_EXTICR3,
        "register_3": AFIO_EXTICR4,
    }
}


gpioa_define = {
    "name": "GPIOA",
    "description": "General-purpose and alternate-function I/O",
    "groupName": "GPIO",
    "baseAddress": "0x40000000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": GPIO_MODER,
        "register_1": GPIO_OTYPER,
        "register_2": GPIO_OSPEEDR,
        "register_3": GPIO_PUPDR,
        "register_4": GPIO_IDR,
        "register_5": GPIO_ODR,
        "register_6": GPIO_BSRR,
        "register_7": GPIO_LCKR,
        "register_8": GPIO_AFRL,
        "register_9": GPIO_AFRH,
        "register_10": GPIO_SMIT,
        "register_11": GPIO_CURRENT,
        "register_12": GPIO_CFGMSK,
    }
}


gpiob_define = {
    "name": "GPIOB",
    "description": "General-purpose and alternate-function I/O",
    "groupName": "GPIO",
    "baseAddress": "0x40000400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": GPIO_MODER,
        "register_1": GPIO_OTYPER,
        "register_2": GPIO_OSPEEDR,
        "register_3": GPIO_PUPDR,
        "register_4": GPIO_IDR,
        "register_5": GPIO_ODR,
        "register_6": GPIO_BSRR,
        "register_7": GPIO_LCKR,
        "register_8": GPIO_AFRL,
        "register_9": GPIO_AFRH,
        "register_10": GPIO_SMIT,
        "register_11": GPIO_CURRENT,
        "register_12": GPIO_CFGMSK,
    }
}


gpioc_define = {
    "name": "GPIOC",
    "description": "General-purpose and alternate-function I/O",
    "groupName": "GPIO",
    "baseAddress": "0x40000800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": GPIO_MODER,
        "register_1": GPIO_OTYPER,
        "register_2": GPIO_OSPEEDR,
        "register_3": GPIO_PUPDR,
        "register_4": GPIO_IDR,
        "register_5": GPIO_ODR,
        "register_6": GPIO_BSRR,
        "register_7": GPIO_LCKR,
        "register_8": GPIO_AFRL,
        "register_9": GPIO_AFRH,
        "register_10": GPIO_SMIT,
        "register_11": GPIO_CURRENT,
        "register_12": GPIO_CFGMSK,
    }
}


gpiod_define = {
    "name": "GPIOD",
    "description": "General-purpose and alternate-function I/O",
    "groupName": "GPIO",
    "baseAddress": "0x40000C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "registers": {
        "register_0": GPIO_MODER,
        "register_1": GPIO_OTYPER,
        "register_2": GPIO_OSPEEDR,
        "register_3": GPIO_PUPDR,
        "register_4": GPIO_IDR,
        "register_5": GPIO_ODR,
        "register_6": GPIO_BSRR,
        "register_7": GPIO_LCKR,
        "register_8": GPIO_AFRL,
        "register_9": GPIO_AFRH,
        "register_10": GPIO_SMIT,
        "register_11": GPIO_CURRENT,
        "register_12": GPIO_CFGMSK,
    }
}


