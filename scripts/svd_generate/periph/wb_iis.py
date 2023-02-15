I2S_IER = {
    "name": "RTCCR",
    "displayName": "RTCCR",
    "description": "RTC signal output control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IEN",
            "description": "I2S Enable",
            "bitRange": "[0:0]"
        },
    }
}

I2S_IRER = {
    "name": "IRER",
    "displayName": "IRER",
    "description": "I2S Receiver Block Enable Register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXEN",
            "description": " Receiver block enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_ITER = {
    "name": "ITER",
    "displayName": "ITER",
    "description": "I2S Transmitter Block Enable Register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXEN",
            "description": "Transmitter block enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_CER = {
    "name": "CER",
    "displayName": "CER",
    "description": "Clock Enable Register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "Clock generation enable/disable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_CCR = {
    "name": "CCR",
    "displayName": "CCR",
    "description": "Clock Configuration Register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCLKG",
            "description": "These bits are used to program the gating of sclk",
            "bitRange": "[2:0]"
        },
        "field_1": {
            "name": "WSS",
            "description": "Set the clock length for the left and right channels",
            "bitRange": "[4:3]"
        },
    }
}


I2S_RXFFR = {
    "name": "RXFFR",
    "displayName": "RXFFR",
    "description": "Receiver Block FIFO Reset Register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXFFR",
            "description": "Write 1 to clear RX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_TXFFR = {
    "name": "TXFFR",
    "displayName": "TXFFR",
    "description": "Transmitter Block FIFO Reset Register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXFFR",
            "description": "Write 1 to clear TX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_LRBR = {
    "name": "Channel0_LRBR",
    "displayName": "Channel0_LRBR",
    "description": "Channel0 Left Receive Buffer Register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LRBR",
            "description": "The left channel of Channel0 receives buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel0_LTHR = {
    "name": "Channel0_LTHR",
    "displayName": "Channel0_LTHR",
    "description": "Channel0 Left Transmit Holding Register",
    "alternateRegister": "Channel0_LRBR",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LTHR",
            "description": "The left channel of Channel0 Transmit buffer data",
            "bitRange": "[31:0]"
        },
    }
}

I2S_Channel0_RRBR = {
    "name": "Channel0_RRBR",
    "displayName": "Channel0_RRBR",
    "description": "Channel0 Right Receive Buffer Register ",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RRBR",
            "description": "The right channel of Channel0 receives buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel0_RTHR = {
    "name": "Channel0_RTHR",
    "displayName": "Channel0_RTHR",
    "description": "Channel0 Right Transmit Holding Register ",
    "alternateRegister": "Channel0_RRBR",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RTHR",
            "description": "The right channel of Channel0 Transmit buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel0_RER = {
    "name": "Channel0_RER",
    "displayName": "Channel0_RER",
    "description": "Channel0 Receive Enable Register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHEN",
            "description": "Channel0 receive enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_TER = {
    "name": "Channel0_TER",
    "displayName": "Channel0_TER",
    "description": "Channel0 Transmit Enable Register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHEN",
            "description": "Channel0 Transmit enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_RCR = {
    "name": "Channel0_RCR",
    "displayName": "Channel0_RCR",
    "description": "Channel0 Receive Configuration Register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLEN",
            "description": "Channel receive resolution",
            "bitRange": "[2:0]"
        },
    }
}


I2S_Channel0_TCR = {
    "name": "Channel0_TCR",
    "displayName": "Channel0_TCR",
    "description": "Channel0 Transmit Configuration Register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLEN",
            "description": "Channel transmit resolution",
            "bitRange": "[2:0]"
        },
    }
}


I2S_Channel0_ISR = {
    "name": "Channel0_ISR",
    "displayName": "Channel0_ISR",
    "description": "Channel0 Interrupt Status Register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDA",
            "description": "Channel0 RX FIFO not empty",
            "bitRange": "[0:0]"
        },
        "field_1": {
            "name": "RXFO",
            "description": "Channel0 RX FIFO overrun",
            "bitRange": "[1:1]"
        },
        "field_2": {
            "name": "TXFE",
            "description": "Channel0 TX FIFO empty",
            "bitRange": "[4:4]"
        },
        "field_3": {
            "name": "TXFO",
            "description": "Channel0 TX FIFO overrun",
            "bitRange": "[5:5]"
        },
    }
}


I2S_Channel0_IMR = {
    "name": "Channel0_IMR",
    "displayName": "Channel0_IMR",
    "description": "Channel0 Interrupt Mask Register",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDAM",
            "description": "Channel0 mask RX FIFO not empty interrupt",
            "bitRange": "[0:0]"
        },
        "field_1": {
            "name": "RXFOM",
            "description": "Channel0 mask RX FIFO overrun interrupt",
            "bitRange": "[1:1]"
        },
        "field_2": {
            "name": "TXFEM",
            "description": "Channel0 mask TX FIFO empty interrupt",
            "bitRange": "[4:4]"
        },
        "field_3": {
            "name": "TXFOM",
            "description": "Channel0 mask TX FIFO overrun interrupt",
            "bitRange": "[5:5]"
        },
    }
}


I2S_Channel0_ROR = {
    "name": "Channel0_ROR",
    "displayName": "Channel0_ROR",
    "description": "Channel0 Receive Overrun Register",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHO",
            "description": "Channel0 clear RX FIFO overrun interrupt",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_TOR = {
    "name": "Channel0_TOR",
    "displayName": "Channel0_TOR",
    "description": "Channel0 Transmit Overrun Register",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CAL",
            "description": "Channel0 clear TX FIFO overrun interrupt",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_RFCR = {
    "name": "Channel0_RFCR",
    "displayName": "Channel0_RFCR",
    "description": "Channel0 RX FIFO Configuration Register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHDT",
            "description": "Channel0 Config RX interrupt trigger level",
            "bitRange": "[3:0]"
        },
    }
}


I2S_Channel0_TFCR = {
    "name": "Channel0_TFCR",
    "displayName": "Channel0_TFCR",
    "description": "Channel0 TX FIFO Configuration Register",
    "addressOffset": "0x4C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHET",
            "description": "Channel0 Config TX interrupt trigger level",
            "bitRange": "[3:0]"
        },
    }
}


I2S_Channel0_RFF = {
    "name": "Channel0_RFF",
    "displayName": "Channel0_RFF",
    "description": "Channel0 RX FIFO Flush Register",
    "addressOffset": "0x50",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHFR",
            "description": "Write 1 to chear Channel0 RX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel0_TFF = {
    "name": "Channel0_TFF",
    "displayName": "Channel0_TFF",
    "description": "Channel0 TX FIFO Flush Register",
    "addressOffset": "0x54",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHFR",
            "description": "Write 1 to chear Channel0 TX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_LRBR = {
    "name": "Channel1_LRBR",
    "displayName": "Channel1_LRBR",
    "description": "Channel1 Left Receive Buffer Register",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LRBR",
            "description": "The left channel of Channel1 receives buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel1_LTHR = {
    "name": "Channel1_LTHR",
    "displayName": "Channel1_LTHR",
    "description": "Channel1 Left Transmit Holding Register",
    "alternateRegister": "Channel1_LRBR",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LTHR",
            "description": "The left channel of Channel1 Transmit buffer data",
            "bitRange": "[31:0]"
        },
    }
}

I2S_Channel1_RRBR = {
    "name": "Channel1_RRBR",
    "displayName": "Channel1_RRBR",
    "description": "Channel1 Right Receive Buffer Register ",
    "addressOffset": "0x64",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RRBR",
            "description": "The right channel of Channel1 receives buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel1_RTHR = {
    "name": "Channel1_RTHR",
    "displayName": "Channel1_RTHR",
    "description": "Channel1 Right Transmit Holding Register ",
    "alternateRegister": "Channel1_RRBR",
    "addressOffset": "0x64",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RTHR",
            "description": "The right channel of Channel1 Transmit buffer data",
            "bitRange": "[31:0]"
        },
    }
}


I2S_Channel1_RER = {
    "name": "Channel1_RER",
    "displayName": "Channel1_RER",
    "description": "Channel1 Receive Enable Register",
    "addressOffset": "0x68",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHEN",
            "description": "Channel1 receive enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_TER = {
    "name": "Channel1_TER",
    "displayName": "Channel1_TER",
    "description": "Channel1 Transmit Enable Register",
    "addressOffset": "0x6C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHEN",
            "description": "Channel1 Transmit enable",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_RCR = {
    "name": "Channel1_RCR",
    "displayName": "Channel1_RCR",
    "description": "Channel1 Receive Configuration Register",
    "addressOffset": "0x70",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLEN",
            "description": "Channel receive resolution",
            "bitRange": "[2:0]"
        },
    }
}


I2S_Channel1_TCR = {
    "name": "Channel1_TCR",
    "displayName": "Channel1_TCR",
    "description": "Channel1 Transmit Configuration Register",
    "addressOffset": "0x74",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "WLEN",
            "description": "Channel transmit resolution",
            "bitRange": "[2:0]"
        },
    }
}


I2S_Channel1_ISR = {
    "name": "Channel1_ISR",
    "displayName": "Channel1_ISR",
    "description": "Channel1 Interrupt Status Register",
    "addressOffset": "0x78",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDA",
            "description": "Channel1 RX FIFO not empty",
            "bitRange": "[0:0]"
        },
        "field_1": {
            "name": "RXFO",
            "description": "Channel1 RX FIFO overrun",
            "bitRange": "[1:1]"
        },
        "field_2": {
            "name": "TXFE",
            "description": "Channel1 TX FIFO empty",
            "bitRange": "[4:4]"
        },
        "field_3": {
            "name": "TXFO",
            "description": "Channel1 TX FIFO overrun",
            "bitRange": "[5:5]"
        },
    }
}


I2S_Channel1_IMR = {
    "name": "Channel1_IMR",
    "displayName": "Channel1_IMR",
    "description": "Channel1 Interrupt Mask Register",
    "addressOffset": "0x7C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDAM",
            "description": "Channel1 mask RX FIFO not empty interrupt",
            "bitRange": "[0:0]"
        },
        "field_1": {
            "name": "RXFOM",
            "description": "Channel1 mask RX FIFO overrun interrupt",
            "bitRange": "[1:1]"
        },
        "field_2": {
            "name": "TXFEM",
            "description": "Channel1 mask TX FIFO empty interrupt",
            "bitRange": "[4:4]"
        },
        "field_3": {
            "name": "TXFOM",
            "description": "Channel1 mask TX FIFO overrun interrupt",
            "bitRange": "[5:5]"
        },
    }
}


I2S_Channel1_ROR = {
    "name": "Channel1_ROR",
    "displayName": "Channel1_ROR",
    "description": "Channel1 Receive Overrun Register",
    "addressOffset": "0x80",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHO",
            "description": "Channel1 clear RX FIFO overrun interrupt",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_TOR = {
    "name": "Channel1_TOR",
    "displayName": "Channel1_TOR",
    "description": "Channel1 Transmit Overrun Register",
    "addressOffset": "0x84",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CAL",
            "description": "Channel1 clear TX FIFO overrun interrupt",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_RFCR = {
    "name": "Channel1_RFCR",
    "displayName": "Channel1_RFCR",
    "description": "Channel1 RX FIFO Configuration Register",
    "addressOffset": "0x88",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHDT",
            "description": "Channel1 Config RX interrupt trigger level",
            "bitRange": "[3:0]"
        },
    }
}


I2S_Channel1_TFCR = {
    "name": "Channel1_TFCR",
    "displayName": "Channel1_TFCR",
    "description": "Channel1 TX FIFO Configuration Register",
    "addressOffset": "0x8C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHET",
            "description": "Channel1 Config TX interrupt trigger level",
            "bitRange": "[3:0]"
        },
    }
}


I2S_Channel1_RFF = {
    "name": "Channel1_RFF",
    "displayName": "Channel1_RFF",
    "description": "Channel1 RX FIFO Flush Register",
    "addressOffset": "0x90",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXCHFR",
            "description": "Write 1 to chear Channel1 RX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_Channel1_TFF = {
    "name": "Channel1_TFF",
    "displayName": "Channel1_TFF",
    "description": "Channel1 TX FIFO Flush Register",
    "addressOffset": "0x94",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXCHFR",
            "description": "Write 1 to chear Channel1 TX FIFO",
            "bitRange": "[0:0]"
        },
    }
}


I2S_RXDMA = {
    "name": "RXDMA",
    "displayName": "RXDMA",
    "description": "Receiver Block DMA Register",
    "addressOffset": "0x1C0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXDMA",
            "description": "Receiver Block DMA Register",
            "bitRange": "[31:0]"
        },
    }
}


I2S_RRXDMA = {
    "name": "RRXDMA",
    "displayName": "RRXDMA",
    "description": "Reset Receiver Block DMA Register",
    "addressOffset": "0x1C4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RRXDMA",
            "description": "Reset Receiver Block DMA Register",
            "bitRange": "[31:0]"
        },
    }
}


I2S_TXDMA = {
    "name": "TXDMA",
    "displayName": "TXDMA",
    "description": "Transmitter Block DMA Register",
    "addressOffset": "0x1C8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXDMA",
            "description": "Transmitter Block DMA Register",
            "bitRange": "[31:0]"
        },
    }
}


I2S_RTXDMA = {
    "name": "RTXDMA",
    "displayName": "RTXDMA",
    "description": "Reset Transmitter Block DMA Register",
    "addressOffset": "0x1CC",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RRXDMA",
            "description": "Reset Transmitter Block DMA Register",
            "bitRange": "[31:0]"
        },
    }
}


iis_define = {
    "name": "I2S",
    "description": "Inter-IC Sound Bus",
    "groupName": "I2S",
    "baseAddress": "0x4000B400",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "I2S",
        "description": "I2S interrupt",
        "value": "36",
    },
    "registers": {
        "register_0 ": I2S_IER,
        "register_1 ": I2S_IRER,            
        "register_2 ": I2S_ITER,
        "register_3 ": I2S_CER,
        "register_4 ": I2S_CCR,
        "register_5 ": I2S_RXFFR,
        "register_6 ": I2S_TXFFR,
        "register_7 ": I2S_Channel0_LRBR,
        "register_8 ": I2S_Channel0_LTHR,
        "register_9 ": I2S_Channel0_RRBR,
        "register_10": I2S_Channel0_RTHR,
        "register_11": I2S_Channel0_RER,            
        "register_12": I2S_Channel0_TER,
        "register_13": I2S_Channel0_RCR,
        "register_14": I2S_Channel0_TCR,
        "register_15": I2S_Channel0_ISR,
        "register_16": I2S_Channel0_IMR,
        "register_17": I2S_Channel0_ROR,
        "register_18": I2S_Channel0_TOR,
        "register_19": I2S_Channel0_RFCR,
        "register_20": I2S_Channel0_TFCR,
        "register_21": I2S_Channel0_RFF,
        "register_22": I2S_Channel0_TFF,
        "register_23": I2S_Channel1_LRBR,
        "register_24": I2S_Channel1_LTHR,
        "register_25": I2S_Channel1_RRBR,
        "register_26": I2S_Channel1_RTHR,
        "register_27": I2S_Channel1_RER,
        "register_28": I2S_Channel1_TER,
        "register_29": I2S_Channel1_RCR,
        "register_30": I2S_Channel1_TCR,
        "register_31": I2S_Channel1_ISR,
        "register_32": I2S_Channel1_IMR,
        "register_33": I2S_Channel1_ROR,
        "register_34": I2S_Channel1_TOR,
        "register_35": I2S_Channel1_RFCR,
        "register_36": I2S_Channel1_TFCR,
        "register_37": I2S_Channel1_RFF,
        "register_38": I2S_Channel1_TFF,
        "register_39": I2S_RXDMA,
        "register_40": I2S_RRXDMA,
        "register_41": I2S_TXDMA,
        "register_42": I2S_RTXDMA,
    }
}
