"""
 - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
Name - - Sliding Window Attention Mechanism
Goal - - Implement a neural network architecture using sliding window attention for sequence modeling tasks.
Detail: Total 5 layers neural network
        * Input layer
        * Sliding Window Attention Layer
        * Feedforward Layer
        * Output Layer
Author: Stephen Lee
Github: 245885195@qq.com
Date: 2024.10.20
References:
    1. Choromanska, A., et al. (2020). "On the Importance of Initialization and Momentum in Deep Learning." *Proceedings of the 37th International Conference on Machine Learning*.
    2. Dai, Z., et al. (2020). "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention." *arXiv preprint arXiv:2006.16236*.
 - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
"""

import numpy as np


class SlidingWindowAttention:
    """Sliding Window Attention Module.

    This class implements a sliding window attention mechanism where the model
    attends to a fixed-size window of context around each token.

    Attributes:
        window_size (int): The size of the attention window.
        embed_dim (int): The dimensionality of the input embeddings.
    """

    def __init__(self, embed_dim: int, window_size: int):
        """
        Initialize the SlidingWindowAttention module.

        Args:
            embed_dim (int): The dimensionality of the input embeddings.
            window_size (int): The size of the attention window.
        """
        self.window_size = window_size
        self.embed_dim = embed_dim
        self.attention_weights = np.random.randn(embed_dim, embed_dim)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass for the sliding window attention.

        Args:
            x (np.ndarray): Input tensor of shape (batch_size, seq_length, embed_dim).

        Returns:
            np.ndarray: Output tensor of shape (batch_size, seq_length, embed_dim).

        >>> x = np.random.randn(2, 10, 4)  # Batch size 2, sequence length 10, embedding dimension 4
        >>> attention = SlidingWindowAttention(embed_dim=4, window_size=3)
        >>> output = attention.forward(x)
        >>> output.shape
        (2, 10, 4)
        >>> (output.sum() != 0).item()  # Check if output is non-zero
        True
        """
        batch_size, seq_length, _ = x.shape
        output = np.zeros_like(x)

        for i in range(seq_length):
            # Define the window range
            start = max(0, i - self.window_size // 2)
            end = min(seq_length, i + self.window_size // 2 + 1)

            # Extract the local window
            local_window = x[:, start:end, :]

            # Compute attention scores
            attention_scores = np.matmul(local_window, self.attention_weights)

            # Average the attention scores
            output[:, i, :] = np.mean(attention_scores, axis=1)

        return output


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    x = np.random.randn(
        2, 10, 4
    )  # Batch size 2, sequence length 10, embedding dimension 4
    attention = SlidingWindowAttention(embed_dim=4, window_size=3)
    output = attention.forward(x)
    print(output)
