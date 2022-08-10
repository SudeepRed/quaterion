from dataclasses import dataclass
from typing import Optional


@dataclass
class XbmConfig:
    """Determine XBM settings.

    This class should be returned from
    :meth:`~quaterion.train.trainable_model.TrainableModel.configure_xbm`
    """

    embedding_size: int
    """Dimensionality of embeddings outputted by the encoder"""

    weight: Optional[float] = 1.0
    """Value to scale the buffer loss before adding it to the final loss"""

    buffer_size: Optional[int] = 10000
    """Size of the memory buffer that holds embeddings from previous batches"""

    start_iteration: Optional[int] = 1000
    """Iteration sttep to start considering the buffer loss"""
