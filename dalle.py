import base64
from PIL import Image
import requests
import json
import io

def get_concat_h():
    images = [Image.open(x) for x in ['0.png', '1.png', '2.png', '3.png']]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save('result.jpg')
    
def getImgFromPrompt (num, prmpt):
    url = "http://127.0.0.1:8080/dalle"
    num_imgs = num
    prompt = prmpt
    reqJson = {"text" : prompt, "num_images" : num_imgs }

    req = json.dumps(reqJson)

    print(req)

    res = requests.post(url, data=req)

    images = res.json()

    for x in range(len(images)):
        imgData = base64.b64decode(images[x])
        buf = io.BytesIO(imgData)
        img = Image.open(buf)
        # img.show()
        img.save("{}.png".format(x), format="png")

def discordEntry(num, prmpt):
    getImgFromPrompt(num, prmpt)
    get_concat_h()