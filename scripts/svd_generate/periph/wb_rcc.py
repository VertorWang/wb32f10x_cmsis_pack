RCC_PLLPRE = {
    "name": "PLLPRE",
    "displayName": "PLLPRE",
    "description": "PLL pre-divider control register",
    "addressOffset": "0x00",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "PLL pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "PLL ratio",
            "bitRange": "[4:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "PLL pre-divider input clock enable",
            "bitRange": "[5:5]",
        }
    }
}

RCC_PLLSRC = {
    "name": "PLLSRC",
    "displayName": "PLLSRC",
    "description": "PLL clock source selection register",
    "addressOffset": "0x04",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRC",
            "description": "PLL clock source selection",
            "bitRange": "[0:0]",
        }
    }
}

RCC_MAINCLKSRC = {
    "name": "MAINCLKSRC",
    "displayName": "MAINCLKSRC",
    "description": "System clock source selection register",
    "addressOffset": "0x08",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRC",
            "description": "main clock source selection",
            "bitRange": "[1:0]",
        }
    }
}

RCC_MAINCLKUEN = {
    "name": "MAINCLKUEN",
    "displayName": "MAINCLKUEN",
    "description": "System clock source update enable register",
    "addressOffset": "0x0C",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "ENA",
            "description": "update main clock source",
            "bitRange": "[0:0]",
        }
    }
}

RCC_USBPRE = {
    "name": "USBPRE",
    "displayName": "USBPRE",
    "description": "USB clock pre-divider control register",
    "addressOffset": "0x014",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "USB in clock pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "USB ratio",
            "bitRange": "[2:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "USB pre-divider input clock enable",
            "bitRange": "[3:3]",
        }
    }
}

RCC_AHBPRE = {
    "name": "AHBPRE",
    "displayName": "AHBPRE",
    "description": "AHB clock pre-divider register",
    "addressOffset": "0x018",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "AHB pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "AHB ratio",
            "bitRange": "[6:1]",
        }
    }
}

RCC_APB1PRE = {
    "name": "APB1PRE",
    "displayName": "APB1PRE",
    "description": "APB1 clock pre-divider control register",
    "addressOffset": "0x01C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "APB1 pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "APB1 ratioo",
            "bitRange": "[6:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "APB1 pre-divider input clock enable",
            "bitRange": "[7:7]",
        },
    }
}

RCC_APB2PRE = {
    "name": "APB2PRE",
    "displayName": "APB2PRE",
    "description": "APB2 clock pre-divider control register",
    "addressOffset": "0x020",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "APB2 pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "APB2 ratio",
            "bitRange": "[6:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "APB2 pre-divider input clock enable",
            "bitRange": "[7:7]",
        },
    }
}

RCC_MCLKPRE = {
    "name": "MCLKPRE",
    "displayName": "MCLKPRE",
    "description": "I2S MCLK clock pre-divider control register",
    "addressOffset": "0x024",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "I2S MCLK pre-divider enable (Divider enable)",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "I2S clock ratio",
            "bitRange": "[6:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "I2S MCLK pre-divider input clock enable",
            "bitRange": "[7:7]",
        },
    }
}

RCC_I2SPRE = {
    "name": "I2SPRE",
    "displayName": "I2SPRE",
    "description": "I2S SCLK clock pre-divider control register",
    "addressOffset": "0x028",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "I2S SCLK pre-divider enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "RATIO",
            "description": "I2S sclk ratio",
            "bitRange": "[9:1]",
        },
        "field_2": {
            "name": "SRCEN",
            "description": "I2S SCLK pre-divider input clock enable",
            "bitRange": "[10:10]",
        },
    }
}

RCC_MCLKSRC = {
    "name": "MCLKSRC",
    "displayName": "MCLKSRC",
    "description": "I2S MCLK clock source selection register",
    "addressOffset": "0x02C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRC",
            "description": "I2S MCLK clock source selection",
            "bitRange": "[0:0]",
        }
    }
}

RCC_USBFIFOCLKSRC = {
    "name": "USBFIFOCLKSRC",
    "displayName": "USBFIFOCLKSRC",
    "description": "USB FIFO clock source selection register",
    "addressOffset": "0x034",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SRC",
            "description": "USB FIFO clock source selection",
            "bitRange": "[0:0]",
        }
    }
}

RCC_MCOSEL = {
    "name": "MCOSEL",
    "displayName": "MCOSEL",
    "description": "Clock output selection register",
    "addressOffset": "0x038",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "AHBCLK",
            "description": "AHB clock output to MCO pin",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "HSE",
            "description": "HSE clock output to MCO pin",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "MHSI",
            "description": "MHSI(8MHz) output to MCO pin",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "PLLDIV2",
            "description": "PLL clock divided by 2 output to MCO pin",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "MCLK",
            "description": "I2S MCLK output to MCO pin",
            "bitRange": "[4:4]",
        }
    }
}

RCC_AHBENR0 = {
    "name": "AHBENR0",
    "displayName": "AHBENR0",
    "description": "AHB peripherals clock enable register0",
    "addressOffset": "0x03C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000007B",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IWDGEN",
            "description": "IWDG clock enable control",
            "bitRange": "[2:2]",
        }
    }
}

RCC_AHBENR1 = {
    "name": "AHBENR1",
    "displayName": "AHBENR1",
    "description": "AHB peripherals clock enable register1",
    "addressOffset": "0x040",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000003D",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "USBEN",
            "description": "USB control clock enable",
            "bitRange": "[1:1]",
        },
        "field_1": {
            "name": "ISOEN",
            "description": "ISO7816 control clock enable",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "FLASHEN",
            "description": "FLASH control clock enable",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "CACHEEN",
            "description": "CACHE control clock enable",
            "bitRange": "[4:4]",
        },
        "field_4": {
            "name": "SYSEN",
            "description": "SYS control clock enable",
            "bitRange": "[5:5]",
        },
        "field_5": {
            "name": "DMAC1BREN",
            "description": "DMAC1-APB1 bridge clock enable",
            "bitRange": "[6:6]",
        },
        "field_6": {
            "name": "DMAC2BREN",
            "description": "DMAC2-APB2 bridge clock enable",
            "bitRange": "[7:7]",
        },
        "field_7": {
            "name": "CRCSFMEN",
            "description": "CRC and SFM clock enable",
            "bitRange": "[8:8]",
        }
    }
}

RCC_AHBENR2 = {
    "name": "AHBENR2",
    "displayName": "AHBENR2",
    "description": "AHB peripherals clock enable register2",
    "addressOffset": "0X044",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000003",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BDIEN",
            "description": "Battery domain interface clock enable",
            "bitRange": "[2:2]",
        }
    }
}

RCC_APB1ENR = {
    "name": "APB1ENR",
    "displayName": "APB1ENR",
    "description": "APB1 peripherals clock enable register",
    "addressOffset": "0x048",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000D",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMAC1EN",
            "description": "DMAC1 control clock enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TIM1EN",
            "description": "TIMER1 control clock enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TIM2EN",
            "description": "TIMER2 control clock enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TIM3EN",
            "description": "TIMER3 control clock enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "TIM4EN",
            "description": "TIMER4 control clock enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "GPIOAEN",
            "description": "GPIOA control clock enable",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "GPIOBEN",
            "description": "GPIOB control clock enable",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "GPIOCEN",
            "description": "GPIOC control clock enable",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "GPIODEN",
            "description": "GPIOD control clock enable",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "EXTIEN",
            "description": "EXTI control clock enable",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "AFIOEN",
            "description": "AFIO control clock enable",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "ADCEN",
            "description": "ADC control clock enable",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "QSPIEN",
            "description": "QSPI control clock enable",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "SPIS1EN",
            "description": "SPIS1 control clock enable",
            "bitRange": "[13:13]",
        },
        "field_14": {
            "name": "UART1EN",
            "description": "UART1 control clock enable",
            "bitRange": "[14:14]",
        },
        "field_15": {
            "name": "BMX1EN",
            "description": "APB1 bus matrix clock enable",
            "bitRange": "[15:15]",
        }
    }
}

RCC_APB2ENR = {
    "name": "APB2ENR",
    "displayName": "APB2ENR",
    "description": "APB2 peripherals clock enable register",
    "addressOffset": "0x04C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000D",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMAC2EN",
            "description": "DMAC2 control clock enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "WWDGEN",
            "description": "WWDG clock enable",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "UART2EN",
            "description": "UART2 control clock enable",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "UART3EN",
            "description": "UART3 control clock enable",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SPIM2EN",
            "description": "SPIM2 control clock enable",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "SPIS2EN",
            "description": "SPIS2 control clock enable",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "I2SEN",
            "description": "I2S control clock enable",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "I2C1EN",
            "description": "I2C1 control clock enable",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "I2C2EN",
            "description": "I2C2 control clock enable",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "RNGEN",
            "description": "RNG control clock enable",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "LEDEN",
            "description": "LED control clock enable",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "BMX2EN",
            "description": "APB2 bus matrix clock enable",
            "bitRange": "[11:11]",
        }
    }
}

RCC_RNGCLKENR = {
    "name": "RNGCLKENR",
    "displayName": "RNGCLKENR",
    "description": "RNG clock enable register",
    "addressOffset": "0x05C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "RNG clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_IWDGCLKENR = {
    "name": "IWDGCLKENR",
    "displayName": "IWDGCLKENR",
    "description": "IWDG clock enable register",
    "addressOffset": "0x064",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000001",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "IWDGCLKEN",
            "description": "IWDG clock enable",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "DCSSCLKEN",
            "description": "DCSS clock enable",
            "bitRange": "[2:2]",
        }
    }
}

RCC_USBCLKENR = {
    "name": "USBCLKENR",
    "displayName": "USBCLKENR",
    "description": "USB48MHz clock enable register",
    "addressOffset": "0x06C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "USB 48MHz clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_I2SCLKENR = {
    "name": "I2SCLKENR",
    "displayName": "I2SCLKENR",
    "description": "I2S SCLK clock enable register",
    "addressOffset": "0x070",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "I2S SCLK clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_SPIS1CLKENR = {
    "name": "SPIS1CLKENR",
    "displayName": "SPIS1CLKENR",
    "description": "SPIS1 clock enable register",
    "addressOffset": "0x074",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "SPIS1 clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_SPIS2CLKENR = {
    "name": "SPIS2CLKENR",
    "displayName": "SPIS2CLKENR",
    "description": "SPIS2 clock enable register",
    "addressOffset": "0x078",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "SPIS2 clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_USBFIFOCLKENR = {
    "name": "USBFIFOCLKENR",
    "displayName": "USBFIFOCLKENR",
    "description": "USB FIFO clock enable register",
    "addressOffset": "0x07C",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "USB FIFO clock enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_AHBRSTR1 = {
    "name": "AHBRSTR1",
    "displayName": "AHBRSTR1",
    "description": "AHB peripheral reset register1",
    "addressOffset": "0x088",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "USBRST",
            "description": "USB reset control",
            "bitRange": "[1:1]",
        },
        "field_1": {
            "name": "ISORST",
            "description": "ISO7816 reset control",
            "bitRange": "[2:2]",
        },
        "field_2": {
            "name": "FLASHRST",
            "description": "FLASH reset control",
            "bitRange": "[3:3]",
        },
        "field_3": {
            "name": "CACHERST",
            "description": "CACHE reset control",
            "bitRange": "[4:4]",
        },
        "field_4": {
            "name": "SYSRST",
            "description": "SYS reset control",
            "bitRange": "[5:5]",
        },
        "field_5": {
            "name": "CRCSFMRST",
            "description": "CRC and SFM reset control",
            "bitRange": "[8:8]",
        }
    }
}

RCC_APB1RSTR = {
    "name": "APB1RSTR",
    "displayName": "APB1RSTR",
    "description": "APB1 peripheral reset register",
    "addressOffset": "0x090",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000D",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMAC1RST",
            "description": "DMAC1 reset control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "TIM1RST",
            "description": "TIMER1 reset control",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "TIM2RST",
            "description": "TIMER2 reset control",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "TIM3RST",
            "description": "TIMER3 reset control",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "TIM4RST",
            "description": "TIMER4 reset control",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "GPIOARST",
            "description": "GPIOA reset control",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "GPIOBRST",
            "description": "GPIOB reset control",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "GPIOCRST",
            "description": "GPIOC reset control",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "GPIODRST",
            "description": "GPIOD reset control",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "EXTIRST",
            "description": "EXTI reset control",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "AFIORST",
            "description": "AFIO reset control",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "ADCRST",
            "description": "ADC reset control",
            "bitRange": "[11:11]",
        },
        "field_12": {
            "name": "QSPIRST",
            "description": "QSPI reset control",
            "bitRange": "[12:12]",
        },
        "field_13": {
            "name": "SPIS1RST",
            "description": "SPIS1 reset control",
            "bitRange": "[13:13]",
        },
        "field_14": {
            "name": "UART1RST",
            "description": "UART1 reset control",
            "bitRange": "[14:14]",
        },
        "field_15": {
            "name": "BMX1RST",
            "description": "APB1 bus matrix reset control",
            "bitRange": "[15:15]",
        }
    }
}

RCC_APB2RSTR = {
    "name": "APB2RSTR",
    "displayName": "APB2RSTR",
    "description": "APB2 peripheral reset register",
    "addressOffset": "0x094",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x0000000D",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DMAC2RST",
            "description": "DMAC2 reset control",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "WWDGRST",
            "description": "WWDG reset control",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "UART2RST",
            "description": "UART2 reset control",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "UART3RST",
            "description": "UART3 reset control",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "SPIM2RST",
            "description": "SPIM2 reset control",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "SPIS2RST",
            "description": "SPIS2 reset control",
            "bitRange": "[5:5]",
        },
        "field_6": {
            "name": "I2SRST",
            "description": "I2S reset control",
            "bitRange": "[6:6]",
        },
        "field_7": {
            "name": "I2C1RST",
            "description": "I2C1 reset control",
            "bitRange": "[7:7]",
        },
        "field_8": {
            "name": "I2C2RST",
            "description": "I2C2 reset control",
            "bitRange": "[8:8]",
        },
        "field_9": {
            "name": "RNGRST",
            "description": "RNG reset control",
            "bitRange": "[9:9]",
        },
        "field_10": {
            "name": "LEDRST",
            "description": "LED reset control",
            "bitRange": "[10:10]",
        },
        "field_11": {
            "name": "BMX2RST",
            "description": "APB2 bus matrix reset",
            "bitRange": "[11:11]",
        }
    }
}

RCC_I2SCLKRSTR = {
    "name": "I2SCLKRSTR",
    "displayName": "I2SCLKRSTR",
    "description": "I2S SCLK reset register",
    "addressOffset": "0x0B8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "SCLKRST",
            "description": "I2S SCLK clock domain reset",
            "bitRange": "[0:0]",
        }
    }
}

RCC_CLRRSTSTAT = {
    "name": "CLRRSTSTAT",
    "displayName": "CLRRSTSTAT",
    "description": "Reset flag clear register",
    "addressOffset": "0x0C8",
    "size": "0x20",
    "access": "write-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLR",
            "description": "clear RCC_RSTSTAT register",
            "bitRange": "[0:0]",
        }
    }
}

RCC_BDRSTR = {
    "name": "BDRSTR",
    "displayName": "BDRSTR",
    "description": "Battery domain reset register",
    "addressOffset": "0x0D4",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "BDRST",
            "description": "battery domain reset",
            "bitRange": "[0:0]",
        }
    }
}

RCC_LSI2RTCENR = {
    "name": "LSI2RTCENR",
    "displayName": "LSI2RTCENR",
    "description": "LSI battery domain clock enable register",
    "addressOffset": "0x0D8",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "CLKEN",
            "description": "LSI enable for battery domain",
            "bitRange": "[0:0]",
        }
    }
}

RCC_HSE2RTCENR = {
    "name": "HSE2RTCENR",
    "displayName": "HSE2RTCENR",
    "description": "HSE clock 128-divider enable register",
    "addressOffset": "0x0DC",
    "size": "0x20",
    "access": "read-write",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "DIVEN",
            "description": "128-divider enable",
            "bitRange": "[0:0]",
        }
    }
}

RCC_RSTSTAT = {
    "name": "RSTSTAT",
    "displayName": "RSTSTAT",
    "description": "Reset flag register",
    "addressOffset": "0x100",
    "size": "0x20",
    "access": "read-only",
    "resetValue": "0x00000000",
    "resetMask": "0xFFFFFFFF",
    "fields": {
        "field_0": {
            "name": "LPWRRSTF",
            "description": "Set by hardware when low-power reset occurs",
            "bitRange": "[0:0]",
        },
        "field_1": {
            "name": "WWDGRSTF",
            "description": "Set by hardware when WWDG reset occurs",
            "bitRange": "[1:1]",
        },
        "field_2": {
            "name": "IWDGRSTF",
            "description": "set by hardware when IWDG reset occurs in VDD domain",
            "bitRange": "[2:2]",
        },
        "field_3": {
            "name": "SFTRSTF",
            "description": "Set by hardware when software reset occurs",
            "bitRange": "[3:3]",
        },
        "field_4": {
            "name": "PORRSTF",
            "description": "set by hardware when POR/PDR reset occurs",
            "bitRange": "[4:4]",
        },
        "field_5": {
            "name": "PINRSTF",
            "description": "set by hardware when NRST pin reset occurs",
            "bitRange": "[5:5]",
        },
    }
}


rcc_define = {
    "name": "RCC",
    "description": "Reset and Clock Control",
    "groupName": "RCC",
    "baseAddress": "0x40010C00",
    "addressBlock": {
        "offset": "0x0",
        "size": "0x400",
        "usage": "registers",
    },
    "interrupt_0": {
        "name": "RCC",
        "description": "RCC interrupt",
        "value": "5",
    },
    "registers": {
        "register_0 ": RCC_PLLPRE,
        "register_1 ": RCC_PLLSRC,
        "register_2 ": RCC_MAINCLKSRC,
        "register_3 ": RCC_MAINCLKUEN,
        "register_4 ": RCC_USBPRE,
        "register_5 ": RCC_AHBPRE,
        "register_6 ": RCC_APB1PRE,
        "register_7 ": RCC_APB2PRE,
        "register_8 ": RCC_MCLKPRE,
        "register_9 ": RCC_I2SPRE,
        "register_10": RCC_MCLKSRC,
        "register_11": RCC_USBFIFOCLKSRC,
        "register_12": RCC_MCOSEL,
        "register_13": RCC_AHBENR0,
        "register_14": RCC_AHBENR1,
        "register_15": RCC_AHBENR2,
        "register_16": RCC_APB1ENR,
        "register_17": RCC_APB2ENR,
        "register_18": RCC_RNGCLKENR,
        "register_19": RCC_IWDGCLKENR,
        "register_20": RCC_USBCLKENR,
        "register_21": RCC_I2SCLKENR,
        "register_22": RCC_SPIS1CLKENR,
        "register_23": RCC_SPIS2CLKENR,
        "register_24": RCC_USBFIFOCLKENR,
        "register_25": RCC_AHBRSTR1,
        "register_26": RCC_APB1RSTR,
        "register_27": RCC_APB2RSTR,
        "register_28": RCC_I2SCLKRSTR,
        "register_29": RCC_CLRRSTSTAT,
        "register_30": RCC_BDRSTR,
        "register_31": RCC_LSI2RTCENR,
        "register_32": RCC_HSE2RTCENR,
        "register_33": RCC_RSTSTAT,
    }
}
