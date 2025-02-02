from flask import Flask, render_template_string
from get_info import get_name_and_age
from categorize_age import categorize_age
from generate_report import generate_report
from together import Together

app = Flask(__name__)
client = Together(api_key="**********************************")

@app.route('/')
def home():
    return "<h1>Exception Yorumlama Test Uygulamasına Hoş Geldiniz!</h1><p>Aşağıdaki butona tıklayarak uygulamayı çalıştırabilirsiniz.</p><a href='/run'><button>Uygulamayı Çalıştır</button></a>"

@app.route('/run')
def run_main_logic():
    print("Uygulama başlatıldı.")
    try:
        # 1. Adım: İsim ve yaş bilgilerini al
        name, age = get_name_and_age()
        
        # 2. Adım: Yaşa göre kategori belirle
        category = categorize_age(age)
        print(f"{name} ({age} yaşında) kategorisi: {category}")
        
        # 3. Adım: İsim ve yaş bilgilerini raporla
        generate_report(name, age)
        
        return f"<h1>İşlem Başarılı!</h1><p>{name} ({age} yaşında) {category}.</p><p>Aşağıdaki butona tıklayarak uygulamayı yeniden çalıştırabilirsiniz.</p><a href='/run'><button>Uygulamayı Yeniden Çalıştır</button></a>"
    
    except Exception as e:
        error_message = str(e)

        # DeepSeek AI'ye hata mesajını soruyoruz
        response = client.chat.completions.create(
            model = "deepseek-ai/DeepSeek-R1",
            messages = [{"role": "user", 
                    "content": f"What caused this error in the code?\n\n{error_message}"}],
            max_tokens = 200
        )
        ai_error_explanation = response.choices[0].message.content
        return render_template_string("""
            <h1>Hata Mesajı:</h1>
            <p>{{ error_message }}</p>
            <h1>AI Cevabı:</h1>
            <p>{{ ai_error_explanation }}</p>
        """, error_message=error_message, ai_error_explanation=ai_error_explanation)
        
if __name__ == "__main__":
    app.run(debug=True)
