from BrotherQL import BrotherQLPrinter


printer = BrotherQLPrinter();

image = printer.resize_dalle_image_with_text("test.png", "hello there");
printer.printLabel(image);