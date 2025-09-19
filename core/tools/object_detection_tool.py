import os
from pathlib import Path

import paddle
from paddleocr import LayoutDetection


class ObjectDetection:
    def __init__(self, model_name, model_dir):
        self.model = LayoutDetection(
        model_name="PP-DocLayout-L",
        model_dir=model_dir
    )

    def process(self, input_path: str, output_folder: str, batch_size: int = 4):
        input_path = Path(input_path)
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
        file_name = input_path.name
        # Case 1: Single image
        if input_path.is_file() and input_path.suffix.lower() in [".png", ".jpg", ".jpeg"]:
            print(f"📄 Processing single image: {input_path.name}")
            outputs = self.model.predict([str(input_path)], batch_size=1, layout_nms=True)
            self._save_results([input_path], outputs, output_path)

        # Case 2: Folder of images
        elif input_path.is_dir():
            image_files = [f for f in input_path.glob("*.*") if f.suffix.lower() in [".png", ".jpg", ".jpeg"]]
            if not image_files:
                print("⚠️ No images found in the folder.")
                return

            print(f"📂 Found {len(image_files)} images. Running detection...")
            outputs = self.model.predict([str(f) for f in image_files], batch_size=batch_size, layout_nms=True)
            self._save_results(image_files, outputs, output_path.joinpath(file_name))

        else:
            print("❌ Input path is not a valid image file or folder.")

    def _save_results(self, image_files, outputs, output_path: Path):
        for img_path, res_list in zip(image_files, outputs):
            img_name = Path(img_path).stem
            output_path.joinpath(img_name).mkdir(parents=True, exist_ok=True)
            image_folder = output_path.joinpath(img_name)

            print(f"✅ Processed: {img_name}{Path(img_path).suffix}")

            vis_path = image_folder / f"{img_name}_layout.png"
            res_list.save_to_img(save_path=str(vis_path))

            # Save JSON
            json_path = image_folder / f"{img_name}_layout.json"
            res_list.save_to_json(save_path=str(json_path))
