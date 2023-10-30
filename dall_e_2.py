import openai

def dalle(flower):
    Prompt = "Make a neat image of a bouquet for a flower shop made of %s" % (flower)

    response = openai.Image.create(
        prompt=Prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )

    image_url = response["data"][0]["url"]
    return(image_url)