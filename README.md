# Hand-written-digit-recognition
Handwritte

This project demonstrates handwritten digit recognition using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The model can accurately identify digits from 0 to 9 in 28x28 grayscale images.

Overview
Handwritten digit recognition is a classic problem in machine learning. The MNIST dataset provides 70,000 labeled images (60,000 for training and 10,000 for testing). This project uses a CNN to learn the features of handwritten digits and classify them effectively.

Let it be done

Trains a CNN on the MNIST dataset

Achieves around 98% accuracy on test data

Includes a prediction script for new images

Optional interface for drawing and predicting digits

Beginner-friendly and easy to understand

Model Architecture

Input: 28x28 grayscale image

Conv2D → ReLU → MaxPooling

With

Flatten

Dense → ReLU

Output Layer: Softmax (10 classes)

Project Structure

model/: Saved CNN model

samples/: Example digit images

train.py: Training script

predict.py: Script to test predictions

app.py: Option

requirements.txt: Python dependencies

README.md

Installation

Clone

Install dependencies using pip install -r requirements.txt

Training the Model
Run 'puddlepython train.py to train the model. This will save the trained model in the model/ directory.

Making Predictions
Use python predict.py --image samples/5.pngthat before

Optional
Run python app.py to launch a UI where you can draw a digit and get predictions in real-time.

Accurate

Training Accuracy: ~99%

Hand

Dataset
MNIST Dataset: A publicly available dataset of handwritten digits created by Yann LeCun.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome. Fork the repository and submit pull requests.
