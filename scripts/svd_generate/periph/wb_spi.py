SPI_CR0_SlAVE = {
    "name": "CR0_SlAVE",
    "displayName": "CR0_SlAVE",
    "description": "Control register 0 for slave",
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
            "name": "SLVOE",
            "description": "Slave output enable",
            "bitRange": "[10:10]",
        },
        "field_6": {
            "name": "CFS",
            "description": "Control frame size",
            "bitRange": "[15:12]",
        },
        "field_7": {
            "name": "SSTE",
            "description": "SSN state",
            "bitRange": "[24:24]",
        }
    }
}

SPI_CR0_MASTER = {
    "name": "CR0_MASTER",
    "displayName": "CR0_MASTER",
    "description": "Control register 0 for master",
    "alternateRegister": "CR0_SLAVE",
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
            "name": "CFS",
            "description": "Control frame size",
            "bitRange": "[15:12]",
        },
        "field_6": {
            "name": "SSTE",
            "description": "SSN state",
            "bitRange": "[24:24]",
        }
    }
}

SPI_CR1 = {
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

SPI_SPIENR = {
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
            "description": "SPI enable",
            "bitRange": "[0:0]",
        }
    }
}

SPI_MWCR_SLAVE = {
    "name": "MWCR_SLAVE",
    "displayName": "MWCR_SLAVE",
    "description": "Microwire control register for slave",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MWMOD",
            "description": "Microwire mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MDD",
            "description": "Microwire date transfer mode",
            "bitRange": "[1:1]",
        }
    }
}

SPI_MWCR_MASTER = {
    "name": "MWCR_MASTER",
    "displayName": "MWCR_MASTER",
    "description": "Microwire control register for master",
    "alternateRegister": "MWCR_SLAVE",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MWMOD",
            "description": "Microwire mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MDD",
            "description": "Microwire date transfer mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MHS",
            "description": "Microwire handshake",
            "bitRange": "[2:2]",
        }
    }
}

SPI_SER = {
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

SPI_BAUDR = {
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

SPI_TXFTLR = {
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

SPI_RXFTLR = {
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

SPI_TXFLR = {
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

SPI_RXFLR = {
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

SPI_SR = {
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

SPI_IER = {
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

SPI_ISR = {
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

SPI_RISR = {
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

SPI_TXOICR = {
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

SPI_RXOICR = {
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

SPI_RXUICR = {
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

SPI_ICR = {
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

SPI_DMACR = {
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

SPI_DMATDLR = {
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

SPI_DMARDLR = {
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
SPI_DR = {
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
            "description": "SPI data",
            "bitRange": "[15:0]",
        }
    }
}


spis1_define = {
    "name": "SPIS1",
    "description": "Serial Peripheral Interface slave 1",
    "groupName": "SPI",
    "baseAddress": "0x40003400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "SPIS1",
        "description": "SPIS1 interrupt",
        "value": "28",
    },
    "registers": {
        "register_0 ": SPI_CR0_SlAVE,
        "register_1 ": SPI_SPIENR,
        "register_2 ": SPI_MWCR_SLAVE,
        "register_3 ": SPI_TXFTLR,
        "register_4 ": SPI_RXFTLR,
        "register_5 ": SPI_TXFLR,
        "register_6 ": SPI_RXFLR,
        "register_7 ": SPI_SR,
        "register_8 ": SPI_IER,
        "register_9 ": SPI_ISR,
        "register_10": SPI_RISR,
        "register_11": SPI_TXOICR,
        "register_12": SPI_RXOICR,
        "register_13": SPI_RXUICR,
        "register_14": SPI_ICR,
        "register_15": SPI_DMACR,
        "register_16": SPI_DMATDLR,
        "register_17": SPI_DMARDLR,
        "register_18": SPI_DR,
    }
}

spim2_define = {
    "name": "SPIM2",
    "description": "Serial Peripheral Interface master 2",
    "groupName": "SPI",
    "baseAddress": "0x40009000",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "SPIM2",
        "description": "SPIM2 interrupt",
        "value": "27",
    },
    "registers": {
        "register_0 ": SPI_CR0_MASTER,
        "register_1 ": SPI_CR1,
        "register_2 ": SPI_SPIENR,
        "register_3 ": SPI_MWCR_MASTER,
        "register_4 ": SPI_SER,
        "register_5 ": SPI_BAUDR,
        "register_6 ": SPI_TXFTLR,
        "register_7 ": SPI_RXFTLR,
        "register_8 ": SPI_TXFLR,
        "register_9 ": SPI_RXFLR,
        "register_10": SPI_SR,
        "register_11": SPI_IER,
        "register_12": SPI_ISR,
        "register_13": SPI_RISR,
        "register_14": SPI_TXOICR,
        "register_15": SPI_RXOICR,
        "register_16": SPI_RXUICR,
        "register_17": SPI_ICR,
        "register_18": SPI_DMACR,
        "register_19": SPI_DMATDLR,
        "register_20": SPI_DMARDLR,
        "register_21": SPI_DR,
    }
}

spis2_define = {
    "name": "SPIS2",
    "description": "Serial Peripheral Interface slave 2",
    "groupName": "SPI",
    "baseAddress": "0x40009400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "SPIS2",
        "description": "SPIS2 interrupt",
        "value": "29",
    },
    "registers": {
        "register_0 ": SPI_CR0_SlAVE,
        "register_1 ": SPI_SPIENR,
        "register_2 ": SPI_MWCR_SLAVE,
        "register_3 ": SPI_TXFTLR,
        "register_4 ": SPI_RXFTLR,
        "register_5 ": SPI_TXFLR,
        "register_6 ": SPI_RXFLR,
        "register_7 ": SPI_SR,
        "register_8 ": SPI_IER,
        "register_9 ": SPI_ISR,
        "register_10": SPI_RISR,
        "register_11": SPI_TXOICR,
        "register_12": SPI_RXOICR,
        "register_13": SPI_RXUICR,
        "register_14": SPI_ICR,
        "register_15": SPI_DMACR,
        "register_16": SPI_DMATDLR,
        "register_17": SPI_DMARDLR,
        "register_18": SPI_DR,
    }
}
