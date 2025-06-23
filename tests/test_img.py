from imagery.classify_image import predict_image_class

def test_image_classifier_output():
    label, score = predict_image_class("data/test_tile.jpg")
    assert label in ['pollution', 'clean']
    assert 0.0 <= score <= 1.0
