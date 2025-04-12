import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import cv2
import numpy as np
from generator import Generator

img_dim=512
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gen = Generator(img_channels = 3, features = 64).to(device)
gen.load_state_dict(torch.load(r"kaggle/working/checkpoints/generator.pth", map_location=device))
gen.eval()

transform = transforms.Compose([
            transforms.Resize((img_dim, img_dim)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
input_img= Image.open(r"kaggle/working/eval/image.jpg").convert("RGB")
img_tensor = transform(input_img).unsqueeze(0).to(device)
with torch.no_grad():
    output_tensor = gen(img_tensor)

output_tensor = (output_tensor * 0.5 + 0.5) * 255
output_image = output_tensor.squeeze().permute(1, 2, 0).cpu().numpy().astype("uint8")

output_pil = Image.fromarray(output_image)
cv_input = np.array(output_pil)
cv_input = cv2.cvtColor(cv_input, cv2.COLOR_RGB2BGR)
sharpening_kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
avg_kernel = np.array([[0.2, 0.5, 0.2],
                      [0.5, 1, 0.5],
                      [0.2, 0.5, 0.2]])
temp1 = cv2.filter2D(cv_input, -1, sharpening_kernel)
temp2 = cv2.GaussianBlur(temp1, (3,3), 0)
#temp3 = cv2.convertScaleAbs(temp2, 1, 0)
cv2.imwrite(r"kaggle/working/eval/image_cartoon.jpg", temp2)
