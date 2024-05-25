from PIL import Image

def xor_images(image1_path, image2_path, output_path):
  # Open encoded & key images
  flag = Image.open('flag.png').convert('RGB')
  lemur = Image.open('lemur.png').convert('RGB')

  width, height = flag.size

  result_img = Image.new('RGB', (width, height))

  for x in range(width):
    for y in range(height):
      r1, g1, b1 = flag.getpixel((x, y))
      r2, g2, b2 = lemur.getpixel((x, y))
      r = r1 ^ r2
      g = g1 ^ g2
      b = b1 ^ b2
      result_img.putpixel((x, y), (r, g, b))

  # Save or display the result image
  result_img.save(output_path)
  result_img.show()

# operation      
xor_images('flag', 'lemur', 'output.png')