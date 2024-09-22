import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def create_3d_matrix(shape):
    """Create a 3D matrix with varying values."""
    return np.random.rand(*shape)

def visualize_3d_matrix(matrix):
    """Visualize a 3D matrix."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Get matrix dimensions
    z, y, x = matrix.shape

    # Create coordinate matrices
    X, Y, Z = np.meshgrid(range(x), range(y), range(z))

    # Flatten the matrices
    X, Y, Z = X.flatten(), Y.flatten(), Z.flatten()
    values = matrix.flatten()

    # Create 3D scatter plot
    scatter = ax.scatter(X, Y, Z, c=values, cmap='viridis', s=100*values)

    # Set labels and title
    ax.set_xlabel('X axis (Columns)')
    ax.set_ylabel('Y axis (Rows)')
    ax.set_zlabel('Z axis (Depth)')
    ax.set_title(f'3D Visualization of a {z}x{y}x{x} Matrix')

    # Set axis limits
    ax.set_xlim(0, x-1)
    ax.set_ylim(0, y-1)
    ax.set_zlim(0, z-1)

    # Add a color bar
    cbar = fig.colorbar(scatter)
    cbar.set_label('Value')

    # Add gridlines
    ax.grid(True)

    plt.tight_layout()
    plt.show()


def load_dataset_to_numpy(csv_file_path):
    """
    Load the image dataset from a CSV file into numpy arrays.
    
    Args:
    csv_file_path (str): Path to the CSV file containing the image dataset.
    
    Returns:
    tuple: (X, y) where X is a numpy array of image data and y is a numpy array of encoded labels.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Separate features and labels
    X = df.drop('label', axis=1).values
    y = df['label'].values
    
    # Reshape the image data
    img_size = int(np.sqrt(X.shape[1] / 3))  # Assuming square RGB images
    X = X.reshape(-1, img_size, img_size, 3)
    
    # Normalize pixel values
    X = X.astype('float32') / 255.0
    
    # Encode labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    
    return X, y
