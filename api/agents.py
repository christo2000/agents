from fastapi import APIRouter

from config.model_config import PADDLE_OCR_BATCH
from core.tools.object_detection_tool import ObjectDetection

agent_router = APIRouter()

@agent_router.post("/object_detection", tags=["agent"])
def object_detection(model_dir, input_path, output_folder, model_name):
    detector = ObjectDetection(model_name= model_name, model_dir=model_dir)
    detector.process(input_path, output_folder, batch_size=PADDLE_OCR_BATCH)


