import matplotlib.pyplot as plt
import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.models import Model
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import numpy as np

datasets = tf.keras.utils.image_dataset_from_directory("datasets", image_size=(360, 640), batch_size=500, shuffle=False)
for image_batch, labels_batch in datasets:
    images = image_batch
    labels = labels_batch
    break
images = images.numpy().astype(np.uint8)

target_size = 224
num_clusters = 50

data_preprocessing = tf.keras.Sequential(
    [
        tf.keras.layers.Resizing(target_size, target_size),
        tf.keras.layers.Normalization(),
    ]
)
data_preprocessing.layers[-1].adapt(images)
images = data_preprocessing(images)

# load model
model = VGG16()
# remove the output layer
model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
features = model.predict(images)

pca = PCA(n_components=100, random_state=22)
pca.fit(features)
x_pca = pca.transform(features)

tsne = TSNE(n_components=2)
x_tsne = tsne.fit_transform(features)

kmeans = KMeans(n_clusters=20, random_state=22)
kmeans.fit(x_tsne)

fig = plt.figure(figsize=(12,  8))
#ax = fig.add_subplot(projection='3d')
plt.scatter(x_tsne[:,0], x_tsne[:,1], c=kmeans.labels_)
plt.show()
