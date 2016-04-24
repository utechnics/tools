#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Utech'
__version__ = 0.1

import qrcode

class WLAN:

    def __init__(self, ssid, password, device='android', description='', wpa=True, hidden=False):
        self.ssid = ssid
        self.password = password
        self.description = description
        self.wpa = wpa
        self.hidden = hidden
        self.device = device    # android, windows, apple
        # QR code properties
        self.error_correction = qrcode.constants.ERROR_CORRECT_L
        self.box_size = 6
        self.border = 1

    def getConfigString(self):
        from string import lower
        if self.wpa:
            security = 'WPA'
        else:
            security = 'WPS'
        if self.device == 'android':
            config = 'WIFI:T:%s;S:%s;P:%s;H:%s' % (security, self.ssid, self.password, lower(str(self.hidden)))
        elif self.device == 'apple':
            config = 'not available yet'
        elif self.device == 'windows':
            config = 'not available yet'
        else:
            config = 'not valid'
        return config

    def createQR(self):
        import qrcode
        qr = qrcode.QRCode(version=1, error_correction=self.error_correction, box_size=self.box_size, border=self.border)
        qr.add_data(self.getConfigString())
        qr.make(fit=True)
        img = qr.make_image()
        return img

    def saveQR(self, img, filename='qr.png'):
        img.save(filename)


def main():
    wlan = WLAN(ssid='ssid', password='pw')
    qr = wlan.createQR()
    wlan.saveQR(qr, filename='qr.png')

if __name__ == '__main__':
    main()

