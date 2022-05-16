# RGB LED Matrix Probjects

This project uses the following hardware:
* https://www.adafruit.com/adabox016

This project uses the following software:
* https://www.piskelapp.com/ For creating sprites (PNG)
* https://imagemagick.org/script/convert.php - For converting PNG -> BMP
* publish.sh - For copying projects onto the CircuitPy

# Example Usage

## Create an app

* Download the raw image to `img/raw`
* Go to https://www.piskelapp.com/ and create the sprite
* Export the sprite to PNG and save to `img/png` dir
* Convert the PNG to BMP: `convert img/png/img.png imp/bmp/img.png`
* Create softlink for the project `cd projects/the-project/img; ln -s ../../../img/bmp/img.bmp .`

## Publish an app

`publish projects/the-project`
