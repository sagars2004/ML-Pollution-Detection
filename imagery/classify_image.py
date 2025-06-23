def predict_image_class(image_path):
    import random
    return random.choice(['pollution', 'clean']), round(random.uniform(0.6, 0.99), 2)
