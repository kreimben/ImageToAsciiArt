from ascii import get_gray_image_from_s3, convert_to_ascii


def lambda_handler(event, context):
    image = event['Records'][0]['s3']['object']['key']
    image_object = get_gray_image_from_s3(image)
    ascii_art = convert_to_ascii(image_object)
    return {
        'result': ascii_art
    }
