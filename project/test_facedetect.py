import facedetect

def test_facedetect():
    assert facedetect.testing(0) == 1
    assert facedetect.testing(1) == 2
    assert facedetect.testing(1) == 3
