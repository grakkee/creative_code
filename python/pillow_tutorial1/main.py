import random
import uuid

from PIL import Image, ImageDraw
from Studio import Studio

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

studio = Studio(run_id)
studio.drawRandomLine()
studio.save()



# rectangle_width = 100
# rectangle_height = 100

# number_of_squares = random.randint(10, 550)

# draw_image = ImageDraw.Draw(image)
# for i in range(number_of_squares):
#     rectangle_x = random.randint(0, width)
#     rectangle_y = random.randint(0, height)

#     rectangle_shape = [
#         (rectangle_x, rectangle_y),
#         (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
#     draw_image.rectangle(
#         rectangle_shape,
#         fill=(
#             random.randint(0, 255),
#             random.randint(0, 255),
#             random.randint(0, 255)
#         )
#     )