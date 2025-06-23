def classify_text(text):
    if "oil" in text.lower():
        return "oil spill", 0.95
    return "pollution", 0.70
