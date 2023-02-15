DMAC_SAR0 = {
    "name": "SAR0",
    "displayName": "SAR0",
    "description": "Source address register for channel 0",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SAR",
            "description": "Source address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_DAR0 = {
    "name": "DAR0",
    "displayName": "DAR0",
    "description": "Destination address register for channel 0",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DAR",
            "description": "Destination address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_CTLL0 = {
    "name": "CTLL0",
    "displayName": "CTLL0",
    "description": "Control low register for channel 0",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00304801",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INT_EN",
            "description": "Interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DST_TR_WIDTH",
            "description": "Destination transfer data width",
            "bitRange": "[3:1]",
        },
        "field_2": {
            "name": "SRC_TR_WIDTH",
            "description": "Source transfer data width",
            "bitRange": "[6:4]",
        },
        "field_3": {
            "name": "DINC",
            "description": "Destination address increment",
            "bitRange": "[8:7]",
        },
        "field_4": {
            "name": "SINC",
            "description": "Source address increment",
            "bitRange": "[10:9]",
        },
        "field_5": {
            "name": "DST_MSIZE",
            "description": "Destination burst transaction data width",
            "bitRange": "[13:11]",
        },
        "field_6": {
            "name": "SRC_MSZIE",
            "description": "Source burst transaction data width",
            "bitRange": "[16:14]",
        },
        "field_7": {
            "name": "SRC_GAT_EN",
            "description": "Source gather enable",
            "bitRange": "[17:17]",
        },
        "field_8": {
            "name": "DST_SCAT_EN",
            "description": "Destination scatter enable",
            "bitRange": "[18:18]",
        },
        "field_9": {
            "name": "TT_FC",
            "description": "Transfer type and flow control",
            "bitRange": "[22:20]",
        },
        "field_10": {
            "name": "DMS",
            "description": "Destination master interface specification",
            "bitRange": "[24:23]",
        },
        "field_11": {
            "name": "SMS",
            "description": "Source master interface specification",
            "bitRange": "[26:25]",
        }
    }
}

DMAC_CTLH0 = {
    "name": "CTLH0",
    "displayName": "CTLH0",
    "description": "Control high register for channel 0",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BLOCK_TS",
            "description": "Block transfer size",
            "bitRange": "[11:0]",
        },
        "field_1": {
            "name": "DONE",
            "description": "Check if the block transfer is done by polling this bit",
            "bitRange": "[12:12]",
        }
    }
}

DMAC_CFGL0 = {
    "name": "CFGL0",
    "displayName": "CFGL0",
    "description": "Channel configuration low register for channel 0",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000C00",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CH_PRIOR",
            "description": "Channel priority",
            "bitRange": "[7:5]",
        },
        "field_1": {
            "name": "CH_SUSP",
            "description": "Channel suspend",
            "bitRange": "[8:8]",
        },
        "field_2": {
            "name": "FIFO_EMPTY",
            "description": "FIFO empty",
            "bitRange": "[9:9]",
        },
        "field_3": {
            "name": "HS_SEL_DST",
            "description": "Handshaking selection of destination",
            "bitRange": "[10:10]",
        },
        "field_4": {
            "name": "HS_SEL_SRC",
            "description": "Handshaking selection of source",
            "bitRange": "[11:11]",
        },
        "field_5": {
            "name": "DST_HS_POL",
            "description": "Destination handshaking polarity",
            "bitRange": "[18:18]",
        },
        "field_6": {
            "name": "SRC_HS_POL",
            "description": "Source handshaking polarity",
            "bitRange": "[19:19]",
        },
        "field_7": {
            "name": "RELOAD_SRC",
            "description": "Source address register automatically reload",
            "bitRange": "[20:20]",
        },
        "field_8": {
            "name": "RELOAD_DST",
            "description": "Destination address register automatically reload",
            "bitRange": "[21:21]",
        }
    }
}

DMAC_CFGH0 = {
    "name": "CFGH0",
    "displayName": "CFGH0",
    "description": "Channel configuration low register for channel 0",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FCMODE",
            "description": "Flow control mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FIFO_MODE",
            "description": "FIFO mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "PROTCTL",
            "description": "Protection control for AMBA peripheral",
            "bitRange": "[4:2]",
        },
        "field_3": {
            "name": "SRC_PER",
            "description": "Source handshaking of specified peripheral",
            "bitRange": "[10:7]",
        },
        "field_4": {
            "name": "DST_PER",
            "description": "Destination handshaking of specified peripheral",
            "bitRange": "[14:11]",
        }
    }
}

DMAC_SAR1 = {
    "name": "SAR1",
    "displayName": "SAR1",
    "description": "Source address register for channel 1",
    "addressOffset": "0x58",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SAR",
            "description": "Source address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_DAR1 = {
    "name": "DAR1",
    "displayName": "DAR1",
    "description": "Destination address register for channel 1",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DAR",
            "description": "Destination address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_CTLL1 = {
    "name": "CTLL1",
    "displayName": "CTLL1",
    "description": "Control low register for channel 1",
    "addressOffset": "0x70",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00304801",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INT_EN",
            "description": "Interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DST_TR_WIDTH",
            "description": "Destination transfer data width",
            "bitRange": "[3:1]",
        },
        "field_2": {
            "name": "SRC_TR_WIDTH",
            "description": "Source transfer data width",
            "bitRange": "[6:4]",
        },
        "field_3": {
            "name": "DINC",
            "description": "Destination address increment",
            "bitRange": "[8:7]",
        },
        "field_4": {
            "name": "SINC",
            "description": "Source address increment",
            "bitRange": "[10:9]",
        },
        "field_5": {
            "name": "DST_MSIZE",
            "description": "Destination burst transaction data width",
            "bitRange": "[13:11]",
        },
        "field_6": {
            "name": "SRC_MSZIE",
            "description": "Source burst transaction data width",
            "bitRange": "[16:14]",
        },
        "field_7": {
            "name": "SRC_GAT_EN",
            "description": "Source gather enable",
            "bitRange": "[17:17]",
        },
        "field_8": {
            "name": "DST_SCAT_EN",
            "description": "Destination scatter enable",
            "bitRange": "[18:18]",
        },
        "field_9": {
            "name": "TT_FC",
            "description": "Transfer type and flow control",
            "bitRange": "[22:20]",
        },
        "field_10": {
            "name": "DMS",
            "description": "Destination master interface specification",
            "bitRange": "[24:23]",
        },
        "field_11": {
            "name": "SMS",
            "description": "Source master interface specification",
            "bitRange": "[26:25]",
        }
    }
}

DMAC_CTLH1 = {
    "name": "CTLH1",
    "displayName": "CTLH1",
    "description": "Control high register for channel 1",
    "addressOffset": "0x74",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BLOCK_TS",
            "description": "Block transfer size",
            "bitRange": "[11:0]",
        },
        "field_1": {
            "name": "DONE",
            "description": "Check if the block transfer is done by polling this bit",
            "bitRange": "[12:12]",
        }
    }
}

DMAC_CFGL1 = {
    "name": "CFGL1",
    "displayName": "CFGL1",
    "description": "Configuration low register for channel 1",
    "addressOffset": "0x98",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000C20",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CH_PRIOR",
            "description": "Channel priority",
            "bitRange": "[7:5]",
        },
        "field_1": {
            "name": "CH_SUSP",
            "description": "Channel suspend",
            "bitRange": "[8:8]",
        },
        "field_2": {
            "name": "FIFO_EMPTY",
            "description": "FIFO empty",
            "bitRange": "[9:9]",
        },
        "field_3": {
            "name": "HS_SEL_DST",
            "description": "Handshaking selection of destination",
            "bitRange": "[10:10]",
        },
        "field_4": {
            "name": "HS_SEL_SRC",
            "description": "Handshaking selection of source",
            "bitRange": "[11:11]",
        },
        "field_5": {
            "name": "DST_HS_POL",
            "description": "Destination handshaking polarity",
            "bitRange": "[18:18]",
        },
        "field_6": {
            "name": "SRC_HS_POL",
            "description": "Source handshaking polarity",
            "bitRange": "[19:19]",
        },
        "field_7": {
            "name": "RELOAD_SRC",
            "description": "Source address register automatically reload",
            "bitRange": "[20:20]",
        },
        "field_8": {
            "name": "RELOAD_DST",
            "description": "Destination address register automatically reload",
            "bitRange": "[21:21]",
        }
    }
}

DMAC_CFGH1 = {
    "name": "CFGH1",
    "displayName": "CFGH1",
    "description": "Configuration low register for channel 1",
    "addressOffset": "0x9C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FCMODE",
            "description": "Flow control mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FIFO_MODE",
            "description": "FIFO mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "PROTCTL",
            "description": "Protection control for AMBA peripheral",
            "bitRange": "[4:2]",
        },
        "field_3": {
            "name": "SRC_PER",
            "description": "source handshaking of specified peripheral",
            "bitRange": "[10:7]",
        },
        "field_4": {
            "name": "DST_PER",
            "description": "Destination handshaking of specified peripheral",
            "bitRange": "[14:11]",
        }
    }
}

DMAC_SAR2 = {
    "name": "SAR2",
    "displayName": "SAR2",
    "description": "Source address register for channel 2",
    "addressOffset": "0xB0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SAR",
            "description": "Source address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_DAR2 = {
    "name": "DAR2",
    "displayName": "DAR2",
    "description": "Destination address register for channel 2",
    "addressOffset": "0xB8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DAR",
            "description": "Destination address",
            "bitRange": "[31:0]",
        }
    }
}

DMAC_CTLL2 = {
    "name": "CTLL2",
    "displayName": "CTLL2",
    "description": "Control low register for channel 2",
    "addressOffset": "0xC8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00304801",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "INT_EN",
            "description": "Interrupt enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DST_TR_WIDTH",
            "description": "Destination transfer data width",
            "bitRange": "[3:1]",
        },
        "field_2": {
            "name": "SRC_TR_WIDTH",
            "description": "Source transfer data width",
            "bitRange": "[6:4]",
        },
        "field_3": {
            "name": "DINC",
            "description": "Destination address increment",
            "bitRange": "[8:7]",
        },
        "field_4": {
            "name": "SINC",
            "description": "Source address increment",
            "bitRange": "[10:9]",
        },
        "field_5": {
            "name": "DST_MSIZE",
            "description": "Destination burst transaction data width",
            "bitRange": "[13:11]",
        },
        "field_6": {
            "name": "SRC_MSZIE",
            "description": "Source burst transaction data width",
            "bitRange": "[16:14]",
        },
        "field_7": {
            "name": "SRC_GAT_EN",
            "description": "Source gather enable",
            "bitRange": "[17:17]",
        },
        "field_8": {
            "name": "DST_SCAT_EN",
            "description": "Destination scatter enable",
            "bitRange": "[18:18]",
        },
        "field_9": {
            "name": "TT_FC",
            "description": "Transfer type and flow control",
            "bitRange": "[22:20]",
        },
        "field_10": {
            "name": "DMS",
            "description": "Destination master interface specification",
            "bitRange": "[24:23]",
        },
        "field_11": {
            "name": "SMS",
            "description": "Source master interface specification",
            "bitRange": "[26:25]",
        }
    }
}

DMAC_CTLH2 = {
    "name": "CTLH2",
    "displayName": "CTLH2",
    "description": "Control high register for channel 2",
    "addressOffset": "0xCC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BLOCK_TS",
            "description": "Block transfer size",
            "bitRange": "[11:0]",
        },
        "field_1": {
            "name": "DONE",
            "description": "Check if the block transfer is done by polling this bit",
            "bitRange": "[12:12]",
        }
    }
}

DMAC_CFGL2 = {
    "name": "CFGL2",
    "displayName": "CFGL2",
    "description": "Configuration low register for channel 2",
    "addressOffset": "0xF0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000C40",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CH_PRIOR",
            "description": "Channel priority",
            "bitRange": "[7:5]",
        },
        "field_1": {
            "name": "CH_SUSP",
            "description": "Channel suspend",
            "bitRange": "[8:8]",
        },
        "field_2": {
            "name": "FIFO_EMPTY",
            "description": "FIFO empty",
            "bitRange": "[9:9]",
        },
        "field_3": {
            "name": "HS_SEL_DST",
            "description": "Handshaking selection of destination",
            "bitRange": "[10:10]",
        },
        "field_4": {
            "name": "HS_SEL_SRC",
            "description": "Handshaking selection of source",
            "bitRange": "[11:11]",
        },
        "field_5": {
            "name": "DST_HS_POL",
            "description": "Destination handshaking polarity",
            "bitRange": "[18:18]",
        },
        "field_6": {
            "name": "SRC_HS_POL",
            "description": "Source handshaking polarity",
            "bitRange": "[19:19]",
        },
        "field_7": {
            "name": "RELOAD_SRC",
            "description": "Source address register automatically reload",
            "bitRange": "[20:20]",
        },
        "field_8": {
            "name": "RELOAD_DST",
            "description": "Destination address register automatically reload",
            "bitRange": "[21:21]",
        }
    }
}

DMAC_CFGH2 = {
    "name": "CFGH2",
    "displayName": "CFGH2",
    "description": "Configuration low register for channel 2",
    "addressOffset": "0xF4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "FCMODE",
            "description": "Flow control mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "FIFO_MODE",
            "description": "FIFO mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "PROTCTL",
            "description": "Protection control for AMBA peripheral",
            "bitRange": "[4:2]",
        },
        "field_3": {
            "name": "SRC_PER",
            "description": "source handshaking of specified peripheral",
            "bitRange": "[10:7]",
        },
        "field_4": {
            "name": "DST_PER",
            "description": "Destination handshaking of specified peripheral",
            "bitRange": "[14:11]",
        }
    }
}

DMAC_SGR0 = {
    "name": "SGR0",
    "displayName": "SGR0",
    "description": "Source gather register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SGI",
            "description": "Source gather interval",
            "bitRange": "[19:0]",
        },
        "field_1": {
            "name": "SGC",
            "description": "Source gather counter",
            "bitRange": "[31:20]",
        }
    }
}

DMAC_DSR0 = {
    "name": "DSR0",
    "displayName": "DSR0",
    "description": "Destination scatter register",
    "addressOffset": "0x50",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DSI",
            "description": "Destination scatter interval",
            "bitRange": "[19:0]",
        },
        "field_1": {
            "name": "DSC",
            "description": "Destination scatter counter",
            "bitRange": "[31:20]",
        }
    }
}

DMAC_RawTfr = {
    "name": "RawTfr",
    "displayName": "RawTfr",
    "description": "Transfer interrupt raw status register",
    "addressOffset": "0x2C0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Transfer interrupt raw status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Transfer interrupt raw status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Transfer interrupt raw status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_RawBlock = {
    "name": "RawBlock",
    "displayName": "RawBlock",
    "description": "Block transfer interrupt raw status register",
    "addressOffset": "0x2C8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Block transfer interrupt raw status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Block transfer interrupt raw status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Block transfer interrupt raw status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_RawSrcTran = {
    "name": "RawSrcTran",
    "displayName": "RawSrcTran",
    "description": "Source transaction raw status register",
    "addressOffset": "0x2D0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Source transaction raw status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Source transaction raw status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Source transaction raw status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_RawDstTran = {
    "name": "RawDstTran",
    "displayName": "RawDstTran",
    "description": "Destination transaction interrupt raw status register",
    "addressOffset": "0x2D8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Destination transaction interrupt raw status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Destination transaction interrupt raw status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Destination transaction interrupt raw status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_RawErr = {
    "name": "RawErr",
    "displayName": "RawErr",
    "description": "Error interrupt raw status register",
    "addressOffset": "0x2E0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Error interrupt raw status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Error interrupt raw status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Error interrupt raw status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusTfr = {
    "name": "StatusTfr",
    "displayName": "StatusTfr",
    "description": "Transfer interrupt status register",
    "addressOffset": "0x2E8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Transfer interrupt status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Transfer interrupt status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Transfer interrupt status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusBlock = {
    "name": "StatusBlock",
    "displayName": "StatusBlock",
    "description": "Block transfer interrupt status register",
    "addressOffset": "0x2F0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Block transfer interrupt status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Block transfer interrupt status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Block transfer interrupt status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusSrcTran = {
    "name": "StatusSrcTran",
    "displayName": "StatusSrcTran",
    "description": "Source transaction interrupt status register",
    "addressOffset": "0x2F8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Source transaction interrupt status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Source transaction interrupt status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Source transaction interrupt status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusDstTran = {
    "name": "StatusDstTran",
    "displayName": "StatusDstTran",
    "description": "Destination transaction interrupt status register",
    "addressOffset": "0x300",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Destination transaction interrupt status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Destination transaction interrupt status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Destination transaction interrupt status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusErr = {
    "name": "StatusErr",
    "displayName": "StatusErr",
    "description": "Error interrupt status register",
    "addressOffset": "0x308",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RAW0",
            "description": "Error interrupt status for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RAW1",
            "description": "Error interrupt status for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "RAW2",
            "description": "Error interrupt status for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_MaskTfr = {
    "name": "MaskTfr",
    "displayName": "MaskTfr",
    "description": "Transfer interrupt mask register",
    "addressOffset": "0x310",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MSK0",
            "description": "Transfer interrupt mask for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MSK1",
            "description": "Transfer interrupt mask for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MSK2",
            "description": "Transfer interrupt mask for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSK0_WE",
            "description": "Transfer interrupt mask write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "MSK1_WE",
            "description": "Transfer interrupt mask write enable for channel 1",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "MSK2_WE",
            "description": "Transfer interrupt mask write enable for channel 2",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_MaskBlock = {
    "name": "MaskBlock",
    "displayName": "MaskBlock",
    "description": "Block transfer interrupt mask register",
    "addressOffset": "0x318",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MSK0",
            "description": "Block transfer interrupt mask for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MSK1",
            "description": "Block transfer interrupt mask for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MSK2",
            "description": "Block transfer interrupt mask for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSK0_WE",
            "description": "Block transfer interrupt mask write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "MSK1_WE",
            "description": "Block transfer interrupt mask write enable for channel 1",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "MSK2_WE",
            "description": "Block transfer interrupt mask write enable for channel 2",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_MaskSrcTran = {
    "name": "MaskSrcTran",
    "displayName": "MaskSrcTran",
    "description": "Source transaction interrupt mask register",
    "addressOffset": "0x320",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MSK0",
            "description": "Source transaction interrupt mask for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MSK1",
            "description": "Source transaction interrupt mask for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MSK2",
            "description": "Source transaction interrupt mask for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSK0_WE",
            "description": "Source transaction interrupt mask write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "MSK1_WE",
            "description": "Source transaction interrupt mask write enable for channel 1",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "MSK2_WE",
            "description": "Source transaction interrupt mask write enable for channel 2",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_MaskDstTran = {
    "name": "MaskDstTran",
    "displayName": "MaskDstTran",
    "description": "Destination transaction interrupt mask register",
    "addressOffset": "0x328",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MSK0",
            "description": "Destination transaction interrupt mask for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MSK1",
            "description": "Destination transaction interrupt mask for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MSK2",
            "description": "Destination transaction interrupt mask for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSK0_WE",
            "description": "Destination transaction interrupt mask write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "MSK1_WE",
            "description": "Destination transaction interrupt mask write enable for channel 1",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "MSK2_WE",
            "description": "Destination transaction interrupt mask write enable for channel 2",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_MaskErr = {
    "name": "MaskErr",
    "displayName": "MaskErr",
    "description": "Error interrupt mask register",
    "addressOffset": "0x330",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MSK0",
            "description": "Error interrupt mask for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MSK1",
            "description": "Error interrupt mask for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MSK2",
            "description": "Error interrupt mask for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "MSK0_WE",
            "description": "Error interrupt mask write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "MSK1_WE",
            "description": "Error interrupt mask write enable for channel 1",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "MSK2_WE",
            "description": "Error interrupt mask write enable for channel 2",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_ClrTrf = {
    "name": "ClrTfr",
    "displayName": "ClrTfr",
    "description": "Transfer interrupt clear register",
    "addressOffset": "0x338",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR0",
            "description": "Clear transfer interrupt for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CLR1",
            "description": "Clear transfer interrupt for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CLR2",
            "description": "Clear transfer interrupt for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_ClrBlock = {
    "name": "ClrBlock",
    "displayName": "ClrBlock",
    "description": "Block transfer interrupt clear register",
    "addressOffset": "0x340",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR0",
            "description": "Clear block transfer interrupt for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CLR1",
            "description": "Clear block transfer interrupt for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CLR2",
            "description": "Clear block transfer interrupt for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_ClrSrcTran = {
    "name": "ClrSrcTran",
    "displayName": "ClrSrcTran",
    "description": "Source transaction interrupt clear register",
    "addressOffset": "0x348",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR0",
            "description": "Clear Source transaction interrupt for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CLR1",
            "description": "Clear Source transaction interrupt for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CLR2",
            "description": "Clear Source transaction interrupt for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_ClrDstTran = {
    "name": "ClrDstTran",
    "displayName": "ClrDstTran",
    "description": "Destination transaction interrupt clear register",
    "addressOffset": "0x350",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR0",
            "description": "Clear Destination transaction interrupt for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CLR1",
            "description": "Clear Destination transaction interrupt for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CLR2",
            "description": "Clear Destination transaction interrupt for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_ClrErr = {
    "name": "ClrErr",
    "displayName": "ClrErr",
    "description": "Error interrupt clear register",
    "addressOffset": "0x358",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR0",
            "description": "Clear error interrupt for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CLR1",
            "description": "Clear error interrupt for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CLR2",
            "description": "Clear error interrupt for channel 2",
            "bitRange": "[2:2]",
        }
    }
}

DMAC_StatusInt = {
    "name": "StatusInt",
    "displayName": "StatusInt",
    "description": "DMAC interrupt status register",
    "addressOffset": "0x360",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TRF",
            "description": "Transfer complete interrupt flag",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "Block",
            "description": "Block transfer interrupt flag",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SRCT",
            "description": "Source transaction interrupt flag",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "DSTT",
            "description": "Destination transaction interrupt flag",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "ERR",
            "description": "Error interrupt flag",
            "bitRange": "[4:4]",
        }
    }
}

DMAC_ReqSrcReg = {
    "name": "ReqSrcReg",
    "displayName": "ReqSrcReg",
    "description": "Source request register",
    "addressOffset": "0x368",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRC_REQ0",
            "description": "Source request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SRC_REQ1",
            "description": "Source request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SRC_REQ2",
            "description": "Source request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Source request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Source request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Source request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_ReqDstReg = {
    "name": "ReqDstReg",
    "displayName": "ReqDstReg",
    "description": "Destination request register",
    "addressOffset": "0x370",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DST_REQ0",
            "description": "Destination request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DST_REQ1",
            "description": "Destination request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "DST_REQ2",
            "description": "Destination request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Destination request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Destination request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Destination request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_SglReqSrcReg = {
    "name": "SglReqSrcReg",
    "displayName": "SglReqSrcReg",
    "description": "Source single request register",
    "addressOffset": "0x378",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "S_SG_REQ0",
            "description": "Source single request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "S_SG_REQ1",
            "description": "Source single request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "S_SG_REQ2",
            "description": "Source single request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Source single request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Source single request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Source single request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_SglReqDstReg = {
    "name": "SglReqDstReg",
    "displayName": "SglReqDstReg",
    "description": "Destination single request register",
    "addressOffset": "0x380",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "D_SG_REQ0",
            "description": "Destination single request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "D_SG_REQ1",
            "description": "Destination single request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "D_SG_REQ2",
            "description": "Destination single request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Destination single request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Destination single request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Destination single request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_LstReqSrcReg = {
    "name": "LStReqSrcReg",
    "displayName": "LstReqSrcReg",
    "description": "Source last request register",
    "addressOffset": "0x388",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSTSRC0",
            "description": "Source last request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "LSTSRC1",
            "description": "Source last request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSTSRC2",
            "description": "Source last request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Source last request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Source last request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Source last request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_LstReqDstReg = {
    "name": "LStReqDstReg",
    "displayName": "LstReqDstReg",
    "description": "Destination last request register",
    "addressOffset": "0x390",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LSTDST0",
            "description": "Destination last request for channel 0",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "LSTDST1",
            "description": "Destination last request for channel 1",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "LSTDST2",
            "description": "Destination last request for channel 2",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "REQ_WE0",
            "description": "Destination last request write enable for channel 0",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "REQ_WE1",
            "description": "Destination last request write enable for channel 0",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "REQ_WE2",
            "description": "Destination last request write enable for channel 0",
            "bitRange": "[10:10]",
        }
    }
}

DMAC_DmaCfgReg = {
    "name": "DmaCfgReg",
    "displayName": "DmaCfgReg",
    "description": "DMA configuration register",
    "addressOffset": "0x398",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMA_EN",
            "description": "DMA enable",
            "bitRange": "[0:0]",
        }
    }
}

DMAC_ChEnReg = {
    "name": "ChEnReg",
    "displayName": "ChEnReg",
    "description": "Channel enable register",
    "addressOffset": "0x3A0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CHEN0",
            "description": "Channel 0 enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "CHEN1",
            "description": "Channel 1 enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "CHEN2",
            "description": "Channel 2 enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "CHEN_WE0",
            "description": "Channel 0 write enable",
            "bitRange": "[8:8]",
        },
        "field_4": {
            "name": "CHEN_WE1",
            "description": "Channel 1 write enable",
            "bitRange": "[9:9]",
        },
        "field_5": {
            "name": "CHEN_WE2",
            "description": "Channel 2 write enable",
            "bitRange": "[10:10]",
        }
    }
}

dmac1_define = {
    "name": "DMAC1",
    "description": "Direct memory access controller1 1",
    "groupName": "DMAC",
    "baseAddress": "0x40007C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "DMAC1",
        "description": "DMAC1 interrupt",
        "value": "11",
    },
    "registers": {
        "register_0": DMAC_SAR0,
        "register_1": DMAC_DAR0,
        "register_2": DMAC_CTLL0,
        "register_3": DMAC_CTLH0,
        "register_4": DMAC_CFGL0,
        "register_5": DMAC_CFGH0,
        "register_6": DMAC_SAR1,
        "register_7": DMAC_DAR1,
        "register_8": DMAC_CTLL1,
        "register_9": DMAC_CTLH1,
        "register_10": DMAC_CFGL1,
        "register_11": DMAC_CFGH1,
        "register_12": DMAC_SAR2,
        "register_13": DMAC_DAR2,
        "register_14": DMAC_CTLL2,
        "register_15": DMAC_CTLH2,
        "register_16": DMAC_CFGL2,
        "register_17": DMAC_CFGH2,
        "register_18": DMAC_SGR0,
        "register_19": DMAC_DSR0,
        "register_20": DMAC_RawTfr,
        "register_21": DMAC_RawBlock,
        "register_22": DMAC_RawSrcTran,
        "register_23": DMAC_RawDstTran,
        "register_24": DMAC_RawErr,
        "register_25": DMAC_StatusTfr,
        "register_26": DMAC_StatusBlock,
        "register_27": DMAC_StatusSrcTran,
        "register_28": DMAC_StatusDstTran,
        "register_29": DMAC_StatusErr,
        "register_30": DMAC_MaskTfr,
        "register_31": DMAC_MaskBlock,
        "register_32": DMAC_MaskSrcTran,
        "register_33": DMAC_MaskDstTran,
        "register_34": DMAC_MaskErr,
        "register_35": DMAC_ClrTrf,
        "register_36": DMAC_ClrBlock,
        "register_37": DMAC_ClrSrcTran,
        "register_38": DMAC_ClrDstTran,
        "register_39": DMAC_ClrErr,
        "register_40": DMAC_StatusInt,
        "register_41": DMAC_ReqSrcReg,
        "register_42": DMAC_ReqDstReg,
        "register_43": DMAC_SglReqSrcReg,
        "register_44": DMAC_SglReqDstReg,
        "register_45": DMAC_LstReqSrcReg,
        "register_46": DMAC_LstReqDstReg,
        "register_47": DMAC_DmaCfgReg,
        "register_48": DMAC_ChEnReg,
    }
}

dmac2_define = {
    "name": "DMAC2",
    "description": "Direct memory access controller1 2",
    "groupName": "DMAC",
    "baseAddress": "0x4000FC00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "DMAC2",
        "description": "DMAC2 interrupt",
        "value": "12",
    },
    "registers": {
        "register_0 ": DMAC_SAR0,
        "register_1 ": DMAC_DAR0,
        "register_2 ": DMAC_CTLL0,
        "register_3 ": DMAC_CTLH0,
        "register_4 ": DMAC_CFGL0,
        "register_5 ": DMAC_CFGH0,
        "register_6 ": DMAC_SAR1,
        "register_7 ": DMAC_DAR1,
        "register_8 ": DMAC_CTLL1,
        "register_9 ": DMAC_CTLH1,
        "register_10": DMAC_CFGL1,
        "register_11": DMAC_CFGH1,
        "register_12": DMAC_SAR2,
        "register_13": DMAC_DAR2,
        "register_14": DMAC_CTLL2,
        "register_15": DMAC_CTLH2,
        "register_16": DMAC_CFGL2,
        "register_17": DMAC_CFGH2,
        "register_18": DMAC_SGR0,
        "register_19": DMAC_DSR0,
        "register_20": DMAC_RawTfr,
        "register_21": DMAC_RawBlock,
        "register_22": DMAC_RawSrcTran,
        "register_23": DMAC_RawDstTran,
        "register_24": DMAC_RawErr,
        "register_25": DMAC_StatusTfr,
        "register_26": DMAC_StatusBlock,
        "register_27": DMAC_StatusSrcTran,
        "register_28": DMAC_StatusDstTran,
        "register_29": DMAC_StatusErr,
        "register_30": DMAC_MaskTfr,
        "register_31": DMAC_MaskBlock,
        "register_32": DMAC_MaskSrcTran,
        "register_33": DMAC_MaskDstTran,
        "register_34": DMAC_MaskErr,
        "register_35": DMAC_ClrTrf,
        "register_36": DMAC_ClrBlock,
        "register_37": DMAC_ClrSrcTran,
        "register_38": DMAC_ClrDstTran,
        "register_39": DMAC_ClrErr,
        "register_40": DMAC_StatusInt,
        "register_41": DMAC_ReqSrcReg,
        "register_42": DMAC_ReqDstReg,
        "register_43": DMAC_SglReqSrcReg,
        "register_44": DMAC_SglReqDstReg,
        "register_45": DMAC_LstReqSrcReg,
        "register_46": DMAC_LstReqDstReg,
        "register_47": DMAC_DmaCfgReg,
        "register_48": DMAC_ChEnReg,
    }
}
