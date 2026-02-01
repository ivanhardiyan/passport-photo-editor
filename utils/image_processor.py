def crop_image(image, crop_area):
    """Crops the image to the specified area.

    Args:
        image: The image to be cropped.
        crop_area: A tuple (left, top, right, bottom) specifying the cropping area.

    Returns:
        Cropped image.
    """
    return image.crop(crop_area)


def resize_image(image, size):
    """Resizes the image to the specified size.

    Args:
        image: The image to be resized.
        size: A tuple (width, height) specifying the new size.

    Returns:
        Resized image.
    """
    return image.resize(size)


def apply_filter(image, filter_type):
    """Applies a filter to the image.

    Args:
        image: The image to be filtered.
        filter_type: The type of filter to apply (e.g., "grayscale", "sepia").

    Returns:
        Filtered image.
    """
    if filter_type == "grayscale":
        return image.convert('L')
    elif filter_type == "sepia":
        # Placeholder for sepia filter logic
        pass
    return image
