from gradio_client import Client
from PIL import Image
client = Client("stabilityai/stable-diffusion-3.5-large")
def generate_image(gender="male"):
    image = client.predict(
        prompt=f"create photo realistic picture of {gender}",
        negative_prompt="",
        seed=0,
        randomize_seed=True,
        width=1024,
        height=1024,
        guidance_scale=4.5,
        num_inference_steps=40,
        api_name="/infer"
    )
    return image

def main():
    user_choice = ""
    while True:
        user_choice = input("Enter 'male' or 'female' to generate a portrait: ")
        if user_choice not in ["male", "female"]:
            print("invalid input")
            continue
        result_image = generate_image(user_choice)
        img_path = list(result_image)[0]
        im = Image.open(img_path)
        im.show()
        break

main()