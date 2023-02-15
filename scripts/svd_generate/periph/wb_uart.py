UART_RBR = {
    "name": "RBR",
    "displayName": "RBR",
    "description": "Receive buffer register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "RBR",
            "description": "Receive buffer",
            "bitRange": "[8:0]",
        }
    }
}

UART_THR = {
    "name": "THR",
    "displayName": "THR",
    "description": "Transmit holding register",
    "alternateRegister": "RBR",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "THR",
            "description": "Transmit hold",
            "bitRange": "[8:0]",
        }
    }
}

UART_DLL = {
    "name": "DLL",
    "displayName": "DLL",
    "description": "Divisor latch low register",
    "alternateRegister": "RBR",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "DLLSB",
            "description": "Divisor latch LSB",
            "bitRange": "[7:0]",
        }
    }
}

UART_DLH = {
    "name": "DLH",
    "displayName": "DLH",
    "description": "Divisor latch high register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DLHSB",
            "description": "Divisor latch HSB",
            "bitRange": "[7:0]",
        }
    }
}

UART_IER = {
    "name": "IER",
    "displayName": "IER",
    "description": "Interrupt enable register",
    "alternateRegister": "DLH",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RDAIE",
            "description": "RBR interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "THREIE",
            "description": "THRE interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RLSIE",
            "description": "Receive interrupt line enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSIE",
            "description": "Modem interrupt control",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "LSRCLRMD",
            "description": "This bit is used to control the clearing mode of status bit in LSR register",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "PTIME",
            "description": "Control programmable THRE interrupt.",
            "bitRange": "[7:7]",
        }
    }
}

UART_IIR = {
    "name": "IIR",
    "displayName": "IIR",
    "description": "Interrupt identification register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INTID",
            "description": "Interrupt identification",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "FIFOSE",
            "description": "FIFO enable",
            "bitRange": "[7:6]",
        }
    }
}

UART_FCR = {
    "name": "FCR",
    "displayName": "FCR",
    "description": "FIFO control register",
    "alternateRegister": "IIR",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FIFOEN",
            "description": "FIFO enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RXFIFORS",
            "description": "Receive FIFO reset",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TXFIFORS",
            "description": "Transmit FIFO reset",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TXTL",
            "description": "Transmit trigger level",
            "bitRange": "[5:4]",
        },
        "field_4": {
            "name": "RXTL",
            "description": "Receive trigger level",
            "bitRange": "[7:6]",
        }
    }
}

UART_LCR = {
    "name": "LCR",
    "displayName": "LCR",
    "description": "Line control register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLS",
            "description": "Word length selection",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "SBS",
            "description": "Stop bit selection",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "PE",
            "description": "Parity check enable",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "PS",
            "description": "Parity check selection",
            "bitRange": "[5:4]",
        },
        "field_4": {
            "name": "BC",
            "description": "Interval control",
            "bitRange": "[6:6]",
        },
        "field_5": {
            "name": "DLAB",
            "description": "Divisor latch access bit",
            "bitRange": "[7:7]",
        }
    }
}

UART_MCR = {
    "name": "MCR",
    "displayName": "MCR",
    "description": "Modem control register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RTS",
            "description": "Modem output pin RTS source",
            "bitRange": "[1:1]",
        },
        "field_1": {
            "name": "AFCE",
            "description": "Automatic flow control",
            "bitRange": "[5:5]",
        },
        "field_2": {
            "name": "SIRE",
            "description": "IrDA SIR enable",
            "bitRange": "[6:6]",
        }
    }
}

UART_LSR = {
    "name": "LSR",
    "displayName": "LSR",
    "description": "Line status register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DR",
            "description": "Data receive ready",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "OE",
            "description": "Overflow error",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "PE",
            "description": "Parity check error",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "FE",
            "description": "Framing error",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "BI",
            "description": "Interval interrupt",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "THRE",
            "description": "Transmitter holds the register empty",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "TEMT",
            "description": "Transmitter is empty",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "RFE",
            "description": "Receive FIFO error",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "ADDR_RCVD",
            "description": "Address receive bit",
            "bitRange": "[8:8]",
        }
    }
}

UART_MSR = {
    "name": "MSR",
    "displayName": "MSR",
    "description": "Modem status register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DCTS",
            "description": "Delta CTS",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DDSR",
            "description": "Delta DSR",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TERI",
            "description": "This bit is set when the input RI is converted from low level to high level",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "DDCD",
            "description": "Delta DCD",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "CTS",
            "description": "Clear transmit status",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "DSR",
            "description": "Data set ready state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "RI",
            "description": "Ringing indicator status",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "DCD",
            "description": "Data carrier detection status",
            "bitRange": "[7:7]",
        }
    }
}

UART_SCR = {
    "name": "SCR",
    "displayName": "SCR",
    "description": "High speed temporary register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0x00000000",
    "fields": {
        "field_0": {
            "name": "PAD",
            "description": "A byte that can be read and written",
            "bitRange": "[7:0]",
        }
    }
}

UART_USR = {
    "name": "USR",
    "displayName": "USR",
    "description": "Uart status register",
    "addressOffset": "0x7C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000006",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BUSY",
            "description": "Busy status",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TFNF",
            "description": "Transmit FIFO is not full",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TFE",
            "description": "Transmit FIFO is empty",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RFNE",
            "description": "Receive FIFO is not empty",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RFF",
            "description": "Receive FIFO is full",
            "bitRange": "[4:4]",
        }
    }
}

UART_TFL = {
    "name": "TFL",
    "displayName": "TFL",
    "description": "Transmit FIFO level register",
    "addressOffset": "0x80",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TFL",
            "description": "Data length of transmit FIFO",
            "bitRange": "[3:0]",
        }
    }
}

UART_RFL = {
    "name": "RFL",
    "displayName": "RFL",
    "description": "Receive FIFO level register",
    "addressOffset": "0x84",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RFL",
            "description": "Data length of Receive FIFO",
            "bitRange": "[3:0]",
        }
    }
}

UART_SRR = {
    "name": "SRR",
    "displayName": "SRR",
    "description": "Software restart register",
    "addressOffset": "0x88",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000006",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "UR",
            "description": "UART module restart control bit",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RFR",
            "description": "Shadow bit of the receive FIFO restart control bit FCR [1]",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "XFR",
            "description": "Shadow bit that sends the FIFO restart control bit FCR [2]",
            "bitRange": "[2:2]",
        }
    }
}

UART_SRTS = {
    "name": "SRTS",
    "displayName": "SRTS",
    "description": "Shadow transmit request register",
    "addressOffset": "0x8C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRTS",
            "description": "Shadow bit of transmit request control",
            "bitRange": "[0:0]",
        }
    }
}

UART_SBCR = {
    "name": "SBCR",
    "displayName": "SBCR",
    "description": "Shadow interrupt control register",
    "addressOffset": "0x90",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SBCR",
            "description": "Shadow bit of interrupt control",
            "bitRange": "[0:0]",
        }
    }
}

UART_SFE = {
    "name": "SFE",
    "displayName": "SFE",
    "description": "Shadow FIFO enable register",
    "addressOffset": "0x98",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SFE",
            "description": "Shadow bit of FIFO enable",
            "bitRange": "[0:0]",
        }
    }
}

UART_SRT = {
    "name": "SRT",
    "displayName": "SRT",
    "description": "Shadow receive trigger register",
    "addressOffset": "0x9C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRT",
            "description": "Shadow bit of receive trigger control",
            "bitRange": "[1:0]",
        }
    }
}

UART_STET = {
    "name": "STET",
    "displayName": "STET",
    "description": "Shadow Transmit trigger register",
    "addressOffset": "0xA0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "STET",
            "description": "Shadow bit of receive Transmit control",
            "bitRange": "[1:0]",
        }
    }
}

UART_DMASA = {
    "name": "DMASA",
    "displayName": "DMASA",
    "description": "Software abort register",
    "addressOffset": "0xA8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMASA",
            "description": "Set this bit to abort DMA transfer",
            "bitRange": "[0:0]",
        }
    }
}

UART_DLF = {
    "name": "DLF",
    "displayName": "DLF",
    "description": "Division latch fraction register",
    "addressOffset": "0xC0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DLF",
            "description": "Division latch fraction",
            "bitRange": "[3:0]",
        }
    }
}

UART_RAR = {
    "name": "RAR",
    "displayName": "RAR",
    "description": "Receive address register",
    "addressOffset": "0xC4",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAR",
            "description": "Address of the comparison in receive mode",
            "bitRange": "[7:0]",
        }
    }
}

UART_TAR = {
    "name": "TAR",
    "displayName": "TAR",
    "description": "Receive address register",
    "addressOffset": "0xC8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TAR",
            "description": "Address in transmit mode",
            "bitRange": "[7:0]",
        }
    }
}

UART_EXTLCR = {
    "name": "EXTLCR",
    "displayName": "EXTLCR",
    "description": "Extended control register",
    "addressOffset": "0xCC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000006",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLS_E",
            "description": "WLS extension",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "ADDR_MATCH",
            "description": "Address matching enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SEND_ADDR",
            "description": "Send address control bit",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TRANSMIT_MODE",
            "description": "Transmission mode",
            "bitRange": "[3:3]",
        }
    }
}


uart1_define = {
    "name": "UART1",
    "description": "Universal Asynchronous 1",
    "groupName": "UART",
    "baseAddress": "0x40003800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "UART1",
        "description": "UART1 interrupt",
        "value": "30",
    },
    "registers": {
        "register_0 ": UART_RBR,
        "register_1 ": UART_THR,
        "register_2 ": UART_DLL,
        "register_3 ": UART_DLH,
        "register_4 ": UART_IER,
        "register_5 ": UART_IIR,
        "register_6 ": UART_FCR,
        "register_7 ": UART_LCR,
        "register_8 ": UART_MCR,
        "register_9 ": UART_LSR,
        "register_10": UART_MSR,
        "register_11": UART_SCR,
        "register_12": UART_USR,
        "register_13": UART_TFL,
        "register_14": UART_RFL,
        "register_15": UART_SRR,
        "register_16": UART_SRTS,
        "register_17": UART_SBCR,
        "register_18": UART_SFE,
        "register_19": UART_SRT,
        "register_20": UART_STET,
        "register_21": UART_DMASA,
        "register_22": UART_DLF,
        "register_23": UART_RAR,
        "register_24": UART_TAR,
        "register_25": UART_EXTLCR,
    }
}

uart2_define = {
    "name": "UART2",
    "description": "Universal Asynchronous 2",
    "groupName": "UART",
    "baseAddress": "0x40008000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "UART2",
        "description": "UART2 interrupt",
        "value": "31",
    },
    "registers": {
        "register_0 ": UART_RBR,
        "register_1 ": UART_THR,
        "register_2 ": UART_DLL,
        "register_3 ": UART_DLH,
        "register_4 ": UART_IER,
        "register_5 ": UART_IIR,
        "register_6 ": UART_FCR,
        "register_7 ": UART_LCR,
        "register_8 ": UART_MCR,
        "register_9 ": UART_LSR,
        "register_10": UART_MSR,
        "register_11": UART_SCR,
        "register_12": UART_USR,
        "register_13": UART_TFL,
        "register_14": UART_RFL,
        "register_15": UART_SRR,
        "register_16": UART_SRTS,
        "register_17": UART_SBCR,
        "register_18": UART_SFE,
        "register_19": UART_SRT,
        "register_20": UART_STET,
        "register_21": UART_DMASA,
        "register_22": UART_DLF,
        "register_23": UART_RAR,
        "register_24": UART_TAR,
        "register_25": UART_EXTLCR,
    }
}

uart3_define = {
    "name": "UART3",
    "description": "Universal Asynchronous 3",
    "groupName": "UART",
    "baseAddress": "0x40008400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "UART3",
        "description": "UART3 interrupt",
        "value": "32",
    },
    "registers": {
        "register_0 ": UART_RBR,
        "register_1 ": UART_THR,
        "register_2 ": UART_DLL,
        "register_3 ": UART_DLH,
        "register_4 ": UART_IER,
        "register_5 ": UART_IIR,
        "register_6 ": UART_FCR,
        "register_7 ": UART_LCR,
        "register_8 ": UART_MCR,
        "register_9 ": UART_LSR,
        "register_10": UART_MSR,
        "register_11": UART_SCR,
        "register_12": UART_USR,
        "register_13": UART_TFL,
        "register_14": UART_RFL,
        "register_15": UART_SRR,
        "register_16": UART_SRTS,
        "register_17": UART_SBCR,
        "register_18": UART_SFE,
        "register_19": UART_SRT,
        "register_20": UART_STET,
        "register_21": UART_DMASA,
        "register_22": UART_DLF,
        "register_23": UART_RAR,
        "register_24": UART_TAR,
        "register_25": UART_EXTLCR,
    }
}
