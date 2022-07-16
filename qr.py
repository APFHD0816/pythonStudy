import qrcode

qr_data = 'http://ww.youtube.com'
qr_img = qrcode.make(qr_data)

save_path = 'myar.png'
qr_img.save(save_path)