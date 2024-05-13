/**
 ******************************************************************************
 * @file pca9674x.h
 * @brief PCA9674/PCA9674A Library Definiation
 *
 * @dauthor Zhen Wei
 * @date 05/11/2024
 ******************************************************************************
 * @copyright
 * Copyright (c) 2024
 * All rights reserved.
 *
 ******************************************************************************
 */

#ifndef PCA9674X_H__
#define PCA9674X_H__

// Includes
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// Header file body
typedef union 
{
    uint32_t raw;
    struct 
    {
        uint32_t reserved : 8;
        uint32_t revision : 3;
        uint32_t part_id : 9;
        uint32_t manufacturer : 12;
    } device_id;
} pca9674x_device_id_t;

typedef struct
{
    uint8_t addr_7bit;

    uint16_t (*fp_i2c_read)(uint8_t addr_7bit, uint8_t size, uint8_t * buf);
    uint16_t (*fp_i2c_write)(uint8_t addr_7bit, uint8_t size,  const uint8_t * buf);

} __attribute__((__packed__)) pca9674x_ctrl_t;

uint16_t pca9674x_software_reset(const pca9674x_ctrl_t * pca9674x_ctrl);
uint16_t pca9674x_read_device_id(const pca9674x_ctrl_t * pca9674x_ctrl, pca9674x_device_id_t * id);
uint16_t pca9674x_write(const pca9674x_ctrl_t * pca9674x_ctrl, const uint8_t * port_values, uint8_t size);
uint16_t pca9674x_read(const pca9674x_ctrl_t * pca9674x_ctrl, uint8_t * port_values, uint8_t size);

#ifdef __cplusplus
}
#endif

#endif /* PCA9674X_H__ */
