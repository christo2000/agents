from core.object_detection_tool import ObjectDetection

def main():
    model_dir = r"D:\Workspace\python\model\PP-DocLayout-L_infer"
    input_path = r"D:\Workspace\python\test"      # can be a single image or a folder
    output_folder = r"D:\Workspace\python\agents\output"
    model_name="PP-DocLayout-L",
    detector = ObjectDetection(model_name= model_name, model_dir=model_dir)
    detector.process(input_path, output_folder, batch_size=4)

if __name__ == "__main__":
    main()