/*
 *
 * This file is part of pyA20.
 * i2c_lib.c is python I2C extension.
 *
 * Copyright (c) 2014 Stefan Mavrodiev @ OLIMEX LTD, <support@olimex.com>
 *
 * pyA20 is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */


#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/ioctl.h>

#include <linux/i2c.h>
#include <linux/i2c-dev.h>

int i2c_open(char *device, uint8_t address) {
    int fd;
    int ret;

    fd = open(device, O_RDWR);
    if (fd < 0)
        return fd;

    ret = ioctl(fd, I2C_SLAVE_FORCE, address);
    if (ret < 0)
        return ret;

    return fd;

}

int i2c_close(int fd) {
    return (close(fd));
}

int i2c_send(int fd, uint8_t *buffer, uint32_t num_bytes) {
    return (write(fd, buffer, num_bytes));
}

int i2c_read(int fd, uint8_t *buffer, uint32_t num_bytes) {
    return (read(fd, buffer, num_bytes));
}

extern int i2c_send_onestop(int fd, uint8_t dev_addr,  uint8_t *buffer, uint32_t num_bytes)
{
	struct i2c_msg messages[1];
	struct i2c_rdwr_ioctl_data packet;

	messages[0].addr = dev_addr;
	messages[0].flags = 0; // 0:write 1:read
	messages[0].len = num_bytes;
	messages[0].buf = buffer;

	packet.msgs = messages;
	packet.nmsgs = 1;

	if (ioctl(fd, I2C_RDWR, &packet) < 0)
	{
		return 1;
	}
	return 0;
}
