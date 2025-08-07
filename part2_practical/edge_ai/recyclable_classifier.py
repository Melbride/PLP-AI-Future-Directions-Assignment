import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

class RecyclableClassifier:
    def __init__(self):
        self.model = None
        self.tflite_model = None
        self.classes = ['plastic', 'glass', 'metal', 'paper', 'organic']
        
    def create_model(self):
        """Create lightweight CNN for recyclable classification"""
        model = models.Sequential([
            layers.Conv2D(16, (3, 3), activation='relu', input_shape=(96, 96, 3)),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.GlobalAveragePooling2D(),
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(len(self.classes), activation='softmax')
        ])
        
        model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
        self.model = model
        return model
    
    def generate_sample_data(self, samples_per_class=200):
        """Generate synthetic training data for demonstration"""
        X = []
        y = []
        
        for class_idx in range(len(self.classes)):
            for _ in range(samples_per_class):
                # Generate synthetic image data with class-specific patterns
                img = np.random.rand(96, 96, 3)
                if class_idx == 0:  # plastic - add blue tint
                    img[:, :, 2] += 0.3
                elif class_idx == 1:  # glass - add transparency effect
                    img *= 0.8
                elif class_idx == 2:  # metal - add metallic shine
                    img += np.random.normal(0, 0.1, img.shape)
                elif class_idx == 3:  # paper - add texture
                    img[:, :, 0] += 0.2
                else:  # organic - add green tint
                    img[:, :, 1] += 0.3
                
                X.append(np.clip(img, 0, 1))
                y.append(class_idx)
        
        X = np.array(X)
        y = np.array(y)
        
        # Shuffle data
        indices = np.random.permutation(len(X))
        return X[indices], y[indices]
    
    def train_model(self):
        """Train the recyclable classification model"""
        print("Generating training data...")
        X_train, y_train = self.generate_sample_data()
        X_val, y_val = self.generate_sample_data(50)
        
        print("Training model...")
        history = self.model.fit(
            X_train, y_train,
            epochs=10,
            batch_size=32,
            validation_data=(X_val, y_val),
            verbose=1
        )
        
        return history
    
    def convert_to_tflite(self):
        """Convert trained model to TensorFlow Lite format"""
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        self.tflite_model = converter.convert()
        
        # Save TFLite model
        with open('recyclable_classifier.tflite', 'wb') as f:
            f.write(self.tflite_model)
        
        print(f"TFLite model size: {len(self.tflite_model) / 1024:.2f} KB")
        return self.tflite_model
    
    def test_tflite_inference(self, test_samples=10):
        """Test TensorFlow Lite model inference"""
        interpreter = tf.lite.Interpreter(model_content=self.tflite_model)
        interpreter.allocate_tensors()
        
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        # Generate test data
        X_test, y_test = self.generate_sample_data(test_samples)
        
        correct_predictions = 0
        inference_times = []
        
        for i in range(test_samples):
            start_time = tf.timestamp()
            
            # Set input tensor
            interpreter.set_tensor(input_details[0]['index'], 
                                 X_test[i:i+1].astype(np.float32))
            
            # Run inference
            interpreter.invoke()
            
            # Get prediction
            output_data = interpreter.get_tensor(output_details[0]['index'])
            predicted_class = np.argmax(output_data[0])
            
            end_time = tf.timestamp()
            inference_times.append((end_time - start_time).numpy() * 1000)  # ms
            
            if predicted_class == y_test[i]:
                correct_predictions += 1
        
        accuracy = correct_predictions / test_samples
        avg_inference_time = np.mean(inference_times)
        
        print(f"TFLite Model Performance:")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Average inference time: {avg_inference_time:.2f} ms")
        
        return accuracy, avg_inference_time

def main():
    """Main execution function"""
    print("=== Edge AI Recyclable Classifier ===")
    
    # Initialize classifier
    classifier = RecyclableClassifier()
    
    # Create and train model
    model = classifier.create_model()
    print(f"Model parameters: {model.count_params():,}")
    
    # Train the model
    history = classifier.train_model()
    
    # Convert to TensorFlow Lite
    tflite_model = classifier.convert_to_tflite()
    
    # Test TFLite inference
    accuracy, inference_time = classifier.test_tflite_inference()
    
    # Calculate model compression
    original_size = model.count_params() * 4 / 1024  # Approximate KB
    tflite_size = len(tflite_model) / 1024
    compression_ratio = original_size / tflite_size
    
    print(f"\n=== Edge AI Benefits ===")
    print(f"Model compression: {compression_ratio:.1f}x smaller")
    print(f"Inference speed: {inference_time:.2f} ms (suitable for real-time)")
    print(f"Memory footprint: {tflite_size:.2f} KB (edge device compatible)")
    print(f"Accuracy maintained: {accuracy:.2%}")

if __name__ == "__main__":
    main()