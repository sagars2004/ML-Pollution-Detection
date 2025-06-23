from nlp.train_text_model import classify_text

def test_classify_pollution_text():
    sample = "Oil spill detected off the coast of Mumbai."
    label, confidence = classify_text(sample)
    assert label in ['plastic', 'oil spill', 'pollution']
    assert 0.0 <= confidence <= 1.0
