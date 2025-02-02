import os
from together import Together

client = Together(api_key="**********************************")

def analyze_code(file_content):
    response = client.chat.completions.create(
        model = "deepseek-ai/DeepSeek-R1",
        messages = [{"role": "user", 
                   "content": f"Check these file names and their tasks. Make a prediction about the subject of the project in which these codes are used and determine a roadmap based on this prediction.\n\n{file_content}"}],
        max_tokens = 500
    )
    return response.choices[0].message.content

def analyze_task(file_content):
    response = client.chat.completions.create(
        model = "deepseek-ai/DeepSeek-R1",
        messages = [{"role": "user", 
                   "content": f"Check these file names and their tasks. Make a prediction about the subject of the project in which these codes are used and determine a roadmap based on this prediction.\n\n{file_content}"}],
        max_tokens = 200
    )
    return response.choices[0].message.content

def read_files_in_test_folder():
    folder_path = os.path.join(os.getcwd(), 'test')
    if not os.path.exists(folder_path):
        print("'test' klasörü bulunamadı.")
        return
    
    file_contents = {}
    file_tasks = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                file_contents[filename] = file.read()
                file_tasks[filename] = analyze_task(file_contents[filename])

    for filename, task in file_tasks.items():
        print(f"\nGörev ({filename}):")
        print(task)

    roadmap = analyze_code(file_tasks)
    print(f"\nYol Haritası:")
    print(roadmap)

if __name__ == "__main__":
    read_files_in_test_folder()