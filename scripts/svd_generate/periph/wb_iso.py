ISO_TXBUF = {
    "name": "TXBUF",
    "displayName": "TXBUF",
    "description": "Transmit buffer register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WDATA",
            "description": "Transmit Date buffer",
            "bitRange": "[7:0]",
        }
    }
}

ISO_RXBUF = {
    "name": "RXBUF",
    "displayName": "RXBUF",
    "description": "Receive buffer register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RDATA",
            "description": "Receive Date buffer",
            "bitRange": "[7:0]",
        }
    }
}

ISO_TXDONE = {
    "name": "TXDONE",
    "displayName": "TXDONE",
    "description": "Transmit done register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXDONE",
            "description": "Transmit done",
            "bitRange": "[0:0]",
        }
    }
}

ISO_RXDONE = {
    "name": "RXDONE",
    "displayName": "RXDONE",
    "description": "Receive done register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDONE",
            "description": "Receive done buffer",
            "bitRange": "[0:0]",
        }
    }
}

ISO_STARTDET = {
    "name": "STARTDET",
    "displayName": "STARTDET",
    "description": "Start detect register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "START",
            "description": "Start bit detected",
            "bitRange": "[0:0]",
        }
    }
}

ISO_CLRTXDONE = {
    "name": "CLRTXDONE",
    "displayName": "CLRTXDONE",
    "description": "Clear transmit done register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLRTXDONE",
            "description": "Clear transmit done",
            "bitRange": "[0:0]",
        }
    }
}

ISO_CLRRXDONE = {
    "name": "CLRRXDONE",
    "displayName": "CLRRXDONE",
    "description": "Clear receive done register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLRRXDONE",
            "description": "Clear receive done",
            "bitRange": "[0:0]",
        }
    }
}

ISO_CLRSTART = {
    "name": "CLRSTART",
    "displayName": "CLRSTART",
    "description": "Clear start bit flag register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLRSTART",
            "description": "Clear start bit flag",
            "bitRange": "[0:0]",
        }
    }
}

ISO_TRANSR = {
    "name": "TRANSR",
    "displayName": "TRANSR",
    "description": "Transmit status register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RESEND",
            "description": "Resend flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "PERR",
            "description": "Parity check error flag",
            "bitRange": "[1:1]",
        }
    }
}

ISO_FIFOSR = {
    "name": "FIFOSR",
    "displayName": "FIFOSR",
    "description": "FIFO status register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FULL",
            "description": "Buffer is full",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "EMPTY",
            "description": "Buffer is empty",
            "bitRange": "[1:1]",
        }
    }
}

ISO_IER = {
    "name": "IER",
    "displayName": "IER",
    "description": "Interrupt mask control register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXIEN",
            "description": "Transmit interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RXIEN",
            "description": "Receive interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SBIEN",
            "description": "Start bit interrupt enable",
            "bitRange": "[2:2]",
        }
    }
}

ISO_MODE = {
    "name": "MODE",
    "displayName": "MODE",
    "description": "Mode register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000008",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "PCHK",
            "description": "Parity check control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "INV",
            "description": "Inverse mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "T",
            "description": "T mode",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "GT",
            "description": "Guard time",
            "bitRange": "[4:3]",
        }
    }
}

ISO_ETU = {
    "name": "ETU",
    "displayName": "ETU",
    "description": "ETU configuration register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CYCLE",
            "description": "ETU cycle",
            "bitRange": "[10:0]",
        }
    }
}

ISO_RISR = {
    "name": "RISR",
    "displayName": "RISR",
    "description": "Raw interrupt status register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXI",
            "description": "Transmit interrupt",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RXI",
            "description": "Receive interrupt",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SBI",
            "description": "Start bit interrupt",
            "bitRange": "[2:2]",
        }
    }
}

ISO_ISR = {
    "name": "ISR",
    "displayName": "ISR",
    "description": "Interrupt status register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXI",
            "description": "Transmit interrupt",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RXI",
            "description": "Receive interrupt",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SBI",
            "description": "Start bit interrupt",
            "bitRange": "[2:2]",
        }
    }
}


iso_define = {
    "name": "ISO",
    "description": "ISO7816 controller",
    "groupName": "ISO",
    "baseAddress": "0x40016000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "ISO",
        "description": "ISO7816 interrupt",
        "value": "37",
    },
    "registers": {
        "register_0 ": ISO_TXBUF,
        "register_1 ": ISO_RXBUF,
        "register_2 ": ISO_TXDONE,
        "register_3 ": ISO_RXDONE,
        "register_4 ": ISO_STARTDET,
        "register_5 ": ISO_CLRTXDONE,
        "register_6 ": ISO_CLRRXDONE,
        "register_7 ": ISO_CLRSTART,
        "register_8 ": ISO_TRANSR,
        "register_9 ": ISO_FIFOSR,
        "register_10": ISO_IER,
        "register_11": ISO_MODE,
        "register_12": ISO_ETU,
        "register_13": ISO_RISR,
        "register_14": ISO_ISR,
    }
}
