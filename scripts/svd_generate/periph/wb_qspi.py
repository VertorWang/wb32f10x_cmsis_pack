QSPI_CR0 = {
    "name": "CR0",
    "displayName": "CR0",
    "description": "Control register 0",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x01000007",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DFS",
            "description": "Data frame size",
            "bitRange": "[3:0]",
        },
        "field_1": {
            "name": "FRF",
            "description": "Frame format protocol select",
            "bitRange": "[5:4]",
        },
        "field_2": {
            "name": "CPHA",
            "description": "Clock phase",
            "bitRange": "[6:6]",
        },
        "field_3": {
            "name": "CPOL",
            "description": "Clock polarity",
            "bitRange": "[7:7]",
        },
        "field_4": {
            "name": "TMOD",
            "description": "Transfer mode",
            "bitRange": "[9:8]",
        },
        "field_5": {
            "name": "SPI_MODE",
            "description": "SPI mode",
            "bitRange": "[22:21]",
        },
        "field_6": {
            "name": "SSTE",
            "description": "SSN state",
            "bitRange": "[24:24]",
        }
    }
}

QSPI_CR1 = {
    "name": "CR1",
    "displayName": "CR1",
    "description": "Control register 1",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "NDF",
            "description": "Number of max data frame",
            "bitRange": "[15:0]",
        }
    }
}

QSPI_SPIENR = {
    "name": "SPIENR",
    "displayName": "SPIENR",
    "description": "SPI enable register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SPI_EN",
            "description": "QSPI enable",
            "bitRange": "[0:0]",
        }
    }
}

QSPI_SER = {
    "name": "SER",
    "displayName": "SER",
    "description": "Slave selection register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SE0",
            "description": "Select slave 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SE1",
            "description": "Select slave 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SE2",
            "description": "Select slave 2",
            "bitRange": "[2:2]",
        }
    }
}

QSPI_BAUDR = {
    "name": "BAUDR",
    "displayName": "BAUDR",
    "description": "Baud rate register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCKDV",
            "description": "SCLK division",
            "bitRange": "[15:0]",
        }
    }
}

QSPI_TXFTLR = {
    "name": "TXFTLR",
    "displayName": "TXFTLR",
    "description": "Transmit FIFO threshold register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TFT",
            "description": "Transmit FIFO threshold",
            "bitRange": "[1:0]",
        }
    }
}

QSPI_RXFTLR = {
    "name": "RXFTLR",
    "displayName": "RXFTLR",
    "description": "Receive FIFO threshold register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RFT",
            "description": "Receive FIFO threshold",
            "bitRange": "[1:0]",
        }
    }
}

QSPI_TXFLR = {
    "name": "TXFLR",
    "displayName": "TXFLR",
    "description": "Transmit buffer state register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXTFL",
            "description": "Date length of transmit FIFO",
            "bitRange": "[2:0]",
        }
    }
}

QSPI_RXFLR = {
    "name": "RXFLR",
    "displayName": "RXFLR",
    "description": "Receive buffer state register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXTFL",
            "description": "Date length of receive FIFO",
            "bitRange": "[2:0]",
        }
    }
}

QSPI_SR = {
    "name": "SR",
    "displayName": "SR",
    "description": "Status register",
    "addressOffset": "0x28",
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
            "description": "Transmit FIFO not full",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TFE",
            "description": "Transmit FIFO empty",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RFNE",
            "description": "Receive FIFO not empty",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RFF",
            "description": "Receive FIFO full",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "TXERR",
            "description": "Transmit error when transmit FIFO is empty",
            "bitRange": "[5:5]",
        }
    }
}

QSPI_IER = {
    "name": "IER",
    "displayName": "IER",
    "description": "Interrupt enable register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000001F",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXEIE",
            "description": "Transmit FIFO empty interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TXOIE",
            "description": "Transmit FIFO overflow interrupt enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RXUIE",
            "description": "Receive FIFO underflow interrupt enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RXOIE",
            "description": "Receive FIFO overflow interrupt enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RXFIE",
            "description": "Receive FIFO full interrupt enable",
            "bitRange": "[4:4]",
        }
    }
}

QSPI_ISR = {
    "name": "ISR",
    "displayName": "ISR",
    "description": "Interrupt status register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXEIS",
            "description": "Transmit FIFO empty interrupt status",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TXOIS",
            "description": "Transmit FIFO overflow interrupt status",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RXUIS",
            "description": "Receive FIFO underflow interrupt status",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RXOIS",
            "description": "Receive FIFO overflow interrupt status",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RXFIS",
            "description": "Receive FIFO full interrupt status",
            "bitRange": "[4:4]",
        }
    }
}

QSPI_RISR = {
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
            "name": "TXEIR",
            "description": "Transmit FIFO empty interrupt raw status",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TXOIR",
            "description": "Transmit FIFO overflow interrupt raw status",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RXUIR",
            "description": "Receive FIFO underflow interrupt raw status",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RXOIR",
            "description": "Receive FIFO overflow interrupt raw status",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RXFIR",
            "description": "Receive FIFO full interrupt raw status",
            "bitRange": "[4:4]",
        }
    }
}

QSPI_TXOICR = {
    "name": "TXOICR",
    "displayName": "TXOICR",
    "description": "Transmit FIFO overflow interrupt clear register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXOICR",
            "description": "Clear transmit FIFO overflow interrupt",
            "bitRange": "[0:0]",
        }
    }
}

QSPI_RXOICR = {
    "name": "RXOICR",
    "displayName": "RXOICR",
    "description": "Receive FIFO overflow interrupt clear register",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXOICR",
            "description": "Clear receive FIFO overflow interrupt",
            "bitRange": "[0:0]",
        }
    }
}

QSPI_RXUICR = {
    "name": "RXUICR",
    "displayName": "RXUICR",
    "description": "Receive FIFO underflow interrupt clear register",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXUICR",
            "description": "Clear receive FIFO underflow interrupt",
            "bitRange": "[0:0]",
        }
    }
}

QSPI_ICR = {
    "name": "ICR",
    "displayName": "ICR",
    "description": "Interrupt clear register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ICR",
            "description": "Clear transmit FIFO overflow, receive FIFO overflow and underflow interrupt",
            "bitRange": "[0:0]",
        }
    }
}

QSPI_DMACR = {
    "name": "DMACR",
    "displayName": "DMACR",
    "description": "DMA control register",
    "addressOffset": "0x4C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RDMAE",
            "description": "Receive DMA enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TDMAE",
            "description": "Transmit DMA enable",
            "bitRange": "[1:1]",
        }
    }
}

QSPI_DMATDLR = {
    "name": "DMATDLR",
    "displayName": "DMATDLR",
    "description": "DMA transmit threshold register",
    "addressOffset": "0x50",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMATDLR",
            "description": "DMA transmit threshold",
            "bitRange": "[1:0]",
        }
    }
}

QSPI_DMARDLR = {
    "name": "DMARDLR",
    "displayName": "DMARDLR",
    "description": "DMA receive threshold register",
    "addressOffset": "0x54",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMARDLR",
            "description": "DMA receive threshold",
            "bitRange": "[1:0]",
        }
    }
}

# 没看明白这个DR寄存器的地址偏移量啥意思
QSPI_DR = {
    "name": "DR",
    "displayName": "DMATDLR",
    "description": "Data register",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DR",
            "description": "QSPI data",
            "bitRange": "[15:0]",
        }
    }
}

QSPI_ESPICR = {
    "name": "ESPICR",
    "displayName": "ESPICR",
    "description": "Enhance SPI control register",
    "addressOffset": "0xF4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000200",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TRANST",
            "description": "Transmit frame format",
            "bitRange": "[1:0]",
        },
        "field_1": {
            "name": "ADDRL",
            "description": "Address length",
            "bitRange": "[5:2]",
        },
        "field_2": {
            "name": "INSTL",
            "description": "Instruction length",
            "bitRange": "[9:8]",
        },
        "field_3": {
            "name": "WCYC",
            "description": "Wait cycle",
            "bitRange": "[15:11]",
        }
    }
}


qspi_define = {
    "name": "QSPI",
    "description": "Queue Serial peripheral interface controller",
    "groupName": "QSPI",
    "baseAddress": "0x40003000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "QSPI",
        "description": "QSPI interrupt",
        "value": "26",
    },
    "registers": {
        "register_0 ": QSPI_CR0,
        "register_1 ": QSPI_CR1,
        "register_2 ": QSPI_SPIENR,
        "register_3 ": QSPI_SER,
        "register_4 ": QSPI_BAUDR,
        "register_5 ": QSPI_TXFTLR,
        "register_6 ": QSPI_RXFTLR,
        "register_7 ": QSPI_TXFLR,
        "register_8 ": QSPI_RXFLR,
        "register_9 ": QSPI_SR,
        "register_10": QSPI_IER,
        "register_11": QSPI_ISR,
        "register_12": QSPI_RISR,
        "register_13": QSPI_TXOICR,
        "register_14": QSPI_RXOICR,
        "register_15": QSPI_RXUICR,
        "register_16": QSPI_ICR,
        "register_17": QSPI_DMACR,
        "register_18": QSPI_DMATDLR,
        "register_19": QSPI_DMARDLR,
        "register_20": QSPI_DR,
        "register_21": QSPI_ESPICR,
    }
}
