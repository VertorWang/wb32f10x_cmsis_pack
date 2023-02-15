I2C_CON_I2C1 = {
    "name": "CON_I2C1",
    "displayName": "CON_I2C1",
    "description": "Control register for I2C1",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000024",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MST_MODE",
            "description": "Master mode enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SPEED",
            "description": "I2C transfer speed",
            "bitRange": "[2:1]",
        },
        "field_2": {
            "name": "IC_10ADDR_SLV",
            "description": "I2C slave 10 bits address selection",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "IC_10ADDR_MST",
            "description": "I2C master 10 bits address selection",
            "bitRange": "[4:4]",
        },
        "field_4": {
            "name": "IC_RS_EN",
            "description": "I2C restart enable",
            "bitRange": "[5:5]",
        },
        "field_5": {
            "name": "IC_SLV_DISABLE",
            "description": "I2C slave mode disable",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "STOP_DET_IFADDRESSED",
            "description": "STOP_DET interrupt enable when slave is addressed ",
            "bitRange": "[7:7]",
        },
        "field_7": {
            "name": "TX_EMP_CTRL",
            "description": "Transmit empty control",
            "bitRange": "[8:8]",
        },
        "field_8": {
            "name": "RX_FIFO_FULL_HLD_CTR",
            "description": "Hold bus when receive FIFO full control bit",
            "bitRange": "[9:9]",
        },
        "field_9": {
            "name": "STOP_DET_IF_MST_ACTIVE",
            "description": " STOP_DET interrupt enable when master is active",
            "bitRange": "[10:10]",
        },
        "field_10": {
            "name": "BUS_CLR_CTRL",
            "description": "Bus clear control",
            "bitRange": "[11:11]",
        },
        "field_11": {
            "name": "OP_SAR_CTRL",
            "description": "Optional slave address control",
            "bitRange": "[16:16]",
        },
        "field_12": {
            "name": "SMBUS_SLV_QUICK_EN",
            "description": "SMBUS slave quick command enable",
            "bitRange": "[17:17]",
        },
        "field_13": {
            "name": "SMBUS_ARP_EN",
            "description": "SMBUS ARP enable",
            "bitRange": "[18:18]",
        },
        "field_14": {
            "name": "SMBUS_PERS_SLV_ADDR_EN",
            "description": "SMBUS PSA enable",
            "bitRange": "[19:19]",
        }
    }
}

I2C_CON_I2C2 = {
    "name": "CON_I2C2",
    "displayName": "CON_I2C2",
    "description": "Control register for I2C2",
    "alternateRegister": "CON_I2C1",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000003E",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "MST_MODE",
            "description": "Master mode enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SPEED",
            "description": "I2C transfer speed",
            "bitRange": "[2:1]",
        },
        "field_2": {
            "name": "IC_10ADDR_SLV",
            "description": "I2C slave 10 bits address selection",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "IC_10ADDR_MST",
            "description": "I2C master 10 bits address selection",
            "bitRange": "[4:4]",
        },
        "field_4": {
            "name": "IC_RS_EN",
            "description": "I2C restart enable",
            "bitRange": "[5:5]",
        },
        "field_5": {
            "name": "IC_SLV_DISABLE",
            "description": "I2C slave mode disable",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "STOP_DET_IFADDRESSED",
            "description": "STOP_DET interrupt enable when slave is addressed ",
            "bitRange": "[7:7]",
        },
        "field_7": {
            "name": "TX_EMP_CTRL",
            "description": "Transmit empty control",
            "bitRange": "[8:8]",
        },
        "field_8": {
            "name": "RX_FIFO_FULL_HLD_CTR",
            "description": "Hold bus when receive FIFO full control bit",
            "bitRange": "[9:9]",
        },
        "field_9": {
            "name": "STOP_DET_IF_MST_ACTIVE",
            "description": " STOP_DET interrupt enable when master is active",
            "bitRange": "[10:10]",
        },
        "field_10": {
            "name": "BUS_CLR_CTRL",
            "description": "Bus clear control",
            "bitRange": "[11:11]",
        },
        "field_11": {
            "name": "OP_SAR_CTRL",
            "description": "Optional slave address control",
            "bitRange": "[16:16]",
        },
        "field_12": {
            "name": "SMBUS_SLV_QUICK_EN",
            "description": "SMBUS slave quick command enable",
            "bitRange": "[17:17]",
        },
        "field_13": {
            "name": "SMBUS_ARP_EN",
            "description": "SMBUS ARP enable",
            "bitRange": "[18:18]",
        },
        "field_14": {
            "name": "SMBUS_PERS_SLV_ADDR_EN",
            "description": "SMBUS PSA enable",
            "bitRange": "[19:19]",
        }
    }
}

I2C_TAR = {
    "name": "TAR",
    "displayName": "TAR",
    "description": "Target register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000055",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TAR",
            "description": "Target address",
            "bitRange": "[9:0]",
        },
        "field_1": {
            "name": "GC_OP_START",
            "description": "GENERAL CALL or START optional",
            "bitRange": "[10:10]",
        },
        "field_2": {
            "name": "SPECIAL",
            "description": "Enable DEVICE_ID,GENERAL_CALL and START transfer",
            "bitRange": "[11:11]",
        },
        "field_3": {
            "name": "DEVICE_ID",
            "description": "Enable DEVICE_ID",
            "bitRange": "[13:13]",
        },
        "field_4": {
            "name": "SMBUS_QUICK_CMD",
            "description": "SMBUS QUICK_CMD enable",
            "bitRange": "[16:16]",
        }
    }
}

I2C_SAR = {
    "name": "SAR",
    "displayName": "SAR",
    "description": "Slave address register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x000003F0",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SAR",
            "description": "Slave address",
            "bitRange": "[9:0]",
        }
    }
}

I2C_HS_MADDR = {
    "name": "HS_MADDR",
    "displayName": "HS_MADDR",
    "description": "High speed master address register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "HS_MAR",
            "description": "Master address in high speed",
            "bitRange": "[2:0]",
        }
    }
}

I2C_DATA_CMD = {
    "name": "DATA_CMD",
    "displayName": "DATA_CMD",
    "description": "I2C data and command register",
    "addressOffset": "0x10",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DAT",
            "description": "Data of I2C bus",
            "bitRange": "[7:0]",
        },
        "field_1": {
            "name": "READ",
            "description": "Master send read command",
            "bitRange": "[8:8]",
        },
        "field_2": {
            "name": "STOP",
            "description": "Send stop command after transmitting or receiving",
            "bitRange": "[9:9]",
        },
        "field_3": {
            "name": "RESTART",
            "description": "Send restart command after transmitting",
            "bitRange": "[10:10]",
        },
        "field_4": {
            "name": "FIRST_DATA_BYTE",
            "description": "First data byte",
            "bitRange": "[11:11]",
        }
    }
}

I2C_SS_SCL_HCNT = {
    "name": "SS_SCL_HCNT",
    "displayName": "SS_SCL_HCNT",
    "description": "Standard speed clock high counter register",
    "addressOffset": "0x14",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000320",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_SS_SCL_HCNT",
            "description": "SCL high level time in I2C standard speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_SS_SCL_LCNT = {
    "name": "SS_SCL_LCNT",
    "displayName": "SS_SCL_LCNT",
    "description": "Standard speed clock low counter register",
    "addressOffset": "0x18",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x000003AC",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_SS_SCL_LCNT",
            "description": "SCL low level time in I2C standard speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_FS_SCL_HCNT = {
    "name": "FS_SCL_HCNT",
    "displayName": "FS_SCL_HCNT",
    "description": "Fast speed clock high counter register",
    "addressOffset": "0x1C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000078",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_FS_SCL_HCNT",
            "description": "SCL high level time in I2C fast speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_FS_SCL_LCNT = {
    "name": "FS_SCL_LCNT",
    "displayName": "FS_SCL_LCNT",
    "description": "Fast speed clock low counter register",
    "addressOffset": "0x20",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000104",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_FS_SCL_LCNT",
            "description": "SCL low level time in I2C fast speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_HS_SCL_HCNT = {
    "name": "HS_SCL_HCNT",
    "displayName": "HS_SCL_HCNT",
    "description": "High speed clock high counter register",
    "addressOffset": "0x24",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000C",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_HS_SCL_HCNT",
            "description": "SCL high level time in I2C high speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_HS_SCL_LCNT = {
    "name": "HS_SCL_LCNT",
    "displayName": "HS_SCL_LCNT",
    "description": "High speed clock low counter register",
    "addressOffset": "0x28",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000020",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_HS_SCL_LCNT",
            "description": "SCL low level time in I2C high speed mode",
            "bitRange": "[15:0]",
        }
    }
}

I2C_INTR_STAT = {
    "name": "INTR_STAT",
    "displayName": "INTR_STAT",
    "description": "I2C interrupt state register",
    "addressOffset": "0x2C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "R_RX_UNDER",
            "description": "R_RX_UNDER interrupt state",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "R_RX_OVER",
            "description": "R_RX_OVER interrupt state",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "R_RX_FULL",
            "description": "R_RX_FULL interrupt state",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "R_TX_OVER",
            "description": "R_TX_OVER interrupt state",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "R_TX_EMPTY",
            "description": "R_TX_EMPTY interrupt state",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "R_RD_REQ",
            "description": "R_RD_REQ interrupt state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "R_TX_ABRT",
            "description": "R_TX_ABRT interrupt state",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "R_RX_DONE",
            "description": "R_RX_DONE interrupt state",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "R_ACTIVITY",
            "description": "R_ACTIVITY interrupt state",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "R_STOP_DET",
            "description": "R_STOP_DET interrupt state",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "R_START_DET",
            "description": "R_START_DET interrupt state",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "R_GEN_CALL",
            "description": "R_GEN_CALL interrupt state",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "R_RS_DET",
            "description": "R_RS_DET interrupt state",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "R_SCL_STUCK_AT_LOW",
            "description": "R_SCL_STUCK_AT_LOW interrupt state",
            "bitRange": "[14:14]",
        }
    }
}

I2C_INTR_MASK = {
    "name": "INTR_MASK",
    "displayName": "INTR_MASK",
    "description": "I2C interrupt mask register",
    "addressOffset": "0x30",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x000048FF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "R_RX_UNDER",
            "description": "R_RX_UNDER interrupt mask",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "R_RX_OVER",
            "description": "R_RX_OVER interrupt mask",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "R_RX_FULL",
            "description": "R_RX_FULL interrupt mask",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "R_TX_OVER",
            "description": "R_TX_OVER interrupt mask",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "R_TX_EMPTY",
            "description": "R_TX_EMPTY interrupt mask",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "R_RD_REQ",
            "description": "R_RD_REQ interrupt mask",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "R_TX_ABRT",
            "description": "R_TX_ABRT interrupt mask",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "R_RX_DONE",
            "description": "R_RX_DONE interrupt mask",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "R_ACTIVITY",
            "description": "R_ACTIVITY interrupt mask",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "R_STOP_DET",
            "description": "R_STOP_DET interrupt mask",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "R_START_DET",
            "description": "R_START_DET interrupt mask",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "R_GEN_CALL",
            "description": "R_GEN_CALL interrupt mask",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "R_RS_DET",
            "description": "R_RS_DET interrupt mask",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "R_SCL_STUCK_AT_LOW",
            "description": "R_SCL_STUCK_AT_LOW interrupt mask",
            "bitRange": "[14:14]",
        }
    }
}

I2C_RAW_INTR_STAT = {
    "name": "RAW_INTR_STAT",
    "displayName": "RAW_INTR_STAT",
    "description": "I2C raw interrupt state register",
    "addressOffset": "0x34",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "R_RX_UNDER",
            "description": "R_RX_UNDER interrupt raw state",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "R_RX_OVER",
            "description": "R_RX_OVER interrupt raw state",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "R_RX_FULL",
            "description": "R_RX_FULL interrupt raw state",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "R_TX_OVER",
            "description": "R_TX_OVER interrupt raw state",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "R_TX_EMPTY",
            "description": "R_TX_EMPTY interrupt raw state",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "R_RD_REQ",
            "description": "R_RD_REQ interrupt raw state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "R_TX_ABRT",
            "description": "R_TX_ABRT interrupt raw state",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "R_RX_DONE",
            "description": "R_RX_DONE interrupt raw state",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "R_ACTIVITY",
            "description": "R_ACTIVITY interrupt raw state",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "R_STOP_DET",
            "description": "R_STOP_DET interrupt raw state",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "R_START_DET",
            "description": "R_START_DET interrupt raw state",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "R_GEN_CALL",
            "description": "R_GEN_CALL interrupt raw state",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "R_RS_DET",
            "description": "R_RS_DET interrupt raw state",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "R_SCL_STUCK_AT_LOW",
            "description": "R_SCL_STUCK_AT_LOW interrupt raw state",
            "bitRange": "[14:14]",
        }
    }
}

I2C_RX_TL = {
    "name": "RX_TL",
    "displayName": "RX_TL",
    "description": "Receive buffer threshold register",
    "addressOffset": "0x38",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000005",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RX_TL",
            "description": "Receive buffer threshold",
            "bitRange": "[7:0]",
        }
    }
}

I2C_TX_TL = {
    "name": "TX_TL",
    "displayName": "TX_TL",
    "description": "Transmit buffer threshold register",
    "addressOffset": "0x3C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000005",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TX_TL",
            "description": "Transmit buffer threshold",
            "bitRange": "[7:0]",
        }
    }
}

I2C_CLR_INTR = {
    "name": "CLR_INTR",
    "displayName": "CLR_INTR",
    "description": "Clear interrupt register",
    "addressOffset": "0x40",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_INTR",
            "description": "Clear all interrupt states when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_RX_UNDER = {
    "name": "CLR_RX_UNDER",
    "displayName": "CLR_RX_UNDER",
    "description": "Clear RX_UNDER interrupt register",
    "addressOffset": "0x44",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RX_UNDER",
            "description": "Clear RX_UNDER interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_RX_OVER = {
    "name": "CLR_RX_OVER",
    "displayName": "CLR_RX_OVER",
    "description": "Clear RX_OVER interrupt register",
    "addressOffset": "0x48",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RX_OVER",
            "description": "Clear RX_OVER interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_TX_OVER = {
    "name": "CLR_TX_OVER",
    "displayName": "CLR_TX_OVER",
    "description": "Clear TX_OVER interrupt register",
    "addressOffset": "0x4C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RX_OVER",
            "description": "Clear TX_OVER interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_RD_REQ = {
    "name": "CLR_RD_REQ",
    "displayName": "CLR_RD_REQ",
    "description": "Clear RD_REQ interrupt register",
    "addressOffset": "0x50",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RD_REQ",
            "description": "Clear RD_REQ interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_TX_ABRT = {
    "name": "CLR_TX_ABRT",
    "displayName": "CLR_TX_ABRT",
    "description": "Clear TX_ABRT interrupt register",
    "addressOffset": "0x54",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_TX_ABRT",
            "description": "Clear TX_ABRT interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_RX_DONE = {
    "name": "CLR_RX_DONE",
    "displayName": "CLR_RX_DONE",
    "description": "Clear RX_DONE interrupt register",
    "addressOffset": "0x58",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RX_DONE",
            "description": "Clear RX_DONE interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_ACTIVITY = {
    "name": "CLR_ACTIVITY",
    "displayName": "CLR_ACTIVITY",
    "description": "Clear TX_OVER interrupt register",
    "addressOffset": "0x5C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_ACTIVITY",
            "description": "Clear ACTIVITY interrupt when read this bit and I2C is not in active state",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_STOP_DET = {
    "name": "CLR_STOP_DET",
    "displayName": "CLR_STOP_DET",
    "description": "Clear STOP_DET interrupt register",
    "addressOffset": "0x60",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_STOP_DET",
            "description": "Clear STOP_DET interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_START_DET = {
    "name": "CLR_START_DET",
    "displayName": "CLR_START_DET",
    "description": "Clear START_DET interrupt register",
    "addressOffset": "0x64",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_START_DET",
            "description": "Clear START_DET interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_CLR_GEN_CALL = {
    "name": "CLR_GEN_CALL",
    "displayName": "CLR_GEN_CALL",
    "description": "Clear GEN_CALL interrupt register",
    "addressOffset": "0x68",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_GEN_CALL",
            "description": "Clear GEN_CALL interrupt when read this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_ENABLE = {
    "name": "ENABLE",
    "displayName": "ENABLE",
    "description": "I2C enable register",
    "addressOffset": "0x6C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ENABLE",
            "description": "Enable I2C",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "ABORT",
            "description": "Abort transfer in master mode by setting this bit",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TX_CMD_BLOCK",
            "description": "Block I2C bus transfer",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SDA_STUCK_RC_EN",
            "description": "Recover SDA bus enable when SDA bus stuck in low level",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SM_CLK_RS",
            "description": "SMBUS clock reset",
            "bitRange": "[16:16]",
        },
        "field_5": {
            "name": "SM_SUSPEND_EN",
            "description": "SMBUS suspend enable",
            "bitRange": "[17:17]",
        },
        "field_6": {
            "name": "SM_ALTER_EN",
            "description": "SMBUS alerter enable",
            "bitRange": "[18:18]",
        }
    }
}

I2C_STATUS = {
    "name": "STATUS",
    "displayName": "STATUS",
    "description": "I2C status register",
    "addressOffset": "0x70",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000006",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ACTIVITY",
            "description": "I2C activity status",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TFNF",
            "description": "Transmit buffer not full",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TFE",
            "description": "Transmit buffer empty",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "RFNE",
            "description": "Receive buffer not empty",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "RFF",
            "description": "Receive buffer full",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "MST_ACTIVITY",
            "description": "Master activity status",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "SLV_ACTIVITY",
            "description": "Slave activity status",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "MST_HOLD_TX_FIFO_EMPTY",
            "description": "Master hold bus when transmit FIFO is empty",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "MST_HOLD_RX_FIFO_FULL",
            "description": "Master hold bus when receive FIFO is full",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "SLV_HOLD_TX_FIFO_EMPTY",
            "description": "Slave hold bus when transmit FIFO is empty",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "SLV_HOLD_RX_FIFO_FULL",
            "description": "Slave hold bus when receive FIFO is full",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "SDA_STUCK_NOT_RECOVERED",
            "description": "SDA status after recover",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "SM_QUICK_CMD_BIT",
            "description": "SMBUS QUICK CMD control",
            "bitRange": "[16:16]",
        },
        "field_13": {
            "name": "SM_SLV_ADDR_VLD",
            "description": "SMBUS slave address valuable",
            "bitRange": "[17:17]",
        },
        "field_14": {
            "name": "SM_SLV_ADDR_RESOLVED",
            "description": "SMBUS slave address resolved",
            "bitRange": "[18:18]",
        },
        "field_15": {
            "name": "SM_SUSPEND_STATUS",
            "description": "SMBUS suspend status",
            "bitRange": "[19:19]",
        },
        "field_16": {
            "name": "SM_ALTER_STATUS",
            "description": "SMBUS alerter satus",
            "bitRange": "[20:20]",
        }
    }
}

I2C_TXFLR = {
    "name": "TXFLR",
    "displayName": "TXFLR",
    "description": "Transmit buffer level register",
    "addressOffset": "0x74",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "TXFLR",
            "description": "Data numbers of transmit buffer",
            "bitRange": "[2:0]",
        }
    }
}

I2C_RXFLR = {
    "name": "RXFLR",
    "displayName": "RXFLR",
    "description": "Receive buffer level register",
    "addressOffset": "0x78",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "RXFLR",
            "description": "Data numbers of Receive buffer",
            "bitRange": "[2:0]",
        }
    }
}

I2C_SDA_HOLD = {
    "name": "SDA_HOLD",
    "displayName": "SDA_HOLD",
    "description": "SDA hold register",
    "addressOffset": "0x7C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000002",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_SDA_TX_HOLD",
            "description": "SDA hold time in transmit mode",
            "bitRange": "[15:0]",
        },
        "field_1": {
            "name": "IC_SDA_RX_HOLD",
            "description": "SDA hold time in receive mode",
            "bitRange": "[23:16]",
        }
    }
}

I2C_TX_ABRT_SOURCE = {
    "name": "TX_ABRT_SOURCE",
    "displayName": "TX_ABRT_SOURCE",
    "description": "Transmit abort source register",
    "addressOffset": "0x80",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "7B_ADDR_NOACK",
            "description": "No ACK in 7 bits address mode",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "10ADDR1_NOACK",
            "description": "No ACK for first address byte in 10 bits address mode",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "10ADDR2_NOACK",
            "description": "No ACK for second address byte in 10 bits address mode",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TXDATA_NOACK",
            "description": "No ACK for transmitting data",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "GCALL_NOACK",
            "description": "No ACK for sending GCALL",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "GCALL_READ",
            "description": "READ command after sending GCALL",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "HS_ACKDET",
            "description": "ACK for master's sending HS code",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "SBYTE_ACKDET",
            "description": "ACK for master's sending START",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "HS_NORSTRT",
            "description": "RESTART is disable when master is switching to HS mode",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "SBYTE_NORSTRT",
            "description": "RESTART is disable when master is sending START",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "10B_RD_NORSTRT",
            "description": "Read data in 10 bits address mode when RESTART is disable",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "MASTER_DIS",
            "description": "Master is disable when asked to transmit",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "LOST",
            "description": "BUS arbitration failure",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "SLVFLUSH_TXFIFO",
            "description": "Data remains in transmit FIFO when slave receive a read request",
            "bitRange": "[13:13]",
        },
        "field_14": {
            "name": "SLV_ARBLOST",
            "description": "BUS arbitration lost when slave is transmitting",
            "bitRange": "[14:14]",
        },
        "field_15": {
            "name": "SLVRD_INTX",
            "description": "Write 1 into DATA_CMD.READ when slave receive a read request from master",
            "bitRange": "[15:15]",
        },
        "field_16": {
            "name": "USER_ABRT",
            "description": "Transfer abort",
            "bitRange": "[16:16]",
        },
        "field_17": {
            "name": "SDA_STUCK_AT_LOW",
            "description": "SDA stucks at low level for several ic_clk cycles which is specified in related register",
            "bitRange": "[17:17]",
        },
        "field_18": {
            "name": "DEVICE_NOACK",
            "description": "No ACK for master's DEVICE_ID transfer",
            "bitRange": "[18:18]",
        },
        "field_19": {
            "name": "DEVICE_SLVADDR_NOACK",
            "description": "No ACK from addressed slave for master's DEVICE_ID transfer",
            "bitRange": "[19:19]",
        },
        "field_20": {
            "name": "DEVICE_WRITE",
            "description": "Other commands remain in Transmit FIFO when master start a DEVICE_ID transfer",
            "bitRange": "[20:20]",
        },
        "field_21": {
            "name": "TX_FLUSH_CNT",
            "description": "Number of data lost because of TX_ABRT interrupt",
            "bitRange": "[31:23]",
        }
    }
}

I2C_SLV_DATA_NACK_ONLY = {
    "name": "SLV_DATA_NACK_ONLY",
    "displayName": "SLV_DATA_NACK_ONLY",
    "description": "Slave data NACK register",
    "addressOffset": "0x84",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "NACK",
            "description": "Generate NACK",
            "bitRange": "[0:0]",
        }
    }
}

I2C_DMA_CR = {
    "name": "DMA_CR",
    "displayName": "DMA_CR",
    "description": "DMA control register",
    "addressOffset": "0x88",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
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

I2C_DMA_TDLR = {
    "name": "DMA_TDLR",
    "displayName": "DMA_TDLR",
    "description": "DMA transmit data level register",
    "addressOffset": "0x8C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMATDL",
            "description": "DMA transmit data level",
            "bitRange": "[2:0]",
        }
    }
}

I2C_DMA_RDLR = {
    "name": "DMA_RDLR",
    "displayName": "DMA_RDLR",
    "description": "DMA receive data level register",
    "addressOffset": "0x90",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMARDL",
            "description": "DMA receive data level",
            "bitRange": "[2:0]",
        }
    }
}

I2C_SDA_SETUP = {
    "name": "SDA_SETUP",
    "displayName": "SDA_SETUP",
    "description": "SDA set-up time register",
    "addressOffset": "0x94",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SDA_SETUP",
            "description": "SDA set-up time",
            "bitRange": "[7:0]",
        }
    }
}

I2C_ACK_GENERAL_CALL = {
    "name": "ACK_GENERAL_CALL",
    "displayName": "ACK_GENERAL_CALL",
    "description": "ACK general call register",
    "addressOffset": "0x98",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000064",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ACK_GENERAL_CALL",
            "description": "ACK/NACK for a general all",
            "bitRange": "[0:0]",
        }
    }
}

I2C_ENABLE_STATUS = {
    "name": "ENABLE_STATUS",
    "displayName": "ENABLE_STATUS",
    "description": "Enable status register",
    "addressOffset": "0x9C",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_EN",
            "description": "I2C enable status",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "SLV_DIS_WHILE_BUSY_LOST",
            "description": "Slave disable while busy lost",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "SLV_RX_DATA_LOST",
            "description": "Slave lost receive data",
            "bitRange": "[2:2]",
        }
    }
}

I2C_FS_SPKLEN1 = {
    "name": "FS_SPKLEN1",
    "displayName": "FS_SPKLEN1",
    "description": "Fast speed spike length register for I2C1",
    "addressOffset": "0xA0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_FS_SPKLEN",
            "description": "Max spike value on SCL and SDA line in standard and fast speed mode",
            "bitRange": "[7:0]",
        }
    }
}

I2C_FS_SPKLEN2 = {
    "name": "FS_SPKLEN2",
    "displayName": "FS_SPKLEN2",
    "description": "Fast speed spike length register for I2C2",
    "alternateRegister": "FS_SPKLEN1",
    "addressOffset": "0xA0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000005",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_FS_SPKLEN",
            "description": "Max spike value on SCL and SDA line in standard and fast speed mode",
            "bitRange": "[7:0]",
        }
    }
}

I2C_HS_SPKLEN = {
    "name": "HS_SPKLEN",
    "displayName": "HS_SPKLEN",
    "description": "High speed spike length register",
    "addressOffset": "0xA4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IC_FS_SPKLEN",
            "description": "Max spike value on SCL and SDA line in high speed mode",
            "bitRange": "[7:0]",
        }
    }
}

I2C_CLR_RESTART_DET = {
    "name": "CLR_RESTART_DET",
    "displayName": "CLR_RESTART_DET",
    "description": "Clear RESTART_DET interrupt register",
    "addressOffset": "0xA8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x0000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_RS_DET",
            "description": "Clear RESTART_DET interrupt when user reads this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_SCL_STUCK_AT_LOW_TIMEOUT = {
    "name": "SCL_STUCK_AT_LOW_TIMEOUT",
    "displayName": "SCL_STUCK_AT_LOW_TIMEOUT",
    "description": "SCl stuck at low level timeout register",
    "addressOffset": "0xAC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0xFFFFFFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCL_LOWTO",
            "description": "Timeout threshold for SCL_STUCK_AT_LOW interrupt",
            "bitRange": "[31:0]",
        }
    }
}

I2C_SDA_STUCK_AT_LOW_TIMEOUT = {
    "name": "SDA_STUCK_AT_LOW_TIMEOUT",
    "displayName": "SDA_STUCK_AT_LOW_TIMEOUT",
    "description": "SDA stuck at low level timeout register",
    "addressOffset": "0xB0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0xFFFFFFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SDA_LOWTO",
            "description": "Timeout threshold for SDA",
            "bitRange": "[31:0]",
        }
    }
}

I2C_CLR_SCL_STUCK_DET = {
    "name": "CLR_SCL_STUCK_DET",
    "displayName": "CLR_SCL_STUCK_DET",
    "description": "Clear SCL STUCK_DET interrupt register",
    "addressOffset": "0xB4",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR_SCL_STUCK_DET",
            "description": "Clear SCL STUCK_DET interrupt when user reads this bit",
            "bitRange": "[0:0]",
        }
    }
}

I2C_SMBUS_CLK_LOW_SEXT = {
    "name": "SMBUS_CLK_LOW_SEXT",
    "displayName": "SMBUS_CLK_LOW_SEXT",
    "description": "SMBUS clock low slave extend timeout register",
    "addressOffset": "0xBC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0xFFFFFFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SMBUS_CLK_LOW_SEXT_TO",
            "description": "Define a paragram of SMBUS",
            "bitRange": "[31:0]",
        }
    }
}

I2C_SMBUS_CLK_LOW_MEXT = {
    "name": "SMBUS_CLK_LOW_MEXT",
    "displayName": "SMBUS_CLK_LOW_MEXT",
    "description": "SMBUS clock low master extend timeout register",
    "addressOffset": "0xC0",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0xFFFFFFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SMBUS_CLK_LOW_MEXT_TO",
            "description": "Define a paragram of SMBUS",
            "bitRange": "[31:0]",
        }
    }
}

I2C_SMBUS_THIGH_MAX_IDLE_COUNT = {
    "name": "SMBUS_THIGH_MAX_IDLE_COUNT",
    "displayName": "SMBUS_THIGH_MAX_IDLE_COUNT",
    "description": "SMBUS master tight max bus-idle count register",
    "addressOffset": "0xC4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000FFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SMBUS_MBI_CNT",
            "description": "Define SMBUS max idle time",
            "bitRange": "[15:0]",
        }
    }
}

I2C_SMBUS_INTR_STAT = {
    "name": "SMBUS_INTR_STAT",
    "displayName": "SMBUS_INTR_STAT",
    "description": "SMBUS interrupt state register",
    "addressOffset": "0xC8",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCLKEXT_TIMEOUT",
            "description": "SCLKEXT_TIMEOUT interrupt state",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MCLKEXT_TIMEOUT",
            "description": "MCLKEXT_TIMEOUT interrupt state",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "QUICK_CMD_DET",
            "description": "QUICK_CMD_DET interrupt state",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HOST_NOTIFY_MST_DET",
            "description": "HOST_NOTIFY_MST_DET interrupt state",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "ARP_PREPARE_CMD_DET",
            "description": "ARP_PREPARE_CMD_DET interrupt state",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "ARP_RST_CMD_DET",
            "description": "ARP_RST_CMD_DET interrupt state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "ARP_GET_UDID_CMD_DET",
            "description": "ARP_GET_UDID_CMD_DET interrupt state",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "ARP_ASSGN_ADDR_CMD_DET",
            "description": "ARP_ASSGN_ADDR_CMD_DET interrupt state",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "SLV_RX_PEC_NACK",
            "description": "SLV_RX_PEC_NACK interrupt state",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "SMBUS_SUSPEND_DET",
            "description": "SMBUS_SUSPEND_DET interrupt state",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "SMBUS_ALERT_DET",
            "description": "SMBUS_ALERT_DET interrupt state",
            "bitRange": "[10:10]",
        }
    }
}

I2C_SMBUS_INTR_MASK = {
    "name": "SMBUS_INTR_MASK",
    "displayName": "SMBUS_INTR_MASK",
    "description": "SMBUS interrupt mask register",
    "addressOffset": "0xCC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "M_SCLKEXT_TIMEOUT",
            "description": "SCLKEXT_TIMEOUT interrupt mask",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "M_MCLKEXT_TIMEOUT",
            "description": "MCLKEXT_TIMEOUT interrupt mask",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "M_QUICK_CMD_DET",
            "description": "QUICK_CMD_DET interrupt mask",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "M_HOST_NOTIFY_MST_DET",
            "description": "HOST_NOTIFY_MST_DET interrupt mask",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "M_ARP_PREPARE_CMD_DET",
            "description": "ARP_PREPARE_CMD_DET interrupt mask",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "M_ARP_RST_CMD_DET",
            "description": "ARP_RST_CMD_DET interrupt mask",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "M_ARP_GET_UDID_CMD_DET",
            "description": "ARP_GET_UDID_CMD_DET interrupt mask",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "M_ARP_ASSGN_ADDR_CMD_DET",
            "description": "ARP_ASSGN_ADDR_CMD_DET interrupt mask",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "M_SLV_RX_PEC_NACK",
            "description": "SLV_RX_PEC_NACK interrupt mask",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "M_SMBUS_SUSPEND_DET",
            "description": "SMBUS_SUSPEND_DET interrupt mask",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "M_SMBUS_ALERT_DET",
            "description": "SMBUS_ALERT_DET interrupt mask",
            "bitRange": "[10:10]",
        }
    }
}

I2C_SMBUS_RAW_INTR_STAT = {
    "name": "SMBUS_RAW_INTR_STAT",
    "displayName": "SMBUS_RAW_INTR_STAT",
    "description": "SMBUS raw interrupt state register",
    "addressOffset": "0xD0",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCLKEXT_TIMEOUT",
            "description": "SCLKEXT_TIMEOUT raw interrupt state",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MCLKEXT_TIMEOUT",
            "description": "MCLKEXT_TIMEOUT raw interrupt state",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "QUICK_CMD_DET",
            "description": "QUICK_CMD_DET raw interrupt state",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HOST_NOTIFY_MST_DET",
            "description": "HOST_NOTIFY_MST_DET raw interrupt state",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "ARP_PREPARE_CMD_DET",
            "description": "ARP_PREPARE_CMD_DET raw interrupt state",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "ARP_RST_CMD_DET",
            "description": "ARP_RST_CMD_DET raw interrupt state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "ARP_GET_UDID_CMD_DET",
            "description": "ARP_GET_UDID_CMD_DET raw interrupt state",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "ARP_ASSGN_ADDR_CMD_DET",
            "description": "ARP_ASSGN_ADDR_CMD_DET raw interrupt state",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "SLV_RX_PEC_NACK",
            "description": "SLV_RX_PEC_NACK raw interrupt state",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "SMBUS_SUSPEND_DET",
            "description": "SMBUS_SUSPEND_DET raw interrupt state",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "SMBUS_ALERT_DET",
            "description": "SMBUS_ALERT_DET raw interrupt state",
            "bitRange": "[10:10]",
        }
    }
}

I2C_CLR_SMBUS_INTR = {
    "name": "CLR_SMBUS_INTR",
    "displayName": "CLR_SMBUS_INTR",
    "description": "Clear SMBUS interrupt register",
    "addressOffset": "0xD4",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCLKEXT_TIMEOUT",
            "description": "Clear SCLKEXT_TIMEOUT interrupt state",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "MCLKEXT_TIMEOUT",
            "description": "Clear MCLKEXT_TIMEOUT interrupt state",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "QUICK_CMD_DET",
            "description": "Clear QUICK_CMD_DET interrupt state",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "HOST_NOTIFY_MST_DET",
            "description": "Clear HOST_NOTIFY_MST_DET interrupt state",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "ARP_PREPARE_CMD_DET",
            "description": "Clear ARP_PREPARE_CMD_DET interrupt state",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "ARP_RST_CMD_DET",
            "description": "Clear ARP_RST_CMD_DET interrupt state",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "ARP_GET_UDID_CMD_DET",
            "description": "Clear ARP_GET_UDID_CMD_DET interrupt state",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "ARP_ASSGN_ADDR_CMD_DET",
            "description": "Clear ARP_ASSGN_ADDR_CMD_DET interrupt state",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "SLV_RX_PEC_NACK",
            "description": "Clear SLV_RX_PEC_NACK interrupt state",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "SMBUS_SUSPEND_DET",
            "description": "Clear SMBUS_SUSPEND_DET interrupt state",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "SMBUS_ALERT_DET",
            "description": "Clear SMBUS_ALERT_DET interrupt state",
            "bitRange": "[10:10]",
        }
    }
}

I2C_OPTIONAL_SAR = {
    "name": "OPTIONAL_SAR",
    "displayName": "OPTIONAL_SAR",
    "description": "Optional slave address register",
    "addressOffset": "0xD8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "OPTIONAL_SAR",
            "description": "Optional slave address",
            "bitRange": "[6:0]",
        }
    }
}


I2C_SMBUS_UDID_LSB = {
    "name": "SMBUS_UDID_LSB",
    "displayName": "SMBUS_UDID_LSB",
    "description": "SMBUS UDID LSB register",
    "addressOffset": "0xDC",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0xFFFFFFFF",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SMBUS_UDID_LSB",
            "description": "LSB 32 bits of SMBUS UDID",
            "bitRange": "[31:0]",
        }
    }
}


i2c1_define = {
    "name": "I2C1",
    "description": "Inter-Integrated Circuit 1",
    "groupName": "I2C",
    "baseAddress": "0x40008800",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "I2C1",
        "description": "I2C1 interrupt",
        "value": "24",
    },
    "registers": {
        "register_0 ": I2C_CON_I2C1,
        "register_1 ": I2C_TAR,
        "register_2 ": I2C_SAR,
        "register_3 ": I2C_HS_MADDR,
        "register_4 ": I2C_DATA_CMD,
        "register_5 ": I2C_SS_SCL_HCNT,
        "register_6 ": I2C_SS_SCL_LCNT,
        "register_7 ": I2C_FS_SCL_HCNT,
        "register_8 ": I2C_FS_SCL_LCNT,
        "register_9 ": I2C_HS_SCL_HCNT,
        "register_10": I2C_HS_SCL_LCNT,
        "register_11": I2C_INTR_STAT,
        "register_12": I2C_INTR_MASK,
        "register_13": I2C_RAW_INTR_STAT,
        "register_14": I2C_RX_TL,
        "register_15": I2C_TX_TL,
        "register_16": I2C_CLR_INTR,
        "register_17": I2C_CLR_RX_UNDER,
        "register_18": I2C_CLR_RX_OVER,
        "register_19": I2C_CLR_TX_OVER,
        "register_20": I2C_CLR_RD_REQ,
        "register_21": I2C_CLR_TX_ABRT,
        "register_22": I2C_CLR_RX_DONE,
        "register_23": I2C_CLR_ACTIVITY,
        "register_24": I2C_CLR_STOP_DET,
        "register_25": I2C_CLR_START_DET,
        "register_26": I2C_CLR_GEN_CALL,
        "register_27": I2C_ENABLE,
        "register_28": I2C_STATUS,
        "register_29": I2C_TXFLR,
        "register_30": I2C_RXFLR,
        "register_31": I2C_SDA_HOLD,
        "register_32": I2C_TX_ABRT_SOURCE,
        "register_33": I2C_SLV_DATA_NACK_ONLY,
        "register_34": I2C_DMA_CR,
        "register_35": I2C_DMA_TDLR,
        "register_36": I2C_DMA_RDLR,
        "register_37": I2C_SDA_SETUP,
        "register_38": I2C_ACK_GENERAL_CALL,
        "register_39": I2C_ENABLE_STATUS,
        "register_40": I2C_FS_SPKLEN1,
        "register_41": I2C_HS_SPKLEN,
        "register_42": I2C_CLR_RESTART_DET,
        "register_43": I2C_SCL_STUCK_AT_LOW_TIMEOUT,
        "register_44": I2C_SDA_STUCK_AT_LOW_TIMEOUT,
        "register_45": I2C_SMBUS_CLK_LOW_SEXT,
        "register_46": I2C_SMBUS_CLK_LOW_MEXT,
        "register_47": I2C_SMBUS_THIGH_MAX_IDLE_COUNT,
        "register_48": I2C_SMBUS_INTR_STAT,
        "register_49": I2C_SMBUS_INTR_MASK,
        "register_50": I2C_SMBUS_RAW_INTR_STAT,
        "register_51": I2C_CLR_SMBUS_INTR,
        "register_52": I2C_OPTIONAL_SAR,
        "register_53": I2C_SMBUS_UDID_LSB,
    }
}

i2c2_define = {
    "name": "I2C2",
    "description": "Inter-Integrated Circuit 2",
    "groupName": "I2C",
    "baseAddress": "0x40008C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "I2C2",
        "description": "I2C2 interrupt",
        "value": "25",
    },
    "registers": {
        "register_0 ": I2C_CON_I2C2,
        "register_1 ": I2C_TAR,
        "register_2 ": I2C_SAR,
        "register_3 ": I2C_HS_MADDR,
        "register_4 ": I2C_DATA_CMD,
        "register_5 ": I2C_SS_SCL_HCNT,
        "register_6 ": I2C_SS_SCL_LCNT,
        "register_7 ": I2C_FS_SCL_HCNT,
        "register_8 ": I2C_FS_SCL_LCNT,
        "register_9 ": I2C_HS_SCL_HCNT,
        "register_10": I2C_HS_SCL_LCNT,
        "register_11": I2C_INTR_STAT,
        "register_12": I2C_INTR_MASK,
        "register_13": I2C_RAW_INTR_STAT,
        "register_14": I2C_RX_TL,
        "register_15": I2C_TX_TL,
        "register_16": I2C_CLR_INTR,
        "register_17": I2C_CLR_RX_UNDER,
        "register_18": I2C_CLR_RX_OVER,
        "register_19": I2C_CLR_TX_OVER,
        "register_20": I2C_CLR_RD_REQ,
        "register_21": I2C_CLR_TX_ABRT,
        "register_22": I2C_CLR_RX_DONE,
        "register_23": I2C_CLR_ACTIVITY,
        "register_24": I2C_CLR_STOP_DET,
        "register_25": I2C_CLR_START_DET,
        "register_26": I2C_CLR_GEN_CALL,
        "register_27": I2C_ENABLE,
        "register_28": I2C_STATUS,
        "register_29": I2C_TXFLR,
        "register_30": I2C_RXFLR,
        "register_31": I2C_SDA_HOLD,
        "register_32": I2C_TX_ABRT_SOURCE,
        "register_33": I2C_SLV_DATA_NACK_ONLY,
        "register_34": I2C_DMA_CR,
        "register_35": I2C_DMA_TDLR,
        "register_36": I2C_DMA_RDLR,
        "register_37": I2C_SDA_SETUP,
        "register_38": I2C_ACK_GENERAL_CALL,
        "register_39": I2C_ENABLE_STATUS,
        "register_40": I2C_FS_SPKLEN2,
        "register_41": I2C_HS_SPKLEN,
        "register_42": I2C_CLR_RESTART_DET,
        "register_43": I2C_SCL_STUCK_AT_LOW_TIMEOUT,
        "register_44": I2C_SDA_STUCK_AT_LOW_TIMEOUT,
        "register_45": I2C_SMBUS_CLK_LOW_SEXT,
        "register_46": I2C_SMBUS_CLK_LOW_MEXT,
        "register_47": I2C_SMBUS_THIGH_MAX_IDLE_COUNT,
        "register_48": I2C_SMBUS_INTR_STAT,
        "register_49": I2C_SMBUS_INTR_MASK,
        "register_50": I2C_SMBUS_RAW_INTR_STAT,
        "register_51": I2C_CLR_SMBUS_INTR,
        "register_52": I2C_OPTIONAL_SAR,
        "register_53": I2C_SMBUS_UDID_LSB,
    }
}
