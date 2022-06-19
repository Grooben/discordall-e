from BrotherQL import BrotherQLPrinter


printer = BrotherQLPrinter();

image = printer.resize_dalle_image_with_text("test.png", "hello there", "ben#8853");
image.show();
# printer.printLabel(image);