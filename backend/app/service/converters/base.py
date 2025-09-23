from abc import ABC, abstractmethod
import os
import uuid

class DocumentToImage(ABC):
    @abstractmethod
    def convert(self, filepath: str) -> str:
        pass

    def _prepare_output_folder(self, filepath: str, base_output_dir: str = "output") -> str:
        """Create folder named after the document + unique ID"""
        doc_name = os.path.splitext(os.path.basename(filepath))[0]
        unique_id = str(uuid.uuid4())
        output_folder = os.path.join(base_output_dir, f"{doc_name}_{unique_id}")
        os.makedirs(output_folder, exist_ok=True)
        return output_folder
