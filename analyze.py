import os
from together import Together

def analyze_code(file_content):
    client = Together(api_key="**********************************")
    response = client.chat.completions.create(
        model = "deepseek-ai/DeepSeek-R1",
        messages = [{"role": "user", 
                   "content": f"Please review these codes and give your feedback. Give your thoughts in terms of architecture, security and best practices. Explain one by one:\n\n{file_content}"}],
        max_tokens = 1000
    )
    return response.choices[0].message.content

def read_files_in_test_folder():
    folder_path = os.path.join(os.getcwd(), 'test')
    if not os.path.exists(folder_path):
        print("'test' klasörü bulunamadı.")
        return
    
    file_contents = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                file_contents[filename] = file.read()
    
    for filename, content in file_contents.items():
        print(f"\nAnaliz sonucu ({filename}):")
        print(analyze_code(content))

if __name__ == "__main__":
    read_files_in_test_folder()
