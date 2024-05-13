/**
 ******************************************************************************
 * @file pca9674x.c
 * @brief Functions for PCA9674/PCA9674A Library
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

#include <stdio.h>
#include "pca9674x.h"

#define PCA9674X_GENERAL_CALL_ADDR_7BIT     ((uint8_t)0x00)
#define PCA9674X_DEVICE_ID_ADDR_7BIT        ((uint8_t)0x7C)

#define PCA9674X_SWRST_DATA                 ((uint8_t)0x06)

uint16_t pca9674x_software_reset (const pca9674x_ctrl_t * pca9674x_ctrl)
{
    uint16_t err_code = 0;
    const uint8_t software_reset_data_size = ((uint8_t)1);
    uint8_t software_reset_data_buf[software_reset_data_size] = { PCA9674X_SWRST_DATA };

    err_code = pca9674x_ctrl->fp_i2c_write(PCA9674X_GENERAL_CALL_ADDR_7BIT, software_reset_data_size, software_reset_data_buf);

    return err_code;
}

uint16_t pca9674x_read_device_id (const pca9674x_ctrl_t * pca9674x_ctrl, pca9674x_device_id_t * id)
{
    uint16_t err_code = 0;
    const uint8_t slave_addr_write_size = ((uint8_t)1);
    const uint8_t device_id_read_size = ((uint8_t)3);
    uint8_t write_buf[slave_addr_write_size] = { pca9674x_ctrl->addr_7bit << 1 };
    uint8_t read_buf[device_id_read_size];

    err_code = pca9674x_ctrl->fp_i2c_write(PCA9674X_DEVICE_ID_ADDR_7BIT, slave_addr_write_size, write_buf);
    err_code = pca9674x_ctrl->fp_i2c_read(PCA9674X_DEVICE_ID_ADDR_7BIT, device_id_read_size, read_buf);

    id->raw = 0;
    for (uint8_t i = 0; i < device_id_read_size; i++)
    {
        id->raw += read_buf[i];
        id->raw <<= 8;
    }

    return err_code;
}

uint16_t pca9674x_write (const pca9674x_ctrl_t * pca9674x_ctrl, const uint8_t * port_values, uint8_t size)
{
    uint16_t err_code = 0;

    err_code = pca9674x_ctrl->fp_i2c_write(pca9674x_ctrl->addr_7bit, size, port_values);

    return err_code;
}

uint16_t pca9674x_read (const pca9674x_ctrl_t * pca9674x_ctrl, uint8_t * port_values, uint8_t size)
{
    uint16_t err_code = 0;

    err_code = pca9674x_ctrl->fp_i2c_read(pca9674x_ctrl->addr_7bit, size, port_values);

    return err_code;
}