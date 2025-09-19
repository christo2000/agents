from core.tools.object_detection_tool import ObjectDetection

def main():
    model_dir = "/home/christopher.paulraj@zucisystems.com/Documents/python/models/PP-DocLayout-L/official_models/PP-DocLayout-L"
    input_path = "/home/christopher.paulraj@zucisystems.com/Downloads/SYNT_166529664_c1_page-0001.jpg"      # can be a single image or a folder
    output_folder = "/home/christopher.paulraj@zucisystems.com/Documents/python/output"
    model_name="PP-DocLayout-L",
    detector = ObjectDetection(model_name= model_name, model_dir=model_dir)
    detector.process(input_path, output_folder, batch_size=4)

if __name__ == "__main__":
    main()