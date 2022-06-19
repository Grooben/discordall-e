from PIL import Image
from PIL import ImageFont, ImageDraw

from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster


class BrotherQLPrinter:

    def __init__(self):
        pass;

    def resize_dalle_image_with_text(self, path, text, subtitle="", font="comic.ttf", textMargin=200):

        # Open the saved image
        oldIm = Image.open(path)

        # Resize canvas for correct margin below (for text)
        im = Image.new(oldIm.mode, (1024, 256 + textMargin));
        im.paste((255, 255, 255), [0, 0, 1024, 256 + textMargin]);
        im.paste(oldIm, (0, 0, 1024, 256));

        # Draw text underneath
        draw = ImageDraw.Draw(im);
        font1 = ImageFont.truetype(font, 48);
        text = text
        text = f'"{text}"';

        # Find draw location, draw the text
        pos = (1024 / 2, 256 + (textMargin/2) + 20);
        draw.text(pos, text, font=font1, anchor="mm", fill=(0,0,0))

        # Draw text above
        font2 = ImageFont.truetype(font, 40);
        text = f'{subtitle}';
        pos = (1024 / 2, 256 + (textMargin/2) - 60);
        draw.text(pos, text, font=font2, anchor="mm", fill=(0,0,0))

        # And return altered image
        return im;



    def printLabel(self, image, backend="pyusb", model="QL-570", printer="usb://0x04f9:0x2028"):

        # Make a brother ql raster file
        qlr = BrotherQLRaster(model)
        qlr.exception_on_warning = True

        # Build instructions
        instructions = convert(

                qlr=qlr, 
                images=[image],    #  Takes a list of file names or PIL objects.
                label='62', 
                rotate='0',    # 'Auto', '0', '90', '270'
                threshold=80.0,    # Black and white threshold in percent.
                dither=True, 
                compress=False, 
                red=False,    # Only True if using Red/Black 62 mm label tape.
                dpi_600=False, 
                hq=True,    # False for low quality.
                cut=True

        )

        # And send them
        send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)