USB_INTRIN = {
    "name": "INTRIN",
    "displayName": "INTRIN",
    "description": "IN endpoint interrupt flag register",
    "addressOffset": "0x02",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EP0",
            "description": "Endpoint 0 interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "IN1",
            "description": "IN endpoint 1 interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "IN2",
            "description": "IN endpoint 2 interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "IN3",
            "description": "IN endpoint 3 interrupt flag",
            "bitRange": "[3:3]",
        }
    }
}

USB_INTROUT = {
    "name": "INTROUT",
    "displayName": "INTROUT",
    "description": "OUT endpoint interrupt flag register",
    "addressOffset": "0x04",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EP0",
            "description": "Endpoint 0 interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "OUT1",
            "description": "OUT endpoint 1 interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "OUT2",
            "description": "OUT endpoint 2 interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "OUT3",
            "description": "OUT endpoint 3 interrupt flag",
            "bitRange": "[3:3]",
        }
    }
}

USB_INTRUSB = {
    "name": "INTRUSB",
    "displayName": "INTRUSB",
    "description": "USB interrupt flag register",
    "addressOffset": "0x06",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SUSIS",
            "description": "Suspend interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RSUIS",
            "description": "Restore interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RSTIS",
            "description": "Reset interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SOFIS",
            "description": "Start of frame interrupt flag",
            "bitRange": "[3:3]",
        }
    }
}

USB_INTRINE = {
    "name": "INTRINE",
    "displayName": "INTRINE",
    "description": "IN endpoint interrupt enable register",
    "addressOffset": "0x07",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x0000000F",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EP0E",
            "description": "Endpoint 0 interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "IN1E",
            "description": "IN endpoint 1 interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "IN2E",
            "description": "IN endpoint 2 interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "IN3E",
            "description": "IN endpoint 3 interrupt enable",
            "bitRange": "[3:3]",
        }
    }
}

USB_INTROUTE = {
    "name": "INTROUTE",
    "displayName": "INTROUTE",
    "description": "OUT endpoint interrupt enable register",
    "addressOffset": "0x09",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x0000000E",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUT1E",
            "description": "OUT endpoint 1 interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_1": {
            "name": "OUT2E",
            "description": "OUT endpoint 2 interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "OUT3E",
            "description": "OUT endpoint 3 interrupt enable",
            "bitRange": "[3:3]",
        }
    }
}

USB_INTRUSBE = {
    "name": "INTRUSBE",
    "displayName": "INTRUSBE",
    "description": "USB interrupt enable register",
    "addressOffset": "0x0B",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000006",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SUSIE",
            "description": "Suspend interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RSUIE",
            "description": "Restore interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RSTIE",
            "description": "Reset interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SOFIE",
            "description": "Start of frame interrupt enable",
            "bitRange": "[3:3]",
        }
    }
}

USB_FADDR = {
    "name": "FADDR",
    "displayName": "FADDR",
    "description": "Function address register",
    "addressOffset": "0x00",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FADDR",
            "description": "Function address",
            "bitRange": "[6:0]",
        },
        "field_1": {
            "name": "UPDATE",
            "description": "Function address update bit",
            "bitRange": "[7:7]",
        }
    }
}

USB_POWER = {
    "name": "POWER",
    "displayName": "POWER",
    "description": "USB power register",
    "addressOffset": "0x01",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SUSEN",
            "description": "Suspend mode enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SUSMD",
            "description": "Suspend mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RESUME",
            "description": "Resume",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "USBRST",
            "description": "USB reset detect",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "ISOUD",
            "description": "ISO update bit",
            "bitRange": "[7:7]",
        }
    }
}

USB_FRAMEL = {
    "name": "FRAMEL",
    "displayName": "FRAMEL",
    "description": "Frame low byte register",
    "addressOffset": "0x0C",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FRAMEL",
            "description": "Frame low byte",
            "bitRange": "[7:0]",
        }
    }
}

USB_FRAMEH = {
    "name": "FRAMEH",
    "displayName": "FRAMEH",
    "description": "Frame high byte register",
    "addressOffset": "0x0D",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FRAMEL",
            "description": "Frame high byte",
            "bitRange": "[7:0]",
        }
    }
}

USB_INDEX = {
    "name": "INDEX",
    "displayName": "INDEX",
    "description": "Endpoint index register",
    "addressOffset": "0x0E",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "EPSEL",
            "description": "Endpoint selection",
            "bitRange": "[3:0]",
        }
    }
}

USB_FIFO0 = {
    "name": "FIFO0",
    "displayName": "FIFO0",
    "description": "Endpoint 0 FIFO register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FIFODATA",
            "description": "FIFO data",
            "bitRange": "[7:0]",
        }
    }
}

USB_FIFO1 = {
    "name": "FIFO1",
    "displayName": "FIFO1",
    "description": "Endpoint 1 FIFO register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FIFODATA",
            "description": "FIFO data",
            "bitRange": "[7:0]",
        }
    }
}

USB_FIFO2 = {
    "name": "FIFO2",
    "displayName": "FIFO2",
    "description": "Endpoint 2 FIFO register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FIFODATA",
            "description": "FIFO data",
            "bitRange": "[7:0]",
        }
    }
}

USB_FIFO3 = {
    "name": "FIFO3",
    "displayName": "FIFO3",
    "description": "Endpoint 3 FIFO register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FIFODATA",
            "description": "FIFO data",
            "bitRange": "[7:0]",
        }
    }
}

USB_INMAXP = {
    "name": "INMAXP",
    "displayName": "INMAXP",
    "description": "Maxium packet size for IN endpoint register",
    "addressOffset": "0x10",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INMAXP",
            "description": "Maximum Packet Size/transaction for IN endpoint",
            "bitRange": "[7:0]",
        }
    }
}

USB_CSR0 = {
    "name": "CSR0",
    "displayName": "CSR0",
    "description": "Endpoint 0 control and status register",
    "addressOffset": "0x11",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUTPKTRDY",
            "description": "Receive a data packet",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "INPKTRDY",
            "description": "Sets this bit after loading a data packet into the FIFO",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SENTSTALL",
            "description": "This bit is set by hardware when a STALL handshake is transmitted",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "DATAEND",
            "description": "Data end",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SETUPEND",
            "description": "Setup end",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "SENDSTALL",
            "description": "Set this bit to terminate the current transaction",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "SVDOUTPKTRDY",
            "description": "Clear OUTPKTRDY bit",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "SVDSETUPEND",
            "description": "Clear SETUPEND bit",
            "bitRange": "[7:7]",
        }
    }
}

USB_INCSR1 = {
    "name": "INCSR1",
    "displayName": "INCSR1",
    "description": "IN endpoint 1 control and status register",
    "alternateRegister": "CSR0",
    "addressOffset": "0x11",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000020",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INPKTRDY",
            "description": "Sets this bit after loading a data packet into the FIFO",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FIFONE",
            "description": "FIFO is not empty",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "UNDERRUN",
            "description": "Under run",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "FLUSHFIFO",
            "description": "Flush FIFO",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SENDSTALL",
            "description": "Set this bit to issue a STALL handshake to an IN token",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "SENTSTALL",
            "description": "This bit is set by hardware when a STALL handshake is transmitted",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "CLRDATATOG",
            "description": "Clear Data toggle bit",
            "bitRange": "[6:6]",
        }
    }
}

USB_INCSR2 = {
    "name": "INCSR2",
    "displayName": "INCSR2",
    "description": "IN endpoint 2 control and status register",
    "alternateRegister": "CSR0",
    "addressOffset": "0x12",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000020",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FRCDATATOG",
            "description": "Force data toggle",
            "bitRange": "[3:3]",
        },
        "field_1": {
            "name": "ISO",
            "description": "IN endpoint synchronous transfer",
            "bitRange": "[6:6]",
        },
        "field_2": {
            "name": "AUTOSET",
            "description": "INPKTRDY is set automatically",
            "bitRange": "[7:7]",
        }
    }
}

USB_OUTMAXP = {
    "name": "OUTMAXP",
    "displayName": "OUTMAXP",
    "description": "Maxium packet size for OUT endpoint register",
    "addressOffset": "0x13",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUTMAXP",
            "description": "Maximum Packet Size/transaction for OUT endpoint",
            "bitRange": "[7:0]",
        }
    }
}

USB_OUTCSR1 = {
    "name": "OUTCSR1",
    "displayName": "OUTCSR1",
    "description": "OUT endpoint 1 control and status register",
    "addressOffset": "0x14",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000020",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUTPKTRDY",
            "description": "Sets this bit after receiving a data packet",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FIFOFULL",
            "description": "FIFO is full",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "OVERRUN",
            "description": "Over run",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "DATAERROR",
            "description": "Data error",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "FLUSHFIFO",
            "description": "Flush FIFO",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "SENDSTALL",
            "description": "Set this bit to issue a STALL handshake",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "SENTSTALL",
            "description": "This bit is set by hardware when a STALL handshake is transmitted",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "CLRDATATOG",
            "description": "Clear Data toggle bit",
            "bitRange": "[7:7]",
        }
    }
}

USB_OUTCSR2 = {
    "name": "OUTCSR2",
    "displayName": "OUTCSR2",
    "description": "OUT endpoint 2 control and status register",
    "alternateRegister": "CSR0",
    "addressOffset": "0x15",
    "size": "0x08",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ISO",
            "description": "OUT endpoint synchronous transfer",
            "bitRange": "[6:6]",
        },
        "field_1": {
            "name": "AUTOSET",
            "description": "OUTPKTRDY is set automatically",
            "bitRange": "[7:7]",
        }
    }
}

USB_COUNT0 = {
    "name": "COUNT0",
    "displayName": "COUNT0",
    "description": "Endpoint 0 data counter register",
    "addressOffset": "0x16",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "COUNT0",
            "description": "Endpoint 0 data counter",
            "bitRange": "[6:0]",
        }
    }
}

USB_OUTCOUNTL = {
    "name": "OUTCOUNTL",
    "displayName": "OUTCOUNTL",
    "description": "Endpoint 0 data counter low register",
    "alternateRegister": "COUNT0",
    "addressOffset": "0x16",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUTCOUNTL",
            "description": "Endpoint 0 data counter low",
            "bitRange": "[7:0]",
        }
    }
}

USB_OUTCOUNTH = {
    "name": "OUTCOUNTH",
    "displayName": "OUTCOUNTH",
    "description": "Endpoint 0 data counter high register",
    "addressOffset": "0x17",
    "size": "0x08",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OUTCOUNTH",
            "description": "Endpoint 0 data counter high",
            "bitRange": "[2:0]",
        }
    }
}


usb_define = {
    "name": "USB",
    "description": "Universal Serial Bus",
    "groupName": "USB",
    "baseAddress": "0x40014000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "USB",
        "description": "USB interrupt",
        "value": "14",
    },
    "interrupt_1": {
        "name": "USB_DMA",
        "description": "USB DMA interrupt",
        "value": "15",
    },
    "interrupt_2": {
        "name": "USB_WKUP",
        "description": "USB wakeup interrupt",
        "value": "35",
    },
    "registers": {
        "register_0 ": USB_FADDR,
        "register_1 ": USB_POWER,
        "register_2 ": USB_INTRIN,
        "register_3 ": USB_INTROUT,
        "register_4 ": USB_INTRUSB,
        "register_5 ": USB_INTRINE,
        "register_6 ": USB_INTROUTE,
        "register_7 ": USB_INTRUSBE,
        "register_8 ": USB_FRAMEL,
        "register_9 ": USB_FRAMEH,
        "register_10": USB_INDEX,
        "register_11": USB_INMAXP,
        "register_12": USB_CSR0,
        "register_13": USB_INCSR1,
        "register_14": USB_INCSR2,
        "register_15": USB_OUTMAXP,
        "register_16": USB_OUTCSR1,
        "register_17": USB_OUTCSR2,
        "register_18": USB_COUNT0,
        "register_19": USB_OUTCOUNTL,
        "register_20": USB_OUTCOUNTH,
        "register_21": USB_FIFO0,
        "register_22": USB_FIFO1,
        "register_23": USB_FIFO2,
        "register_24": USB_FIFO3,
    }
}
