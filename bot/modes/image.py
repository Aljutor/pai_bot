import os
import cv2
import openface

from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier


dir_path = os.path.dirname(os.path.realpath(__file__))

model_dir = os.path.join(dir_path, 'models')
faces_dir = os.path.join(dir_path, 'faces')

dlib_face_predictor = os.path.join(model_dir, 'shape_predictor_68_face_landmarks.dat')
network_model       = os.path.join(model_dir, 'nn4.small2.v1.t7')

img_dim = 96

align = openface.AlignDlib(dlib_face_predictor)
net   = openface.TorchNeuralNet(network_model, img_dim)

def face_rep(rgb_img):
    bb = align.getLargestFaceBoundingBox(rgb_img)
    alignedFace = align.align(img_dim, rgb_img, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    return net.forward(alignedFace)


def read_path(img_path):
    bgr_img = cv2.imread(str(img_path))
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img


def load_data():
    images = []
    labels = []

    for path in Path(faces_dir).glob("*.jpg"):
        label = path.name.lower().split('-')[0]
        images.append(path)
        labels.append(label)

    X = [face_rep(read_path(img)) for img in images]
    Y = labels

    return X, Y


def gen_model():
    X, Y = load_data()
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X, Y)

    return clf


def predict(rgb_img, clf):
    rep = [face_rep(rgb_img)]
    return sorted(list(zip(clf.classes_, clf.predict_proba(rep)[0])), key=lambda tup: tup[1], reverse=True)[:5]

